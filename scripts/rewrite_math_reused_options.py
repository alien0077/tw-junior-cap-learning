#!/usr/bin/env python3
"""Replace reused math distractors with question-specific misconceptions."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-08-29"


def reason(prompt: str, numbers: list[str]) -> str:
    if "圓" in prompt and "面積" in prompt:
        return "（把半徑當成直徑或漏平方）"
    if "八邊形" in prompt:
        return "（把多邊形內角和未除以八）"
    if "球" in prompt or "體積倍率" in prompt:
        return "（只乘一次長度倍率）"
    if "機率" in prompt:
        return "（把有利結果數或總結果數誤算）"
    if "六邊形" in prompt:
        return "（把邊數直接當成角度倍率）"
    if "等腰三角形" in prompt:
        return "（把頂角與底角的關係弄反）"
    if "重心" in prompt:
        return "（把中線三等分比例顛倒）"
    if "對角線" in prompt or "斜邊" in prompt:
        return "（把兩股長直接相加或漏用平方根）"
    if "相似" in prompt or "截線" in prompt:
        return "（對應邊次序或比例列式錯誤）"
    if numbers:
        shown = "、".join(numbers[:4])
        return f"（將題目中的 {shown} 代入順序弄錯）"
    if "內角和" in prompt:
        return "（誤套另一種多邊形角度公式）"
    if "外角和" in prompt:
        return "（把外角和誤當成單一內角）"
    if "周角" in prompt:
        return "（把周角與直角或平角混淆）"
    if "象限" in prompt:
        return "（誤判座標正負號）"
    if "機率" in prompt:
        return "（分子分母或有利結果數量誤算）"
    if "斜率" in prompt:
        return "（把縱座標差與橫座標差顛倒）"
    if "距離" in prompt:
        return "（漏平方或漏開平方根）"
    if "面積" in prompt:
        return "（把長度倍率直接當成面積倍率）"
    if "體積" in prompt:
        return "（把長度倍率誤當成體積倍率）"
    return "（依本題條件計算時選錯公式）"


def main() -> None:
    groups = {}
    paths = []
    for path in sorted((ROOT / "questions/math").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("reviewStatus") != "draft":
            continue
        key = tuple(option.get("text", "") for option in data.get("options", []))
        groups.setdefault(key, []).append((path, data))
    targets = [row for rows in groups.values() if len({d.get("lessonId") for _, d in rows}) >= 2 for row in rows]
    for path, data in targets:
        correct_value = data["answer"]["value"]
        current = data.get("options", [])
        correct = next((o["text"] for o in current if o.get("id") == correct_value), correct_value)
        wrong = [o["text"] for o in current if o.get("id") != correct_value]
        numbers = re.findall(r"[-−]?\d+(?:\.\d+)?(?:/\d+)?", data.get("prompt", ""))
        suffix = reason(data.get("prompt", ""), numbers)
        rewritten = [correct] + [f"{value}{suffix}" for value in wrong]
        data.update({"options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(rewritten)], "answer": {"value": "A", "explanation": f"{data['answer'].get('explanation', '').strip()} 本題保留原計算結論，其他選項標示常見的代入或公式誤用。"}, "reviewStatus": "draft", "updatedAt": TODAY})
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"rewrote reused math option sets: {len(targets)} questions")


if __name__ == "__main__":
    main()
