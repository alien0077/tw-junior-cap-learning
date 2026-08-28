"""替換國文 6-Ⅳ-4 各類文本模板題為功能與格式判讀題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-6-iv-4.json").read_text())["source"]["url"]
ITEMS = [
    ("邀請校長參加成果展的信件，開頭最需要先交代哪項資訊？", ["活動名稱、日期時間、地點與邀請目的", "作者最喜歡的電影類型", "與成果展無關的天氣預測", "只寫一句『請務必來』而不說明原因"], "A", "正式邀請需先讓收件者知道活動是什麼、何時何地舉行及為何邀請。", "easy", "邀請信"),
    ("校慶集合公告要讓全校學生都能立即理解，哪種語氣最適當？", ["直接、清楚且有禮，列出時間、地點與注意事項", "使用大量隱喻，不說明集合位置", "只用命令與責罵語句，不提供資訊", "寫成只供作者自己閱讀的日記"], "A", "公告重視快速傳達公共資訊，需清楚、直接、有禮並交代必要細節。", "easy", "公告"),
    ("讀書心得中，哪一句最能表現讀者自己的思考，而不是只重述情節？", ["我原以為主角的選擇很自私，讀完後才理解他是在保護家人", "主角先回家，接著走到街上，最後回到家", "這本書共有十二章", "故事發生在一個地方"], "A", "選項 A 提出閱讀前後觀點的改變，呈現個人理解與反思。", "medium", "讀書心得"),
    ("實驗報告若要讓他人理解結果，哪種安排最完整？", ["列出目的、材料方法、觀察結果與結論", "只寫實驗最後成功或失敗", "只貼照片而不標示操作條件", "只寫自己的心情，不交代資料"], "A", "實驗報告需要讓讀者重現或檢核過程，因此應交代目的、方法、結果與結論。", "medium", "實驗報告"),
    ("將訪談內容整理成新聞稿時，哪項做法最重要？", ["核對受訪者原意，區分事實與引用，並交代時間地點", "把所有回答改成記者自己的意見", "刪除事件的時間與地點", "只保留最誇張的一句話吸引注意"], "A", "新聞稿重視可核對的事實與引用準確，不能把受訪者意見改成記者主張。", "hard", "新聞稿"),
    ("設計『午餐剩食原因』問卷前，哪個做法最能使問題符合調查目的？", ["先界定要了解的原因，再設計清楚且互不重疊的選項", "先寫出最想得到的答案", "每題同時詢問三件無關的事", "讓選項彼此重疊且不說明範圍"], "A", "先界定目的，再設計清楚選項，可降低受訪者誤解並提高資料可用性。", "hard", "問卷"),
    ("寫給同學的請假訊息，哪項資訊不可缺少？", ["請假日期、原因的適當說明與需要同學協助的事項", "作者最喜歡的歌曲排行榜", "沒有日期的模糊道歉", "只寫『我不去』而不交代對象"], "A", "請假訊息要讓對方知道何時、為何及是否需要配合，才能採取正確行動。", "easy", "訊息"),
    ("產品介紹若要幫助讀者判斷是否適合自己，最應包含什麼？", ["主要功能、適用對象、限制與價格或使用條件", "只使用『最好、最強』等無證據形容詞", "只放漂亮圖片，不說明功能", "隱藏可能影響選擇的限制"], "A", "完整產品資訊需同時呈現功能、對象、限制與條件，避免只靠誇張宣稱。", "medium", "產品介紹"),
    ("研究結果要寫成摘要，哪項原則最重要？", ["保留研究目的、方法、主要結果與結論，刪除不必要細節", "加入原文沒有的新結論", "只留下最吸引人的一句話", "把限制與不利結果全部刪除"], "A", "摘要要濃縮原研究的核心資訊，不可捏造新結論或刪去影響判斷的重要限制。", "hard", "摘要"),
    ("同一活動要同時發布給低年級學生與家長，最適當的做法是什麼？", ["保留相同事實，依讀者需要調整詞語、細節與說明方式", "對所有讀者使用完全相同的艱深術語", "只寫給作者自己理解的縮寫", "為不同讀者故意改變活動日期"], "A", "文本可依受眾調整表達，但活動日期等核心事實必須一致。", "medium", "受眾調整"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-6-iv-4-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究各類文本功能與應用文判讀題型（{locator}）；課綱 6-Ⅳ-4：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
