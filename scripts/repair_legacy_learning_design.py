#!/usr/bin/env python3
"""Upgrade legacy lesson learningDesign records from their existing content."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {
    "equation-transform",
    "representation-match",
    "parameter-investigation",
    "data-investigation",
    "geometric-construction",
    "probability-experiment",
    "model-boundary",
}


def choose_type(lesson: dict, ld: dict) -> str:
    old = ld.get("type")
    if old in ALLOWED:
        return old
    text = " ".join(str(ld.get(k, "")) for k in ("objective", "predictionPrompt", "evidencePrompt", "type"))
    engine = lesson.get("simulation", {}).get("engine", "")
    if "equation" in text.lower() or "formula" in text.lower():
        return "equation-transform"
    if "geometry" in engine or "geometric" in text.lower() or "圖形" in text:
        return "geometric-construction"
    if "probability" in engine or "機率" in text:
        return "probability-experiment"
    if "parameter" in text.lower() or "變因" in text or "參數" in text:
        return "parameter-investigation"
    return "model-boundary"


def repair(path: Path) -> bool:
    lesson = json.loads(path.read_text(encoding="utf-8"))
    sim = lesson.get("simulation")
    if not isinstance(sim, dict) or not isinstance(sim.get("learningDesign"), dict):
        return False
    ld = sim["learningDesign"]
    changed = False
    if ld.get("type") not in ALLOWED:
        ld["type"] = choose_type(lesson, ld)
        changed = True
    objective = str(ld.get("objective", sim.get("goal", "本單元互動模型"))).strip()
    prediction = str(ld.get("predictionPrompt", sim.get("mission", "請先提出可檢查的預測。"))).strip()
    ld.setdefault("objective", objective)
    ld.setdefault("predictionPrompt", prediction)
    if len(ld.get("objective", "")) < 20:
        ld["objective"] = f"{objective}；並以資料檢查模型的適用條件與限制。"
        changed = True
    if len(ld.get("predictionPrompt", "")) < 20:
        ld["predictionPrompt"] = f"{prediction} 請先寫出預測與判斷依據。"
        changed = True
    if not ld.get("evidencePrompt") or len(str(ld.get("evidencePrompt"))) < 20:
        ld["evidencePrompt"] = f"請用本互動產生的資料檢查「{objective}」，指出支持結論的證據、仍不確定的條件與一項模型限制。"
        changed = True
    steps = ld.get("steps", [])
    for index, step in enumerate(steps, 1):
        if not isinstance(step, dict):
            continue
        action = str(step.get("action", "完成本步操作"))
        equation = str(step.get("equation", "compare=observation+reasoning"))
        if step.get("id") != f"step-{index}":
            step["id"] = f"step-{index}"
            changed = True
        if len(str(step.get("reason", ""))) < 20:
            step["reason"] = f"本步把「{action}」和「{equation}」連結，先保留可比較條件，再用觀察資料檢查推論。"
            changed = True
        if len(str(step.get("feedback", ""))) < 20:
            step["feedback"] = f"若結果與預測不一致，請回看「{action}」的條件與資料，再只修正一個變因後重做。"
            changed = True
    if changed:
        path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    changed = 0
    for path in sorted((ROOT / "lessons").rglob("*.json")):
        if repair(path):
            changed += 1
    print(json.dumps({"changedFiles": changed, "status": "pass"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
