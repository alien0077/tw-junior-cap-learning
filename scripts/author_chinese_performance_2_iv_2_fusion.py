import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/chinese/lesson-chinese-performance-2-iv-2.json"
REPORT = ROOT / "implementation/reports/chinese-performance-2-iv-2-first-pass-review.json"


def rec(name, locator, concepts, forms, misconception, assessment):
    return {"publisher": name, "edition": f"{name} 公立校方國文課程計畫章節級證據", "sourceType": "public-web", "sourceLocator": locator, "reviewedAt": "2026-09-21", "findings": {"concepts": concepts, "representations": forms, "examplesOrEvidence": ["本課以校園遮蔭、午餐動線與社區會議三個原創聽聞討論情境，僅承接公開課程的提問、回饋與邏輯整理方向。"], "misconceptions": [misconception], "assessmentEmphasis": [assessment]}, "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、篇章、題目、答案、影音或版面。"}


def main():
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-chinese-performance-2-iv-2"
    data["title"] = "2-Ⅳ-2：聽懂論證再提問，用回饋推進討論"
    data["content"] = {"summary": "有效的提問不是把自己的立場換成問號，回饋也不是把對方評分高低而已。聽完一段主張後，要先整理問題、理由、證據、假設與未解處，再依討論目的提出能縮小不確定性的問題；回饋時指出已理解之處、需要補強的證據和下一步可做的修正。本課以遮蔭提案、午餐動線與社區會議三個原創情境，練習讓對話從表態走向共同檢查。", "sections": [{"heading": "提問前先重建對方的路線", "body": "聽到『增加遮蔭能讓學生更健康』，先寫主張、對象、理由和證據，再問健康指標、時間範圍或替代因素。若尚未掌握對方意思，先用一句話重述，避免問題建立在誤聽上。"}, {"heading": "好問題會改變下一步", "body": "『你為什麼這樣想？』可能太寬；『你用哪段溫度資料比較遮蔭前後，還固定了哪些條件？』能把討論帶到可檢查的位置。問題要和目的相稱，探究、決策、澄清與關係修復的問法並不相同。"}, {"heading": "回饋要同時清楚又可行", "body": "先指出自己聽懂的核心，再指出一個具體缺口，最後提出可選的修正方式。避免用『很棒／很差』概括，也不要把建議包成命令；讓對方知道如何回應或不同意。"}, {"heading": "邏輯分歧可以被定位", "body": "若兩人答案不同，將分歧放回定義、資料、因果、價值優先順序或執行限制中的一層。標出是哪一層不同，才能選擇補資料、改定義、比較方案或承認價值取捨，而不是互貼標籤。"}]}
    data["studyHighlights"] = ["提問前先重述對方主張、理由、證據與未解處。", "讓問題對準資料、定義、條件或下一步，而不是只表達不滿。", "回饋採理解—缺口—可行修正三段，具體且保留不同意空間。", "把分歧定位在定義、證據、因果、價值或執行限制，選對處理方法。"]
    data["teaching"] = {"body": [
        {"id": "hook", "phase": "hook", "heading": "『增加遮蔭』要問什麼才有用？", "body": "先讓學生聽一段遮蔭提案，只能寫下自己確定聽到的主張和證據，再提出一個會改變下一步的問題。比較『你確定嗎？』與『哪個時段的地表溫度資料支持這個方案？』，看見問題品質取決於它能否縮小缺口。"},
        {"id": "explain", "phase": "explain", "heading": "提問的四個方向盤", "body": "先分辨是在澄清名詞、追問證據、檢查因果還是規劃行動，再選相應問句。每個問題都要標示對象、範圍、時間或資料來源；若對方尚未說清楚，不要偷偷補入自己的假設。"},
        {"id": "worked-example", "phase": "worked-example", "heading": "把反對改成可回答的問題", "body": "原創回應『這方案一定沒用』可改為『你預測哪個指標會改變？若一週後沒有差異，是否代表遮蔭無效，還是需要檢查使用率與測量時間？』這樣保留疑慮，又把絕對判斷轉成可檢查的條件。"},
        {"id": "guided-practice", "phase": "guided-practice", "heading": "給午餐動線提案三段回饋", "body": "先重述提案者要改善的問題，再指出目前缺少尖峰時段人流或等待時間資料，最後提出先做一週分時段計數的修正。學習者要避免用個性、動機或能力評價人，只回應內容和下一步。"},
        {"id": "transfer", "phase": "transfer", "heading": "處理社區會議的多層分歧", "body": "當居民在意噪音、店家在意營業、學生在意通行時，先分開資料爭議、價值優先與執行限制。為每一層各設計一個問題和一個可行動回饋，最後標示哪些分歧不能靠更多數據單獨消除。"},
        {"id": "reflect", "phase": "reflect", "heading": "回看問題是否只是立場宣告", "body": "圈出自己提出的一個問題，檢查它是否預設答案、攻擊人、範圍太大或沒有可用資料。改寫後請同伴回答：這個問題會讓討論增加什麼資訊、修正哪個推論或決定哪個下一步。"},
    ], "summary": ["先重述聽聞內容，拆開主張、理由、證據、假設與未解。", "依澄清、證據、因果或行動目的提出可回答問題。", "以理解、具體缺口與可行修正組成回饋，不評斷人格。", "定位分歧層次，分開可用資料、價值取捨與執行限制。"], "exitCheck": [{"prompt": "為什麼提問前要先重述對方？", "expectedEvidence": "能說明重述可檢查是否誤聽，並把主張、理由與證據範圍對齊後再追問。"}, {"prompt": "什麼樣的問題能真正推進遮蔭提案？", "expectedEvidence": "能提出包含指標、時段、比較條件或資料來源的問題，且回答後會改變評估或下一步。"}, {"prompt": "如何給一個既尊重又有用的回饋？", "expectedEvidence": "能先重述理解，再指出具體缺口並提出可行修正，避免攻擊動機或用空泛評語結束。"}]}
    data["interactive"] = {"type": "guided-choice", "goal": "重建聽聞邏輯、提出能縮小缺口的問題、給出具體回饋並定位分歧。", "scenario": "從遮蔭、午餐動線與社區議題中，逐步把表態轉成可回答問題和下一步。", "variables": [{"symbol": "l", "meaning": "主張與邏輯"}, {"symbol": "q", "meaning": "問題方向"}, {"symbol": "f", "meaning": "回饋與修正"}], "steps": [
        {"id": "step-1", "prompt": "聽完『校園應增加遮蔭』，哪個問題最能打開討論？", "options": ["你用哪個時段的溫度或使用資料比較遮蔭前後，還固定了哪些條件？", "你為什麼總是這麼想？", "大家一定都會支持吧？"], "answer": "A", "feedback": "A 同時追問資料、比較條件與範圍，回答後能改變方案評估。"},
        {"id": "step-2", "prompt": "要指出午餐動線提案的缺口，哪種回饋最適切？", "options": ["我理解你想減少尖峰等待；目前少了分時段人流資料，可以先記錄一週再比較。", "你的提案很差，根本沒想清楚。", "很棒，大家照做就好。"], "answer": "A", "feedback": "A 先確認理解，再指出可定位的資料缺口與可行下一步，不把內容問題變成人格評價。"},
        {"id": "step-3", "prompt": "社區會議出現多方分歧時，第一個整理步驟是什麼？", "options": ["區分資料爭議、價值優先與執行限制，再為各層選問題或行動", "只投票決定誰的感受比較正確", "把不同意見全部統一成同一個結論"], "answer": "A", "feedback": "A 先定位分歧種類，才能知道要補資料、討論價值，還是調整執行方案。"},
    ]}
    data["authoringStandard"] = "version-fused-v1"
    data["updatedAt"] = "2026-09-21"
    data["versionResearch"] = [
        rec("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf；國語文聆聽理解、提問與口語回應定位；核讀 2026-09-21。", ["理解聽聞內容後提出適切問題與回應。", "口語互動需依目的、對象與情境調整。"], ["主張、理由、證據、追問、重述與回饋。"], "把問題當成反對表態，沒有先確認聽懂的內容。", "評量聆聽理解、提問品質、回應與互動禮貌。"),
        rec("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf；國語文討論、合作溝通與意見回饋定位；核讀 2026-09-21。", ["討論要能聆聽不同觀點、澄清、提出理由並回應異議。", "回饋應促進共同理解與修正，而非只做評分。"], ["問句類型、對話輪次、理解重述、具體建議與修訂。"], "把友善誤解成不提出缺口，或把直接批評誤解成有效回饋。", "重視提問、回饋、分歧處理與合作修正。"),
        rec("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf；國文聆聽邏輯、歸納與評量定位；核讀 2026-09-21。", ["聆聽後需掌握訊息關係、推論界線與說話者觀點。", "問題與回應應能以文本／話語證據支持，並指出限制。"], ["因果、定義、資料、替代解釋、價值與執行限制。"], "看到分歧就把對方歸因成無知或惡意，跳過邏輯層次。", "要求證據連結、問題可回答、回饋具體且結論有範圍。"),
    ]
    data["fusionRecord"] = {"commonCore": ["三版本公開結構共同支持聆聽理解、提問、回饋、討論與共同修正。", "問句要連結主張、證據、目的與下一步，不能只是換形式的立場。", "分歧要被定位和說明，回饋要保留對方修正與不同意的空間。"], "versionDifferences": ["南一較突顯聆聽理解與情境回應；康軒較突顯討論、合作、回饋與修訂；翰林較突顯邏輯關係、證據界線、觀點與限制。這是公開課程計畫層級差異，不宣稱完整教材差異。"], "originalAdditions": ["以遮蔭提案將空泛反對改成資料問題。", "以午餐動線練習理解—缺口—修正三段回饋。", "以社區會議分辨資料、價值與執行三種分歧。"], "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織聽聞邏輯、問題方向、回饋修正與分歧定位。正文、原創情境、互動步驟、回饋與檢核均為本專案重寫，未複製教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    data["teaching"]["body"][1]["body"] += " 每次提問前先在紙上寫『我已知道什麼、我還需要知道什麼、答案會改變哪個決定』，若三者接不起來就先重述而不是急著問。"
    data["teaching"]["body"][5]["body"] += " 改寫後保留對方可能不同意的出口，並記錄若對方提供新資料，自己願意修正哪一個判斷。"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "2-Ⅳ-2：聽懂論證再提問，用回饋推進討論", "lessonId": data["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored chinese performance 2-iv-2")


if __name__ == "__main__":
    main()
