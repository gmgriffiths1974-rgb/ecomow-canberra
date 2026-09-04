#!/usr/bin/env python3
import os, re
from bs4 import BeautifulSoup

ROOT = os.path.expanduser("~/Projects/ecomow-site")
BASE = "https://ecomowcanberra.com.au"
os.chdir(ROOT)

def make_md(html_path):
    with open(html_path) as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    t = soup.find("title")
    title = t.get_text(strip=True) if t else ""
    m = soup.find("meta", attrs={"name":"description"})
    desc = m["content"] if m else ""
    c = soup.find("link", attrs={"rel":"canonical"})
    canon = c["href"] if c else ""
    main = soup.find("main") or soup.find("body")
    if not main: return
    for x in main.find_all(["script","style","svg","noscript"]): x.decompose()
    lines, seen = [], set()
    for el in main.find_all(["h1","h2","h3","h4","p","li","blockquote"]):
        txt = el.get_text(" ", strip=True)
        if not txt or len(txt)<3 or txt in seen: continue
        if el.find_parent("nav"): continue
        seen.add(txt)
        if el.name=="h1": lines.append(f"\n# {txt}\n")
        elif el.name=="h2": lines.append(f"\n## {txt}\n")
        elif el.name=="h3": lines.append(f"\n### {txt}\n")
        elif el.name=="h4": lines.append(f"\n#### {txt}\n")
        elif el.name=="li": lines.append(f"- {txt}")
        elif el.name=="blockquote": lines.append(f"\n> {txt}\n")
        else: lines.append(f"\n{txt}\n")
    body = re.sub(r'\n{3,}','\n\n',"\n".join(lines)).strip()
    ct = re.sub(r'\s*\|.*$','',title)
    return f'---\ntitle: "{ct}"\ndescription: "{desc}"\ncanonical: "{canon}"\n---\n\n{body}\n\n---\n*Source: [{ct}]({canon})*\n'

# Generate markdown mirrors
pages = []
for root, dirs, files in sorted(os.walk(".")):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d!='assets']
    for fn in files:
        if fn=="404.html": continue
        if fn=="index.html" or fn.endswith(".html"):
            hp = os.path.join(root, fn)
            md = make_md(hp)
            if not md: continue
            mp = hp.replace(".html",".md")
            with open(mp,"w") as f: f.write(md)
            rel = os.path.relpath(root,".")
            path = "/" if rel=="." and fn=="index.html" else f"/{rel}/" if fn=="index.html" else f"/{fn.replace('.html','/')}/"
            with open(hp) as f: soup = BeautifulSoup(f.read(),"html.parser")
            tt = soup.find("title").get_text(strip=True).replace(" | ","  — ") if soup.find("title") else ""
            mm = soup.find("meta",attrs={"name":"description"})
            dd = mm["content"][:120] if mm else ""
            pages.append((path,tt,dd))
print(f"Created {len(pages)} markdown mirrors")

# Write robots.txt
with open("robots.txt","w") as f:
    f.write("""User-agent: *
Allow: /

Allow: /llms.txt
Allow: /sitemap-ai.md
Allow: /*.md$

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Crawl-delay: 1

Sitemap: https://ecomowcanberra.com.au/sitemap.xml
Sitemap: https://ecomowcanberra.com.au/sitemap-ai.md
""")
print("Created robots.txt")

# Write sitemap-ai.md
core_order = ["/","/services/","/suburbs/","/reviews/","/contact/","/gallery/","/customer-charter/"]
core = sorted([p for p in pages if p[0] in core_order], key=lambda x: core_order.index(x[0]))
mow = sorted([p for p in pages if "/lawn-mowing" in p[0]])
hedge = sorted([p for p in pages if "/hedge-trimming" in p[0]])
subs = sorted([p for p in pages if p[0].startswith("/suburbs/") and p[0]!="/suburbs/"])
out = "# EcoMow Canberra — AI Sitemap\n\n> Structured index of all pages with markdown mirrors.\n\n## Core Pages\n"
for group, label in [(core,"Core"),(mow,"Lawn Mowing"),(hedge,"Hedge Trimming"),(subs,"Suburb")]:
    if group != core: out += f"\n## {label} Pages\n"
    for path, title, desc in group:
        url = f"{BASE}{path}"
        md_url = f"{BASE}/index.md" if path=="/" else f"{BASE}{path}index.md"
        out += f"- **{title}**: {desc}...\n  - HTML: {url}\n  - Markdown: {md_url}\n\n"
with open("sitemap-ai.md","w") as f: f.write(out)
print("Created sitemap-ai.md")
print("Done! Now create llms.txt manually or run: git add -A && git status")
