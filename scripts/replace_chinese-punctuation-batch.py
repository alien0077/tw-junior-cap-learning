"""替換國文 6-Ⅳ-1 標點模板題為句子語意判讀題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-6-iv-1.json").read_text())["source"]["url"]
ITEMS = [
    ("句子『請先確認姓名、班級與座號：再交回表單。』若要使冒號用法正確，應如何修改？", ["將冒號改為逗號，因後面只是同一句的連續動作", "將冒號改為問號，因前句正在提問", "刪除所有標點，讓語氣更快", "在冒號後改接完全無關的話題"], "A", "冒號後不是對前文的具體說明，而是同一句中的下一個動作，使用逗號較合適。", "medium", "冒號語意"),
    ("下列哪一句的標點最能表現突然發現禮物時的強烈驚喜？", ["原來你把禮物藏在這裡！", "原來你把禮物藏在這裡。", "原來你把禮物藏在這裡？", "原來，你把，禮物，藏在這裡"], "A", "驚嘆號能表現強烈情緒；句意是驚喜發現，不是平淡敘述或疑問。", "easy", "驚嘆號"),
    ("『如果明天下雨我們就改在教室集合』要使條件與結果清楚，最適合在哪裡加逗號？", ["如果明天下雨，我們就改在教室集合", "如果，明天下雨我們就改在教室集合", "如果明天下雨我們，就改在教室集合", "如果明天下雨我們就改，在教室集合"], "A", "條件分句與結果分句之間加逗號，可清楚區分『下雨』與『改在教室集合』。", "easy", "逗號分句"),
    ("下列哪個版本最適合表達『你已經完成報告了嗎』的疑問語氣？", ["你已經完成報告了嗎？", "你已經完成報告了嗎！", "你已經完成報告了嗎。", "你已經完成，報告了嗎。"], "A", "句子詢問是否完成報告，句末應使用問號。", "easy", "問號"),
    ("校刊句子『我們需要三項資料；訪談紀錄、問卷結果和借閱統計。』若要正確列舉，最適合如何修改？", ["將分號改為冒號，後面引出三項資料", "將分號改為問號，表示疑問", "刪除三項資料，只保留前句", "將三項資料改成沒有標點的長句"], "A", "前句『需要三項資料』，後文具體列出內容，應用冒號引出說明或列舉。", "medium", "冒號列舉"),
    ("『他不是不想參加而是還沒收到通知』若要標示轉折語意，最恰當的標點是什麼？", ["他不是不想參加，而是還沒收到通知。", "他不是不想參加？而是還沒收到通知。", "他不是不想參加！而是還沒收到通知。", "他不是，不想參加而是還沒收到通知。"], "A", "『不是……而是……』前後是語意轉折，逗號放在前一分句後可使結構清楚。", "medium", "轉折與逗號"),
    ("朗讀『你真的願意再試一次嗎』時，句末標點除了影響停頓，也主要提示什麼？", ["說話者是在提出疑問，語氣應上揚", "說話者已經下達命令，語氣必須下降", "說話者正在列舉三個項目", "說話者完全沒有情緒或目的"], "A", "問號不只提示停頓，也提示句子的疑問功能與相應語氣。", "medium", "標點與語氣"),
    ("說服文寫『我們應減少一次性餐具，因為校園每天產生大量垃圾』。若要讓理由清楚，哪種寫法最恰當？", ["我們應減少一次性餐具，因為校園每天產生大量垃圾。", "我們應減少一次性餐具？因為校園每天產生大量垃圾。", "我們應減少一次性餐具！因為校園每天產生大量垃圾？", "我們應減少，一次性餐具因為，校園每天產生大量垃圾。"], "A", "主張與『因為』引出的理由屬同一完整論述，逗號分隔、句末用句號最清楚。", "medium", "說服語句"),
    ("下列哪一句最適合用分號連接兩個意思相關、結構相近的分句？", ["紙本資料便於批註；電子資料便於搜尋。", "今天下雨；所以我帶傘嗎？", "請問你；何時回家？", "哇；這場表演真精彩！"], "A", "分號可連接兩個相關且相對獨立的分句；第一句的兩個分句結構相近，最合適。", "hard", "分號"),
    ("修改說服文章時，發現一句話連續使用五個逗號，讀者難以分辨主張和理由。最適合的做法是什麼？", ["依語意分成兩句或改用適當的句號、分號與冒號", "把五個逗號全部保留並再增加三個", "刪去主張，只留下標點", "不看語意，改成全部使用驚嘆號"], "A", "標點應服務語意層次；可依主張、理由與列舉關係分句並選用適當標點。", "hard", "標點修訂"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-6-iv-1-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究標點與語意判讀題型（{locator}）；課綱 6-Ⅳ-1：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
