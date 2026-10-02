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
    "math-visual-area",
    "math-polynomial-model",
    "math-system-model",
    "math-quadratic-model",
    "math-factor-model",
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
VIEWPORTS = (320, 375, 390, 430, 768)


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
        current: node.getAttribute('aria-current'),
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
    for index in range(min(count, 12)):
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
        after = await root.evaluate("""root => JSON.stringify({
          text: root.innerText,
          controls: [...root.querySelectorAll('input,button,select')].map(node => ({
            tag: node.tagName,
            type: node.type || '',
            value: node.value || '',
            checked: Boolean(node.checked),
            pressed: node.getAttribute('aria-pressed'),
            current: node.getAttribute('aria-current'),
            disabled: Boolean(node.disabled)
          }))
        })""")
        if before != after:
            return {"controlIndex": index, "accessibleName": name, "tag": tag, "type": input_type or None}
        attempts.append({"index": str(index), "reason": "keyboard action produced no observable state change"})

    raise AssertionError(f"no keyboard-driven control produced an observable state change: {attempts}")


async def require_count(sim: Locator, selector: str, minimum: int, message: str) -> None:
    count = await sim.locator(selector).count()
    if count < minimum:
        raise AssertionError(f"{message}: expected >= {minimum}, got {count}")


async def assert_renderer_depth(sim: Locator, engine: str, model: str | None) -> None:
    """Verify the lesson reached its dedicated production renderer, not only sim-design."""
    PHASE2_FAMILY_EXPECTED = {
        "linear-function-linked-v1": ("f81Data", ".mff-graph"),
        "a-7-1-like-terms-v1": ("a71Choice", ".mnf-structure"),
        "a-7-3-balance-equation-v1": ("a73Step", ".mnf-structure"),
        "d-7-1-chart-choice-v1": ("d71Chart", ".mdf-chart"),
        "d-7-2-center-outlier-v1": ("d72Outlier", ".mdf-stats"),
        "d-8-1-cumulative-frequency-v1": ("d81Point", ".mdf-curve"),
        "d-9-3-classical-sample-space-v1": ("d93Event", ".mdf-grid"),
        "a-7-6-system-graph-v1": ("a76Case", ".mff-graph"),
        "a-7-7-inequality-meaning-v1": ("a77Relation", ".mff-numberline"),
        "f-8-1-linear-two-point-v1": ("f81Data", ".mff-graph"),
        "f-9-1-quadratic-meaning-v1": ("f91A", ".mff-graph"),
        "f-9-2-parabola-vertex-v1": ("f92A", ".mff-graph"),
        "g-7-1-coordinate-address-v1": ("g71Point", ".mff-graph"),
        "g-8-1-distance-triangle-v1": ("g81Points", ".mff-graph"),
    }
    if model in PHASE2_FAMILY_EXPECTED:
        control, visual = PHASE2_FAMILY_EXPECTED[model]
        await require_count(sim, visual, 1, f"{model} semantic visual missing")
        await require_count(sim, f'[data-sim-control="{control}"]', 1, f"{model} semantic control missing")
        return
    GEOMETRY_FAMILY_EXPECTED = {
        "s-7-5-symmetry-axes-v1": ("s75Shape", ".mgf-proof"),
        "s-8-7-composite-area-v1": ("s87Split", ".mgf-proof"),
        "s-8-8-triangle-properties-v1": ("s88Case", ".mgf-proof"),
        "s-8-9-parallelogram-v1": ("s89Property", ".mgf-proof"),
        "s-8-10-quadrilateral-properties-v1": ("s810Shape", ".mgf-proof"),
        "s-8-11-trapezoid-v1": ("s811Type", ".mgf-proof"),
        "s-8-12-compass-bisector-v1": ("s812Step", ".mgf-proof"),
        "s-9-4-right-triangle-ratio-v1": ("s94Scale", ".mgf-proof"),
        "s-9-5-sector-v1": ("s95Angle", ".mgf-proof"),
        "s-9-6-circle-properties-v1": ("s96Element", ".mgf-proof"),
        "s-9-7-line-circle-relation-v1": ("s97Distance", ".mgf-proof"),
        "s-9-8-circumcenter-v1": ("s9Center", ".mgf-proof"),
        "s-9-9-incenter-v1": ("s9Center", ".mgf-proof"),
        "s-9-10-centroid-v1": ("s9Center", ".mgf-proof"),
        "s-9-11-proof-chain-v1": ("s911Reason", ".mgf-proof"),
        "s-9-12-line-plane-v1": ("s912Relation", ".mgf-proof"),
        "s-7-1-geometry-symbols-v1": ("s71Type", ".mgf-svg"),
        "s-7-2-orthographic-v1": ("s72View", ".mgf-cubes"),
        "s-7-3-perpendicular-bisector-v1": ("s73Point", ".mgf-svg"),
        "s-7-4-reflection-v1": ("s74Axis", ".mgf-svg"),
        "s-8-1-protractor-v1": ("s81Angle", ".mgf-svg"),
        "s-8-2-polygon-triangulation-v1": ("s82Sides", ".mgf-fan"),
        "s-8-3-parallel-transversal-v1": ("s83Relation", ".mgf-svg"),
        "s-8-4-congruence-motion-v1": ("s84Motion", ".mgf-congruence"),
        "s-8-5-triangle-congruence-v1": ("s85Evidence", ".mgf-proof"),
        "s-9-2-triangle-similarity-v1": ("s92Evidence", ".mgf-proof"),
        "s-9-3-parallel-ratio-v1": ("s93Move", ".mgf-svg"),
    }
    if model in GEOMETRY_FAMILY_EXPECTED:
        control, visual = GEOMETRY_FAMILY_EXPECTED[model]
        await require_count(sim, ".mgf-root", 1, f"{model} Geometry-family renderer missing")
        await require_count(sim, visual, 1, f"{model} concept-specific geometry visual missing")
        await require_count(sim, f'[data-sim-control="{control}"]', 1, f"{model} concept-specific control missing")
        return
    NUMBER_FAMILY_EXPECTED = {
        "n-7-1-sieve-v1": ("n71Prediction", ".mnf-hundred"),
        "n-7-2-factor-tree-v1": ("n72Prediction", ".mnf-tree"),
        "n-7-4-operation-laws-v1": ("n74Prediction", ".mnf-structure"),
        "n-7-5-signed-number-line-v1": ("n75Move", ".mnf-line"),
        "n-7-6-exponent-factors-v1": ("n76Exponent", ".mnf-factor-chain"),
        "n-7-7-scientific-place-value-v1": ("n77Place", ".mnf-place"),
        "n-7-8-ratio-table-v1": ("n78Scale", ".mnf-table"),
        "n-7-9-ratio-table-v1": ("n78Scale", ".mnf-table"),
        "n-8-1-square-root-bracket-v1": ("n81Root", ".mnf-root-bar"),
        "n-8-2-root-number-line-v1": ("n81Root", ".mnf-root-bar"),
        "n-8-3-sequence-pattern-v1": ("n83Pattern", ".mnf-sequence"),\n        "n-8-4-arithmetic-sequence-v1": ("n84Case", ".mnf-sequence"),\n        "n-8-5-arithmetic-series-v1": ("n85Series", ".mnf-pairs"),\n        "n-8-3-radical-structure-v1": ("n81Root", ".mnf-root-bar"),
        "n-8-4-radical-operations-v1": ("n81Root", ".mnf-root-bar"),
        "n-8-5-radical-denominator-v1": ("n81Root", ".mnf-root-bar"),
        "n-8-6-chained-ratio-v1": ("n86Ratio", ".mnf-ratio-align"),
    }
    if model in NUMBER_FAMILY_EXPECTED:
        control, visual = NUMBER_FAMILY_EXPECTED[model]
        await require_count(sim, ".mnf-root", 1, f"{model} Number-family renderer missing")
        await require_count(sim, visual, 1, f"{model} concept-specific visual missing")
        await require_count(sim, f'[data-sim-control="{control}"]', 1, f"{model} concept-specific control missing")
        return
    if model == "s9-1-polygon-similarity-v1":
        await require_count(sim, ".sim-similarity-lab", 1, "similarity renderer missing")
        return
    if model == "s9-13-prism-surface-volume-v2":
        await require_count(sim, ".sim-prism-lab", 1, "prism renderer missing")
        return
    if model == "n-7-3-signed-operations-v1":
        await require_count(sim, ".mgs-signed", 1, "signed-operation Gold renderer missing")
        await require_count(sim, '[role="img"]', 1, "signed-operation number line missing")
        prediction = sim.locator('[data-sim-control="n73Prediction"]')
        await require_count(sim, '[data-sim-control="n73Prediction"]', 1, "signed-operation prediction missing")
        await require_count(sim, '[data-sim-control="n73Transfer"]', 1, "signed-operation transfer missing")
        await prediction.select_option("1")
        await require_count(sim, '[data-sim-control="n73Evidence"]', 1, "signed-operation evidence selector missing after prediction")
        return
    if model == "f-8-2-linear-parameter-v1":
        await require_count(sim, ".mgs-function", 1, "linear-parameter Gold renderer missing")
        await require_count(sim, '[role="img"]', 1, "linear-parameter graph missing")
        mode = sim.locator('[data-sim-control="f82Mode"]')
        await require_count(sim, '[data-sim-control="f82Mode"]', 1, "linear-parameter mode missing")
        await require_count(sim, '[data-sim-control="f82Transfer"]', 1, "linear-parameter transfer missing")
        await mode.select_option("0")
        await require_count(sim, '[data-sim-control="f82A"]', 1, "slope control missing")
        await mode.select_option("1")
        await require_count(sim, '[data-sim-control="f82B"]', 1, "intercept control missing")
        await mode.select_option("2")
        await require_count(sim, '[data-sim-control="f82X"]', 1, "intersection input control missing")
        await mode.select_option("0")
        return
    if model == "s-8-6-pythagorean-area-v1":
        await require_count(sim, ".mgs-pythagorean", 1, "Pythagorean Gold renderer missing")
        await require_count(sim, '[role="img"]', 1, "Pythagorean area visual missing")
        prediction = sim.locator('[data-sim-control="s86Prediction"]')
        await require_count(sim, '[data-sim-control="s86Prediction"]', 1, "Pythagorean prediction missing")
        await require_count(sim, '[data-sim-control="s86Transfer"]', 1, "Pythagorean reverse transfer missing")
        await prediction.select_option("1")
        await require_count(sim, '[data-sim-control="s86A"]', 1, "Pythagorean leg-a control missing after prediction")
        await require_count(sim, '[data-sim-control="s86B"]', 1, "Pythagorean leg-b control missing after prediction")
        return
    if model == "d-9-1-boxplot-iqr-v1":
        await require_count(sim, ".mgs-boxplot", 1, "box-plot Gold renderer missing")
        await require_count(sim, '[role="img"]', 1, "box-plot visual missing")
        prediction = sim.locator('[data-sim-control="d91Prediction"]')
        await require_count(sim, '[data-sim-control="d91Prediction"]', 1, "box-plot prediction missing")
        await require_count(sim, '[data-sim-control="d91Transfer"]', 1, "box-plot transfer missing")
        await prediction.select_option("1")
        await require_count(sim, '[data-sim-control="d91MaxA"]', 1, "box-plot maximum control missing after prediction")
        await require_count(sim, '[data-sim-control="d91Q3A"]', 1, "box-plot Q3 control missing after prediction")
        return
    if model == "d-9-2-relative-frequency-v1":
        await require_count(sim, ".mgs-probability", 1, "relative-frequency Gold renderer missing")
        await require_count(sim, '[role="img"]', 1, "relative-frequency plot missing")
        prediction = sim.locator('[data-sim-control="d92Prediction"]')
        await require_count(sim, '[data-sim-control="d92Prediction"]', 1, "relative-frequency prediction missing")
        await require_count(sim, '[data-sim-control="d92Transfer"]', 1, "relative-frequency transfer missing")
        await prediction.select_option("2")
        await require_count(sim, '[data-sim-control="d92Trials"]', 1, "relative-frequency trial-count control missing after prediction")
        return
    if engine == "math-number-line":
        await require_count(sim, '[role="img"]', 1, "number-line visual missing")
        await require_count(sim, '[data-sim-control="n"]', 1, "number-line slider missing")
    elif engine == "math-inequality-range":
        await require_count(sim, '[role="img"]', 1, "inequality number line missing")
        await require_count(sim, '[data-inequality-relation]', 4, "inequality relation controls missing")
        await require_count(sim, '[data-sim-control="boundary"]', 1, "inequality boundary slider missing")
    elif engine == "math-visual-area":
        await require_count(sim, ".mvl-area", 1, "visual area renderer missing")
        await require_count(sim, '[role="img"]', 1, "area-model SVG missing")
        await require_count(sim, '[data-sim-control="formulaMode"]', 1, "formula-mode control missing")
        await require_count(sim, '[data-sim-control="prediction"]', 1, "prediction control missing")
        await require_count(sim, '[data-sim-control="transferPrediction"]', 1, "transfer control missing")
    elif engine == "math-polynomial-model":
        await require_count(sim, ".mvl-poly", 1, "polynomial visual workbench missing")
        mode = sim.locator('[data-sim-control="polyMode"]')
        await require_count(sim, '[data-sim-control="polyMode"]', 1, "polynomial mode control missing")
        await require_count(sim, '[data-sim-control="polyTransfer"]', 1, "polynomial transfer missing")
        await mode.select_option("0")
        await require_count(sim, ".mvl-poly-subtract", 1, "subtraction visual missing")
        await require_count(sim, '[data-sim-control="subtractPrediction"]', 1, "subtraction prediction missing")
        await mode.select_option("1")
        await require_count(sim, ".mvl-poly-multiply", 1, "multiplication grid missing")
        await require_count(sim, '[data-sim-control="multiplyPrediction"]', 1, "multiplication prediction missing")
        await mode.select_option("2")
        await require_count(sim, ".mvl-poly-divide", 1, "division reconstruction visual missing")
        await require_count(sim, '[data-sim-control="dividePrediction"]', 1, "division prediction missing")
        await mode.select_option("0")
    elif engine == "math-quadratic-model":
        if model == "a-8-6-quadratic-meaning-v1":
            await require_count(sim, ".mvl-quadratic-meaning", 1, "quadratic-meaning renderer missing")
            mode = sim.locator('[data-sim-control="quadMeaningMode"]')
            await require_count(sim, '[data-sim-control="quadMeaningMode"]', 1, "quadratic meaning mode control missing")
            await require_count(sim, '[data-sim-control="quadMeaningTransfer"]', 1, "quadratic meaning transfer missing")
            await mode.select_option("0")
            await require_count(sim, ".mvl-q-classify", 1, "quadratic classification visual missing")
            await require_count(sim, '[data-sim-control="quadClassify"]', 1, "quadratic classification prediction missing")
            await mode.select_option("1")
            await require_count(sim, ".mvl-q-root-check", 1, "candidate-root two-side check missing")
            await require_count(sim, '[data-sim-control="quadCandidate"]', 1, "candidate-root control missing")
            await mode.select_option("2")
            await require_count(sim, '[role="img"]', 1, "quadratic context area visual missing")
            await require_count(sim, '[data-sim-control="quadContextPrediction"]', 1, "context-equation prediction missing")
            await mode.select_option("0")
        elif model == "a-8-7-quadratic-solution-v1":
            await require_count(sim, ".mvl-quadratic-solution", 1, "quadratic-solution renderer missing")
            mode = sim.locator('[data-sim-control="quadSolveMode"]')
            await require_count(sim, '[data-sim-control="quadSolveMode"]', 1, "quadratic solution mode control missing")
            await mode.select_option("0")
            await require_count(sim, '[data-sim-control="quadRootPrediction"]', 1, "full-root prediction missing")
            await require_count(sim, '[data-sim-control="quadContextFilter"]', 1, "context-filter control missing")
            await mode.select_option("1")
            await require_count(sim, ".mvl-q-balance", 1, "complete-square balance visual missing")
            await require_count(sim, '[data-sim-control="quadCompleteSquare"]', 1, "complete-square prediction missing")
            await mode.select_option("2")
            await require_count(sim, ".mvl-q-coeff", 1, "quadratic coefficient cards missing")
            await require_count(sim, '[data-sim-control="quadDeltaPrediction"]', 1, "discriminant prediction missing")
            await mode.select_option("3")
            await require_count(sim, ".mvl-q-method-map", 1, "quadratic method map missing")
            await require_count(sim, '[data-sim-control="quadSolutionTransfer"]', 1, "quadratic solution transfer missing")
            await mode.select_option("0")
        else:
            raise AssertionError(f"renderer-depth rule missing for quadratic model {model}")
    elif engine == "math-system-model":
        if model == "a-7-4-system-meaning-v1":
            await require_count(sim, ".mvl-system-meaning", 1, "system-meaning renderer missing")
            await require_count(sim, ".mvl-system-cards", 1, "dual-condition cards missing")
            await require_count(sim, '[data-sim-control="meaningPrediction"]', 1, "system-meaning prediction missing")
            await require_count(sim, '[data-sim-control="systemX"]', 1, "system candidate control missing")
            await require_count(sim, '[data-sim-control="systemMeaningTransfer"]', 1, "system-meaning transfer missing")
        elif model == "a-7-5-system-elimination-v1":
            await require_count(sim, ".mvl-system-elimination", 1, "system-elimination renderer missing")
            await require_count(sim, ".mvl-system-stack", 1, "aligned equation stack missing")
            await require_count(sim, '[data-sim-control="eliminationMethod"]', 1, "elimination prediction missing")
            await require_count(sim, '[data-sim-control="eliminationBack"]', 1, "back-substitution control missing")
            await require_count(sim, '[data-sim-control="eliminationTransfer"]', 1, "elimination transfer missing")
        else:
            raise AssertionError(f"renderer-depth rule missing for system model {model}")
    elif engine == "math-factor-model":
        if model == "a-8-4-factor-meaning-v1":
            await require_count(sim, ".mvl-factor-meaning", 1, "factor-meaning renderer missing")
            await require_count(sim, '[role="img"]', 1, "factor-meaning area visual missing")
            await require_count(sim, '[data-sim-control="factorMeaningX"]', 1, "factor-meaning x control missing")
            await require_count(sim, '[data-sim-control="candidateFactor"]', 1, "factor candidate prediction missing")
            await require_count(sim, '[data-sim-control="factorMeaningTransfer"]', 1, "factor-meaning transfer missing")
        else:
            await require_count(sim, ".mvl-factor-board", 1, "factor-token visual missing")
            await require_count(sim, ".mvl-token", 4, "factor tokens missing")
            await require_count(sim, '[data-sim-control="commonFactor"]', 1, "common-factor prediction missing")
            await require_count(sim, '[data-sim-control="factorTransfer"]', 1, "factor transfer missing")
    elif engine == "math-algebra-balance":
        if model == "a-7-3-linear-equation-check-v1":
            await require_count(sim, ".mvl-linear-equation", 1, "linear-equation verification renderer missing")
            await require_count(sim, '[data-sim-control="linearFirstStep"]', 1, "linear-equation first-step prediction missing")
            await require_count(sim, '[data-sim-control="linearCandidate"]', 1, "linear-equation candidate control missing")
            await require_count(sim, '[data-sim-control="linearTransfer"]', 1, "linear-equation transfer missing")
        else:
            await require_count(sim, ".balance", 1, "algebra balance visual missing")
            await require_count(sim, '[data-sim-control="addend"]', 1, "balance addend slider missing")
            await require_count(sim, '[data-sim-control="target"]', 1, "balance target slider missing")
    elif engine == "math-ticket-equation":
        await require_count(sim, ".sim-ticket-equation", 1, "ticket equation renderer missing")
        await require_count(sim, '[data-ticket-action="check"]', 1, "ticket equation verification control missing")
    elif engine == "math-equation-meaning":
        await require_count(sim, ".sim-equation-meaning", 1, "equation-meaning renderer missing")
        await require_count(sim, '[data-sim-control="x"]', 1, "equation candidate slider missing")
    elif engine == "math-reasoning-lab":
        await require_count(sim, ".sim-reasoning-lab", 1, "reasoning-lab renderer missing")
        await require_count(sim, '[data-reasoning-choice]', 2, "reasoning choices missing")
        await require_count(sim, ".sim-reasoning-feedback", 1, "reasoning feedback missing")
    elif engine == "math-expression-lab":
        await require_count(sim, ".sim-expression-check", 1, "expression equality renderer missing")
        await require_count(sim, '[data-expression-original]', 1, "original expression output missing")
        await require_count(sim, '[data-expression-reduced]', 1, "reduced expression output missing")
        await require_count(sim, '[data-sim-control="x"]', 1, "expression test-value slider missing")
    elif engine == "math-function-graph":
        await require_count(sim, '[role="img"]', 1, "function graph missing")
        await require_count(sim, '[data-sim-control="m"]', 1, "slope slider missing")
        await require_count(sim, '[data-sim-control="b"]', 1, "intercept slider missing")
    elif engine == "math-system-graph":
        await require_count(sim, '[role="img"]', 1, "system graph missing")
        await require_count(sim, '[data-sim-control="sum"]', 1, "system parameter slider missing")
    elif engine == "math-geometry":
        await require_count(sim, '[role="img"]', 1, "geometry visual missing")
        await require_count(sim, '[data-sim-control="base"]', 1, "geometry base slider missing")
        await require_count(sim, '[data-sim-control="height"]', 1, "geometry height slider missing")
    elif engine == "math-data-lab":
        await require_count(sim, ".sim-bars", 1, "data bar visual missing")
        await require_count(sim, '[data-sim-control="a"]', 1, "data slider a missing")
        await require_count(sim, '[data-sim-control="b"]', 1, "data slider b missing")
        await require_count(sim, '[data-sim-control="c"]', 1, "data slider c missing")
    elif engine == "math-probability-lab":
        await require_count(sim, ".sim-result", 1, "probability result missing")
        await require_count(sim, '[data-sim-action="run-trials"]', 1, "probability trial action missing")
        await require_count(sim, '[data-sim-control="trials"]', 1, "probability trials slider missing")
    else:
        raise AssertionError(f"renderer-depth rule missing for engine {engine}")


