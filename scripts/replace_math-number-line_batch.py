"""以公開數學試題的數與量判讀方向，獨立替換 N-7-5 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-n-7-5.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-n-7-5"
KNOWLEDGE = "kg-math-content-n-7-5"

ITEMS = [
    ("在數線上，從原點向左 3 個單位所表示的數為何？", ["－3", "3", "－1/3", "1/3"], "A", "數線向左表示負數，從 0 向左 3 個單位是－3。"),
    ("數線上 A 點為－2、B 點為 4，A、B 兩點的距離是多少？", ["6", "2", "－6", "8"], "A", "兩點距離為 |4－(－2)|＝|6|＝6。"),
    ("－7 的相反數為何？", ["7", "－7", "1/7", "0"], "A", "相反數與原數相加為 0，因此－7 的相反數是 7。"),
    ("|－3.5| 的值為何？", ["3.5", "－3.5", "0.35", "－0.35"], "A", "絕對值表示到 0 的距離，|－3.5|＝3.5。"),
    ("下列哪個數較大？", ["－1", "－4", "－6", "－9"], "A", "負數在數線上越靠右越大，因此－1 大於其餘三數。"),
    ("將－2、0、－5、3 由小到大排列，何者正確？", ["－5、－2、0、3", "－2、－5、0、3", "3、0、－2、－5", "－5、0、－2、3"], "A", "數線上由左到右遞增，所以順序為－5、－2、0、3。"),
    ("數線上 x＝－1/2 與 y＝1/4，哪一個點在較右方？", ["y 點", "x 點", "兩點相同", "無法判斷"], "A", "1/4 大於－1/2，因此 y 點在數線上較右方。"),
    ("數線上兩點坐標為－3/2 與 5/2，兩點距離是多少？", ["4", "1", "－4", "5"], "A", "距離為 |5/2－(－3/2)|＝|8/2|＝4。"),
    ("某地氣溫原為－6℃，上升 9℃ 後變為多少？", ["3℃", "－3℃", "15℃", "－15℃"], "A", "上升 9℃ 表示 (－6)＋9＝3，所以氣溫為 3℃。"),
    ("若 |x|＝4，則 x 的所有可能值為何？", ["4 或－4", "只有 4", "只有－4", "0 或 4"], "A", "到 0 距離為 4 的數在兩側，故 x＝4 或－4。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-n-7-5-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        rotated = options[shift:] + options[:shift]
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + j), "text": value} for j, value in enumerate(rotated)]
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["knowledgeIds"] = [KNOWLEDGE]
        data["lessonId"] = LESSON
        data["difficulty"] = "medium"
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究數線位置、相反數、絕對值、比較與距離能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 number-line questions")


if __name__ == "__main__":
    main()
