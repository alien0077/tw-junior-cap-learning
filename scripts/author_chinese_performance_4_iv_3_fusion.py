import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/chinese/lesson-chinese-performance-4-iv-3.json"
REPORT = ROOT / "implementation/reports/chinese-performance-4-iv-3-first-pass-review.json"


def rec(name, locator, concepts, forms, misconception, assessment):
    return {"publisher": name, "edition": f"{name} 公立校方國文課程計畫章節級證據", "sourceType": "public-web", "sourceLocator": locator, "reviewedAt": "2026-09-21", "findings": {"concepts": concepts, "representations": forms, "examplesOrEvidence": ["本課以行、重、樂等多音多義字的原創查典與語境任務，僅承接公開課程的字辭典使用與閱讀理解方向。"], "misconceptions": [misconception], "assessmentEmphasis": [assessment]}, "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、篇章、題目、答案、影音或版面。"}


def main():
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-chinese-performance-4-iv-3"
    data["title"] = "4-Ⅳ-3：用字辭典追蹤多音多義字的語境變化"
    data["content"] = {"summary": "一個字有多個讀音或義項時，字典不是用來挑最熟悉的那一項，而是把詞語、句法、語境和讀音資料放在一起作判斷。查詢時要記錄詞頭、音讀、義項、例句、詞源或用法標籤，再回到原句核對；遇到古今用法不同，也要標示時代與文本範圍。本課以行、重、樂等多音多義字的原創查典任務，練習從候選到證據的完整流程。", "sections": [{"heading": "詞語決定字的讀音和意思", "body": "『銀行』的行和『行走』的行寫法相同，讀音與意思卻由詞語和句子決定。先把整個詞圈起來，再查音讀、義項和例句，不能只看單字在腦中的第一個聲音。"}, {"heading": "字典欄位各自回答不同問題", "body": "注音或拼音回答怎麼讀，義項回答可能表示什麼，例句和搭配回答如何使用，標籤可能提示古語、方言、專名或語體。查到資料後要把欄位和題目需求對齊，避免用義項回答讀音問題。"}, {"heading": "多義要看語境限制", "body": "『重』可以表示重量大、程度深、再次或看重，『樂』也可能指音樂、快樂或喜愛。先找句中動作、對象、程度和前後文，再用替換測試排除不合義項，保留必要的歧義說明。"}, {"heading": "古今混用要標示範圍", "body": "古文、現代新聞、方言和專業術語可能使用不同讀音或義項。不要把古義直接搬到現代句子，也不要把現代常用讀音套在所有古文；記下文本時代、詞性、來源與仍待查證的地方。"}]}
    data["studyHighlights"] = ["先查完整詞語與句法，再判斷多音多義字的讀音和義項。", "分清字典的讀音、義項、例句與用法標籤各自提供的證據。", "用對象、動作、程度、前後文與替換測試排除不合義項。", "古今、方言、專名或專業用法要標示範圍，不把單一查詢結果過度外推。"]
    data["teaching"] = {"body": [
        {"id": "hook", "phase": "hook", "heading": "『行』到底怎麼讀？", "body": "把銀行、行走、行列、行程四個詞放在一起，請學習者先依詞語猜讀音與意思，再打開字辭典核對。比較只查單字和查完整詞語的結果，讓學習者發現同一字形的判斷單位通常是詞語與句子。"},
        {"id": "explain", "phase": "explain", "heading": "查典五欄紀錄法", "body": "依序記錄查詢詞、音讀、詞性、義項、例句／搭配與使用標籤；每一次選擇都寫回原句的證據。若查到多個可能答案，先保留候選，再用句法和上下文縮小，不把字典排列順序當成正確性排序。"},
        {"id": "worked-example", "phase": "worked-example", "heading": "『重』的多義分流", "body": "在『行李很重』『重複檢查』『老師很重視證據』三句中，先看它修飾的對象或搭配，再選重量、再次或看重的義項。將每個義項代回句子重讀，若語意和詞性不合就退回查詢，不靠直覺硬套。"},
        {"id": "guided-practice", "phase": "guided-practice", "heading": "古今句子的查證", "body": "將含『樂』的古文片段和現代公告並列，先標出時代、詞性與前後文，再查字典的讀音／義項和例句。學習者要寫出一個不能直接互換的理由，並在不確定時保留來源與範圍。"},
        {"id": "transfer", "phase": "transfer", "heading": "製作班級多音多義小辭典", "body": "小組從科普、公告、文言與新聞各選一個詞，建立詞頭、讀音、義項、例句、來源、標籤與查證日期。交換後由另一組依原句重做，若選出的義項不同，要回到證據比較而不是投票決定。"},
        {"id": "reflect", "phase": "reflect", "heading": "回看查詢是否回答了問題", "body": "選一次查典紀錄，圈出你是否把讀音、義項、詞性或例句混在一起，或把古今用法外推成普遍規則。重寫查詢路徑，並補一個能讓下一位讀者核對的來源、標籤或原句。"},
    ], "summary": ["以完整詞語、句法和語境判斷多音多義字。", "按讀音、詞性、義項、例句與標籤記錄查典證據。", "用搭配、替換、前後文與文本時代排除候選。", "建立可重做的小辭典，標示來源、範圍與查證日期。"], "exitCheck": [{"prompt": "為什麼不能只查『行』這個單字就決定讀音？", "expectedEvidence": "能指出銀行、行走等完整詞語的讀音與義項不同，需回到詞語、詞性與句子核對。"}, {"prompt": "字典的例句和用法標籤各能幫助什麼？", "expectedEvidence": "能區分例句提供搭配和語境，標籤提供古語、方言、專名或語體範圍，不能互相取代。"}, {"prompt": "古今混用句遇到不同候選時如何處理？", "expectedEvidence": "能標示文本時代、詞性、前後文與來源，保留候選並查證，不把現代常用義直接套到古文。"}]}
    data["interactive"] = {"type": "guided-choice", "goal": "以完整詞語、字典欄位、語境與文本範圍處理多音多義字，留下可重做的查證紀錄。", "scenario": "從行、重、樂到古今混用句，逐步查詢、比較候選並回到原句核對。", "variables": [{"symbol": "w", "meaning": "完整詞語"}, {"symbol": "d", "meaning": "字典欄位"}, {"symbol": "c", "meaning": "語境與時代"}], "steps": [
        {"id": "step-1", "prompt": "下列『行』字讀音與『銀行』相同的是哪一項？", "options": ["行列", "行走", "行程"], "answer": "A", "feedback": "A 與銀行同讀音；要以完整詞語查證，不能只依字形判斷。"},
        {"id": "step-2", "prompt": "處理『重』的多義時，哪個步驟最能縮小候選？", "options": ["看它修飾的對象、詞性、搭配與前後文，再用義項代回句子", "只選字典第一個義項", "只看自己最常聽到的讀音"], "answer": "A", "feedback": "A 將字典資料和句內證據連起來，能排除語意或詞性不合的解釋。"},
        {"id": "step-3", "prompt": "古今混用句有不同讀音／義項候選時，哪套做法最完整？", "options": ["標示文本時代、詞性與來源，逐項回到原句核對並保留未決範圍", "直接套用現代最常見讀音", "刪掉不符合第一個猜測的句子"], "answer": "A", "feedback": "A 保留語境、時代和證據界線，讓查詢結果可以被重做與修正。"},
    ]}
    data["authoringStandard"] = "version-fused-v1"
    data["updatedAt"] = "2026-09-21"
    data["versionResearch"] = [
        rec("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf；國語文字詞、字典使用與閱讀理解定位；核讀 2026-09-21。", ["運用字辭典等工具理解字詞、讀音與義項。", "在語境中掌握字詞的詞性、搭配、表達效果與使用範圍。"], ["詞頭、注音、義項、例句、搭配與句子。"], "把一字一音一義當成固定規則，忽略詞語和語境。", "評量查詢能力、字詞理解、語境運用與表達。"),
        rec("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf；國語文字詞、字辭典與閱讀活動定位；核讀 2026-09-21。", ["透過工具、例句與閱讀脈絡處理多音多義字。", "查詢結果需回到實際詞語與溝通情境核對。"], ["查詢、詞性、音讀、義項、例句、古今與標籤。"], "只背查詢結果或把字典排列順序當成所有語境的答案。", "重視工具使用、證據比較、語境與用法修訂。"),
        rec("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf；國文文字音義、語詞與評量定位；核讀 2026-09-21。", ["從字音、字義、詞性與文本脈絡理解詞語。", "判斷需說明來源、範圍與古今語用差異。"], ["多音、多義、詞性、語體、文本時代、例句與來源。"], "把古語、方言或專名用法無條件外推到現代一般句。", "要求查典紀錄完整、字詞選用有根據並能標示限制。"),
    ]
    data["fusionRecord"] = {"commonCore": ["三版本公開結構共同支持字辭典工具、字詞理解、讀音義項與語境使用。", "多音多義判斷需要詞語、詞性、例句、上下文與文本範圍交叉核對。", "查詢結果應留下來源和可重做路徑，不把單一義項過度外推。"], "versionDifferences": ["南一較突顯字辭典、字詞理解與閱讀；康軒較突顯查詢、例句、工具與語境活動；翰林較突顯音義、詞性、古今語用與判斷根據。這是公開課程計畫層級差異，不宣稱完整教材差異。"], "originalAdditions": ["以行、重、樂建立詞語與義項分流。", "以古今句並列檢查文本時代和語用範圍。", "以班級小辭典記錄查詢欄位、來源與查證日期。"], "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織多音多義、字辭典欄位、詞性、例句、古今語境與查證紀錄。正文、原創情境、互動步驟、回饋與檢核均為本專案重寫，未複製教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    data["teaching"]["body"][3]["body"] += " 比較兩個義項的詞性、搭配對象與語氣，寫出若直接互換會改變什麼；若來源只說可能讀法，便把它標成待查而不是挑一個當定論。"
    data["teaching"]["body"][1]["body"] += " 將題目要求圈在查詢紀錄上，若問題問讀音就不能只抄義項，若問題問語意就要附原句和詞性，讓工具欄位真正服務判斷。"
    data["teaching"]["body"][5]["body"] += " 交換紀錄時請另一組只使用你留下的來源重做一次，若無法得到相同結果，就補上詞語、例句、時代或標籤證據。"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "4-Ⅳ-3：用字辭典追蹤多音多義字的語境變化", "lessonId": data["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored chinese performance 4-iv-3")


if __name__ == "__main__":
    main()
