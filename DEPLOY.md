# EcoMow Canberra — Vercel Deploy Guide

This is a pure static HTML site. No build step. No framework. Vercel will serve these files from its global CDN — fast, free, and auto-deployed from GitHub on every push.

## What you're deploying

- 51 HTML pages (home, services, suburbs hub, 31 suburbs, 11 service × suburb crossovers, reviews, gallery, customer charter, contact, 404)
- Shared CSS + JS + image folder
- `sitemap.xml` and `robots.txt` at the root
- All internal links use absolute paths (`/services/`, `/suburbs/ainslie/` etc.) — these only work when served from a web server, which is why they looked broken opening the files directly on your Mac. They'll resolve cleanly on Vercel.

## One-time setup

1. Create a new empty GitHub repo (e.g. `ecomow-canberra-site`). Don't initialise it with a README — keep it empty.
2. On your Mac, in a terminal, from the folder containing this file:
   ```
   git init
   git add .
   git commit -m "Initial site build"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ecomow-canberra-site.git
   git push -u origin main
   ```
3. Go to vercel.com → Add New → Project → Import the repo you just pushed.
4. When Vercel asks about framework preset, choose **Other** (static). Leave build command empty. Leave output directory as the project root.
5. Click Deploy. First deploy takes under a minute.

## Custom domain (ecomowcanberra.com.au)

1. In the Vercel project, go to Settings → Domains.
2. Add `ecomowcanberra.com.au` and `www.ecomowcanberra.com.au`.
3. Vercel will show you DNS records to add at your registrar (likely an A record for the apex and a CNAME for www, or Vercel nameservers).
4. Once DNS propagates (usually minutes, sometimes hours), Vercel provisions a free SSL cert automatically.
5. In Settings → Domains, set `ecomowcanberra.com.au` as the primary and redirect www to apex (or vice versa — pick one).

## Ongoing updates

Any time you push a change to the `main` branch on GitHub, Vercel rebuilds and deploys within seconds. Pull requests get preview URLs automatically.

To edit the site locally and preview before pushing, from the project folder run:
```
python3 -m http.server 8000
```
then open `http://localhost:8000` in your browser. All internal links will resolve correctly.

## Images you still need to add

Replace the placeholder references in `/assets/images/` with real files:

- `logo.png` (site logo)
- `og-image.jpg` (1200×630 social share card)
- `favicon.ico`, `favicon.svg`, `apple-touch-icon.png`
- `team-1.jpg` through `team-6.jpg` (gallery photos of Kai working)

The HTML references these paths already — just drop the files in and push.

## Once you've deployed

You can cancel your Lovable subscription. Vercel's free tier handles this site comfortably — no traffic limits you'll hit at current scale.

## Later (app + quoting features)

When you're ready to add quoting, bookings, customer accounts etc., Supabase slots in cleanly as the backend:

- Auth for customers and admin
- Postgres tables for quotes, jobs, suburbs
- Row-level security
- Edge functions for the quoting logic

You can add a `/app/` path on the same Vercel project (or a separate project at `app.ecomowcanberra.com.au`) that talks to Supabase. The static site stays untouched.
