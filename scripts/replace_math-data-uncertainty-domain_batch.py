"""以公開數學試題的資料分析與機率判讀方向，獨立替換 D 領域彙整題。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-d.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-d"
KNOWLEDGE = "kg-math-content-d"

ITEMS = [
    ("資料 8、12、15、5 的平均數為何？", ["10", "8", "12", "40"], "A", "總和為 40，共 4 筆資料，平均數為 40÷4＝10。"),
    ("資料 4、6、9、11、15 的中位數為何？", ["9", "6", "11", "15"], "A", "資料已排序，中間第三筆為 9，所以中位數是 9。"),
    ("資料 3、8、14、10 的全距為何？", ["11", "8", "6", "35"], "A", "全距為最大值 14 減最小值 3，等於 11。"),
    ("某類別有 12 筆資料，全部資料共 30 筆，其相對次數為何？", ["40%", "30%", "12%", "60%"], "A", "相對次數為 12÷30＝0.4＝40%。"),
    ("公平骰子擲一次，出現小於 3 點的機率為何？", ["1/3", "1/2", "1/6", "2/3"], "A", "小於 3 的結果為 1、2，共 2 個，機率為 2/6＝1/3。"),
    ("若事件 A 的機率為 0.7，則其互補事件的機率為何？", ["0.3", "0.7", "1.7", "0"], "A", "互補事件機率為 1－0.7＝0.3。"),
    ("比較兩組資料的長條圖時，哪項資訊最需要先核對？", ["縱軸單位與刻度", "只看柱子顏色", "只看柱子寬度", "忽略圖表標題"], "A", "單位與刻度決定柱高代表的數值，必須先核對才能比較。"),
    ("想估計全校學生最常使用的交通方式，哪種抽樣較能代表全校？", ["從各年級各抽取部分學生", "只調查一個班", "只詢問校隊學生", "只詢問放學最早的學生"], "A", "各年級抽樣可涵蓋不同年級，代表性通常比只調查單一群體高。"),
    ("甲組平均數 72、全距 8；乙組平均數 72、全距 20。哪項敘述較合理？", ["兩組平均表現相同，但乙組分數較分散", "甲組平均表現較高", "乙組每個人的分數都較高", "只由平均數可知甲組較分散"], "A", "平均數相同表示中心位置相同；乙組全距較大，表示分布範圍較廣。"),
    ("看到樣本調查結果後，哪種結論最恰當？", ["先說明樣本範圍與限制，再評估能否推論母體", "一定能代表所有人", "樣本越少結論越可靠", "只要百分比漂亮就不必看樣本"], "A", "統計推論須考慮抽樣方式、樣本範圍與限制，不能直接過度推論。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-d-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究資料統計、圖表、抽樣與古典機率的跨單元判讀方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 data-uncertainty domain questions")


if __name__ == "__main__":
    main()