async def check_lesson(page, lesson: dict[str, Any]) -> dict[str, Any]:
    lesson_id = lesson["id"]
    title = lesson["title"]
    simulation = lesson.get("simulation") or {}
    engine = simulation.get("engine")
    if engine not in SUPPORTED_ENGINES:
        raise AssertionError(f"unsupported production engine: {engine!r}")

    search = page.locator("#search")
    await search.fill(lesson_id)
    # lesson_id also appears inside its ten linked questions, and short lesson titles
    # such as 「代數」/「函數」are substrings of other lesson titles.  The production
    # simulation key is unique, so use it as the authoritative lesson-card locator.
    sim = page.locator(f'#contentGrid [data-simulation-lesson^="{lesson_id}:"]').first
    await sim.wait_for(state="visible", timeout=3_000)
    card = sim.locator("xpath=ancestor::article[contains(@class,'card')][1]")
    await card.wait_for(state="visible", timeout=3_000)
    rendered_title = (await card.locator("h3").first.inner_text()).strip()
    if rendered_title != title:
        raise AssertionError(
            f"simulation resolved to wrong lesson card: expected title {title!r}, got {rendered_title!r}"
        )

    text = (await sim.inner_text()).strip()
    if len(text) < 30:
        raise AssertionError("simulation lacks a substantive textual fallback")
    forbidden = ("尚未支援", "待實作", "TODO", "placeholder")
    if any(token.lower() in text.lower() for token in forbidden):
        raise AssertionError(f"placeholder/fallback-only text leaked into production simulation: {text[:160]!r}")

    controls = sim.locator("input,button,select")
    if await controls.count() == 0:
        raise AssertionError("simulation rendered without interactive controls")

    status_like = sim.locator('[role="status"], [aria-live], output, .sim-feedback, .sim-status, .feedback')
    if await status_like.count() == 0:
        raise AssertionError("simulation lacks visible/live feedback output")

    model = simulation.get("model")
    await assert_renderer_depth(sim, engine, model)
    interaction = await mutate_with_keyboard(sim)

    viewport_metrics: dict[str, Any] = {}
    for width in VIEWPORTS:
        await page.set_viewport_size({"width": width, "height": 900})
        metrics = await page.evaluate("""() => {
          const client = document.documentElement.clientWidth;
          const offenders = [...document.querySelectorAll('body *')]
            .map((el) => {
              const rect = el.getBoundingClientRect();
              return {
                tag: el.tagName.toLowerCase(),
                id: el.id || '',
                className: typeof el.className === 'string' ? el.className : '',
                left: Math.round(rect.left * 10) / 10,
                right: Math.round(rect.right * 10) / 10,
                width: Math.round(rect.width * 10) / 10,
                scrollWidth: el.scrollWidth,
                clientWidth: el.clientWidth,
              };
            })
            .filter((item) => item.right > client + 0.5 || item.left < -0.5)
            .sort((a, b) => Math.max(b.right - client, -b.left) - Math.max(a.right - client, -a.left))
            .slice(0, 8);
          return {
            body: document.body.scrollWidth,
            doc: document.documentElement.scrollWidth,
            client,
            offenders,
          };
        }""")
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
        status = page.locator("#status")
        await status.wait_for(state="visible", timeout=10_000)
        await page.wait_for_function(
            """() => {
              const value = document.querySelector('#status')?.textContent || '';
              return value.includes('資料載入完成') || value.includes('資料載入失敗');
            }""",
            timeout=30_000,
        )
        status_text = (await status.inner_text()).strip()
        if "資料載入完成" not in status_text:
            raise AssertionError(f"public site data did not initialize: {status_text}")

        for index, lesson in enumerate(lessons, start=1):
            try:
                passed.append(await check_lesson(page, lesson))
            except Exception as exc:
                failures.append({"id": lesson.get("id", "unknown"), "file": lesson.get("_file", "unknown"), "error": str(exc)})
            if index % 16 == 0:
                print(f"math browser QA progress: {index}/{len(lessons)}")

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
                "dedicated production simulation renderer renders",
                "substantive text fallback is present",
                "live/visible feedback output exists",
                "interactive control has an accessible name",
                "keyboard action causes observable state change",
                "engine/model-specific renderer depth",
                "no horizontal overflow at 320/375/390/430/768px",
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
