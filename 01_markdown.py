"""The minimal scrape — and what contentMode actually changes.

`smart` keeps the page minus nav/footer/cookie chrome, `article` runs Readability
(the right call for news and blog posts), `full` returns the entire <body>.
Same fetch, three different amounts of noise to pay tokens for.
"""
from qd import scrape

URL = "https://quanticdata.io/blog/what-is-a-web-scraper-api/"

for mode in ("smart", "article", "full"):
    page = scrape(url=URL, format="markdown", contentMode=mode)
    md = page.get("markdown", "")
    print(f"{mode:<8} {len(md):>7} chars   title={(page.get('metadata') or {}).get('title')!r}")

# Several formats from one fetch — you are billed once.
both = scrape(url=URL, format="markdown", formats=["markdown", "text"])
print("\nformats returned:", list((both.get("formats") or {}).keys()) or ["markdown"])
print("cost:", (both.get("usage") or {}).get("cost_usd"))
