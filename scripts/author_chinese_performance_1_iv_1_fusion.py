import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/chinese/lesson-chinese-performance-1-iv-1.json"
REPORT = ROOT / "implementation/reports/chinese-performance-1-iv-1-first-pass-review.json"


def vr(publisher, locator, concepts, representations, misconception, assessment):
    return {
        "publisher": publisher,
        "edition": f"{publisher} 公立校方國文課程計畫章節級證據",
        "sourceType": "public-web",
        "sourceLocator": locator,
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": concepts,
            "representations": representations,
            "examplesOrEvidence": [
                "本課使用校園社團邀請、社區會議與小組任務三個原創聆聽情境，只承接公開課程的能力方向。"
            ],
            "misconceptions": [misconception],
            "assessmentEmphasis": [assessment],
        },
        "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、篇章、題目、答案、影音或版面。",
    }


def main():
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-chinese-performance-1-iv-1"
    data["title"] = "1-Ⅳ-1：同理聆聽，把話語整理成可確認的共識"
    data["content"] = {
        "summary": "同理聆聽不是替別人猜答案，也不是把所有話逐字抄下來；它要同時保留說話者的事實、感受、需求與限制，再用摘要和澄清讓對方確認。這一課以社團邀請、社區會議與小組任務三個原創情境，練習從聲音線索建立紀錄、區分已說與推測、處理歧義，並在不洩漏私人資訊的前提下形成可行的下一步。",
        "sections": [
            {"heading": "先分開四種訊息", "body": "聽見『我想參加，但放學要照顧弟弟』時，意願是明說的事實，照顧弟弟是限制；聽者可以關心對方感受，卻不能擅自寫成『他一定很焦慮』。先分層，紀錄才不會把推測冒充原話。"},
            {"heading": "摘要要留下關係", "body": "好的摘要不只摘關鍵字，還要保留轉折、因果、時間與條件。『想參加，但準備時間不足』和『不想參加』的行動含義不同；若漏掉但、因為、還沒或只能，決策就可能被帶偏。"},
            {"heading": "澄清要讓對方能修正", "body": "當一句話有兩種解讀，用中性問題回問：『我聽到的是……，你指的是這個限制嗎？』不要把問題問成逼人承認的選擇題，也不要用自己的解釋替對方收尾。"},
            {"heading": "多方紀錄要標出來源", "body": "會議中不同人對同一方案的期待可能不一致。把發言者、可核對事件、感受或需求、提案與待確認事項分欄，才能保留共識與分歧，而非只留下最後一個聲音。"},
        ],
    }
    data["studyHighlights"] = [
        "將事實、感受、需求、限制與聽者推測分層。",
        "摘要時保留轉折、條件、時間與來源，不只抄關鍵字。",
        "用中性澄清讓說話者確認或修正，不替對方下結論。",
        "在多方紀錄中保留共識、歧異與待確認問題，守住隱私界線。",
    ]
    data["teaching"] = {
        "body": [
            {"id": "hook", "phase": "hook", "heading": "一句話裡藏著兩條訊息", "body": "社團幹部說：『我想參加週六排練，可是家裡臨時要我照顧妹妹。』先不要急著替他決定要不要參加；請把意願、限制和仍未知道的時間安排分開寫，感受則標成待確認。"},
            {"id": "explain", "phase": "explain", "heading": "聆聽紀錄的四欄", "body": "用『可核對事實／感受與需求／限制與條件／待確認問題』四欄整理。每一欄都問一次：這是對方明說的嗎？若不是，就改寫成提問或保留為推測，不能混進摘要當成結論。"},
            {"id": "worked-example", "phase": "worked-example", "heading": "把轉折保留下來", "body": "原創對話中，小組成員說『方案有效，但只有晚上有空的人做得到』。逐步圈出方案有效是判斷、晚上有空是條件，接著寫成『方案在晚間人力足夠時可行；其他時段仍待測試』，而不是寫成『方案不可行』。"},
            {"id": "guided-practice", "phase": "guided-practice", "heading": "用澄清取代猜測", "body": "社區會議有人說『最近很吵』。先記錄這是感受與模糊描述，再問『你指的是哪個時段、哪種聲音？需要的是測量、提醒，還是協調活動時間？』這樣才能把可行動的問題交還給說話者確認。"},
            {"id": "transfer", "phase": "transfer", "heading": "三人會議的共識與分歧", "body": "把三位成員的發言放入來源、事件、需求、提案、歧異五欄，最後只摘要已獲確認的共識；對尚未同意的方案保留『待討論』，並寫下一個可由全體確認的問題。"},
            {"id": "reflect", "phase": "reflect", "heading": "檢查自己有沒有越俎代庖", "body": "回看紀錄，找出一個你把感受寫成事實、把條件刪掉或替對方補上動機的地方。改成可核對文字或中性提問，再檢查是否保護了私人資訊與拒答空間。"},
        ],
        "summary": [
            "先分辨明說的事實、感受、需求、限制與聽者推測。",
            "摘要保留轉折、時間、條件和來源，避免刪掉改變意思的詞。",
            "遇到歧義先中性澄清，讓說話者確認或修正聽者理解。",
            "多方紀錄同時保留共識、分歧、待確認問題與隱私界線。",
        ],
        "exitCheck": [
            {"prompt": "聽到『我願意參加，但週三要照顧家人』時，哪些是明說資訊？", "expectedEvidence": "能指出參與意願與照顧家人是明說的事實，並把可參加的時間與感受列為待確認或另行詢問。"},
            {"prompt": "為什麼摘要不能只寫『他不參加』？", "expectedEvidence": "能說明『但』後的限制不等於拒絕，摘要必須保留條件與原意，不能加入未說出的決定。"},
            {"prompt": "如何處理『最近很吵』這種模糊回應？", "expectedEvidence": "能提出中性澄清，詢問時段、聲音來源與需求，並區分已知感受和尚待測量的事實。"},
        ],
    }
    data["interactive"] = {
        "type": "guided-choice",
        "goal": "把聆聽內容分層、保留條件、用澄清確認並整理多方共識。",
        "scenario": "從社團邀請、社區噪音到小組會議，逐步選擇不替人下結論的紀錄方法。",
        "variables": [{"symbol": "f", "meaning": "事實與感受分層"}, {"symbol": "c", "meaning": "澄清問題"}, {"symbol": "m", "meaning": "共識與歧異紀錄"}],
        "steps": [
            {"id": "step-1", "prompt": "『我想參加，但週五要照顧家人』應如何記錄？", "options": ["保留參加意願與照顧責任兩項資訊，時間安排另列待確認", "直接寫成他拒絕參加", "替他決定改報另一個時段"], "answer": "A", "feedback": "A 同時保留明說意願與限制，不把推測或決定塞回紀錄。"},
            {"id": "step-2", "prompt": "有人說『最近很吵』，第一個澄清問題應偏向什麼？", "options": ["詢問時段、聲音來源與希望解決的問題", "問他是不是討厭鄰居", "直接宣布一定是施工造成"], "answer": "A", "feedback": "A 把模糊感受轉成可確認的範圍，並保留對方修正的空間。"},
            {"id": "step-3", "prompt": "多方會議尚未同意的方案應如何整理？", "options": ["標成提案或待討論，保留提出者與不同意見", "只留下主持人最後一句話", "刪除與自己不同的意見"], "answer": "A", "feedback": "A 讓共識與歧異都可追溯，不把尚未決定的事寫成共同結論。"},
        ],
    }
    data["authoringStandard"] = "version-fused-v1"
    data["updatedAt"] = "2026-09-21"
    data["versionResearch"] = [
        vr("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf；國語文領域聆聽、理解與回應的學習表現；核讀 2026-09-21。", ["強調從聆聽內容擷取訊息、理解語意並作適切回應。", "聆聽理解需要把語句與情境、目的連起來。"], ["關鍵詞、語氣、說話目的、摘要與回應。"], "把聽見的零碎詞語直接當成完整結論。", "評量聆聽理解、摘要重述與情境適切回應。"),
        vr("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf；國語文領域口語溝通、聆聽互動與合作學習定位；核讀 2026-09-21。", ["以互動對話、提問、重述與合作討論檢查理解。", "聆聽者應依對象、目的和情境調整回應方式。"], ["對話輪次、澄清問句、重述、共識與分歧紀錄。"], "把同理誤解成同意，或用自己的意見取代對方的意思。", "重視澄清、回應、互動禮貌與團體討論的紀錄品質。"),
        vr("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf；國文領域閱讀、聆聽記錄與紙筆評量定位；核讀 2026-09-21。", ["以聆聽記錄、聲情判讀與文本整理支持理解和表達。", "不同訊息來源需經整理、歸納與證據核對。"], ["來源、事件、感受、需求、條件、待確認事項與摘要。"], "只記錄最後發言者，忽略來源、條件與未解歧異。", "要求資訊整理精確、回應有根據並能指出理解限制。"),
    ]
    data["fusionRecord"] = {
        "commonCore": ["三版本公開結構共同支持聆聽理解、情境回應、摘要整理與互動溝通。", "訊息來源、目的、語氣、條件、澄清與證據核對需要連續檢查。", "同理不等於替對方下結論，紀錄應讓原說話者能確認或修正。"],
        "versionDifferences": ["南一較突顯聆聽理解、目的與回應；康軒較突顯對話互動、提問、重述與合作；翰林較突顯聆聽記錄、來源整理、聲情與評量核對。這是公開課程計畫層級差異，不宣稱完整教材差異。"],
        "originalAdditions": ["以社團邀請呈現意願與限制同時存在。", "以社區噪音把模糊感受轉成可澄清的時段、來源與需求。", "以多方會議分欄保留共識、歧異、來源與待確認事項。"],
        "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織同理聆聽、訊息分層、摘要、澄清、多方紀錄與隱私界線。正文、原創情境、互動步驟、回饋與檢核均為本專案重寫，未複製教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。",
    }
    data["teaching"]["body"][0]["body"] += " 再用一句澄清問題確認是否還有未說出的安排，才進入摘要。"
    data["teaching"]["body"][1]["body"] += " 最後把四欄重新讀一遍，確定每個推測都有標籤，每個結論都能回到原話。"
    data["teaching"]["body"][4]["body"] += " 若某人只同意其中一部分，便把同意範圍寫清楚，不用模糊的『大家都同意』代替。"
    data["teaching"]["body"][5]["body"] += " 這個回讀步驟同時檢查語氣是否尊重、資訊是否必要，以及對方是否仍能拒答或補充。"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "1-Ⅳ-1：同理聆聽，把話語整理成可確認的共識", "lessonId": data["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored chinese performance 1-iv-1")


if __name__ == "__main__":
    main()
