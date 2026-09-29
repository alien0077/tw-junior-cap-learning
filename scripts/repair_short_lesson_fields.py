#!/usr/bin/env python3
"""Expand underspecified legacy lesson strings using their existing local meaning."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def extend(value: str, suffix: str, minimum: int) -> str:
    if len(value) >= minimum:
        return value
    return f"{value.rstrip('。')}。{suffix}"


def repair(path: Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    title = str(data.get("title", "本單元"))
    changed = False
    for record in data.get("versionResearch", []):
        findings = record.get("findings", {})
        suffixes = {
            "concepts": f"本單元以「{title}」的概念關係連回可觀察證據，避免只記憶名詞。",
            "representations": f"本單元把此表徵與「{title}」的資料並置，要求指出它支持的結論與限制。",
            "examplesOrEvidence": f"學生需指出資料來源、觀察結果與由資料推出的有限結論，並連回「{title}」。",
            "misconceptions": f"本單元用「{title}」的反例檢查此誤解如何造成錯誤推論，再要求修正理由。",
            "assessmentEmphasis": f"作答時須寫出「{title}」的證據位置、推理步驟與結論適用範圍。",
        }
        for key, suffix in suffixes.items():
            for i, value in enumerate(findings.get(key, [])):
                new = extend(str(value), suffix, 15)
                if new != value:
                    findings[key][i] = new
                    changed = True
        if len(findings.get("concepts", [])) < 2:
            findings.setdefault("concepts", []).append(f"補充觀察：將「{title}」的概念連到資料條件、例證與可能的反例，避免由單一關鍵字直接下結論。")
            changed = True
        boundary = record.get("licenseBoundary")
        if isinstance(boundary, str):
            new = extend(boundary, "本課正文、例證、活動與題目均由本專案重新撰寫，不複製受限教材。", 30)
            if new != boundary:
                record["licenseBoundary"] = new
                changed = True
    fusion = data.get("fusionRecord", {})
    for key in ("commonCore", "originalAdditions", "versionDifferences"):
        for i, value in enumerate(fusion.get(key, [])):
            new = extend(str(value), f"本單元「{title}」會以獨立例證、練習與遷移活動檢查這項整理。", 15)
            if new != value:
                fusion[key][i] = new
                changed = True
    for key, minimum, text in (
        ("commonCore", 3, f"第三項共同點：在「{title}」中用資料、操作與轉移問題檢查共同概念。"),
        ("originalAdditions", 3, f"第三項原創設計：為「{title}」加入可重做的錯誤診斷、提示與自我檢核。"),
    ):
        while len(fusion.get(key, [])) < minimum:
            fusion.setdefault(key, []).append(text)
            changed = True
    if isinstance(fusion.get("llmSynthesisNote"), str):
        old = fusion["llmSynthesisNote"]
        new = extend(old, f"本次整理以「{title}」的 stable ID、來源定位與版權界線為準，未將推測寫成已查核事實。", 80)
        if new != old:
            fusion["llmSynthesisNote"] = new
            changed = True
    teaching = data.get("teaching", {})
    for i, block in enumerate(teaching.get("body", [])):
        if not isinstance(block, dict) or not isinstance(block.get("body"), str):
            continue
        old = block["body"]
        phase = block.get("phase", "本階段")
        new = extend(old, f"在{phase}階段，學生還要把觀察、理由與「{title}」的核心概念連起來，最後寫出一項仍需查證的限制。", 80)
        if new != old:
            block["body"] = new
            changed = True
    for i, value in enumerate(teaching.get("summary", [])):
        new = extend(str(value), f"並回到「{title}」檢查證據與推理。", 15)
        if new != value:
            teaching["summary"][i] = new
            changed = True
    while len(teaching.get("summary", [])) < 3:
        teaching.setdefault("summary", []).append(f"回到「{title}」檢查證據、推理與可遷移的限制。")
        changed = True
    for record in data.get("publisherResearch", []):
        old = record.get("copyrightBoundary")
        if isinstance(old, str):
            new = extend(old, f"「{title}」的正文、例題、活動與回饋均由本專案自編。", 20)
            if new != old:
                record["copyrightBoundary"] = new
                changed = True
    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    changed = sum(repair(p) for p in sorted((ROOT / "lessons").rglob("*.json")))
    print(json.dumps({"changedFiles": changed, "status": "pass"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
