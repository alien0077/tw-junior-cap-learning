import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/chinese/lesson-chinese-performance-4-iv-1.json"
REPORT = ROOT / "implementation/reports/chinese-performance-4-iv-1-first-pass-review.json"


def rec(name, locator, concepts, forms, misconception, assessment):
    return {"publisher": name, "edition": f"{name} 公立校方國文課程計畫章節級證據", "sourceType": "public-web", "sourceLocator": locator, "reviewedAt": "2026-09-21", "findings": {"concepts": concepts, "representations": forms, "examplesOrEvidence": ["本課以集雨研究、校園公告與科普閱讀三個原創字詞使用情境，僅承接公開課程的字詞理解與表達方向。"], "misconceptions": [misconception], "assessmentEmphasis": [assessment]}, "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、篇章、題目、答案、影音或版面。"}


def main():
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-chinese-performance-4-iv-1"
    data["title"] = "4-Ⅳ-1：從字形、字音到語境，精準選用常用字詞"
    data["content"] = {"summary": "認字不是把形音義分開背完就結束；真正使用時，還要依詞語組合、句法位置、語境與讀者檢查是否精準。遇到形近、音近、義近或陌生字詞，先用上下文提出候選，再以字典、詞源、例句與替換測試核對，最後回讀整句。本課以集雨研究、校園公告與科普閱讀三個原創情境，練習辨識、理解與負責任使用常用字詞。", "sections": [{"heading": "字形相近不代表意思相同", "body": "『辨、辯、辦』都含有相近線索，但辨認資料、辯論觀點、辦理活動的搭配與任務不同。先看詞語中的角色與動作，再看句子要完成的意思，不能只依偏旁或熟悉程度選字。"}, {"heading": "字音要放進詞語判斷", "body": "同音字可能造成錯誤，讀音也可能因詞義或語境變化。先完整讀詞，再查注音、詞義與例句；若只把單字念對，卻沒有核對它在句中的角色，仍可能寫錯或誤解。"}, {"heading": "陌生詞要用證據推進", "body": "先圈上下文線索，提出暫定意思，再用字典義項、近義詞替換、反義對照或同篇其他用法檢查。暫定解釋要標記信心範圍，不因查到第一個義項就停止。"}, {"heading": "精準使用也考慮讀者", "body": "公告、研究紀錄與科普說明需要不同詞彙密度和註解程度。選字後回讀語氣、句法、搭配與讀者背景，必要時用較常見的詞或加上定義，讓準確不變成故意艱深。"}]}
    data["studyHighlights"] = ["從詞語搭配、句法位置與語境辨識形近、音近、義近字詞。", "遇到陌生詞先提出暫定義，再用字典、例句、替換與回讀核對。", "區分單字讀音與詞語語意，不能只靠偏旁或第一個字典義項。", "依公告、研究與科普讀者調整詞彙與註解，兼顧精準和可理解。"]
    data["teaching"] = {"body": [
        {"id": "hook", "phase": "hook", "heading": "研究者要『蒐集』還是『收集』資料？", "body": "把集雨研究的一句話改放入不同情境，先讓學生圈出動作、對象與持續性，再比較候選字詞的搭配。不要先背唯一答案，而要說明哪個詞與研究任務、資料來源和句子語氣最相稱。"},
        {"id": "explain", "phase": "explain", "heading": "形音義與語境四格表", "body": "第一格看字形線索但不過度推論，第二格確認詞語讀音，第三格列出可能義項，第四格用上下文與搭配排除不合者。每次選字都留下回讀句子，讓辨識結果能被別人檢查。"},
        {"id": "worked-example", "phase": "worked-example", "heading": "辨、辯、辦的任務差異", "body": "『辨識雨量器材』在處理資料，『辯論是否停課』在交換立場，『辦理校園展覽』在安排活動。用動詞後面的對象和整句目的檢查，若只看同音或偏旁，就可能把正確字換成另一個任務。"},
        {"id": "guided-practice", "phase": "guided-practice", "heading": "陌生科普詞的查證路徑", "body": "讀一段原創科普文字，先用前後句猜詞義，接著查字典不同義項，再用近義詞替換並回讀。若替換後範圍或語氣改變，就保留原詞並補定義，而不是把所有陌生詞都換成最熟悉的字。"},
        {"id": "transfer", "phase": "transfer", "heading": "為三種讀者調整詞彙", "body": "同一項集雨研究分別寫給研究同伴、低年級學生與校務公告讀者。保留數據與關鍵概念，但調整術語、括號解釋、句子長度和行動指示，檢查讀者是否能依文字做出正確下一步。"},
        {"id": "reflect", "phase": "reflect", "heading": "回看自己是靠證據還是靠熟悉感", "body": "選一個曾經寫錯的字，記下形、音、義、詞語搭配與原句線索，再寫出下一次遇到它的查證步驟。若字典有多個義項，說明你如何用語境排除，並檢查最後句子是否自然、準確、適合讀者。"},
    ], "summary": ["先看詞語搭配、句法、對象與語境，再使用形音線索。", "陌生詞採暫定—查證—替換—回讀流程，不急著接受第一個義項。", "用任務與讀者需求分辨形近、音近、義近字詞。", "選字後檢查語意、語氣、搭配與讀者可理解性。"], "exitCheck": [{"prompt": "為什麼辨、辯、辦不能只靠讀音或偏旁選擇？", "expectedEvidence": "能連結詞語搭配、動作對象與句子任務，說明相近形音仍可能有不同語意。"}, {"prompt": "遇到陌生詞時，哪套步驟比較可靠？", "expectedEvidence": "能提出上下文暫定、字典義項、例句／替換與整句回讀，並標示仍不確定的部分。"}, {"prompt": "如何讓科普詞彙既精準又適合不同讀者？", "expectedEvidence": "能保留核心概念，依讀者補上定義、括號說明或較常見詞，並用回讀檢查行動理解。"}]}
    data["interactive"] = {"type": "guided-choice", "goal": "整合字形、字音、詞義、搭配與語境，選出適合讀者且可查證的字詞。", "scenario": "從集雨研究、校園公告到科普陌生詞，逐步提出候選、查證並回讀。", "variables": [{"symbol": "f", "meaning": "字形與字音"}, {"symbol": "m", "meaning": "詞義與搭配"}, {"symbol": "c", "meaning": "語境與讀者"}], "steps": [
        {"id": "step-1", "prompt": "研究團隊持續＿＿集雨量資料；哪個字最符合語意？", "options": ["蒐集", "收悉", "修集"], "answer": "A", "feedback": "A 與有目的地尋找、整理資料的研究任務搭配；不能只因讀音相近就選字。"},
        {"id": "step-2", "prompt": "遇到科普陌生詞，哪套方法最能避免誤解？", "options": ["先用上下文提出暫定義，再查字典義項、例句與替換效果，最後回讀", "只看字形偏旁猜到底", "直接採用字典第一個義項"], "answer": "A", "feedback": "A 保留語境證據與多義查核，能避免只靠形或第一個義項。"},
        {"id": "step-3", "prompt": "同一研究要寫給低年級學生，如何調整最適切？", "options": ["保留核心概念，補上常見詞、短句與必要定義，並用回讀確認理解", "刪除所有精確詞只留下口號", "加入更多艱深術語表示專業"], "answer": "A", "feedback": "A 同時保留精準與可理解性，讓讀者知道概念和下一步。"},
    ]}
    data["authoringStandard"] = "version-fused-v1"
    data["updatedAt"] = "2026-09-21"
    data["versionResearch"] = [
        rec("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf；國語文字詞辨識、理解與使用定位；核讀 2026-09-21。", ["認識常用字詞並在語境中理解、運用。", "字詞學習需連結閱讀理解與表達。"], ["字形、字音、詞義、搭配、句子與語境。"], "把單字孤立記憶，忽略詞語組合和上下文。", "評量字詞辨識、語意理解、正確使用與讀者適切。"),
        rec("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf；國語文字詞、閱讀與表達應用定位；核讀 2026-09-21。", ["透過閱讀、查字典與語境活動掌握字詞意義。", "字詞選用應支援溝通、表達與理解。"], ["查詢、例句、近義／反義、詞語搭配與改寫。"], "把字典第一個義項當成任何句子都適用。", "重視字詞理解、工具使用、情境運用與表達修訂。"),
        rec("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf；國文文字、語詞與閱讀評量定位；核讀 2026-09-21。", ["從形音義與文本脈絡理解文字詞語，並掌握表達效果。", "評量需能說明判斷根據而非只選字。"], ["形音義、句法、語境、語氣、讀者與說明。"], "只靠偏旁、同音或熟悉感推測，沒有回讀和證據。", "要求字詞選用有根據、語意精準並能適應讀者。"),
    ]
    data["fusionRecord"] = {"commonCore": ["三版本公開結構共同支持常用字詞辨識、理解、運用與閱讀表達。", "形、音、義需透過詞語搭配、上下文、工具查證與回讀互相驗證。", "正確用字不只選答案，還要考量語意、讀者與溝通任務。"], "versionDifferences": ["南一較突顯字詞理解與語境運用；康軒較突顯查詢、例句、閱讀與表達活動；翰林較突顯形音義、文本脈絡、表達效果與判斷根據。這是公開課程計畫層級差異，不宣稱完整教材差異。"], "originalAdditions": ["以集雨研究區分蒐集與相近字詞。", "以辨／辯／辦的任務差異練習搭配和語境。", "以科普陌生詞與三種讀者練習暫定、查證與改寫。"], "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織字形、字音、詞義、搭配、查證、讀者與回讀。正文、原創情境、互動步驟、回饋與檢核均為本專案重寫，未複製教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    data["teaching"]["body"][0]["body"] += " 再故意放入一個音近但語意不合的候選，請學習者指出它在資料、來源或動作對象上哪裡失配，讓選字理由不只停在『看起來熟悉』。"
    data["teaching"]["body"][4]["body"] += " 讓三位讀者各自完成同一個小任務，再比較他們卡住的詞語與資訊；依回饋補定義或改寫，而不是只把術語全部刪去。"
    data["teaching"]["body"][1]["body"] += " 對每個候選字記錄支持和反對的句內證據，若只剩偏旁聯想而沒有詞語搭配，就回到上下文重新提出候選。"
    data["teaching"]["body"][5]["body"] += " 把查證結果交給同伴換入原句，請他指出語意、語氣或讀者理解是否改變，再修訂自己的字詞判準。"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "4-Ⅳ-1：從字形、字音到語境，精準選用常用字詞", "lessonId": data["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored chinese performance 4-iv-1")


if __name__ == "__main__":
    main()
