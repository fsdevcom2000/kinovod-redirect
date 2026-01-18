"""
Kinovod Auto-Domain Redirector

This module provides an asynchronous domain availability checker for kinovod*.pro.

Key features:
- Checks the availability of domains for today and up to 5 days back.
- Uses aiohttp + asyncio to perform all HTTP checks concurrently for maximum speed.
- Automatically selects the most recent working domain.
- Integrates with Flask: users are redirected to the first available domain or shown an error page.

Author: fsdevcom2000
URL: https://github.com/fsdevcom2000/kinovod-redirect

"""

import datetime
import asyncio
import aiohttp
from flask import Flask, render_template, jsonify



app = Flask(__name__)

MAX_LOGS = 100

# In-memory log storage
logs = []


def log_event(event_type, message, extra=None):
    """Append structured log entry."""
    logs.append({
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "event": event_type,
        "message": message,
        "extra": extra or {}
    })
    # Clear log
    if len(logs) > MAX_LOGS: 
        del logs[:-MAX_LOGS] # clear all except last N



def get_date_shift(days_shift: int) -> str:
    target_date = datetime.datetime.today() - datetime.timedelta(days=days_shift)
    return target_date.strftime("%d%m%y")


async def check_url(session, url):
    """Check URL: first verify status 200, then try to read at least 30 KB of body."""
    MIN_SIZE = 30 * 1024  # Content size: minimum 30 KB

    try:
        # 1. Fast status check (timeout 7 sec)
        async with session.get(url, timeout=7) as resp:
            if resp.status != 200:
                log_event("check", f"{url} returned non-200", {"status": resp.status})
                return None

            size = 0

            # 2. Read body with timeout via wait_for
            async def read_body():
                nonlocal size
                async for chunk in resp.content.iter_chunked(4096):
                    size += len(chunk)
                    if size >= MIN_SIZE:
                        return True
                return False

            try:
                ok = await asyncio.wait_for(read_body(), timeout=5)
            except Exception as e:
                log_event(
                    "error",
                    f"Timeout while reading body from {url}",
                    {"error": repr(e), "size_bytes": size}
                )
                return None

            if ok:
                log_event(
                    "check",
                    f"{url} accepted: content size OK",
                    {"size_bytes": size}
                )
                return url

            log_event(
                "check",
                f"{url} rejected: content too small",
                {"size_bytes": size}
            )
            return None

    except Exception as e:
        log_event("error", f"Error checking {url}", {"error": repr(e)})
        return None


async def find_available_domain():
    base = "http://kinovod{}.pro"

    urls = [
        base.format(get_date_shift(shift))
        for shift in range(0, 6)
    ]

    log_event("start_check", "Starting domain scan", {"urls": urls})

    async with aiohttp.ClientSession() as session:
        tasks = [check_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for result in results:
        if result:
            log_event("domain_found", "Working domain found", {"url": result})
            return result

    log_event("domain_not_found", "No working domains found")
    return None


# --- ROUTES ----

@app.route('/')
def index():
    return render_template("checking.html")


@app.route('/check')
def check():
    url = asyncio.run(find_available_domain())
    if url:
        return jsonify({"ok": True, "url": url})
    return jsonify({"ok": False})


@app.route('/error')
def error_page():
    return render_template("error.html")


@app.route('/data')
def data():
    """Return logs in JSON format."""
    return jsonify(logs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)
