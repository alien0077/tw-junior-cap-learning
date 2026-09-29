#!/usr/bin/env python3
"""Learner-page regression for Fa-IV-4 original manuscript and atmospheric model."""
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
        page = browser.new_page(viewport={"width": 375, "height": 950})
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(args.url, wait_until="networkidle")
        page.get_by_label("搜尋我們的教材或題目").fill("Fa-Ⅳ-4")
        card = page.locator(".card").filter(has_text="大氣依溫度變化分層").first
        card.wait_for()
        headings = card.locator(".lesson-sections article b").all_text_contents()
        authored_headings = [
            "同一片天空，四種不同的高度線索",
            "一條曲線如何變成四層模型",
            "替四張現象卡找座標，而不是找關鍵字",
            "剖面郵遞：讓證據和現象一起移動",
            "遇到新剖面，先改模型再改答案",
            "把四層模型折回一張圖",
        ]
        assert 6 <= len(headings) <= 10 and len(set(headings)) == len(headings), headings
        assert headings[-6:] == authored_headings, headings
        assert "透明大樓" in card.locator(".lesson-sections").inner_text()
        assert card.locator(".activity-step").count() == 4
        for step in card.locator(".activity-step").all():
            assert step.locator("[data-answer]").count() == 3
        first = card.locator(".activity-step").nth(0)
        first.locator('[data-answer="B"]').click()
        assert "再想一次" in first.locator(".feedback").inner_text()
        first.locator('[data-answer="A"]').click()
        assert "可進入下一步" in first.locator(".feedback").inner_text()

        simulation = card.locator(".simulation[data-simulation-lesson]").first
        assert "大氣溫度剖面模型" in simulation.get_attribute("aria-label")
        assert simulation.locator(".sim-atmos-profile").count() == 1
        assert simulation.locator(".sim-orbit, [data-sim-control]").count() == 0
        assert "日照長度" not in simulation.inner_text()
        assert simulation.locator(".sim-design-steps button").count() == 4
        assert "原創教學示意" in simulation.locator("figcaption").inner_text()
        assert simulation.locator("svg[aria-label]").count() == 1

        shifted = simulation.locator('[data-atmo-scenario="shifted"]')
        shifted.focus()
        page.keyboard.press("Enter")
        assert simulation.locator('[data-atmo-scenario="shifted"]').get_attribute("aria-pressed") == "true"
        assert "假設情境" in simulation.locator("figcaption").inner_text()
        assert page.evaluate("document.activeElement.dataset.atmoScenario") == "shifted"
        assert "55／90 km" in simulation.locator("figcaption").inner_text()
        simulation.get_by_role("button", name="我已提出預測").click()
        assert "已記錄預測" in simulation.locator(".sim-status").inner_text()
        simulation.get_by_role("button", name="我已記錄觀察").click()
        assert "已記錄觀察" in simulation.locator(".sim-status").inner_text()
        reflection = simulation.locator("[data-sim-reflection]")
        reflection.fill("轉折點移動是題設假設，不能當成實測結果。")
        page.reload(wait_until="networkidle")
        page.get_by_label("搜尋我們的教材或題目").fill("Fa-Ⅳ-4")
        card = page.locator(".card").filter(has_text="大氣依溫度變化分層").first
        simulation = card.locator(".simulation[data-simulation-lesson]").first
        assert "轉折點移動" in simulation.locator("[data-sim-reflection]").input_value()
        simulation.locator("[data-sim-reset]").click()
        assert simulation.locator("[data-sim-reflection]").input_value() == ""
        assert "尚未記錄" in simulation.locator(".sim-status").inner_text()

        widths = {}
        for width in (320, 375, 768):
            page.set_viewport_size({"width": width, "height": 950})
            widths[str(width)] = page.evaluate("({body: document.body.scrollWidth, document: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})")
            assert widths[str(width)]["body"] <= width and widths[str(width)]["document"] <= width, widths
        assert not errors, errors

        page.route("**/simulations.js", lambda route: route.abort())
        page.reload(wait_until="networkidle")
        page.get_by_label("搜尋我們的教材或題目").fill("Fa-Ⅳ-4")
        fallback_card = page.locator(".card").filter(has_text="大氣依溫度變化分層").first
        fallback_card.wait_for()
        assert fallback_card.locator(".lesson-sections article").count() >= 6
        assert "互動模型目前無法載入" in fallback_card.locator(".simulation-fallback").inner_text()
        assert fallback_card.locator(".activity-step").count() == 4
        fallback_first = fallback_card.locator(".activity-step").nth(0)
        fallback_first.locator('[data-answer="B"]').click()
        assert "再想一次" in fallback_first.locator(".feedback").inner_text()
        fallback_first.locator('[data-answer="A"]').click()
        assert "可進入下一步" in fallback_first.locator(".feedback").inner_text()
        assert not errors, errors
        browser.close()
    print(json.dumps({"status": "passed", "url": args.url, "visibleSections": len(headings), "visibleAuthoredSections": len(authored_headings), "answeredSteps": 4, "keyboardScenarioSwitch": "passed", "simulationFailureFallback": "passed; lesson and four text questions remain usable", "responsiveWidths": widths, "pageErrors": errors}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
