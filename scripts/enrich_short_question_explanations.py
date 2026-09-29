#!/usr/bin/env python3
"""Expand short answer explanations with the item's own evidence and answer."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def compact(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", str(text)).strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"

def main() -> None:
    changed = 0
    files = sorted((ROOT / "questions").glob("*/*.json"))
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        explanation = str(data.get("answer", {}).get("explanation", "")).strip()
        if len(explanation) >= 30:
            continue
        answer = data.get("answer", {})
        answer_id = str(answer.get("value", ""))
        option_text = next((str(o.get("text", "")) for o in data.get("options", []) if str(o.get("id")) == answer_id), answer_id)
        prompt = compact(data.get("prompt", ""), 115)
        if path.parent.name == "math":
            tail = "先把題幹的數值、單位與運算關係列出，再代入或推導；最後回算，確認正解不是只靠選項外觀猜出來。"
        elif path.parent.name == "science":
            tail = "先把題幹的現象、變因與證據方向對齊，再檢查是否漏掉必要條件或過度延伸因果。"
        elif path.parent.name == "english":
            tail = "先檢查題目要求的句型、時態、語意與語用，再逐字比對選項，避免只看到熟悉單字就選答案。"
        elif path.parent.name == "chinese":
            tail = "先回到題幹或文本中的直接線索，再區分字面證據、表達功能與推論範圍，避免把印象當成文意。"
        else:
            tail = "先核對題幹的時間、空間、制度、資料來源與尺度，再區分可直接確認的事實和需要證據支持的推論。"
        data.setdefault("answer", {})["explanation"] = f"{explanation} 本題要回到題幹「{prompt}」核對；正確選項 {answer_id}「{compact(option_text, 100)}」符合這個判準。{tail}"
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-09-07"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    report = {
        "updatedAt": "2026-09-07",
        "questionFiles": len(files),
        "changedFiles": changed,
        "status": "draft-content-enrichment-pending-subject-review",
        "boundary": "Only short existing explanations were expanded with the same question's prompt, selected option and subject-specific checking advice; answer values and options were not changed.",
    }
    out = ROOT / "implementation/reports/short-question-explanation-enrichment.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))

if __name__ == "__main__":
    main()
