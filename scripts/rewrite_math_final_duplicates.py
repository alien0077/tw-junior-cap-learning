#!/usr/bin/env python3
"""Turn the remaining near-identical math pairs into distinct authored items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-08-29"

ITEMS = {
    "question-math-content-s-8-7-10": ("若圓周率取 π，半徑 6 公分的圓周長為何？", ["12π 公分", "6π 公分", "18π 公分", "36π 公分"], "A", "圓周長＝2πr＝2π×6＝12π 公分。"),
    "question-math-performance-s-iv-2-6": ("正八邊形的一個外角是多少？", ["45°", "135°", "120°", "30°"], "A", "正多邊形外角和為 360°，正八邊形每個外角為 360÷8＝45°。"),
    "question-math-performance-s-iv-6-8": ("若球的半徑變為原來的 1/2，球體積變為原來的幾倍？", ["1/8 倍", "1/2 倍", "1/4 倍", "1/16 倍"], "A", "球體積與半徑的三次方成正比，故倍率為 (1/2)³＝1/8。"),
    "question-math-performance-s-iv-14-6": ("圓的半徑變成原來的 2 倍，圓周長變成原來的幾倍？", ["2 倍", "4 倍", "6 倍", "8 倍"], "A", "圓周長與半徑成正比，因此半徑加倍時圓周長也加倍。"),
    "question-math-content-d-9-3-8": ("袋中有紅球 3 顆、藍球 2 顆，隨機取出 1 顆，取到藍球的機率為何？", ["2/5", "3/5", "1/2", "1/5"], "A", "藍球有 2 顆，總球數 5 顆，機率為 2/5。"),
    "question-math-content-s-8-2-2": ("正五邊形的一個外角是多少？", ["72°", "108°", "60°", "90°"], "A", "正多邊形外角和為 360°，正五邊形每個外角為 360÷5＝72°。"),
    "question-math-content-s-8-8-5": ("等腰三角形的頂角為 50°，每個底角為何？", ["65°", "50°", "75°", "80°"], "A", "兩底角相等，故每個底角為 (180°－50°)÷2＝65°。"),
    "question-math-content-s-9-10-3": ("若中線 AM＝18 公分，從頂點 A 到重心 G 的長度為何？", ["12 公分", "6 公分", "9 公分", "18 公分"], "A", "重心將中線由頂點起分成 2:1，AG＝(2/3)×18＝12 公分。"),
    "question-math-performance-n-iv-5-8": ("直角三角形兩股長為 5 與 12，斜邊長為何？", ["13", "7", "17", "60"], "A", "由畢氏定理，斜邊＝√(5²＋12²)＝√169＝13。"),
    "question-math-content-s-9-3-7": ("在 △ABC 中，DE∥BC。若 AD/AB＝2/5 且 AB＝25，則 AD 為何？", ["10", "5", "15", "20"], "A", "AD＝(2/5)×AB＝(2/5)×25＝10。"),
    "question-math-content-s-9-13-5": ("一個長方體各邊同時放大為原來 2 倍，體積變為原來的幾倍？", ["8 倍（長、寬、高都納入）", "2 倍（只考慮一個方向）", "4 倍（只考慮兩個方向）", "6 倍（誤將倍率相加）"], "A", "長、寬、高均放大 2 倍，體積倍率為 2³＝8 倍。"),
}


def main() -> None:
    changed = 0
    for path in (ROOT / "questions/math").glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        item = ITEMS.get(data.get("id"))
        if not item:
            continue
        prompt, texts, answer, explanation = item
        data.update({"prompt": prompt, "options": [{"id": chr(65+i), "text": text} for i, text in enumerate(texts)], "answer": {"value": answer, "explanation": explanation}, "reviewStatus": "draft", "updatedAt": TODAY})
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    print(f"rewrote final math duplicate variants: {changed}")


if __name__ == "__main__":
    main()
