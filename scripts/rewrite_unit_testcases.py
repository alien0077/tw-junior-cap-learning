#!/usr/bin/env python3
"""Author unit-specific implementation test cases from each unit spec."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def first(values, fallback: str) -> str:
    for value in values or []:
        if isinstance(value, str) and value.strip():
            return " ".join(value.split())
    return fallback


def build(spec: dict) -> list[str]:
    title = spec["title"]
    concept = first(spec.get("coreConcepts"), title)
    representation = first(spec.get("coreConcepts", [])[1:], concept)
    misconception = first(spec.get("misconceptions"), "題幹限制條件")
    component = first(spec.get("visualizations"), "本單元表徵")
    transfer = spec.get("capTransfer", {})
    transfer_rule = transfer.get("stemConstraint", f"保留「{concept}」的核心關係")
    response = transfer.get("requiredResponse", "指出證據或推理步驟")
    return [
        f"載入「{title}」時不得先顯示正解；學生必須先提交對「{concept}」的預測，且預測會被保留供後續比較。",
        f"操作「{component}」中的主要變項後，與「{representation}」相關的圖、表、句構或因果鏈必須同步更新，文字狀態也要說明改變了什麼。",
        f"學生觸發「{misconception}」時，系統必須命中本單元的 misconception check，要求學生指出可定位證據，並先給一階提示而非直接揭露答案。",
        f"在 320px、375px 與 768px 寬度，以鍵盤完成「{title}」的預測—操作—觀察—解釋流程時，核心題幹、控制項、回饋與可讀狀態不得溢位或遺失。",
        f"以新資料執行「{title}」的 CAP transfer：{transfer_rule}；學生回答必須{response}，評分同時檢查概念、證據對應與表達完整度。",
    ]


def main() -> int:
    changed = 0
    for path in sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        spec = data["unitImplementationSpec"]
        tests = build(spec)
        if spec.get("testCases") != tests:
            spec["testCases"] = tests
            path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
            changed += 1
    print(json.dumps({"unitCount": len(list((ROOT / "implementation/unit-specs").glob("*/*.yaml"))), "changed": changed}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
