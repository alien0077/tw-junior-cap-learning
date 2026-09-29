#!/usr/bin/env python3
"""Verify S-9-13 lesson and guided-choice fallback if its simulation script is unavailable."""
from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="")
    args = parser.parse_args()
    chrome = Path(os.environ.get("TW_BROWSER_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
    errors: list[str] = []
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(ROOT)))
    Thread(target=server.serve_forever, daemon=True).start()
    url = args.url or f"http://127.0.0.1:{server.server_port}/site/index.html"
    with sync_playwright() as playwright:
        launch = {"headless": True}
        if chrome.is_file():
            launch["executable_path"] = str(chrome)
        browser = playwright.chromium.launch(**launch)
        page = browser.new_page(viewport={"width": 375, "height": 900})
        page.on("pageerror", lambda error: errors.append(str(error)))
        blocked: list[str] = []

        def route_request(route):
            if route.request.url.endswith("/simulations.js"):
                blocked.append(route.request.url)
                route.abort()
            else:
                route.continue_()

        page.route("**/*", route_request)
        page.goto(url, wait_until="networkidle")
        page.locator("#search").fill("S-9-13")
        card = page.locator(".card").filter(has_text="表面積與體積").first
        card.wait_for()
        assert len(blocked) == 1, blocked
        assert card.locator(".lesson-sections article").count() == 6
        assert card.locator(".sim-prism-lab").count() == 0, "unavailable model should not leave a broken/empty simulation"
        choices = card.locator(".activity")
        assert choices.count() == 1, "the lesson's text-based practice must remain available"
        first = choices.locator("button").first
        first.focus()
        page.keyboard.press("Enter")
        assert choices.locator(".feedback").first.inner_text().strip(), "keyboard answer should produce visible feedback"
        assert not errors, errors
        browser.close()
    server.shutdown()
    print(json.dumps({"status": "passed", "blockedSimulationScript": blocked, "visibleLessonSections": 6, "guidedChoiceAvailable": True, "pageErrors": errors}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
