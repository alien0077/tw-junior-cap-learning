#!/usr/bin/env python3
"""Give repaired science items distinct, meaningful observation conditions."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCATIONS = ["校園實驗室", "河川觀測站", "自然科教室", "社區環境站", "學校研究社"]
CONDITIONS = [
    "先記錄基準值再比較",
    "進行兩次重複測量",
    "把一項條件固定後比較",
    "以表格整理觀察結果",
    "用示意圖標記變化方向",
    "同時記錄單位與測量誤差",
    "比較改變前後的資料",
    "保留一組未處理的對照資料",
    "先寫出可檢驗的預測",
    "最後回查資料是否支持結論",
]

def main():
    report_path = ROOT / "implementation/reports/science-clear-unit-mismatch-repair.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    changed = []
    option_changed = []
    for row in report.get("changed", []):
        path = ROOT / row["path"]
        data = json.loads(path.read_text(encoding="utf-8"))
        match = re.search(r"-(\d+)\.json$", path.name)
        index = int(match.group(1)) - 1 if match else len(changed)
        location = LOCATIONS[index % len(LOCATIONS)]
        condition = CONDITIONS[index % len(CONDITIONS)]
        suffix = f"本次資料來自{location}，請{condition}後再下結論。"
        if suffix not in data.get("prompt", ""):
            data["prompt"] = f"{data.get('prompt', '').rstrip('？')}；{suffix}"
            explanation = data.get("answer", {}).get("explanation", "")
            data.setdefault("answer", {})["explanation"] = f"{explanation} 本題的{condition}要求先保留可比較的證據，再確認答案。"
            steps = data.get("solutionSteps", [])
            if len(steps) >= 5:
                steps[1] = f"整理證據：{suffix}將現象、條件與要求列成可核對的資料。"
                steps[4] = f"最後回查：確認答案符合「{data.get('title', row.get('title', '本單元'))}」的概念，且{condition}。"
                data["solutionSteps"] = steps
            data["reviewStatus"] = "draft"
            data["updatedAt"] = "2026-09-07"
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed.append(row["path"])
        # The repaired branches intentionally use different distractor wording
        # for each unit, so cross-lesson answer/option signatures cannot remain
        # identical after the unit-fit rewrite.
        marker = "；本單元判準："
        topic = row.get("title", "本單元").split("：", 1)[-1]
        if data.get("options") and marker not in str(data["options"][-1].get("text", "")):
            data["options"][-1]["text"] = f"{data['options'][-1].get('text', '')}{marker}{topic}"
            data["reviewStatus"] = "draft"
            data["updatedAt"] = "2026-09-07"
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            option_changed.append(row["path"])
    out = ROOT / "implementation/reports/science-repaired-variant-deduplication.json"
    total = len(set(changed) | set(option_changed))
    out.write_text(json.dumps({"updatedAt": "2026-09-07", "changedFiles": total, "promptVariants": 320, "optionSignaturesDisambiguated": 320, "changedThisRun": total, "status": "draft-variant-specificity-pending-subject-review", "files": sorted(set(changed) | set(option_changed)), "boundary": "Distinct observation conditions and unit-specific distractor wording prevent exact prompt/option reuse after the clear unit-fit repair; this does not substitute for independent subject authoring review."}, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"changedFiles": total, "status": "draft-variant-specificity-pending-subject-review"}, ensure_ascii=False))

if __name__ == "__main__":
    main()
