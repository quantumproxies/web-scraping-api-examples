"""Full-page screenshot from the same endpoint — base64 PNG in the payload."""
import base64
import pathlib

from qd import scrape

page = scrape(url="https://quanticdata.io/", render=True, screenshot="fullPage")

raw = page.get("screenshot") or ""
if raw.startswith("data:"):
    raw = raw.split(",", 1)[1]

out = pathlib.Path("screenshot.png")
out.write_bytes(base64.b64decode(raw))
print(f"wrote {out} ({out.stat().st_size // 1024} KB)")
