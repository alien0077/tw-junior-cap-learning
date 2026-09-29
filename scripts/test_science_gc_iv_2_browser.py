#!/usr/bin/env python3
"""Real-browser regression for the Gc-IV-2 learner-facing food-web model."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from playwright.sync_api import sync_playwright


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    args = parser.parse_args()
    chrome = Path(os.environ.get("TW_BROWSER_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
    errors: list[str] = []
    with sync_playwright() as playwright:
        launch = {"headless": True}
        if chrome.is_file():
            launch["executable_path"] = str(chrome)
        browser = playwright.chromium.launch(**launch)
        page = browser.new_page(viewport={"width": 375, "height": 900})
        page.route("**/*", lambda route: route.continue_() if route.request.url.startswith(("http://127.0.0.1:8765/", "http://localhost:8765/")) else route.abort())
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(args.url, wait_until="networkidle")
        page.get_by_label("搜尋我們的教材或題目").fill("Gc-Ⅳ-2")
        card = page.locator(".card").filter(has_text="生物多樣性與生態系穩定").first
        card.wait_for()
        assert card.locator(".lesson-sections article").count() == 6
        assert card.locator(".lesson-sections").inner_text().count("池塘少了一種生物") == 1
        assert card.locator(".sim-pond-web").count() == 1
        assert "概念示意，不是實測食物網" in card.locator(".sim-pond-web").inner_text()
        control = card.get_by_role("slider", name="水草擾動情境")
        control.focus()
        page.keyboard.press("ArrowRight")
        assert control.input_value() == "1"
        assert "局部移除部分水草" in card.locator(".sim-pond-web").inner_text()
        page.keyboard.press("ArrowRight")
        assert control.input_value() == "2"
        assert "不能由此模型推定池塘必然崩解" in card.locator(".sim-pond-web").inner_text()
        widths = {}
        for width in (320, 375, 768):
            page.set_viewport_size({"width": width, "height": 900})
            widths[str(width)] = page.evaluate("({body: document.body.scrollWidth, document: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})")
            assert widths[str(width)]["body"] <= width and widths[str(width)]["document"] <= width, widths
        assert not errors, errors
        browser.close()
    print(json.dumps({"status": "passed", "url": args.url, "visibleSections": 6, "keyboardDisturbanceStates": [1, 2], "offlineFallback": "local model remains interactive with external requests blocked", "responsiveWidths": widths, "pageErrors": errors}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
