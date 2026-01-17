"""
Kinovod Auto-Domain Redirector

This module provides an asynchronous domain availability checker for kinovod*.pro.

Key features:
- Checks the availability of domains for today and up to 10 days back.
- Uses aiohttp + asyncio to perform all HTTP checks concurrently for maximum speed.
- Automatically selects the most recent working domain.
- Caches the discovered working URL for the lifetime of the process to avoid repeated lookups.
- Integrates with Flask: users are redirected to the first available domain or shown an error page.
"""

import datetime
import asyncio
import aiohttp
from flask import Flask, redirect, render_template

app = Flask(__name__)

# Cache the discovered working URL for the lifetime of the process
cached_url = None


def get_date_shift(days_shift: int) -> str:
    """Return a date string (DDMMYY) shifted by N days from today."""
    target_date = datetime.datetime.today() - datetime.timedelta(days=days_shift)
    return target_date.strftime("%d%m%y")


async def check_url(session, url):
    """Check if the given URL is accessible (HTTP 200)."""
    try:
        async with session.get(url, timeout=3) as resp:
            return url if resp.status == 200 else None
    except:
        return None


async def find_available_domain():
    """Find the first accessible domain from today up to 5 days back."""
    global cached_url

    # Return cached result immediately if previously found
    if cached_url:
        return cached_url

    base = "http://kinovod{}.pro"

    # Generate list of URLs for the last 6 days (0 = today)
    urls = [
        base.format(get_date_shift(shift))
        for shift in range(0, 6)
    ]

    # Perform all checks concurrently
    async with aiohttp.ClientSession() as session:
        tasks = [check_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    # Return the first available URL (most recent)
    for result in results:
        if result:
            cached_url = result
            return result

    return None


@app.route('/')
def index():
    """Main route: redirect to the first available domain or show error page."""
    url = asyncio.run(find_available_domain())

    if url:
        return redirect(url)

    return render_template("error.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)

