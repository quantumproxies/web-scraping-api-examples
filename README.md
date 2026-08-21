# Web Scraping API examples — page to Markdown, HTML, JSON or screenshot

Practical Python examples for the [QuanticData Web Scraping API](https://quanticdata.io/web-scraping-api/):
one `POST /v1/scrape` that hands back a page already cleaned, rendered when needed, and shaped
the way you want it — Markdown for LLMs, HTML for parsers, CSS-extracted JSON for pipelines.

$0.0002 per page, and a failed fetch costs nothing.

```bash
pip install requests
export QUANTICDATA_API_KEY=qd_live_your_key_here
python3 01_markdown.py
```

## The examples

| File | What it shows |
|---|---|
| [`01_markdown.py`](01_markdown.py) | the minimal call, plus `contentMode` (`smart` / `article` / `full`) side by side |
| [`02_css_extract.py`](02_css_extract.py) | `extract` — a `{field: selector}` schema turned into a JSON row, no BeautifulSoup |
| [`03_render_actions.py`](03_render_actions.py) | JS pages: `render`, `waitForSelector`, `scrollToBottom`, `actions` (click, scroll) |
| [`04_screenshot.py`](04_screenshot.py) | full-page PNG out of the same endpoint |
| [`05_geo.py`](05_geo.py) | the same URL from five countries — localized prices, currencies and redirects |
| [`06_app_state.py`](06_app_state.py) | `app_state` / `xhr`: read the SPA's own hydration data instead of its DOM |

## Parameters you will actually use

| Field | Values | Notes |
|---|---|---|
| `url` | http/https | required (or pass `html` to convert a document you already have) |
| `format` | `markdown` (default), `html`, `text` | `formats: [...]` returns several at once |
| `contentMode` | `smart` (default), `article`, `full` | `article` is Readability — news and blogs |
| `render` | `true` / `false` | stealth headless browser; needed for JS-only content |
| `waitForSelector`, `waitMs`, `scrollToBottom` | | render mode only |
| `actions` | `[{"click":"#accept"},{"scroll":"bottom"}]` | ordered interactions before capture |
| `extract` | `{field: "css selector"}` | structured JSON in `payload.data` |
| `ai_prompt` / `ai_schema` | text / JSON Schema | LLM extraction, lands in `payload.ai.data` |
| `screenshot` | `true` or `"fullPage"` | base64 PNG |
| `country`, `state`, `city` | ISO code + names | proxy exit geo |
| `rotation`, `sessionId`, `sessionDuration` | `rotating` / `sticky` | keep one IP across calls |
| `mode` | `"summary"` | metadata only — the cheap view for audits |

Full reference: [quanticdata.io/docs](https://quanticdata.io/docs/).

## Many URLs at once

`POST /v1/batch` takes up to 1,000 URLs and answers with a job id — see
[batch-url-scraping-jobs](https://github.com/quantumproxies/batch-url-scraping-jobs).
For a whole site you do not have a URL list for, use
[Crawl & Map](https://quanticdata.io/crawl-map/).

## Related

- [What is a web scraper API?](https://quanticdata.io/blog/what-is-a-web-scraper-api/)
- [Web scraping with Python, start to finish](https://quanticdata.io/blog/how-to-web-scraping-using-python/)
- [Is web scraping legal in the US?](https://quanticdata.io/blog/is-web-scraping-legal-in-us/)
- [Ready-made Collectors](https://quanticdata.io/collectors/) — when a semantic input beats a URL

MIT licensed.
