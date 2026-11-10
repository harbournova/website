# HarbourNova project website

Website update: **November 10, 2026**.

A responsive, pre-release project website for **https://harbournova.org/**,
hosted through the `harbournova/website` GitHub repository. The site is static
HTML and CSS. No build step, JavaScript, package installation, external fonts,
or analytics is needed.

The compiler is being developed for free distribution. The public
[HarbourNova repository](https://github.com/harbournova/harbournova) contains
design documents now and will host future HN downloads. No public compiler or
HN Web Framework release is available yet.

## Changes in this update

- The homepage lists all six documents in the public `design/` directory, with
  a direct GitHub link and a short topic description for each.
- The list covers the build toolset and editor integration, Number, temporal
  data types, Local SQL, multiple return values, and Tensors.
- The build toolset entry includes hnmake, VS Code/VSCodium build controls,
  the project tree, and the graphical Project Editor with HN Web Foundation.
- The main navigation on all three pages and the homepage introduction link
  to the design-document section. The Development section also links directly
  to the public design directory.
- The list uses the site's existing responsive reading-card layout.
- The site checker includes the design directory and all six document URLs;
  the delivery manifest records the updated file hashes.

The existing artwork, domain configuration, page structure, and pre-release
status are retained. The core and HN Web Framework development repositories
remain private.

## Source baseline

This update was prepared from the website repository's `main` branch:

```text
Repository: https://github.com/harbournova/website
Commit: d25252ac811f8a6e68b78144b873fddefc27a557
```

The fetched files were checked against their Git blob hashes before editing.

## Maintaining the design-document list

The source list is the public
[HarbourNova design directory](https://github.com/harbournova/harbournova/tree/main/design).
When a document is added, renamed, or removed:

1. Update the reading cards in the `design` section of `index.html`. Use the
   document's exact public GitHub path and describe its topic without adding
   implementation-status claims.
2. Update `EXTERNAL_LINKS` in `tools/check_site.py` to match the linked documents.
3. Refresh the SHA-256 hashes in `manifest.sha256` for changed files, then run
   the checks below before committing.

Each document link opens in a new tab with `rel="noopener noreferrer"`.
The list reuses the existing responsive layout and requires no JavaScript or
additional assets.

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

- `index.html`: project overview, development status, design-document list,
  community, and seven FAQs.
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
