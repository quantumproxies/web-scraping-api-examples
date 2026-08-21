"""One URL, five exits — what a page looks like from each market.

Geo matters more than people expect: currency, tax-inclusive prices, stock,
consent walls and outright redirects all change with the exit IP.
"""
from concurrent.futures import ThreadPoolExecutor

from qd import scrape

URL = "https://www.apple.com/shop/buy-iphone"
COUNTRIES = ["us", "gb", "de", "jp", "br"]


def probe(country: str) -> tuple[str, str]:
    page = scrape(url=URL, country=country, mode="summary")
    meta = page.get("metadata") or {}
    return country, f"{meta.get('title')!r} -> {meta.get('canonical')}"


with ThreadPoolExecutor(max_workers=5) as pool:
    for country, line in pool.map(probe, COUNTRIES):
        print(f"{country:<3} {line}")
