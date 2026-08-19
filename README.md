# IntelliGenesis LLC — website rebuild

A brand-new, standalone rebuild of intelligenesisllc.com. No WordPress, no
database, no paid theme licence. Plain HTML/CSS/JS that runs on any hosting.

## What this is

The existing site runs WordPress with the commercial **YOOtheme Pro** builder,
which is built on top of **UIkit**. This rebuild uses UIkit 3 directly — the
same framework, MIT licensed and free — so the grid, spacing and components
match the original rather than being approximated by eye.

Every colour, font size, line height and section padding in `theme.css` was
measured off the live site, not guessed.

## Accuracy

Measured at a 1280px viewport, section by section:

| Section                      | Original | Rebuild | Diff |
|------------------------------|---------:|--------:|-----:|
| Hero slideshow               |    480px |   480px |   0  |
| Centred wordmark             |    209px |   207px |  -2  |
| Hero                         |    468px |   468px |   0  |
| "Advanced Solutions" band    |    130px |   130px |   0  |
| Three product cards          |    496px |   496px |   0  |
| "Your strategic partner"     |    149px |   149px |   0  |
| Differentiators              |    264px |   264px |   0  |
| Capability buttons           |     80px |    80px |   0  |
| Testimonial                  |    144px |   144px |   0  |
| Mission Services / Tech      |    386px |   387px |  +1  |
| Certifications               |    243px |   243px |   0  |
| Footer + subfooter           |    385px |   385px |   0  |
| **Total page height**        | **3515** |**3513** |**-2**|

Mobile (390px): 5135px vs 5157px, no horizontal overflow.

## Performance

|              | Requests | Transferred |
|--------------|---------:|------------:|
| Original     |       52 |     3.27 MB |
| This rebuild |       19 |     0.98 MB |

Fonts are self-hosted (no Google Fonts call), images kept in their original
AVIF/WebP formats.

## Layout

```
index.html              homepage
assets/css/uikit.min.css    UIkit 3.21.16 (MIT)
assets/css/fonts.css        @font-face for the two self-hosted families
assets/css/theme.css        all site-specific styling — this is the file to edit
assets/js/                  UIkit core + icons
assets/fonts/               Roboto + Work Sans (variable woff2, SIL OFL)
assets/img/                 page images
assets/docs/                linked PDFs
```

## Deploying

Upload the whole folder to the web root. No build step, no server-side
requirements, works on any shared host, cPanel, S3 or static host.

## Notes on the source site

Two things found while rebuilding, both present on the live site today:

1. `/privacy-policy/` returns **404**. It is linked from the footer of every page.
2. The Code of Ethics PDF (`/wp-content/uploads/2024/08/Ethics-Handbook-Final.pdf`)
   returns **404**. Also linked from every footer.
3. The footer "Employee Portal" button is a navy pill on a navy background, so
   only its white text is visible. Reproduced as-is — one line to change if wanted.
4. `/2026-virtual-open-house/` has no meta description, and 58 of 126 page titles
   exceed 60 characters so Google truncates them in search results.
