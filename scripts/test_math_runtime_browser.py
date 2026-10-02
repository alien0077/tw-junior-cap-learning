#!/usr/bin/env python3
"""Real-Chromium QA for the complete math workbench and production simulations."""
from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path
from urllib.parse import urlsplit

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]


async def run(url: str, browser_channel: str) -> dict:
    async with async_playwright() as playwright:
        system_chrome = Path(os.environ.get(
            "TW_BROWSER_CHROME",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        ))
        launch_kwargs = {"headless": True}
        if system_chrome.is_file():
            launch_kwargs["executable_path"] = str(system_chrome)
        elif browser_channel:
            launch_kwargs["channel"] = browser_channel

        browser = await playwright.chromium.launch(**launch_kwargs)
        page = await browser.new_page(viewport={"width": 375, "height": 900})
        page_errors: list[str] = []
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        await page.goto(url, wait_until="networkidle")

        values = await page.locator("#unit option").evaluate_all(
            "(options) => options.map(o => o.value).filter(v => v.startsWith('cur-math-'))"
        )
        assert len(values) == 125, f"expected 125 math specs, got {len(values)}"

        viewport_results: dict[str, dict] = {}
        for width in (320, 375, 768):
            await page.set_viewport_size({"width": width, "height": 900})
            checked = 0
            for value in values:
                await page.select_option("#unit", value)
                article = page.locator("article.student-lesson-shell")
                assert await article.get_attribute("data-lesson-id") == value, value
                assert await page.locator("article section[data-section]").count() == 7, value
                assert await page.locator(".interactive-block").count() >= 1, value
                semantic = await page.locator(".component-visual-body").first.get_attribute("data-semantic-model")
                assert semantic, value
                title = (await page.locator(".interactive-block h3").first.text_content() or "").strip()
                assert title and not title.endswith("Block") and not title.endswith("Lab"), (value, title)
                placeholder = await page.locator(".component-visual-prompts").first.text_content()
                assert placeholder and "待由本單元操作資料填入" not in placeholder, value
                overflow = await page.evaluate("""() => ({
                    body: document.body.scrollWidth,
                    doc: document.documentElement.scrollWidth,
                    client: document.documentElement.clientWidth
                })""")
                assert overflow["body"] <= width and overflow["doc"] <= width, (value, width, overflow)
                checked += 1
            viewport_results[str(width)] = {"checkedMathSpecs": checked}

        # Shared state-machine and keyboard/a11y semantics on a representative math unit.
        await page.set_viewport_size({"width": 375, "height": 900})
        await page.select_option("#unit", "cur-math-content-a-8-1")
        assert await page.locator(".math-live-lab").count() == 1
        assert await page.locator(".math-live-canvas").count() == 1
        buttons = page.locator(".interactive-controls button")
        await buttons.nth(0).click()
        await buttons.nth(1).click()
        await buttons.nth(2).click()
        explanation = page.locator('input[aria-label="用一句話說明觀察到的關係"]')
        await explanation.fill("操作後圖形與數值同步改變，因此可用兩種表徵互相檢查。")
        await buttons.nth(3).click()
        await buttons.nth(4).click()
        assert "已檢核" in (await page.locator(".interactive-status").text_content() or "")

        cdp = await page.context.new_cdp_session(page)
        ax_tree = await cdp.send("Accessibility.getFullAXTree")
        def ax_value(node: dict, key: str):
            return node.get(key, {}).get("value")
        statuses = [node for node in ax_tree["nodes"] if ax_value(node, "role") == "status"]
        assert statuses, "math workbench has no accessibility status node"
        status_properties = {
            item.get("name"): item.get("value", {}).get("value")
            for item in statuses[0].get("properties", [])
        }
        assert status_properties.get("live") == "polite", status_properties

        # Production-site regression for A-7-8: the dedicated range control must open on x < -2.
        parts = urlsplit(url)
        site = await browser.new_page(viewport={"width": 375, "height": 900})
        site_errors: list[str] = []
        site.on("pageerror", lambda error: site_errors.append(str(error)))
        await site.goto(f"{parts.scheme}://{parts.netloc}/site/index.html", wait_until="networkidle")
        await site.locator("#status").wait_for()
        await site.locator("#search").fill("lesson-math-content-a-7-8")
        simulation = site.locator('[data-simulation-lesson^="lesson-math-content-a-7-8:"]')
        await simulation.wait_for()
        live_svg = simulation.locator(".sim-stage svg").first
        aria = await live_svg.get_attribute("aria-label")
        assert aria and "x ＜ -2" in aria and "端點不包含" in aria and "向左延伸" in aria, aria
        slider = simulation.locator('[data-sim-control="boundary"]')
        assert await slider.get_attribute("min") == "-6"
        assert await slider.get_attribute("max") == "4"
        assert await slider.input_value() == "-2"
        assert await simulation.locator('[data-inequality-relation="less"]').get_attribute("aria-pressed") == "true"
        stage_text = await simulation.locator(".sim-stage").inner_text()
        assert "-3 符合" in stage_text and "-2 不符合" in stage_text and "-1 不符合" in stage_text, stage_text

        await slider.fill("-3")
        simulation = site.locator('[data-simulation-lesson^="lesson-math-content-a-7-8:"]')
        await simulation.wait_for()
        aria = await simulation.locator(".sim-stage svg").first.get_attribute("aria-label")
        assert aria and "x ＜ -3" in aria, aria
        await simulation.locator('[data-inequality-relation="at-least"]').click()
        simulation = site.locator('[data-simulation-lesson^="lesson-math-content-a-7-8:"]')
        aria = await simulation.locator(".sim-stage svg").first.get_attribute("aria-label")
        assert aria and "x ≥ -3" in aria and "端點包含" in aria and "向右延伸" in aria, aria

        production_viewports = {}
        for width in (320, 375, 768):
            await site.set_viewport_size({"width": width, "height": 900})
            metrics = await site.evaluate("""() => ({
                body: document.body.scrollWidth,
                doc: document.documentElement.scrollWidth,
                client: document.documentElement.clientWidth
            })""")
            assert metrics["body"] <= width and metrics["doc"] <= width, (width, metrics)
            production_viewports[str(width)] = metrics

        assert not page_errors, page_errors
        assert not site_errors, site_errors
        await site.close()
        await browser.close()
        return {
            "status": "passed",
            "mathSpecCount": len(values),
            "workbenchViewports": viewport_results,
            "productionA78": {
                "initial": "x < -2",
                "manipulatedBoundary": -3,
                "relationToggle": "x >= -3",
                "viewports": production_viewports,
            },
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/implementation/workbench.html")
    parser.add_argument("--browser-channel", default="")
    args = parser.parse_args()
    result = asyncio.run(run(args.url, args.browser_channel))
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
