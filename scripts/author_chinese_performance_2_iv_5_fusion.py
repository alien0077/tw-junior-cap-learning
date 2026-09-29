import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/chinese/lesson-chinese-performance-2-iv-5.json"
REPORT = ROOT / "implementation/reports/chinese-performance-2-iv-5-first-pass-review.json"


def rec(name, locator, concepts, forms, misconception, assessment):
    return {"publisher": name, "edition": f"{name} 公立校方國文課程計畫章節級證據", "sourceType": "public-web", "sourceLocator": locator, "reviewedAt": "2026-09-21", "findings": {"concepts": concepts, "representations": forms, "examplesOrEvidence": ["本課以午休噪音、飲水機提案與校園讀書角三個原創公開表達情境，僅承接公開課程的報告、評論、演說與論辯方向。"], "misconceptions": [misconception], "assessmentEmphasis": [assessment]}, "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、篇章、題目、答案、影音或版面。"}


def main():
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-chinese-performance-2-iv-5"
    data["title"] = "2-Ⅳ-5：把資料、觀點與行動說成負責任的公開表達"
    data["content"] = {"summary": "報告、評論、演說和論辯都要面對公開聽眾，但它們的任務並不相同：報告要交代資料與方法，評論要提出判準與評價，演說要讓聽眾理解並願意行動，論辯則要公平回應不同主張。本課以午休噪音、飲水機提案與校園讀書角三個原創情境，練習依目的組織證據、控制語氣、處理反方與提出可追蹤的行動。", "sections": [{"heading": "先選公開表達的任務", "body": "同一份七天噪音資料可以用報告呈現測量方法，用評論比較不同時段的影響，用演說呼籲改善，也可在論辯中檢查增設隔音設備的成本與公平。先定任務，才能決定材料順序和結論語氣。"}, {"heading": "資料要交代怎麼來的", "body": "數字、訪談、照片與觀察各有能回答的問題。說明樣本、時間、測量方式、選取原因與限制，讀者才知道資料代表什麼；三名受訪者的經驗可以提供觀點，不能直接代表全校。"}, {"heading": "評論需要判準和取捨", "body": "『很好』『很糟』不是完整評論。先提出公平、效果、成本、可行性或安全等判準，再用資料比較方案，承認不同判準可能衝突，讓評價可以被檢查而不是只看作者喜好。"}, {"heading": "演說結尾要能追蹤", "body": "有感染力的結尾不等於誇大承諾。行動呼籲要說明對象、時間、第一步、所需資源與檢討方式；遇到不確定性要說清楚，讓聽眾能在後續用資料確認成效並修正方案。"}]}
    data["studyHighlights"] = ["先分辨報告、評論、演說與論辯的任務和聽眾需求。", "交代資料來源、方法、樣本與限制，不把少數經驗擴大成全體。", "以明確判準比較方案，承認效果、成本、公平與安全的取捨。", "用可追蹤的對象、時間、第一步與檢討指標完成行動呼籲。"]
    data["teaching"] = {"body": [
        {"id": "hook", "phase": "hook", "heading": "七天噪音資料要怎麼開口？", "body": "把同一組午休噪音資料交給四組人，分別要求做報告、評論、演說或論辯。先比較他們會把什麼放在開頭、資料段與結尾，再指出任務改變時，證據不一定改變，但組織與語氣必須改變。"},
        {"id": "explain", "phase": "explain", "heading": "公開表達的任務矩陣", "body": "報告回答發生什麼、怎麼知道；評論回答依什麼判準評估；演說回答為何現在要行動；論辯回答不同主張哪裡相同、哪裡有證據分歧。每一格都標記聽眾、資料、限制與希望產生的回應。"},
        {"id": "worked-example", "phase": "worked-example", "heading": "讓訪談和測量各就其位", "body": "七天測量顯示午休某時段平均較高，三名學生說明干擾感受。報告中分開描述數值與訪談，評論時以學習影響和可行性作判準，演說時才提出先試行分流；不能把三名同學的感受寫成全校民調。"},
        {"id": "guided-practice", "phase": "guided-practice", "heading": "為飲水機提案補上反方", "body": "提案說增設飲水機能減少排隊，學習者要補查尖峰人流、用水量、維修成本、位置公平與替代方案。再用一段公平的反方陳述測試提案，最後把呼籲改成有試行、責任與檢討日期的行動。"},
        {"id": "transfer", "phase": "transfer", "heading": "用同一證據對不同聽眾說話", "body": "把校園讀書角資料改寫給校長、同學、家長與管理人員：校長需要資源與成效指標，同學需要使用規則，家長關心安全，管理人員關心維護。保留資料來源與限制，但調整例證、順序和行動要求。"},
        {"id": "reflect", "phase": "reflect", "heading": "回看公開表達的責任", "body": "圈出一個誇大因果、藏起成本、忽略反方或承諾無法追蹤的句子。改成有資料範圍、判準、條件與檢討點的版本，再請同伴指出聽完後能做的第一步與仍需要查的問題。"},
    ], "summary": ["先判斷報告、評論、演說或論辯的任務與聽眾。", "區分測量、訪談、觀察與推論，交代樣本、方法與限制。", "用判準比較方案，公平呈現反方與多面向取捨。", "將行動呼籲寫成有對象、時間、資源與檢討指標的方案。"], "exitCheck": [{"prompt": "報告、評論、演說和論辯的主要任務有何不同？", "expectedEvidence": "能分別說明資料交代、判準評價、行動說服與回應不同主張的任務。"}, {"prompt": "為什麼三名訪談者不能直接代表全校？", "expectedEvidence": "能指出樣本數、選取方式與觀點範圍限制，並說明訪談可提供感受或觀點但不等同全體統計。"}, {"prompt": "如何讓演說的行動呼籲可追蹤？", "expectedEvidence": "能列出對象、時間、第一步、資源、成功指標與檢討／修正方式。"}]}
    data["interactive"] = {"type": "guided-choice", "goal": "依公開表達任務組織資料、判準、反方與可追蹤行動，讓結論與證據相稱。", "scenario": "從午休噪音、飲水機與讀書角專題中，逐步切換報告、評論、演說與論辯。", "variables": [{"symbol": "g", "meaning": "表達任務"}, {"symbol": "e", "meaning": "證據與判準"}, {"symbol": "a", "meaning": "行動與追蹤"}], "steps": [
        {"id": "step-1", "prompt": "已有七天噪音值與三名訪談，要向校務會議報告，哪句最適合作為開頭主旨？", "options": ["本報告整理午休七天噪音測量與三名學生訪談，說明時段差異及資料限制", "午休噪音已經讓全校都無法學習", "只要立刻裝隔音設備就能解決"], "answer": "A", "feedback": "A 交代資料種類、範圍與任務，不把少數訪談或測量直接擴大成全校結論。"},
        {"id": "step-2", "prompt": "要說服校園增設飲水機，哪項證據整理較負責任？", "options": ["比較尖峰排隊、人流、用水需求、成本、維修與位置公平，並標示替代方案和限制", "只展示最長排隊照片", "說大家一定會喜歡新設備"], "answer": "A", "feedback": "A 以多面向判準比較方案，能處理效果、成本、公平與執行風險。"},
        {"id": "step-3", "prompt": "演說結尾如何把呼籲變成可追蹤行動？", "options": ["指定對象、時間、第一步、資源、成功指標與檢討日期", "用更激動的口號要求立即答應", "承諾一定能解決所有問題"], "answer": "A", "feedback": "A 讓聽眾知道如何開始、如何判斷成效與何時修正，不用誇大保證。"},
    ]}
    data["authoringStandard"] = "version-fused-v1"
    data["updatedAt"] = "2026-09-21"
    data["versionResearch"] = [
        rec("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf；國語文口語表達、報告與意見溝通定位；核讀 2026-09-21。", ["依目的、對象與情境組織口語表達和意見。", "表達需能整理資料、說明重點並回應聽眾。"], ["報告、說明、演說、理由、例證與回應。"], "把聲量與情緒當成說服力，忽略資料與聽眾任務。", "評量口語組織、資料運用、表達適切與互動。"),
        rec("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf；國語文討論、報告、辯論與合作表達定位；核讀 2026-09-21。", ["公開表達需聆聽不同觀點、提出理由並依回饋修正。", "合作報告和辯論要兼顧資料、態度與行動可行性。"], ["資料鏈、判準、反方、讓步、方案與檢討。"], "把報告、評論、演說和辯論混成同一種說話，只追求說服而不交代證據。", "重視任務辨識、組織、反駁、回饋與修正。"),
        rec("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf；國文報告、評論、論證與評量定位；核讀 2026-09-21。", ["表達要區分資料、觀點、推論與評價，並掌握結論範圍。", "公開溝通需提出證據、限制與可行的回應。"], ["來源、樣本、判準、因果、反例、成本與行動指標。"], "把少數經驗擴大成全體，或把價值選擇說成純粹事實。", "要求證據連結、任務適配、反方回應與結論可追蹤。"),
    ]
    data["fusionRecord"] = {"commonCore": ["三版本公開結構共同支持報告、評論、演說、論辯與依目的組織表達。", "資料、觀點、判準、反方、限制與行動回應需要互相對齊。", "公開說服不能超過證據，行動需要可追蹤的對象、時間與檢討。"], "versionDifferences": ["南一較突顯口語表達、資料整理與對象；康軒較突顯報告、辯論、合作與回饋；翰林較突顯論證、判準、限制、因果與結論追蹤。這是公開課程計畫層級差異，不宣稱完整教材差異。"], "originalAdditions": ["以噪音資料切換報告、評論、演說與論辯任務。", "以飲水機提案比較效果、成本、公平與維修證據。", "以讀書角方案依不同聽眾重排資料並設計行動指標。"], "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織公開表達任務、資料方法、判準、反方、公平說服與行動追蹤。正文、原創情境、互動步驟、回饋與檢核均為本專案重寫，未複製教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    data["teaching"]["body"][1]["body"] += " 讀者完成矩陣後，必須說出哪一項資料會改變結論、哪一項價值取捨不能單靠資料解決，避免把四種任務只當成不同標題。"
    data["teaching"]["body"][5]["body"] += " 把同伴的第一步與疑問寫進修訂版，並檢查承諾是否有明確負責人、資料來源與可以撤回或調整的條件。"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "2-Ⅳ-5：把資料、觀點與行動說成負責任的公開表達", "lessonId": data["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored chinese performance 2-iv-5")


if __name__ == "__main__":
    main()
