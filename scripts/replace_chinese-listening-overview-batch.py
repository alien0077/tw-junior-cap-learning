"""替換國文聆聽導覽單元的全 A 泛用題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/learning-performance.json").read_text())["source"]["url"]
ITEMS = [
    ("廣播先宣布『明日下午停課』，再說明原因與查詢管道。若只保留一項核心訊息，應保留什麼？", ["明日下午停課這項決定及適用時間", "廣播員使用的麥克風品牌", "背景音樂的曲名", "聽眾所在教室的顏色"], "A", "停課決定與適用時間直接影響聽者行動；原因與查詢管道則是後續的重要補充。", "easy", "核心訊息"),
    ("對話中說『我原本以為你不會來，沒想到你真的出現了』，最合理的態度判讀是什麼？", ["原先預期落空後感到意外，可能帶有驚喜", "對方早已確定不會出現且毫不意外", "說話者正在宣布正式規定", "這句話只是在列舉時間順序"], "A", "『原本以為』與『沒想到』形成預期和實際的落差，顯示意外，情緒仍需結合語氣判斷。", "medium", "語意與態度"),
    ("聽到『先整理資料，再比較結果，最後提出建議』，聽者應如何整理這段內容？", ["依三個順序詞記錄工作流程", "把三個步驟視為同時發生", "只記住最後的建議，不理會前面", "把資料、結果與建議當成三位人物"], "A", "『先、再、最後』明確標示步驟先後，適合用流程方式記錄。", "easy", "順序理解"),
    ("講者提高音量並放慢速度說『最重要的是安全』，這種聲音變化主要提示什麼？", ["這是需要特別注意的重點", "這句話與主題無關", "講者已經忘記所有內容", "聽者不必記錄這句話"], "A", "提高音量與放慢速度通常用來凸顯重點，提醒聽者特別注意安全。", "easy", "聲情提示"),
    ("聽到『雖然今天下雨，但是活動仍照常舉行』，前後分句的關係是什麼？", ["轉折：下雨的限制與活動照常的結果並存", "因果：下雨必然使活動舉行", "選擇：只能在下雨或活動中選一項", "並列：兩句沒有語意關係"], "A", "『雖然……但是……』表示轉折，前句提出不利條件，後句說明不同結果。", "easy", "轉折理解"),
    ("訪談先詢問受訪者的工作，再問遇到的困難，最後請其提出建議。最後一問的功能是什麼？", ["引導受訪者提出解決方向或經驗性的建議", "確認受訪者的出生日期", "重複第一題的工作內容", "結束訪談而不需要回答"], "A", "在了解工作與困難後詢問建議，可將訪談導向可能的做法或解決方向。", "medium", "訪談結構"),
    ("聽到『請於週五前填妥表單，交至教務處』，最需要記住哪兩項資訊？", ["截止時間與繳交地點", "廣播的音量與速度", "表單的紙張顏色與大小", "教務處附近的景物"], "A", "『週五前』是期限，『教務處』是繳交地點，兩者直接決定如何完成任務。", "easy", "公告資訊"),
    ("說話者先承認方案成本較高，接著說明它較安全。這段話最可能展現什麼論述態度？", ["承認限制後提出理由，較為完整而不迴避問題", "只挑優點而否認所有成本", "表示成本與安全完全無關", "沒有任何主張或理由"], "A", "先承認成本限制，再說明安全優點，表示說話者同時處理方案的代價與支持理由。", "medium", "主張與理由"),
    ("聽到『所以我們改在室內舉行』，前文最可能包含哪項內容？", ["原定戶外活動受到下雨等因素影響", "室內活動已經結束很久", "參加者都不喜歡室內場所", "沒有任何活動安排"], "A", "『所以』引出結果，前文應是導致改在室內舉行的原因或條件，例如天候不佳。", "medium", "因果推論"),
    ("若只聽到演講開頭與結尾，想判斷主旨，最適合比較哪些內容？", ["開頭提出的問題或主張與結尾的總結或呼籲", "講者的姓名與衣著", "背景音樂和麥克風聲音", "聽眾進場與離場的時間"], "A", "開頭常提出主題，結尾常重申觀點或提出行動；比較兩者可初步推測主旨，但不能代替完整聆聽。", "hard", "主旨判讀"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-1-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究聆聽組織、聲情、語意與主旨判讀題型（{locator}）；官方語文課綱學習表現：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
