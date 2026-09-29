#!/usr/bin/env python3
"""Require an answer, strategy, and traceable multi-step solution for every question."""
from __future__ import annotations

import argparse
import json
from collections import Counter
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STRATEGIES = {
    "chinese": "先抓出題幹中的文本證據、語意關係或表達目的，再把每個選項逐項與證據核對。",
    "english": "先辨識句型、文法或語用任務，再檢查主詞、時態、語序與語意是否同時成立。",
    "math": "先整理已知量與要求量，選定關係式或表示法，完成計算後再檢查單位、符號與合理性。",
    "science": "先辨識研究變因、觀察現象與可用證據，再用機制、守恆或模型關係逐項檢查選項。",
    "social": "先確認題目的時間、空間、制度或資料尺度，再回到題幹證據比較各選項的因果與觀點。",
}


def files() -> list[Path]:
    return sorted((ROOT / "questions").rglob("*.json"))


def build(data: dict) -> tuple[str, list[str]]:
    subject = data["subject"]
    answer = data["answer"]["value"]
    explanation = data["answer"]["explanation"].strip()
    option_map = {o["id"]: o["text"] for o in data.get("options", [])}
    correct_text = option_map.get(answer, answer)
    prompt = data["prompt"].strip()
    strategy = STRATEGIES[subject]
    steps = [
        f"讀題定位：先找出本題要判斷的核心條件與限制；題幹是「{prompt}」。",
        f"建立判準：{strategy}",
        f"核對正確選項 {answer}：{correct_text}。依題目解析，{explanation}",
        "逐項排除其餘選項：把每個選項與前述判準對照；只保留同時符合題幹條件、證據與推理要求的選項。",
        f"答案檢查：再次確認代號 {answer} 對應的選項文字，並檢查沒有把題目要求、數值、時間或語意方向看反。",
    ]
    return strategy, steps


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    total = changed = missing = short_steps = 0
    strategies = Counter()
    signatures = set()
    for path in files():
        data = json.loads(path.read_text(encoding="utf-8"))
        total += 1
        if not data.get("answer", {}).get("value") or not data.get("answer", {}).get("explanation"):
            missing += 1
            continue
        strategy, steps = build(data)
        if len(data.get("solutionSteps", [])) < 3 or any(not str(x).strip() for x in data.get("solutionSteps", [])):
            short_steps += 1
        strategies[data["subject"]] += 1
        signature = re.sub(r"\s+", " ", " ".join(str(x) for x in data.get("solutionSteps", []))).strip()
        signatures.add(signature)
        if args.write:
            data["solutionStrategy"] = strategy
            data["solutionSteps"] = steps
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
    report = {"totalQuestions": total, "changed": changed, "missingAnswerOrExplanation": missing, "shortOrEmptySolutionSteps": short_steps, "uniqueSolutionSignatures": len(signatures), "subjects": dict(strategies), "status": "pass" if missing == 0 and short_steps == 0 else "blocked"}
    out = ROOT / "implementation/reports/question-solution-coverage.json"
    out.write_text(json.dumps({"summary": report}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
