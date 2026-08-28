"""以公開數學試題的資料分布分析方向，獨立替換 D-9-1 題目。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/math/content-d-9-1.json").read_text())["source"]["url"]
LESSON = "lesson-math-content-d-9-1"
KNOWLEDGE = "kg-math-content-d-9-1"

ITEMS = [
    ("資料 3、5、7、9、11 的中位數為何？", ["7", "5", "9", "11"], "A", "資料已由小到大排列，中間第三筆是 7，因此中位數為 7。"),
    ("某組資料的五數摘要為最小值 2、第一四分位數 5、中位數 8、第三四分位數 12、最大值 15，全距為何？", ["13", "10", "7", "15"], "A", "全距為最大值減最小值：15－2＝13。"),
    ("某組資料的第一四分位數為 7、第三四分位數為 14，四分位距為何？", ["7", "21", "10.5", "14"], "A", "四分位距為第三四分位數減第一四分位數：14－7＝7。"),
    ("甲組全距為 18，乙組全距為 11。若以全距比較資料分散程度，哪組較分散？", ["甲組", "乙組", "兩組相同", "無法由全距判斷"], "A", "全距越大，資料從最小值到最大值的分布範圍越大，因此甲組較分散。"),
    ("箱型圖中，右側鬚比左側鬚長許多，通常表示資料分布較可能具有哪種特徵？", ["右偏", "左偏", "完全對稱", "所有資料相等"], "A", "右側延伸較長代表較大的值向右拉長尾端，常稱為右偏分布。"),
    ("一組資料中只有最大值由 20 改成 100，哪個統計量通常受此極端值影響較明顯？", ["平均數", "中位數", "第一四分位數", "四分位距一定不變"], "A", "平均數會把每個數值納入計算，最大值大幅增加會明顯拉高平均數。"),
    ("甲組五數摘要為 2、5、8、12、16；乙組為 4、6、8、10、12。哪組全距較大？", ["甲組", "乙組", "兩組相同", "無法判斷"], "A", "甲組全距 16－2＝14，乙組全距 12－4＝8，因此甲組較大。"),
    ("五數摘要為 1、4、9、15、20，其中第三四分位數為何？", ["15", "4", "9", "20"], "A", "五數摘要依序為最小值、第一四分位數、中位數、第三四分位數、最大值，故第三四分位數為 15。"),
    ("某箱型圖的第一四分位數為 10、第三四分位數為 18，箱體代表的中間 50% 資料範圍是多少？", ["8", "28", "14", "50"], "A", "箱體長度就是四分位距：18－10＝8。"),
    ("關於箱型圖與資料分布，下列何者正確？", ["箱體涵蓋由第一四分位數到第三四分位數的資料範圍", "箱體一定涵蓋全部資料", "中位數一定等於平均數", "鬚的長度與資料單位無關"], "A", "箱體由第一、第三四分位數界定，代表中間約 50% 的資料；其他敘述不一定成立。"),
]


def main() -> None:
    for i, (prompt, options, _answer, explanation) in enumerate(ITEMS, 1):
        path = ROOT / "questions/math" / f"question-math-content-d-9-1-{i}.json"
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
            "sourceLocator": f"114 年國中教育會考數學科公開試題；研究資料分布、五數摘要、四分位距、箱型圖與離群值能力方向；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、圖表或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("replaced 10 statistical-distribution questions")


if __name__ == "__main__":
    main()
