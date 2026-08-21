"""JS-rendered pages: wait for the thing you need, or click your way to it.

Rendering costs more than the HTTP tier, so only reach for it when the content
is genuinely absent from the raw HTML — check with `render=False` first.
"""
from qd import scrape

URL = "https://quotes.toscrape.com/js/"

raw = scrape(url=URL, render=False, format="text")
print("without render:", len(raw.get("text", "")), "chars")

rendered = scrape(
    url=URL,
    render=True,
    waitForSelector=".quote",
    scrollToBottom=True,
    format="text",
)
print("with render   :", len(rendered.get("text", "")), "chars")

# Interactions run in order before the capture: dismiss a banner, then load more.
interactive = scrape(
    url=URL,
    render=True,
    actions=[
        {"click": ".quote"},
        {"scroll": "bottom"},
        {"wait": 1000},
    ],
    format="markdown",
)
print("after actions :", len(interactive.get("markdown", "")), "chars")
