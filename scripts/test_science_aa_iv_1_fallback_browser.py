#!/usr/bin/env python3
"""Verify Aa-IV-1 lesson and text practice remain usable without simulations.js."""
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
    server = None
    if args.url:
        url = args.url
    else:
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(ROOT)))
        Thread(target=server.serve_forever, daemon=True).start()
        url = f"http://127.0.0.1:{server.server_port}/site/index.html"
    with sync_playwright() as playwright:
        launch = {"headless": True}
        if chrome.is_file():
            launch["executable_path"] = str(chrome)
        browser = playwright.chromium.launch(**launch)
        page = browser.new_page(viewport={"width": 375, "height": 950})
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
        page.get_by_label("搜尋我們的教材或題目").fill("Aa-Ⅳ-1")
        card = page.locator(".card").filter(has_text="原子模型演變").first
        card.wait_for()
        assert len(blocked) == 1, blocked
        assert card.locator(".lesson-sections article").count() == 6
        notice = card.locator(".simulation-fallback")
        assert notice.count() == 1
        assert "互動模型目前無法載入" in notice.inner_text()
        assert "完整課文與文字練習仍可使用" in notice.inner_text()
        activity = card.locator(".activity")
        assert activity.count() == 1
        assert activity.locator(".activity-step").count() == 4
        first = activity.locator(".activity-step").first
        first.get_by_role("button", name="B.", exact=False).focus()
        page.keyboard.press("Enter")
        assert "再想一次" in first.locator(".feedback").inner_text()
        first.get_by_role("button", name="A.", exact=False).focus()
        page.keyboard.press("Enter")
        assert "支持電子存在" in first.locator(".feedback").inner_text()
        widths = {}
        for width in (320, 375, 768):
            page.set_viewport_size({"width": width, "height": 950})
            widths[str(width)] = page.evaluate("({body: document.body.scrollWidth, document: document.documentElement.scrollWidth})")
            assert widths[str(width)]["body"] <= width and widths[str(width)]["document"] <= width, widths
        assert not errors, errors
        browser.close()
    if server is not None:
        server.shutdown()
    print(json.dumps({"status": "passed", "blockedSimulationScript": blocked, "visibleLessonSections": 6, "textPracticeSteps": 4, "keyboardRetryAndFeedback": "passed", "responsiveWidths": widths, "pageErrors": errors}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
