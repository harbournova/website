#!/usr/bin/env python3
"""Read-only checks for the static HarbourNova website; Python 3.10+, no packages.

Run from anywhere:
    python tools/check_site.py
    python tools/check_site.py --verify-manifest
The optional manifest check validates the original delivery byte-for-byte. It is
expected to fail after intentional edits until a new manifest is generated.
This checker makes no network requests and writes no files.
"""
from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PAGES = ('index.html', 'privacy.html', '404.html')
EXTERNAL_LINKS = {
    'https://groups.google.com/g/harbournova-users',
    'https://groups.google.com/g/harbour-users/c/l5xDg-FEUDo',
    'https://groups.google.com/g/harbour-users/c/x07DD1650ro',
    'https://github.com/harbournova/harbournova',
}
ORIGINAL_LOGO_BLOBS = {
    'assets/images/HarbourNovaLogoBoatTitleHN.svg': 'a9b4e39dc33b3e9417587bf10242bc1e2eddec00',
    'assets/images/HarbourNovaLogoHN.svg': '60badac844bc336fd79bc8a59fa6eb673bc25c2e',
    'assets/favicon.svg': '60badac844bc336fd79bc8a59fa6eb673bc25c2e',
}

class Document(HTMLParser):
    def __init__(self, name: str) -> None:
        super().__init__(convert_charrefs=True)
        self.name = name
        self.ids: set[str] = set()
        self.links: list[tuple[str, str]] = []
        self.issues: list[str] = []
        self.counts: dict[str, int] = {}
        self.canonical: str | None = None
        self.robots: str | None = None
        self.language: str | None = None
        self.release_stage: str | None = None
        self.metadata: dict[str, str] = {}
        self.has_description = False
        self.has_viewport = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        self.counts[tag] = self.counts.get(tag, 0) + 1
        if 'id' in a:
            ident = a['id'] or ''
            if not ident or ident in self.ids:
                self.issues.append(f'Empty or duplicate id: {ident!r}')
            self.ids.add(ident)
        if tag == 'html':
            self.language = a.get('lang')
        if tag == 'body':
            self.release_stage = a.get('data-release-stage')
        if tag == 'a' and 'download' in a:
            self.issues.append('Unexpected software/download action on this pre-release site')
        if tag in ('script', 'iframe', 'form'):
            self.issues.append(f'Unexpected active/external feature: <{tag}>')
        if any(key.startswith('on') for key in a):
            self.issues.append('Unexpected inline event handler')
        if tag == 'img' and 'alt' not in a:
            self.issues.append('Image missing alt attribute')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a.get('href')
        if tag == 'meta':
            key = a.get('property') or a.get('name')
            if key:
                if key in self.metadata:
                    self.issues.append(f'Duplicate metadata: {key}')
                self.metadata[key] = a.get('content') or ''
            if a.get('name') == 'robots':
                self.robots = a.get('content')
            if a.get('name') == 'description':
                self.has_description = bool(a.get('content'))
            if a.get('name') == 'viewport':
                self.has_viewport = True
        for key in ('href', 'src'):
            if key in a:
                value = a[key] or ''
                self.links.append((tag, value))
                if not value or value == '#':
                    self.issues.append(f'Empty placeholder {key}')
                if value.startswith(('javascript:', 'http:')):
                    self.issues.append(f'Insecure or active link: {value}')
                if key == 'src' and urlsplit(value).netloc:
                    self.issues.append(f'Unexpected external asset: {value}')


