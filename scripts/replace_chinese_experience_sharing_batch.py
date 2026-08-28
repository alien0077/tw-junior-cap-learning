"""替換國文 2-Ⅳ-1 經驗分享題；題目為公開試題能力方向的安全獨立改編。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/806/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1(%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F%E2%94%80%E5%9C%8B%E8%AA%9E%E6%96%87).pdf"

ITEMS = [
    ("向班上介紹校外教學經驗時，開頭最需要先交代哪項資訊？", ["活動時間、地點與目的", "自己最喜歡的零食", "全班同學的座號", "報告共有幾個字"], "A", "先交代時間、地點與目的，聽眾才能建立事件背景。", "easy", "經驗分享的背景交代"),
    ("小芸分享迷路經驗，依序說明出發、發現走錯路、詢問店家與找到車站。這樣安排最主要的作用是什麼？", ["呈現事件發展順序", "刪除所有關鍵事件", "把經驗改成無關公告", "只強調說話者外表"], "A", "依事件發生先後說明，能讓聽眾掌握經過與轉折。", "easy", "事件順序與脈絡"),
    ("向低年級學生介紹登山經驗時，下列哪種說法最適合？", ["使用清楚短句，並解釋必要的專有詞", "只使用未說明的專業縮寫", "假定聽眾知道所有背景", "只朗讀投影片上的長段文字"], "A", "應依聽眾調整詞語與說明深度，讓資訊可理解。", "medium", "聽眾與表達調整"),
    ("分享參加志工活動的經驗時，若想讓聽眾理解自己的收穫，最適合加入什麼？", ["具體事件與由事件得到的感受或體會", "與活動完全無關的傳聞", "只有抽象口號而無例子", "未經查證的他人私事"], "A", "具體事件連結感受或體會，能支持經驗分享的重點。", "medium", "事件與感受的連結"),
    ("小組報告中，前一位同學已說明活動流程，下一位要分享自己遇到的困難。最適合的銜接方式是什麼？", ["先承接流程，再說明自己遇到的具體困難", "重複前一位同學的每句話", "突然改談與活動無關的新聞", "只說『我不知道』便結束"], "A", "承接前文後補充新面向，可維持報告的連貫性。", "medium", "口語銜接與組織"),
    ("分享球賽經驗時，說者想表達『雖然落後，仍靠合作逆轉』。哪項材料最能支持這個重點？", ["說明落後情況及隊員如何分工追回分數", "只列出觀眾穿什麼顏色的衣服", "只報告比賽開始的時間", "只說自己喜歡哪位球員"], "A", "落後情況與分工合作的具體內容，直接支持逆轉與合作的主題。", "medium", "主題與細節取捨"),
    ("聽同學分享受傷復健經驗時，哪個回應最能表示理解並保持尊重？", ["先表達關心，再詢問對方願意分享的復健過程", "立刻比較誰受過更嚴重的傷", "未經同意把故事轉告全班", "打斷對方並批評他的選擇"], "A", "先關心並尊重分享界線，回應才符合溝通情境。", "medium", "聆聽回應與尊重"),
    ("若三分鐘經驗分享只剩最後半分鐘，最適合如何收束？", ["用一句話重申重點，再說明自己的主要收穫", "新增三個完全無關的故事", "重新從頭逐字朗讀", "只說『以上』而不交代結論"], "A", "時間有限時應保留主旨與收穫，清楚完成結尾。", "easy", "時間限制與結尾"),
    ("分享第一次煮飯的經驗時，哪種內容最能讓聽眾判斷失敗原因？", ["說明食材、步驟與哪一步出現問題", "只說最後很好吃", "只描述廚房的牆壁顏色", "只引用與煮飯無關的名言"], "A", "食材、步驟與問題位置能提供可理解的因果線索。", "medium", "經驗細節與因果"),
    ("準備經驗分享的講稿後，哪項檢查最重要？", ["確認內容符合目的、順序清楚且聽眾能理解", "只計算每段有幾個逗號", "把所有具體例子刪掉", "只確認字體顏色一致"], "A", "口語表達須回到目的、組織與聽眾理解進行檢查。", "easy", "口語表達整體檢核"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-performance-2-iv-1-{i}.json"
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
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究經驗分享、口語組織與聆聽回應能力方向（{locator}）；另以官方語文領域課綱核對 2-Ⅳ-1（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
