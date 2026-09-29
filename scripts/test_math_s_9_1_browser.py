#!/usr/bin/env python3
"""Real Chromium interaction and degraded-fallback checks for S-9-1."""
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


def find_lesson(page):
    page.locator("#search").fill("S-9-1")
    card = page.locator(".card").filter(has_text="相似形").first
    card.wait_for()
    return card


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="")
    args = parser.parse_args()
    chrome = Path(os.environ.get("TW_BROWSER_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(ROOT)))
    Thread(target=server.serve_forever, daemon=True).start()
    url = args.url or f"http://127.0.0.1:{server.server_port}/site/index.html"
    errors: list[str] = []
    with sync_playwright() as playwright:
        launch = {"headless": True}
        if chrome.is_file():
            launch["executable_path"] = str(chrome)
        browser = playwright.chromium.launch(**launch)

        fallback = browser.new_page(viewport={"width": 375, "height": 900})
        fallback.on("pageerror", lambda error: errors.append(f"fallback: {error}"))
        blocked: list[str] = []

        def block_simulation(route):
            if route.request.url.endswith("/simulations.js"):
                blocked.append(route.request.url)
                route.abort()
            else:
                route.continue_()

        fallback.route("**/*", block_simulation)
        fallback.goto(url, wait_until="networkidle")
        fallback_card = find_lesson(fallback)
        assert len(blocked) == 1, blocked
        assert fallback_card.locator(".lesson-sections article").count() == 6
        assert fallback_card.locator(".simulation").count() == 0
        assert "互動模型目前無法載入" in fallback_card.locator(".simulation-fallback").inner_text()
        activity = fallback_card.locator(".activity")
        assert activity.locator(".activity-step").count() == 4
        wrong = activity.locator(".activity-step").nth(0).locator("[data-answer]").nth(1)
        wrong.focus()
        fallback.keyboard.press("Enter")
        assert activity.locator(".feedback").nth(0).inner_text().strip()
        right = activity.locator(".activity-step").nth(0).locator("[data-answer]").first
        right.focus()
        fallback.keyboard.press("Enter")
        assert "固定邊界" in activity.locator(".feedback").nth(0).inner_text()

        page = browser.new_page(viewport={"width": 375, "height": 900})
        page.on("pageerror", lambda error: errors.append(f"interactive: {error}"))
        page.goto(url, wait_until="networkidle")
        card = find_lesson(page)
        model = card.locator(".sim-similarity-lab")
        assert model.count() == 1
        assert model.locator('[data-sim-control="scaleX"]').count() == 0, "prediction must gate manipulation"
        model.locator('[data-sim-similarity="prediction"][data-value="yes"]').click()
        model.locator('[data-sim-similarity="submit-prediction"]').click()
        scale_x = model.locator('[data-sim-control="scaleX"]')
        scale_x.focus()
        page.keyboard.press("ArrowRight")
        assert scale_x.input_value() == "1.25"
        assert "1.25" in model.locator("tbody").inner_text()
        model.locator('[data-sim-similarity="verify"][data-value="no"]').click()
        model.locator('[data-sim-similarity="check"]').click()
        assert "判斷正確" in model.locator(".sim-status").nth(1).inner_text()
        model.locator('[data-sim-similarity="transfer"][data-value="yes"]').click()
        model.locator('[data-sim-similarity="submit-transfer"]').click()
        assert "5→2.5 與 7→3.5" in model.locator(".sim-status").nth(2).inner_text()
        page.reload(wait_until="networkidle")
        card = find_lesson(page)
        model = card.locator(".sim-similarity-lab")
        assert model.locator('[data-sim-control="scaleX"]').input_value() == "1.25", "saved state survives reload"
        widths = {}
        for width in (320, 375, 768):
            page.set_viewport_size({"width": width, "height": 900})
            widths[str(width)] = page.evaluate("({body:document.body.scrollWidth,doc:document.documentElement.scrollWidth,client:document.documentElement.clientWidth})")
            assert widths[str(width)]["body"] <= width and widths[str(width)]["doc"] <= width, widths
        card.locator(".simulation [data-sim-reset]").click()
        assert card.locator('[data-sim-control="scaleX"]').count() == 0, "reset restores prediction lock"
        assert not errors, errors
        browser.close()
    server.shutdown()
    print(json.dumps({"status": "passed", "blockedSimulationScript": blocked, "fallbackSections": 6, "fallbackGuidedChoice": 4, "similarityStages": ["predict", "manipulate", "observe", "explain", "verify", "transfer"], "keyboardScale": "1.25", "transfer": "5×7 -> 2.5×3.5", "statePersistence": "pass", "responsiveWidths": widths, "pageErrors": errors}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
