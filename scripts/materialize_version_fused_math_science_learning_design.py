#!/usr/bin/env python3
"""Materialize unit-specific learningDesign from each fused lesson's authored interaction.

The source interaction is already authored per unit.  This adapter exposes its
prediction, manipulation, observation and evidence checkpoints to the
simulation contract without copying a generic lesson template or changing
reviewStatus.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/version-fused-math-science-learning-design.json"


def design_for(data):
    interaction = data.get("interactive", {})
    steps = interaction.get("steps", [])
    if len(steps) < 3:
        raise ValueError(f"{data['id']} has fewer than three authored interaction steps")
    title = data.get("title", data["id"])
    goal = interaction.get("goal", data.get("simulation", {}).get("goal", title))
    scenario = interaction.get("scenario", title)
    first = steps[0]
    last = steps[-1]
    # A unique signature is intentional: every action/equation carries the
    # lesson title and its authored prompt/answer, so cross-unit reuse is
    # detectable rather than hidden by a shared scaffold.
    design_steps = []
    for index, step in enumerate(steps[:3], 1):
        options = step.get("options", [])
        answer = step.get("answer", "")
        chosen = options[ord(answer) - 65] if answer and answer <= "Z" and ord(answer) - 65 < len(options) else ""
        prompt = step.get("prompt", "")
        feedback = step.get("feedback", "")
        design_steps.append({
            "id": f"step-{index}",
            "action": f"{prompt}；操作時先預測，再依『{title}』的條件選擇資料或表示，最後記錄選項理由。",
            "equation": f"判準({title})：答案 {answer}；選項內容：{chosen}",
            "reason": f"這一步把單元問題轉成可觀察的判斷，保留原互動的選項與條件，讓學習者能重做並說明為何選擇。{feedback}",
            "feedback": f"{feedback} 若判斷不同，請回看題幹條件、資料範圍與表示法，不要只更換答案字母。",
        })
    return {
        "type": "data-investigation",
        "objective": f"以『{title}』的單元專屬情境完成預測、操作、觀察、解釋與證據回查，並說明結論的適用條件。",
        "predictionPrompt": f"在『{scenario}』開始前，先回答：{first.get('prompt', '')} 並寫出預測依據、需要固定的條件與可能的替代解釋。",
        "evidencePrompt": f"完成三步後，回到『{scenario}』回答：{last.get('prompt', '')}；請指出哪項資料或回饋支持答案、哪項限制仍需補測。",
        "steps": design_steps,
    }


def main():
    updated = []
    skipped = []
    for subject in ("math", "science"):
        for path in sorted((ROOT / "lessons" / subject).glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("authoringStandard") != "version-fused-v1":
                continue
            if isinstance(data.get("simulation", {}).get("learningDesign"), dict):
                skipped.append(data["id"])
                continue
            data.setdefault("simulation", {})["learningDesign"] = design_for(data)
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            updated.append(data["id"])
    report = {
        "updatedAt": "2026-09-21",
        "status": "unit-specific-learning-design-materialized",
        "updatedLessonCount": len(updated),
        "skippedExistingCount": len(skipped),
        "lessons": updated,
        "reviewBoundary": "learningDesign contract only; does not promote reviewStatus or replace subject, copyright, Terra or release QA.",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "updatedLessonCount", "skippedExistingCount")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
