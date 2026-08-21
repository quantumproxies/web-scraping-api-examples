"""Read the SPA's data, not its DOM.

Modern sites hydrate from a JSON blob (__NEXT_DATA__, Nuxt payload, JSON islands)
or fetch it over XHR. Both are cleaner than the rendered HTML and often contain
fields the page never displays.

  app_state="auto"  mine the hydration blob into payload.metadata.appState
  xhr=True          record the page's own fetch/XHR traffic into payload.xhr
"""
import json

from qd import scrape

page = scrape(url="https://quanticdata.io/collectors/", app_state="auto", format="markdown")
state = (page.get("metadata") or {}).get("appState")
print("hydration state:", "found" if state else "none on this page")
if state:
    print(json.dumps(state, indent=2)[:600])

# Discover which endpoint the page calls, then hit it directly next time.
traffic = scrape(url="https://quotes.toscrape.com/js/", xhr=True)
for call in (traffic.get("xhr") or [])[:10]:
    print(f"{call.get('status')} {call.get('method')} {call.get('url')}")
