#!/usr/bin/env python3
"""Exhaustive real-browser QA for every active math lesson.

This is deliberately stricter than the static math coverage audit. It opens the
public lesson page in real Chromium, locates each active math lesson, requires
its production simulation to render, performs a keyboard-driven manipulation,
checks textual/accessibility fallbacks, and verifies the page at the three
mobile/desktop widths named by the unit implementation specs.

The JSON report is only written as PASS when every active lesson passes. A
separate script may promote unit-spec qaStatus only from that PASS report.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from playwright.async_api import Locator, async_playwright

ROOT = Path(__file__).resolve().parents[1]
LESSON_DIR = ROOT / "lessons" / "math"
DEFAULT_REPORT = ROOT / "implementation" / "reports" / "math-browser-qa-current.json"
SUPPORTED_ENGINES = {
    "math-number-line",
    "math-inequality-range",
    "math-algebra-balance",
    "math-ticket-equation",
    "math-equation-meaning",
    "math-reasoning-lab",
    "math-expression-lab",
    "math-function-graph",
    "math-system-graph",
    "math-geometry",
    "math-data-lab",
    "math-probability-lab",
}
VIEWPORTS = (320, 375, 768)


def load_lessons() -> list[dict[str, Any]]:
    lessons: list[dict[str, Any]] = []
    for path in sorted(LESSON_DIR.glob("lesson-math-*.json")):
        lesson = json.loads(path.read_text(encoding="utf-8"))
        if lesson.get("reviewStatus") == "deprecated":
            continue
        lesson["_file"] = path.name
        lessons.append(lesson)
    return lessons


def control_snapshot_script() -> str:
    return """el => {
      const root = el.closest('[data-simulation-lesson]');
      const controls = [...root.querySelectorAll('input,button,select')].map(node => ({
        tag: node.tagName,
        type: node.type || '',
        value: node.value || '',
        checked: Boolean(node.checked),
        pressed: node.getAttribute('aria-pressed'),
        disabled: Boolean(node.disabled)
      }));
      return JSON.stringify({text: root.innerText, controls});
    }"""


async def accessible_name(control: Locator) -> str:
    return await control.evaluate("""el => {
      const labelled = el.getAttribute('aria-labelledby');
      if (labelled) {
        const text = labelled.split(/\\s+/).map(id => document.getElementById(id)?.innerText || '').join(' ').trim();
        if (text) return text;
      }
      const label = el.getAttribute('aria-label') || el.labels?.[0]?.innerText || el.title || el.innerText || el.textContent || '';
      return label.trim();
    }""")


async def mutate_with_keyboard(root: Locator) -> dict[str, Any]:
    candidates = root.locator(
        'input[type="range"]:not([disabled]), input[type="radio"]:not([disabled]), '
        'input[type="checkbox"]:not([disabled]), select:not([disabled]), '
        'button:not([disabled]):not([data-sim-reset])'
    )
    count = await candidates.count()
    if count == 0:
        raise AssertionError("no enabled production interaction control")

    attempts: list[dict[str, str]] = []
    for index in range(min(count, 8)):
        control = candidates.nth(index)
        if not await control.is_visible():
            continue
        name = await accessible_name(control)
        if not name:
            attempts.append({"index": str(index), "reason": "missing accessible name"})
            continue
        tag = await control.evaluate("el => el.tagName.toLowerCase()")
        input_type = (await control.get_attribute("type") or "").lower()
        before = await control.evaluate(control_snapshot_script())
        await control.focus()
        focused = await control.evaluate("el => document.activeElement === el")
        if not focused:
            attempts.append({"index": str(index), "reason": "control could not receive keyboard focus"})
            continue

        if tag == "input" and input_type == "range":
            value = float(await control.input_value())
            minimum = float(await control.get_attribute("min") or value - 1)
            maximum = float(await control.get_attribute("max") or value + 1)
            key = "ArrowLeft" if value >= maximum and value > minimum else "ArrowRight"
            await control.press(key)
        elif tag == "input" and input_type in {"radio", "checkbox"}:
            await control.press("Space")
        elif tag == "select":
            await control.press("ArrowDown")
            await control.press("Enter")
        else:
            await control.press("Enter")

        await asyncio.sleep(0.02)
        # The simulation may rerender the clicked node, so snapshot the current root.
        after = await root.evaluate("""root => JSON.stringify({
          text: root.innerText,
          controls: [...root.querySelectorAll('input,button,select')].map(node => ({
            tag: node.tagName,
            type: node.type || '',
            value: node.value || '',
            checked: Boolean(node.checked),
            pressed: node.getAttribute('aria-pressed'),
            disabled: Boolean(node.disabled)
          }))
        })""")
        if before != after:
            return {"controlIndex": index, "accessibleName": name, "tag": tag, "type": input_type or None}
        attempts.append({"index": str(index), "reason": "keyboard action produced no observable state change"})

    raise AssertionError(f"no keyboard-driven control produced an observable state change: {attempts}")


async def check_lesson(page, lesson: dict[str, Any]) -> dict[str, Any]:
    lesson_id = lesson["id"]
    title = lesson["title"]
    simulation = lesson.get("simulation") or {}
    engine = simulation.get("engine")
    if engine not in SUPPORTED_ENGINES:
        raise AssertionError(f"unsupported production engine: {engine!r}")

    search = page.locator("#search")
    await search.fill(lesson_id)
    card = page.locator("#contentGrid article.card").filter(has=page.locator("h3", has_text=title)).first
    await card.wait_for(state="visible", timeout=10_000)
    sim = card.locator(f'[data-simulation-lesson^="{lesson_id}:"]').first
    await sim.wait_for(state="visible", timeout=10_000)

    text = (await sim.inner_text()).strip()
    if len(text) < 30:
        raise AssertionError("simulation lacks a substantive textual fallback")
    forbidden = ("尚未支援", "待實作", "TODO", "placeholder")
    if any(token.lower() in text.lower() for token in forbidden):
        raise AssertionError(f"placeholder/fallback-only text leaked into production simulation: {text[:160]!r}")

    controls = sim.locator("input,button,select")
    if await controls.count() == 0:
        raise AssertionError("simulation rendered without interactive controls")

    status_like = sim.locator('[role="status"], [aria-live], output, .sim-feedback, .feedback')
    if await status_like.count() == 0:
        raise AssertionError("simulation lacks visible/live feedback output")

    # Engine/model-specific depth checks prevent a generic card with controls from
    # satisfying the exhaustive browser gate.
    model = simulation.get("model")
    if model == "s9-1-polygon-similarity-v1":
        await sim.locator(".sim-similarity-lab").wait_for()
    elif model == "s9-13-prism-surface-volume-v2":
        await sim.locator(".sim-prism-lab").wait_for()
    elif engine in {"math-number-line", "math-inequality-range", "math-function-graph", "math-system-graph"}:
        if await sim.locator('[role="img"]').count() == 0:
            raise AssertionError(f"{engine} rendered without its visual model")
    elif engine == "math-expression-lab" and await sim.locator(".sim-expression-lab").count() == 0:
        raise AssertionError("expression lab renderer missing")
    elif engine == "math-equation-meaning" and await sim.locator(".sim-equation-meaning").count() == 0:
        raise AssertionError("equation-meaning renderer missing")
    elif engine == "math-reasoning-lab" and await sim.locator(".sim-reasoning-lab").count() == 0:
        raise AssertionError("reasoning-lab renderer missing")
    elif engine == "math-data-lab" and await sim.locator(".sim-data-lab").count() == 0:
        raise AssertionError("data-lab renderer missing")
    elif engine == "math-probability-lab" and await sim.locator(".sim-probability-lab").count() == 0:
        raise AssertionError("probability-lab renderer missing")

    interaction = await mutate_with_keyboard(sim)

    viewport_metrics: dict[str, Any] = {}
    for width in VIEWPORTS:
        await page.set_viewport_size({"width": width, "height": 900})
        metrics = await page.evaluate("""() => ({
          body: document.body.scrollWidth,
          doc: document.documentElement.scrollWidth,
          client: document.documentElement.clientWidth
        })""")
        if metrics["body"] > width or metrics["doc"] > width or metrics["client"] > width:
            raise AssertionError(f"horizontal overflow at {width}px: {metrics}")
        viewport_metrics[str(width)] = metrics

    return {
        "id": lesson_id,
        "file": lesson["_file"],
        "engine": engine,
        "model": model,
        "keyboardInteraction": interaction,
        "viewports": viewport_metrics,
    }


async def run(url: str, report_path: Path) -> dict[str, Any]:
    lessons = load_lessons()
    if len(lessons) != 128:
        raise AssertionError(f"expected 128 active math lessons, got {len(lessons)}")

    failures: list[dict[str, str]] = []
    passed: list[dict[str, Any]] = []
    page_errors: list[str] = []

    async with async_playwright() as playwright:
        launch_kwargs: dict[str, Any] = {"headless": True}
        system_chrome = Path(os.environ.get("TW_BROWSER_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
        if system_chrome.is_file():
            launch_kwargs["executable_path"] = str(system_chrome)
        browser = await playwright.chromium.launch(**launch_kwargs)
        page = await browser.new_page(viewport={"width": 375, "height": 900})
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        await page.emulate_media(reduced_motion="reduce")
        await page.goto(url, wait_until="networkidle")
        await page.locator("#search").wait_for()

        for index, lesson in enumerate(lessons, start=1):
            try:
                passed.append(await check_lesson(page, lesson))
            except Exception as exc:  # collect the complete failure set in one run
                failures.append({"id": lesson.get("id", "unknown"), "file": lesson.get("_file", "unknown"), "error": str(exc)})
            if index % 16 == 0:
                print(f"math browser QA progress: {index}/{len(lessons)}")

        # Reduced-motion is part of every math spec's accessibility contract.
        reduced_motion_match = await page.evaluate("() => matchMedia('(prefers-reduced-motion: reduce)').matches")
        if not reduced_motion_match:
            failures.append({"id": "global", "file": "site", "error": "Chromium did not enter reduced-motion mode"})
        await browser.close()

    if page_errors:
        failures.append({"id": "global", "file": "site", "error": f"page errors: {page_errors}"})

    report = {
        "schemaVersion": 1,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceCommit": os.environ.get("GITHUB_SHA") or os.environ.get("MATH_QA_SOURCE_COMMIT") or "local",
        "status": "PASS" if not failures and len(passed) == 128 else "FAIL",
        "scope": {
            "browser": "Chromium/Playwright",
            "activeLessonsExpected": 128,
            "activeLessonsPassed": len(passed),
            "viewports": list(VIEWPORTS),
            "checks": [
                "public lesson card renders",
                "production simulation renders",
                "substantive text fallback is present",
                "live/visible feedback output exists",
                "interactive control has an accessible name",
                "keyboard action causes observable state change",
                "engine/model-specific renderer depth",
                "no horizontal overflow at 320/375/768px",
                "reduced-motion browser mode",
                "zero page runtime errors",
            ],
        },
        "engineCounts": dict(sorted(Counter(item["engine"] for item in passed).items())),
        "failures": failures,
        "lessons": passed,
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "sourceCommit", "scope", "engineCounts", "failures")}, ensure_ascii=False, indent=2))
    if report["status"] != "PASS":
        raise AssertionError(f"math browser QA failed for {len(failures)} issue(s); see {report_path}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/site/index.html")
    parser.add_argument("--report", default=str(DEFAULT_REPORT))
    args = parser.parse_args()
    asyncio.run(run(args.url, Path(args.report)))


if __name__ == "__main__":
    main()
