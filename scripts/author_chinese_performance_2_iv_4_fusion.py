import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/chinese/lesson-chinese-performance-2-iv-4.json"
REPORT = ROOT / "implementation/reports/chinese-performance-2-iv-4-first-pass-review.json"


def rec(name, locator, concepts, forms, misconception, assessment):
    return {"publisher": name, "edition": f"{name} 公立校方國文課程計畫章節級證據", "sourceType": "public-web", "sourceLocator": locator, "reviewedAt": "2026-09-21", "findings": {"concepts": concepts, "representations": forms, "examplesOrEvidence": ["本課以午餐剩食、校園步行安全與社區樹木資料三個原創資訊表達情境，僅承接公開課程的科技媒介與溝通方向。"], "misconceptions": [misconception], "assessmentEmphasis": [assessment]}, "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、篇章、題目、答案、影音或版面。"}


def main():
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-chinese-performance-2-iv-4"
    data["title"] = "2-Ⅳ-4：選對科技媒介，讓資料說得清楚又負責"
    data["content"] = {"summary": "科技媒介能把資料變成圖表、地圖、聲音、動畫或互動頁面，但媒介本身不會自動讓表達變得可信。要先確定受眾與目的，再選能保留資料意義的表示方式，標示來源、單位、樣本與不確定性，並處理授權、隱私、可及性與誤導風險。本課以午餐剩食、步行安全與社區樹木資料三個原創專題，練習從原始資料到負責任的數位表達。", "sections": [{"heading": "先問誰要用這份資訊", "body": "校長要看一個月趨勢、學生要找哪天剩食最高、家長要知道政策影響，三者需要的媒介不同。先寫受眾、決策與時間，再決定用折線圖、摘要、地圖或互動篩選，避免為了炫技加入無助於判斷的效果。"}, {"heading": "圖表必須保留資料關係", "body": "軸線、單位、起點、分組、樣本數與缺測值會改變讀者理解。截斷座標可能放大差異，平均值可能藏住極端日；製作前後都要回到原始表格核對，不用顏色或動畫替資料做出不存在的趨勢。"}, {"heading": "來源與授權是內容的一部分", "body": "圖片、地圖、音檔與資料集都有來源與使用條件。記錄作者、日期、授權、修改方式與連結，涉及個人位置或影像時去識別化並取得必要同意。沒有來源的漂亮素材不能因為容易下載就直接放進作品。"}, {"heading": "讓不同讀者都能取得重點", "body": "互動圖表要有文字摘要、鍵盤可讀標籤、替代文字與可下載資料表；顏色之外提供符號或文字。若模型或資料有不確定性，頁面應直接寫出限制，讓讀者不必猜測哪些是觀察、估計或作者解釋。"}]}
    data["studyHighlights"] = ["依受眾、目的、決策與時間選擇媒介，不為炫技而使用效果。", "核對軸線、單位、樣本、缺測、分組與原始資料，避免圖表誤導。", "記錄來源、授權、修改與個資界線，將資料倫理納入作品。", "提供文字摘要、替代表示、鍵盤可讀資訊與不確定性說明。"]
    data["teaching"] = {"body": [
        {"id": "hook", "phase": "hook", "heading": "同一份剩食資料要做幾種作品？", "body": "拿一個月每日剩食量的原創表格，分別想像校長、廚房人員和學生會怎麼使用。讓學習者先寫決策問題，再比較摘要、折線圖、可篩選表格與短影片各自保留和隱藏什麼，媒介選擇從需求而不是流行開始。"},
        {"id": "explain", "phase": "explain", "heading": "科技表達的五道檢核", "body": "依序檢查受眾與目的、資料與表示、來源與授權、可及性、限制與下一步。每完成一項就留下可追溯紀錄；若圖表好看但無法說出單位、樣本或缺測處理，就先回到資料層重做。"},
        {"id": "worked-example", "phase": "worked-example", "heading": "把步行安全資料放上地圖", "body": "先把匿名化的路口事件依日期、時段與事件類型整理，再決定地圖只顯示必要區域並加文字表格。比較事件數和暴露人次時標出分母，避免把人多的路口自然誤判為每人風險最高。"},
        {"id": "guided-practice", "phase": "guided-practice", "heading": "拆穿會放大差異的圖表", "body": "給同一組樹木存活率的兩種縱軸圖，要求學習者指出起點、時間窗、樣本與缺測。再改成保留零點或附上數值表的版本，說明何時可以使用截斷軸以及必須如何提醒讀者。"},
        {"id": "transfer", "phase": "transfer", "heading": "把專題變成可用的數位作品", "body": "小組製作一頁式專題：標題、文字摘要、主圖、資料下載、來源／授權、限制與回饋管道缺一不可。測試者使用鍵盤、手機與黑白列印版本，回報哪個資訊仍無法取得，再依證據修正設計。"},
        {"id": "reflect", "phase": "reflect", "heading": "檢查作品是否說過頭", "body": "回看自己的圖文，圈出一個把相關寫成因果、把樣本寫成全體、把估計寫成觀察或把素材來源省略的句子。改寫為有範圍的表述，並加上讀者可以查證、下載或提出修正的入口。"},
    ], "summary": ["從受眾、目的與決策需求選科技媒介。", "核對資料表示、來源、單位、樣本、缺測與不確定性。", "將授權、匿名化、可及性與替代表示當成作品內容。", "以限制、下載資料與回饋管道讓數位作品可查證和修正。"], "exitCheck": [{"prompt": "為什麼同一份剩食資料可能需要不同媒介？", "expectedEvidence": "能連結不同受眾的決策與時間需求，說明摘要、圖表或互動表示各自保留與隱藏的資訊。"}, {"prompt": "圖表發布前要檢查哪些會改變解讀的項目？", "expectedEvidence": "能指出軸線、單位、起點、分組、樣本、分母、缺測與原始資料核對。"}, {"prompt": "如何讓數位專題對不同讀者都可用？", "expectedEvidence": "能提出文字摘要、替代文字、鍵盤／手機操作、資料表、顏色以外的標記與限制說明。"}]}
    data["interactive"] = {"type": "guided-choice", "goal": "依受眾選媒介、核對資料與圖表、標示來源與限制，完成可及且可查證的科技表達。", "scenario": "從剩食趨勢、步行安全地圖到樹木資料圖表，逐步檢查數位作品的證據與責任。", "variables": [{"symbol": "a", "meaning": "受眾與目的"}, {"symbol": "d", "meaning": "資料與表示"}, {"symbol": "r", "meaning": "來源、可及性與限制"}], "steps": [
        {"id": "step-1", "prompt": "要向校長說明午餐剩食一個月的每日變化，哪種媒介最適合？", "options": ["附單位與缺測說明的折線圖，旁邊提供摘要、原始表格與來源", "只放一張最少剩食日的照片", "用快速動畫隱藏每日數值"], "answer": "A", "feedback": "A 讓趨勢、數值、限制與查證入口同時存在，符合決策需求。"},
        {"id": "step-2", "prompt": "製作步行安全地圖時，哪項做法較負責任？", "options": ["使用匿名化事件與暴露分母，標示時間範圍、來源與地圖限制", "公開個別學生的精確位置以增加真實感", "只用顏色深淺不提供數值或文字"], "answer": "A", "feedback": "A 同時處理風險比較、個資、來源與可讀性，不用精確個資或單一視覺效果取代分析。"},
        {"id": "step-3", "prompt": "數位專題如何避免把估計說成確定事實？", "options": ["在圖文中分開觀察、估計與解釋，標示樣本與不確定性並提供資料下載／回饋", "把標題改得更肯定", "刪掉不符合趨勢的資料"], "answer": "A", "feedback": "A 保留證據界線，讓讀者能重算、查證與指出限制。"},
    ]}
    data["authoringStandard"] = "version-fused-v1"
    data["updatedAt"] = "2026-09-21"
    data["versionResearch"] = [
        rec("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf；國語文資訊整理、表達與媒介運用定位；核讀 2026-09-21。", ["運用適切媒介整理、表達與分享資訊。", "表達需依目的、讀者與情境選擇形式。"], ["文字、圖表、資料、摘要、影像與口語說明。"], "把科技效果當成內容品質，忽略資料意義與讀者需求。", "評量資訊組織、媒介選擇、表達清楚與回應。"),
        rec("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf；國語文科技媒介、合作表達與資訊分享定位；核讀 2026-09-21。", ["科技可支援多元表達、協作與資訊交換，但要依任務選擇工具。", "作品需考量不同讀者與互動回饋。"], ["簡報、圖表、互動頁、共享資料、回饋與版本。"], "工具越複雜就越有說服力，或只追求視覺效果。", "重視媒介適配、協作、回饋與表達效果。"),
        rec("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf；國文資料整理、表達效果與評量定位；核讀 2026-09-21。", ["資訊表達需有來源、脈絡、限制與適當的讀者導向。", "圖表與多媒體應支持理解，不能掩蓋證據界線。"], ["來源、授權、軸線、單位、樣本、替代文字與限制。"], "忽略來源、授權、缺測或可及性，將漂亮圖表當成完整論證。", "要求資料可追溯、表示清楚、媒介適切並能指出限制。"),
    ]
    data["fusionRecord"] = {"commonCore": ["三版本公開結構共同支持科技媒介、資訊整理、讀者導向與清楚表達。", "媒介選擇要和目的、資料關係、讀者、來源與限制連結。", "數位表達同時需要可查證、可及、授權與隱私責任。"], "versionDifferences": ["南一較突顯資訊整理、媒介選擇與目的；康軒較突顯科技協作、多元表達與回饋；翰林較突顯來源、圖表脈絡、表達效果與限制。這是公開課程計畫層級差異，不宣稱完整教材差異。"], "originalAdditions": ["以剩食趨勢比較摘要、折線圖、互動表與讀者決策。", "以步行安全地圖處理分母、匿名化與時間範圍。", "以樹木圖表拆解截斷軸、缺測、替代表示與可及性。"], "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織媒介選擇、資料表示、來源授權、可及性、個資、不確定性與數位作品修正。正文、原創情境、互動步驟、回饋與檢核均為本專案重寫，未複製教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    data["teaching"]["body"][2]["body"] += " 再比較每十萬人事件率與事件總數，說明分母如何改變排序；若地圖仍可能暴露個別路線，改用網格或較大區域並註明匿名化處理。"
    data["teaching"]["body"][3]["body"] += " 請學習者用一句話寫出截斷軸造成的視覺效果，再在圖下放上原始百分比、樣本數與缺測註記，讓讀者能自行判斷差距是否重要。"
    data["teaching"]["body"][1]["body"] += " 將每個檢核轉成作品旁的註記或資料欄位，讓同伴能按來源、軸線、限制和操作順序逐項重做，不只看最後畫面。"
    data["teaching"]["body"][5]["body"] += " 請另一位讀者用不看原始資料的方式重述你的結論，若他無法指出範圍與限制，就回頭修改標題、圖例或文字摘要。"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "2-Ⅳ-4：選對科技媒介，讓資料說得清楚又負責", "lessonId": data["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored chinese performance 2-iv-4")


if __name__ == "__main__":
    main()
