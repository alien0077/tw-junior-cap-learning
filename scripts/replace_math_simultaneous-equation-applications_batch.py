"""以公開國中數學段考的聯立方程式應用題方向，獨立替換 A-7-5 題目。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-a-7-5.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-a-7-5"
KNOWLEDGE = "kg-math-content-a-7-5"
ITEMS = [
    ("水果籃有蘋果 x 顆、橘子 y 顆，共 10 顆；每顆價格 30、50 元，總價 380 元。x、y 為何？", ["x＝6，y＝4", "x＝4，y＝6", "x＝5，y＝5", "x＝8，y＝2"], "A", "x＋y＝10 且 30x＋50y＝380，解得 x＝6、y＝4。"),
    ("兩數和為 15，且大數比小數多 3，兩數為何？", ["9 與 6", "8 與 7", "10 與 5", "12 與 3"], "A", "設大數 x、小數 y，x＋y＝15、x－y＝3，解得 x＝9、y＝6。"),
    ("解聯立方程式 2x＋y＝16、x＋3y＝18，x、y 為何？", ["x＝6，y＝4", "x＝4，y＝6", "x＝5，y＝6", "x＝7，y＝2"], "A", "由第一式 y＝16－2x，代入第二式得 x＝6，再得 y＝4。"),
    ("電影票成人票 x 張、學生票 y 張共 9 張，票價 240、180 元且總額 1,860 元。x、y 為何？", ["x＝3，y＝6", "x＝6，y＝3", "x＝4，y＝5", "x＝2，y＝7"], "A", "x＋y＝9、240x＋180y＝1860，解得 x＝3、y＝6。"),
    ("甲乙兩數和為 50，甲比乙多 8，甲數為何？", ["29", "21", "25", "42"], "A", "設甲為 x、乙為 y，x＋y＝50、x－y＝8；相加得 2x＝58，所以甲為 29。"),
    ("2 本相同筆記本與 3 枝相同筆的總價為 190 元；1 本筆記本與 1 枝筆共 80 元。筆記本與筆各多少元？", ["筆記本 50 元、筆 30 元", "筆記本 30 元、筆 50 元", "筆記本 60 元、筆 20 元", "筆記本 40 元、筆 40 元"], "A", "設筆記本 x、筆 y，2x＋3y＝190、x＋y＝80，解得 x＝50、y＝30。"),
    ("某班男生 x 人、女生 y 人共 32 人，女生比男生多 4 人。男生有幾人？", ["14 人", "18 人", "16 人", "12 人"], "A", "x＋y＝32、y－x＝4；相加得 2y＝36，故 x＝14。"),
    ("5 元硬幣 x 枚、10 元硬幣 y 枚共 18 枚，合計 135 元。5 元硬幣有幾枚？", ["9 枚", "7 枚", "8 枚", "11 枚"], "A", "x＋y＝18、5x＋10y＝135；除以 5 得 x＋2y＝27，解得 y＝9、x＝9。"),
    ("甲乙兩種果汁共 12 杯，甲每杯 25 元、乙每杯 35 元，總價 360 元。乙果汁有幾杯？", ["6 杯", "5 杯", "7 杯", "8 杯"], "A", "x＋y＝12、25x＋35y＝360；代入 x＝12－y 得 300＋10y＝360，所以 y＝6。"),
    ("某停車場汽車 x 輛、機車 y 輛共 20 輛，車輪總數 56 個。汽車有幾輛？", ["8 輛", "12 輛", "10 輛", "6 輛"], "A", "x＋y＝20、4x＋2y＝56；代入 y＝20－x 得 2x＝16，所以 x＝8。"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-a-7-5-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        rotated = options[shift:] + options[:shift]
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + j), "text": value} for j, value in enumerate(rotated)]
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["knowledgeIds"] = [KNOWLEDGE]
        data["lessonId"] = LESSON
        data["difficulty"] = "medium"
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中公開數學段考；研究聯立方程式列式、代入、消去與生活情境能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。"}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 simultaneous-equation application questions")

if __name__ == "__main__":
    main()
