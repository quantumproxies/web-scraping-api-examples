"""Structured extraction with CSS selectors — no parser in your codebase.

`extract` maps field names to selectors and returns them under payload.data.
A selector can be a plain string, or an object with `attr` (read an attribute)
and `all` (collect every match instead of the first).
"""
import json

from qd import scrape

page = scrape(
    url="https://news.ycombinator.com/",
    extract={
        "titles": {"selector": ".titleline > a", "all": True},
        "links": {"selector": ".titleline > a", "attr": "href", "all": True},
        "points": {"selector": ".score", "all": True},
    },
)

data = page.get("data", {})
rows = [
    {"title": t, "url": u, "points": p}
    for t, u, p in zip(data.get("titles", []), data.get("links", []), data.get("points", []))
]
print(json.dumps(rows[:10], indent=2))
print(f"\n{len(rows)} rows for ${(page.get('usage') or {}).get('cost_usd')}")
