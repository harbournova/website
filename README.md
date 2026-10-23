# HarbourNova project website

Website update: **October 23, 2026**.

A responsive, pre-release project website for **https://harbournova.org/**,
hosted through the `harbournova/website` GitHub repository. The site is static
HTML and CSS. No build step, JavaScript, package installation, external fonts,
or analytics is needed.

The compiler is being developed for free distribution. The public
[HarbourNova repository](https://github.com/harbournova/harbournova) contains
design documents now and will host future HN downloads. No public compiler or
HN Web Framework release is available yet.

## Changes in this update

- Community and introduction links open in a new browser tab, including the
  homepage buttons and corresponding links elsewhere on the site.
- `JOIN NOW` in the homepage status strip is a keyboard-accessible link to the
  same HarbourNova users group, with a visible focus outline on the dark background.
- A `Design documents & future downloads` link appears below the homepage actions.
- The Development section, repository FAQ, and site-information page distinguish
  the existing public design documents from future software downloads.
- The site checker permits the public HarbourNova repository alongside the
  existing Google Groups destinations.
- The delivery manifest records the updated file hashes.

The existing artwork, domain configuration, page structure, and pre-release
status are retained. The core and HN Web Framework development repositories
remain private.

## Source baseline

This update was prepared from the website repository's `main` branch:

```text
Repository: https://github.com/harbournova/website
Commit: 11a727e7d82d70302b58e0571dcc4a51969e68bf
```

The fetched files were checked against their Git blob hashes before editing.

## Apply the ZIP

`HarbourNova-website-update-2026-10-23.zip` is an incremental update for an
existing checkout. Its seven entries are relative to the repository root;
there is no enclosing folder:

- `index.html`
- `privacy.html`
- `404.html`
- `assets/site.css`
- `tools/check_site.py`
- `README.md`
- `manifest.sha256`

Retain any local edits you need, then extract the ZIP directly into the website
repository root, allowing these files to be replaced. Use the extraction option
that preserves the `assets/` and `tools/` paths. No file deletions are required.

The ZIP contains no replacement logos, icons, hosting configuration, repository
metadata, or editor settings. Existing site assets must already be present.
It is not a standalone copy of the complete website.

After extracting, review the changes and publish using the repository's normal
commit and push process. This ZIP does not itself publish the website.

## Check and preview

The optional checker requires Python 3.10 or newer and no additional packages.
From the website repository root on Windows:

```cmd
python tools\check_site.py --verify-manifest && git diff --check
```

On Linux or macOS:

```sh
python3 tools/check_site.py --verify-manifest && git diff --check
```

A successful check prints `HN_WEBSITE_CHECK_PASSED`. It checks all three pages,
local links and fragments, metadata, original artwork, the canonical domain,
the approved external destinations, and the delivery manifest. It makes no
network requests and writes no files.

The manifest covers the complete resulting site, including unchanged files;
it excludes itself and repository/editor metadata. Intentional local changes
or line-ending conversions can cause a hash mismatch. After later edits, use
the checker without `--verify-manifest` until preparing a new delivery manifest.

Open `index.html` in a browser for a basic preview. For a local HTTP preview:

```cmd
python -m http.server 8000 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8000/`. Python is not required to host the site.
The checker does not test external service behavior, Google Group membership,
DNS, HTTPS, or the live GitHub Pages deployment.

## Site files and publishing

- `index.html`: project overview, development status, community, and seven FAQs.
- `privacy.html`: site information and privacy explanation.
- `404.html`: missing-page response with root-absolute links.
- `assets/site.css`: responsive styling and keyboard focus.
- `assets/images/`: original HarbourNova SVG artwork.
- `favicon.ico`, `assets/favicon.svg`, `assets/apple-touch-icon.png`: site icons.
- `assets/social-preview.png`: social-sharing image.
- `CNAME`, `.nojekyll`, `robots.txt`, `sitemap.xml`: hosting and indexing files.

Continue using the existing GitHub Pages deployment configuration. The
canonical domain remains `harbournova.org`; no DNS or hosting change is part
of this update.

Files use UTF-8 with LF endings. Site links to Google Groups and the public HN
repository use `target="_blank"` with `rel="noopener noreferrer"`.
Internal navigation stays within the website.

When an actual HN release is published, update the pre-release statements and
add verified download links, release documentation, and applicable license
notices. Update the checker deliberately to support those real release
resources, regenerate the manifest, and validate the resulting site.

## Artwork and notices

The original HarbourNova SVG artwork is retained byte-for-byte. The website
uses HarbourNova™ branding. Software licenses and applicable notices will
accompany actual compiler and framework releases.

Copyright 2026 Eric Lendvai (WA-USA).
