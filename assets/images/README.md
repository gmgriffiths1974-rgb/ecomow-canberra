# Image assets — drop these in before deploy

All of the exemplar pages reference image paths under `/assets/images/`. The site is built to work without them (alt text carries meaning, layouts don't collapse) but you'll want real files in place before going live.

## Required files

| File | Used where | Recommended size |
|---|---|---|
| `logo.png` | LocalBusiness JSON-LD schema + Open Graph fallback | 1200x1200 square, transparent PNG |
| `og-image.jpg` | Open Graph / social share cards (all pages) | 1200x630 JPG |
| `favicon.ico` | Browser tab | 32x32 ICO (multi-size) |
| `favicon.svg` | Modern browser tab | SVG (any size) |
| `apple-touch-icon.png` | iOS home screen | 180x180 PNG |

## Team and job photos

The homepage and suburb pages reference:

| File | Suggested content |
|---|---|
| `team-1.jpg` | Kai on-site, battery mower, mid-cut |
| `team-2.jpg` | Finished lawn + clean edges, hero shot |
| `team-3.jpg` | Hedge trim — before/after side-by-side |
| `team-4.jpg` | Solar-charged battery rig |
| `team-5.jpg` | Gutter cleaning or tree pruning |
| `team-6.jpg` | Kai portrait, friendly, looking at camera |

Recommended dimensions: 1600 wide, JPG, under 250KB each (use `tinypng.com` or similar).

## If you don't have them yet

That's fine. The pages will render with broken image icons only where `<img>` tags exist. The LocalBusiness schema won't have a logo until `logo.png` is present, which is a small SEO hit but not a blocker.

Bare minimum for launch: `logo.png`, `og-image.jpg`, `favicon.ico`.
