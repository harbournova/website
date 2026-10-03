# HarbourNova project website

Terminology revision: **October 3, 2026**. This complete package supersedes
`HarbourNova-website-2026-10-03-revised.zip` and the October 2 package;
it is not an incremental patch.

A responsive, pre-release project website for **https://harbournova.org/**.
No build step, JavaScript, external fonts, package installation, or analytics is
needed. The homepage introduces HarbourNova and links to its Google Group.
The compiler is being developed for free distribution, but no public compiler
or HN Web Framework release is offered yet.

## What changed in this revision

The headline now reads “A new direction for the xBase family of languages.”
The introduction, supporting copy, page title, and search/social metadata use
language-family wording instead of presenting xBase as a standalone product.
A seventh FAQ explains the term and avoids implying universal compatibility.
The site-information page explains how the family name is used on this site.
The social-sharing card has been re-rendered with the same explicit wording.

The existing palette, layout, Google Group links, domain configuration, original
SVG logo, compact emblem, and icons are preserved. A small headline typography
rule accommodates the longer wording without changing the design direction.
Pre-release status and the plan for free compiler distribution remain unchanged.

Public pages retain HarbourNova(TM) branding without asserting registration.
No trademark application history, filing deadline, or legal strategy is added.
This is a terminology clarification, not trademark clearance or evidence of
software distribution. The website offers no compiler download yet.

Terminology references consulted for this revision (not a trademark search report):
- Harbour project overview: https://harbour.github.io/
- Alaska Software product overview, which uses “xBase language dialects” for
  Clipper and Visual FoxPro: https://www.alaska-software.com/products/overview.cxp


## Contents

- `index.html`: project overview, development status, community, and seven FAQs.
- `privacy.html`: site information and privacy explanation specific to this code.
- `404.html`: custom missing-page response, with root-absolute links.
- `assets/site.css`: responsive styling, keyboard focus, and reduced-motion support.
- `assets/images/HarbourNovaLogoBoatTitleHN.svg`: unmodified primary artwork.
- `assets/images/HarbourNovaLogoHN.svg`: unmodified compact emblem.
- `assets/favicon.svg`, `favicon.ico`, `assets/apple-touch-icon.png`: site icons.
- `assets/social-preview.png`: 1200 x 630 sharing image using the supplied artwork.
- `CNAME`, `.nojekyll`, `robots.txt`, `sitemap.xml`: host and indexing configuration.
- `tools/check_site.py`: optional read-only checker using Python 3.10 or newer.
- `manifest.sha256`: byte-level delivery inventory, excluding the manifest itself.

All ZIP entries are repository-relative, with no enclosing directory. There is
no `.git`, `.vscode`, private source code, or CI artifact in the package. There
are no required file deletions. Preserve existing repository/editor settings.

## Validation of this delivery

All three pages were rendered offline in Chromium at widths of 320, 360, 390,
600, 768, 1024, 1440, and 1920 pixels. Checks covered horizontal overflow,
image loading, the seven FAQs, keyboard activation, the skip link, and
reduced-motion behavior. The rendering harness embedded the exact local CSS
and image bytes in the test DOM; the delivered HTML was not changed for testing.

The exact ZIP was extracted over the preceding delivery in an isolated test
repository. Its original SVG assets, CNAME, and protected editor settings were
verified unchanged. The package checker, manifest verification, ZIP integrity,
and staged/unstaged Git whitespace checks passed. Live deployment, actual HTTP
hosting, and external Google Group membership flows were not tested.

## Review before copying

The preceding delivery recorded the following website baseline. This terminology
revision was prepared from that delivery ZIP, not from a new live repository read:

```text
Repository: harbournova/website
Branch: main
Commit: 05ac9ae1376b7d04897e78e5e340be69b064fa85
```

Extract this ZIP into an empty review folder OUTSIDE your checkout. Do not
extract over the checkout before completing the review. From the review folder:

```cmd
python tools\check_site.py --verify-manifest
```

This checker makes no network requests and writes no files. Success prints
`HN_WEBSITE_CHECK_PASSED`. Python is not needed to host the website.
Without Python, verify the ZIP against its accompanying SHA-256 file and inspect
the site in a browser.

Before copying into your checkout, inspect `git status --short`, run
`git fetch origin`, and compare both your local branch and `origin/main` with
the baseline above. Stop and reconcile local edits or newer commits before
replacing anything. Do not force-reset or replace the repository directory.

