#!/usr/bin/env python3
"""Make answer strategies and solution steps question-specific without changing answers."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_ROOT = ROOT / "questions"
SUBJECT_LABELS = {
    "chinese": "國文的文本證據與表達功能",
    "english": "英文的句型、語意與溝通功能",
    "math": "數學的條件、符號與運算關係",
    "science": "自然的現象、變因與證據機制",
    "social": "社會的時空、制度、資料與觀點",
}

def compact(value: str, limit: int = 120) -> str:
    value = re.sub(r"\s+", " ", str(value)).strip()
    return value if len(value) <= limit else value[: limit - 1] + "…"

def subject_of(path: Path) -> str:
    return path.parent.name

def make_strategy(subject: str, prompt: str, explanation: str) -> str:
    label = SUBJECT_LABELS.get(subject, "本題的條件、證據與結論")
    focus = compact(prompt, 72)
    reason = compact(explanation, 104)
    if subject == "math":
        return f"先從題幹「{focus}」圈出已知量、未知量、單位與限制，判斷應用的{label}；依運算順序或公式逐步代入，再用「{reason}」回算答案並檢查符號、單位與合理性。"
    if subject == "science":
        return f"先把題幹「{focus}」拆成現象、變因、觀察量與因果方向，建立{label}的判準；逐項檢查選項是否符合「{reason}」，最後確認沒有把相關現象誤當成充分原因。"
    if subject == "english":
        return f"先辨認題幹「{focus}」要求的句型、時態、詞義或語用功能，再以{label}逐字檢查主詞、動詞、語序與語意；用「{reason}」確認正解並排除只改一個字卻破壞句意的選項。"
    if subject == "chinese":
        return f"先從題幹「{focus}」找出關鍵語句、段落位置與表達任務，再依{label}區分原文直接證據和推論；以「{reason}」核對選項是否能被文本支持，並保留不能過度推論的範圍。"
    return f"先從題幹「{focus}」定位時間、空間、制度、資料尺度與利害關係，再依{label}建立判準；用「{reason}」逐項檢核，最後區分資料事實、因果推論與仍有限制的解釋。"

def replace_if_generic_steps(data: dict, subject: str) -> tuple[bool, list[str]]:
    prompt = data.get("prompt", "")
    answer = data.get("answer", {})
    explanation = answer.get("explanation", "")
    options = {str(o.get("id")): str(o.get("text", "")) for o in data.get("options", [])}
    answer_id = str(answer.get("value", ""))
    answer_text = options.get(answer_id, answer_id)
    steps = list(data.get("solutionSteps", []))
    if len(steps) < 5:
        return False, steps

    changed = False
    steps[1] = f"建立本題判準：先記下題幹「{compact(prompt, 110)}」的要求，再用答案解析指出的核心理由「{compact(explanation, 150)}」作為逐項比對標準。"
    if subject == "math":
        steps[3] = f"逐項核算：先檢查選項是否符合題目給的數值、符號、單位與運算順序；正解 {answer_id}「{compact(answer_text, 100)}」符合「{compact(explanation, 125)}」，其餘選項至少有一項條件不符。"
    elif subject == "science":
        steps[3] = f"逐項比對證據：檢查每個選項的現象、變因與因果方向是否能由題幹支持；正解 {answer_id}「{compact(answer_text, 100)}」符合「{compact(explanation, 125)}」，錯誤選項多半省略必要條件或把推測當結論。"
    elif subject == "english":
        steps[3] = f"逐項檢查語言證據：對照主詞、動詞形式、語序、搭配與語境功能；正解 {answer_id}「{compact(answer_text, 100)}」符合「{compact(explanation, 125)}」，其他選項逐一指出文法或語意衝突。"
    elif subject == "chinese":
        steps[3] = f"逐項回到文本：檢查選項是否有原句、段落位置、語氣或修辭證據支持；正解 {answer_id}「{compact(answer_text, 100)}」能由「{compact(explanation, 125)}」推出，其他選項超出文本或錯置表達功能。"
    else:
        steps[3] = f"逐項檢驗資料與觀點：對照題幹的時間、空間、制度、來源和尺度；正解 {answer_id}「{compact(answer_text, 100)}」符合「{compact(explanation, 125)}」，其餘選項有資料缺口、因果跳躍或程序不符。"
    steps[4] = f"最後回查：把答案 {answer_id}「{compact(answer_text, 100)}」放回完整題幹「{compact(prompt, 120)}」，確認它同時滿足題目要求與解析理由；若條件、數字、語境或資料尺度改變，必須重新建立判準，不可只沿用答案代號。"
    changed = True
    data["solutionSteps"] = steps
    return changed, steps

def main() -> None:
    files = sorted(QUESTION_ROOT.glob("*/*.json"))
    changed = 0
    strategy_changed = 0
    step_changed = 0
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        subject = subject_of(path)
        strategy = str(data.get("solutionStrategy", ""))
        if len(strategy) < 30:
            data["solutionStrategy"] = make_strategy(subject, data.get("prompt", ""), data.get("answer", {}).get("explanation", ""))
            strategy_changed += 1
        did_change, _ = replace_if_generic_steps(data, subject)
        if did_change:
            step_changed += 1
        if did_change or len(strategy) < 30:
            data["reviewStatus"] = "draft"
            data["updatedAt"] = "2026-09-07"
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
    report = {
        "updatedAt": "2026-09-07",
        "scope": "canonical questions/*/*.json; answer.value, options and answer.explanation are preserved",
        "questionFiles": len(files),
        "changedFiles": changed,
        "strategyChanged": strategy_changed,
        "solutionStepsChanged": step_changed,
        "status": "draft-content-enrichment-pending-subject-review",
        "boundary": "This pass makes reasoning fields question-specific from existing prompt, options and explanation; it does not claim independent subject correctness, distractor quality, copyright review or human review.",
    }
    out = ROOT / "implementation/reports/question-reasoning-enrichment.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))

if __name__ == "__main__":
    main()
