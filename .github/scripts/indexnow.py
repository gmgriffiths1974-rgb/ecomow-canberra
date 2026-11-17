#!/usr/bin/env python3
"""Tell IndexNow (Bing, and the engines that share its pings) which pages changed.

Runs from .github/workflows/indexnow.yml after Vercel reports a successful
production deploy. Steps:

1. Work out the last production deploy before this one (GitHub deployments API)
   and diff it against this one.
2. Keep the pages in sitemap.xml whose HTML file changed, plus any URL added to
   or removed from the sitemap.
3. Wait until the key file is live on the domain, then submit the list.

Nothing is submitted when no page changed. Standard library only.

Settings come from the workflow's env: SITE_URL, SITE_ROOT, INDEXNOW_KEY,
HEAD_SHA, and optionally BASE_SHA, SUBMIT_ALL, GH_TOKEN, REPO, DEPLOYMENT_ID,
ENVIRONMENT, DRY_RUN. With SUBMIT_ALL=true and SITEMAP_FILE set, it sends every
URL in that file instead (for sites deployed by hand rather than from GitHub).
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from urllib.parse import quote, urlsplit

ENDPOINT = "https://api.indexnow.org/indexnow"
MAX_URLS = 10_000


def env(name, default=""):
    return (os.environ.get(name) or default).strip()


SITE_URL = env("SITE_URL").rstrip("/")
HOST = urlsplit(SITE_URL).netloc
ROOT = env("SITE_ROOT", ".").strip("/") or "."
KEY = env("INDEXNOW_KEY")
SUBMIT_ALL = env("SUBMIT_ALL", "false").lower() == "true"
DRY_RUN = env("DRY_RUN", "false").lower() == "true"


def log(msg):
    print(msg, flush=True)


def summary(lines):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")


def git(*args, check=True):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), r.stderr.strip()))
    return r.stdout if r.returncode == 0 else None


def repo_path(rel):
    return rel if ROOT == "." else "%s/%s" % (ROOT, rel)


def sitemap_urls(sha):
    """URLs in sitemap.xml at a commit (or in SITEMAP_FILE on disk), limited to this site's host."""
    if sha == "FILE":
        with open(env("SITEMAP_FILE"), encoding="utf-8") as f:
            text = f.read()
    else:
        text = git("show", "%s:%s" % (sha, repo_path("sitemap.xml")), check=False)
    if not text:
        return set()
    urls = set(re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", text))
    return {u for u in urls if urlsplit(u).netloc == HOST}


def files_for(url):
    """Repository files that render a URL, given cleanUrls and either slash style."""
    path = urlsplit(url).path.lstrip("/")
    if path == "":
        cands = ["index.html"]
    elif path.endswith("/"):
        cands = [path + "index.html", path.rstrip("/") + ".html"]
    else:
        cands = [path + ".html", path + "/index.html", path]
    return [repo_path(c) for c in cands]


def gh_get(path):
    token = env("GH_TOKEN")
    req = urllib.request.Request(
        "https://api.github.com" + path,
        headers={"Accept": "application/vnd.github+json",
                 "Authorization": "Bearer " + token,
                 "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def previous_production_sha(head):
    """SHA of the last successful production deploy before this one, if any."""
    repo, envname, current = env("REPO"), env("ENVIRONMENT"), env("DEPLOYMENT_ID")
    if not (repo and envname and env("GH_TOKEN")):
        return None
    try:
        q = quote(envname)
        deps = gh_get("/repos/%s/deployments?environment=%s&per_page=50" % (repo, q))
        for d in deps:
            if str(d["id"]) == current or d["sha"] == head:
                continue
            statuses = gh_get("/repos/%s/deployments/%s/statuses?per_page=1" % (repo, d["id"]))
            if statuses and statuses[0].get("state") == "success":
                return d["sha"]
    except Exception as e:  # the fallback below still gives a sensible diff
        log("Could not read earlier deployments (%s); falling back to the parent commit." % e)
    return None


def changed_urls(base, head):
    now, before = sitemap_urls(head), sitemap_urls(base)
    changed = set(filter(None, (git("diff", "--name-only", base, head) or "").splitlines()))
    urls = {u for u in now if any(f in changed for f in files_for(u))}
    urls |= now - before      # new pages
    urls |= before - now      # removed pages, so Bing re-crawls and sees the redirect or 404
    return sorted(urls)


def key_is_live(attempts=12, wait=10):
    url = "%s/%s.txt" % (SITE_URL, KEY)
    for i in range(attempts):
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                if r.read().decode("utf-8").strip() == KEY:
                    log("Key file live at %s" % url)
                    return True
        except Exception as e:
            log("Key file not live yet (%s), try %d of %d" % (e, i + 1, attempts))
        time.sleep(wait)
    return False


def submit(urls):
    body = json.dumps({"host": HOST, "key": KEY,
                       "keyLocation": "%s/%s.txt" % (SITE_URL, KEY),
                       "urlList": urls}).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def main():
    if not (SITE_URL and KEY):
        log("SITE_URL and INDEXNOW_KEY must be set.")
        return 1
    if SUBMIT_ALL and env("SITEMAP_FILE"):
        # Hand deploys (The Den's deploy.sh): send what is on disk, committed or not.
        urls = sorted(sitemap_urls("FILE"))
        reason = "every URL in %s" % env("SITEMAP_FILE")
    elif SUBMIT_ALL:
        head = env("HEAD_SHA") or git("rev-parse", "HEAD").strip()
        urls = sorted(sitemap_urls(head))
        reason = "every URL in the sitemap (manual run)"
    else:
        head = env("HEAD_SHA") or git("rev-parse", "HEAD").strip()
        base = env("BASE_SHA") or previous_production_sha(head)
        if not base:
            base = (git("rev-parse", head + "^1", check=False) or "").strip()
        if not base:
            log("No earlier commit to compare with; nothing submitted.")
            return 0
        urls = changed_urls(base, head)
        reason = "pages changed between %s and %s" % (base[:7], head[:7])

    log("%d URL(s): %s" % (len(urls), reason))
    for u in urls:
        log("  " + u)
    if not urls:
        summary(["IndexNow: no page changed in this deploy, nothing submitted."])
        return 0
    if len(urls) > MAX_URLS:
        urls = urls[:MAX_URLS]
    if DRY_RUN:
        log("Dry run: nothing submitted.")
        return 0
    if not key_is_live():
        log("Key file never came up on %s; not submitting." % SITE_URL)
        return 1

    status, text = submit(urls)
    log("IndexNow answered %s %s" % (status, text[:300]))
    ok = status in (200, 202)
    summary(["IndexNow: %s %d URL(s) (%s), answer %s." % (
        "submitted" if ok else "FAILED to submit", len(urls), reason, status)] +
        ["- " + u for u in urls[:50]])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