The input for this revision is the October 3 revised ZIP, with SHA-256:
`0dbd6d78670ae6ca38a69bb66c9f44576887b5ba1064b88db922b8698821eb31`.
It is a prepared package, not a published commit. If you already copied an earlier
ZIP locally, compare your working files against that unedited delivery before
replacing the same paths. Preserve subsequent local edits. Use this terminology
ZIP as a complete replacement; do not mix files or manifests from deliveries.

Make a normal backup or commit of existing work. Copy the reviewed replacement
files into the checkout, preserving `.git`, `.vscode`, and unrelated files.
Do not copy the ZIP, screenshots, or separate ZIP checksum into the website.

## Preview locally

Open `index.html` in a browser for a basic preview, or run this from the review
folder for an ordinary local server:

```cmd
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. Stop the server with Ctrl+C. Header links and FAQ
controls work without JavaScript. Open `/404.html` directly to preview it;
Python's simple server does not select this custom page for missing paths.
The 404 page uses root-absolute links so it works at nested paths on the live host.

## Domain and publishing

The confirmed canonical domain is `harbournova.org`. The existing `CNAME` is
preserved byte-for-byte. Canonical and social-sharing addresses, `robots.txt`,
and `sitemap.xml` consistently use `https://harbournova.org`.
No DNS, custom-domain, certificate, or forwarding change is required by this ZIP.
Those live settings are not modified or validated by the package checker.

Use the repository's existing deployment route. For branch-based GitHub Pages,
confirm Settings > Pages publishes `main` and `/(root)`. Keep `.nojekyll` and
`CNAME` in the publishing root. No new workflow or build service is included.

From the website checkout, before staging:

```cmd
python tools\check_site.py --verify-manifest && git diff --check && git status --short
```

Review the full diff, stage only intended website files, and run
`git diff --cached --check`. Use a normal non-forced push or the usual PR process.
No repository changes or website publication have been performed for you.

The homepage permits indexing. This intentionally replaces the original
placeholder page's `noindex, nofollow` directive. The 404 page stays `noindex`.

After deployment, check the actual `.org` website and HTTPS, the images, mobile
layout, all three Google Groups destinations, and a missing nested path. Test
membership with a non-owner account. Website links do not change group settings.

## Maintaining the current pre-release site

Files use UTF-8 and LF endings; original brand SVG bytes are preserved.
The checker validates local links, page metadata, canonical domain, original
artwork, and the declared pre-release state. It rejects scripts, forms, external
asset loads, private-source links, and downloadable-release links in this version.
It does not test external URLs or establish software-distribution facts.

After deliberate edits, run `python tools/check_site.py` without the manifest
option. The original manifest is a delivery receipt and will no longer match
edited files. Regenerate it only for a reviewed new delivery. Git line-ending
conversion can also cause original-byte verification to fail; inspect such
changes rather than ignoring the failure.

Do not add unsupported feature claims, performance numbers, release promises,
nonfunctional downloads, or private repository links. Group joining instructions
refer to Google's membership prompts rather than assuming a particular interface.

## Transition when an actual compiler release is ready

This is a future maintenance checklist, not an announcement of availability.
Do not activate downloads until the actual release artifacts are published.

1. Publish the real distribution repository and versioned artifacts with the
   approved software licenses, notices, supported-platform information, and
   install/build instructions. Do not infer a software license from this website.
2. Update the homepage status, compiler card, distribution paragraph, and FAQs
   to distinguish released components from work that remains in development.
3. Add tested links to the actual downloads, release notes, documentation, and
   licenses. Keep the HarbourNova name visibly associated with the compiler.
4. Update site information, social/search metadata, and the sharing image as
   needed. Update the checker's pre-release restrictions deliberately; do not
   simply bypass failing checks. Regenerate the manifest and rerun validation.
5. Preserve the exact release archive/checksum and genuine release records.
   Keep private feedback or usage evidence outside this public website repo.

Do not publish legal filing deadlines or treat this website's revision date as
a software-release date. Website deployment and software release are different
activities. Any trademark-use filing needs its own review of the actual facts;
this package and its locally generated previews do not establish those facts.

## Artwork

The boat-and-title SVG and compact emblem remain byte-for-byte identical to the
original artwork in the prior verified delivery. Raster icons and the newly typeset social
image use that supplied artwork. No font files are included. This package does
not assign a license to unreleased compiler or framework code.

Copyright 2026 Eric Lendvai (WA-USA).