def check(verify_manifest: bool) -> list[str]:
    errors: list[str] = []
    docs: dict[str, Document] = {}
    for name in PAGES:
        p = ROOT / name
        if not p.is_file():
            errors.append(f'Missing page: {name}')
            continue
        doc = Document(name)
        html = p.read_text(encoding='utf-8')
        if '\u00ae' in html or re.search(r'&(?:reg|#174|#x0*ae);', html, re.I):
            errors.append(f'{name}: registration symbol is not approved for this delivery')
        doc.feed(html)
        docs[name] = doc
        errors.extend(f'{name}: {issue}' for issue in doc.issues)
        for tag in ('html', 'head', 'body', 'title', 'h1', 'main'):
            if doc.counts.get(tag) != 1:
                errors.append(f'{name}: expected exactly one {tag}')
        if doc.language != 'en' or not doc.has_viewport:
            errors.append(f'{name}: language or viewport missing')
        if name != '404.html' and not doc.has_description:
            errors.append(f'{name}: missing description')
        if 'main' not in doc.ids:
            errors.append(f'{name}: skip link target is missing')

    external: set[str] = set()
    for name, doc in docs.items():
        for tag, link in doc.links:
            url = urlsplit(link)
            if tag == 'a' and re.search(r'\.(?:zip|exe|msi|7z|tar|gz|bz2|xz|dmg|pkg|deb|rpm)$', unquote(url.path), re.I):
                errors.append(f'{name}: downloadable-release link on this pre-release site: {link}')
            if url.netloc:
                if tag == 'a':
                    external.add(link)
                continue
            if url.scheme:
                continue
            raw = unquote(url.path)
            candidate = (ROOT/raw.lstrip('/')) if raw.startswith('/') else (ROOT/name).parent/raw
            if not raw:
                candidate = ROOT/name
            candidate = candidate.resolve()
            if not candidate.is_relative_to(ROOT):
                errors.append(f'{name}: local link escapes site: {link}')
                continue
            if candidate.is_dir():
                candidate /= 'index.html'
            if not candidate.is_file():
                errors.append(f'{name}: missing local link/asset: {link}')
                continue
            rel = candidate.relative_to(ROOT).as_posix()
            if url.fragment and rel in docs and unquote(url.fragment) not in docs[rel].ids:
                errors.append(f'{name}: missing fragment in {link}')
    if external != EXTERNAL_LINKS:
        errors.append(f'External anchor targets differ from approved community and public repository links: {external ^ EXTERNAL_LINKS}')

    for name, expected in ORIGINAL_LOGO_BLOBS.items():
        p = ROOT/name
        if not p.is_file():
            errors.append(f'Missing original brand asset: {name}')
            continue
        data = p.read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        if blob != expected:
            errors.append(f'Original brand asset changed: {name}')
        ET.fromstring(data)

    cname = ROOT/'CNAME'
    if not cname.is_file() or cname.read_text(encoding='utf-8').strip() != 'harbournova.org':
        errors.append('Custom domain differs from the reviewed harbournova.org configuration')
    if not (ROOT/'.nojekyll').is_file():
        errors.append('Missing .nojekyll')
    for name in ('index.html', 'privacy.html'):
        expected = 'https://harbournova.org/' + ('' if name == 'index.html' else name)
        if name in docs and docs[name].canonical != expected:
            errors.append(f'{name}: canonical URL mismatch')
    if 'index.html' in docs and docs['index.html'].robots != 'index, follow':
        errors.append('Homepage must permit indexing')
    if 'index.html' in docs:
        home = docs['index.html']
        if home.release_stage != 'pre-release':
            errors.append('Homepage must declare this delivery as pre-release')
        for key, expected in {
            'og:url': 'https://harbournova.org/',
            'og:image': 'https://harbournova.org/assets/social-preview.png',
            'twitter:image': 'https://harbournova.org/assets/social-preview.png',
        }.items():
            if home.metadata.get(key) != expected:
                errors.append(f'Homepage sharing metadata mismatch: {key}')
    ET.parse(ROOT/'sitemap.xml')
    css = (ROOT/'assets/site.css').read_text(encoding='utf-8')
    if '@import' in css or re.search(r'url\s*\(', css):
        errors.append('Unexpected CSS asset/network dependency')
    for path in ROOT.rglob('*'):
        if not path.is_file() or '.git' in path.parts or '__pycache__' in path.parts:
            continue
        if path.suffix in {'.html', '.css', '.md', '.txt', '.xml', '.py'}:
            data = path.read_bytes()
            if b'\r' in data:
                errors.append(f'{path.relative_to(ROOT)}: non-LF line ending')
            text = data.decode('utf-8')
            if any(line.rstrip() != line for line in text.splitlines()):
                errors.append(f'{path.relative_to(ROOT)}: trailing whitespace')
        if path.suffix in {'.html', '.css', '.svg'}:
            text = path.read_text(encoding='utf-8')
            if re.search(r'github\.com/harbournova/core|[?&]token=|ghp_[A-Za-z0-9]+', text):
                errors.append(f'{path.relative_to(ROOT)}: private-source reference or token')
    if verify_manifest:
        manifest = ROOT/'manifest.sha256'
        if not manifest.is_file():
            errors.append('Missing manifest.sha256')
        else:
            listed: set[str] = set()
            for line in manifest.read_text(encoding='utf-8').splitlines():
                digest, separator, name = line.partition('  ')
                if not separator or not re.fullmatch('[0-9a-f]{64}', digest):
                    errors.append(f'Malformed manifest line: {line}')
                    continue
                path = (ROOT/name).resolve()
                if not path.is_relative_to(ROOT) or name in listed:
                    errors.append(f'Unsafe or duplicate manifest path: {name}')
                    continue
                listed.add(name)
                if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                    errors.append(f'Manifest mismatch: {name}')
            required = set(PAGES) | set(ORIGINAL_LOGO_BLOBS) | {
                'CNAME', '.nojekyll', 'assets/site.css', 'assets/social-preview.png',
                'assets/apple-touch-icon.png', 'favicon.ico', 'robots.txt',
                'sitemap.xml', 'README.md', 'tools/check_site.py',
            }
            if listed != required:
                errors.append(f'Manifest file inventory mismatch: {listed ^ required}')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-manifest', action='store_true')
    args = parser.parse_args()
    try:
        errors = check(args.verify_manifest)
    except (OSError, UnicodeError, ValueError, ET.ParseError) as exc:
        print(f'HN_WEBSITE_CHECK_FAILED: {exc}', file=sys.stderr)
        return 1
    if errors:
        print('HN_WEBSITE_CHECK_FAILED', file=sys.stderr)
        for error in errors:
            print(f'  - {error}', file=sys.stderr)
        return 1
    print('HN_WEBSITE_CHECK_PASSED')
    print('3 pages; local links and fragments; original logos; canonical domain; no active scripts.')
    if args.verify_manifest:
        print('Original delivery manifest: all listed files match SHA-256.')
    print('External URLs, DNS, HTTPS, Google membership and live deployment are not tested here.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
