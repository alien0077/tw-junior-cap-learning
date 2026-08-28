"""替換國文 4-Ⅳ-2 造字原則與形音義模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-4-iv-2.json").read_text())["source"]["url"]

ITEMS = [
    ("「湖」由「氵」和「胡」組成。下列說明何者最恰當？", ["「氵」提示意義與水有關，「胡」主要提示讀音", "「氵」只表示聲音，「胡」只表示筆畫", "兩個部件都只表示字義，沒有讀音線索", "「胡」決定湖泊一定在北方"], "A", "『氵』是形旁，提示與水相關；『胡』是聲旁，提供讀音線索。", "easy", "形旁與聲旁"),
    ("「清、情、晴、請」都有「青」這個部件。由此最合理的推論是什麼？", ["「青」在這組字中多提供相近的讀音線索", "四字的意思完全相同", "「青」都必定是表示水的形旁", "只要看到「青」就能確定整字讀音"], "A", "同一聲旁常提供相近讀音線索，但不能據此斷定字義相同或讀音完全相同。", "medium", "聲旁線索與限制"),
    ("下列哪一字較能作為會意字的例子，而不是形聲字？", ["休（人依木而息）", "江（氵加工）", "河（氵加可）", "晴（日加青）"], "A", "『休』由人與木的意義組合表達休息概念；其餘可分析為形聲結構。", "medium", "會意與形聲辨識"),
    ("「江」的「氵」在造字結構中最主要提示什麼？", ["字義與水域或水流相關", "整個字一定讀作三聲", "字形必須左右對稱", "聲旁一定表示河流大小"], "A", "『氵』是水部形旁，主要提供意義範疇，不直接決定聲調或水流大小。", "easy", "形旁與意義"),
    ("「鈴」含有「金」部件，若只依形旁推測，哪項最合理？", ["可先推測與金屬或金屬製品有關，再查字典確認", "可直接斷定它一定是金礦名稱", "可確定它的讀音與金完全相同", "可推測所有含金部件的字都指同一物品"], "A", "形旁提供意義範疇線索，但仍須結合語境或工具查證，不能過度推論。", "medium", "形旁推測限制"),
    ("「梅」可分析為「木」與「每」。下列說明何者正確？", ["「木」提示植物意義範疇，「每」提供讀音線索", "「木」提供聲音，「每」表示樹木部位", "兩部件都只表示梅花顏色", "只要看「每」就能確定字義"], "A", "『木』為形旁，『每』為聲旁；形聲字的部件功能可能不同。", "easy", "形聲字分析"),
    ("若看到一個生字左側是「言」部，最穩妥的學習方法是什麼？", ["先推測可能與言語相關，再依上下文與字典確認", "直接把它讀成『言』的讀音", "認定它一定表示稱讚", "只記部件不查整字用法"], "A", "部件能提供初步意義線索，但實際字義與讀音仍需依語境及工具確認。", "easy", "部件線索與查證"),
    ("「晴」與「清」都有「青」，但一字與天氣、一字與水有關。這說明什麼？", ["相同聲旁不代表字義相同，形旁能提供不同意義線索", "相同聲旁會使所有字義完全相同", "形旁只負責讓字變好看", "只要聲旁相同就不必查語境"], "A", "『日』與『氵』等形旁分別提供不同意義範疇，說明聲旁相同不等於字義相同。", "medium", "聲旁相同與字義"),
    ("下列哪一項最能說明學習造字結構的目的？", ["利用部件線索輔助辨認字音與字義，再以語境驗證", "只靠部件猜答案，不必閱讀句子", "把所有相似字當成同義字", "只背部首名稱，不理解整字"], "A", "造字結構是輔助線索，仍要回到語境與工具驗證，不能取代完整理解。", "medium", "形音義整合"),
    ("分析形聲字時，哪個步驟最能避免把聲旁當成絕對讀音規則？", ["先指出聲旁提供的可能讀音，再查現代字音與語境", "看到相同聲旁就一律讀完全相同", "只比較字的筆畫數", "忽略字典標音，只看部件外形"], "A", "聲旁是讀音線索而非絕對規則，應以字典與實際語境核對。", "hard", "聲旁推論與驗證"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-performance-4-iv-2-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        options = options[shift:] + options[:shift]
        answer = chr(65 + ((4 - shift) % 4))
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(options)]
        data["difficulty"] = difficulty
        data["answer"] = {"value": answer, "explanation": explanation}
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究造字原則與形音義判讀能力方向（{locator}）；另以官方語文領域課綱核對 4-Ⅳ-2（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
