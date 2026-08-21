"""Tiny shared client for the QuanticData API — imported by every example here."""
import os

import requests

BASE = "https://api.quanticdata.io/v1"
_session = requests.Session()


def scrape(**body):
    """POST /v1/scrape and return the payload, or raise with the API's own message."""
    key = os.environ.get("QUANTICDATA_API_KEY")
    if not key:
        raise SystemExit("set QUANTICDATA_API_KEY — https://app.quanticdata.io/register")

    r = _session.post(
        f"{BASE}/scrape",
        json=body,
        headers={"Authorization": f"Bearer {key}"},
        timeout=180,
    )
    data = r.json()
    if data.get("type") == "error" or not r.ok:
        raise RuntimeError(f"scrape failed ({r.status_code}): {data.get('message')}")
    return data.get("payload", {})
