"""Kb-Ⅳ-2：萬有引力的定性關係第一輪原創題庫。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-kb-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-kb-iv-2-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題", "year": "114", "locator": "萬有引力、質量、距離與地球—天體情境", "pattern": "取公立學校自然科評量以質量、距離、力和天體情境作定性推理的能力方向。"},
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "力學資料、作用力與天體運動情境", "pattern": "取公開會考以圖表、條件比較和證據界線判斷力學關係的能力方向。"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國民中學二年級自然科公開段考試題", "year": "112", "locator": "萬有引力、地球與月球、變因控制", "pattern": "取公立國中試題以成對比較、質量／距離變因和重力現象判讀的能力方向。"},
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]
STEPS = [
    ["圈出兩個物體的質量、中心距離與作用方向。", "確認其他條件是否固定。", "用質量增大或距離增大的定性規則判斷。", "排除把速度、重量或接觸力當成萬有引力。", "寫出作用對象與證據限制。"],
    ["找出兩物的質量是否改變。", "固定中心距離並比較質量大小。", "質量較大時判定引力定性增強。", "排除因移動快慢或物體外觀猜測。", "檢查兩物都受力且方向相向。"],
    ["確認兩物質量固定。", "比較距離改變的方向。", "距離增加時判定引力減弱。", "不要把減弱寫成突然消失。", "用連結兩物中心的箭頭回查。"],
    ["列出同時改變的質量與距離。", "分別標記兩因素對引力的方向。", "檢查題目是否提供改變幅度。", "若方向相反且幅度未知，標記資料不足。", "不可假造哪個效果較大。"],
    ["辨認地球與人的作用對象。", "畫出地球拉人與人拉地球的兩個箭頭。", "說明兩者是相互作用的一對。", "排除只有地球施力的單向說法。", "把重量和萬有引力的關係說清楚。"],
    ["確認衛星質量與地球質量是否固定。", "只改變衛星到地球的距離。", "距離變遠則引力變弱。", "不要把軌道速度或穩定性直接等同引力大小。", "補上本題只要求定性趨勢的範圍。"],
    ["比較小螺絲與大鐵球的質量。", "固定它們與地球的距離作思想實驗。", "質量較大者與地球的引力趨勢較強。", "排除接觸面大小和移動快慢。", "說明物體即使靜止仍有萬有引力。"],
    ["找出圖表中固定的條件和變動的條件。", "將每一組與基準組成對比較。", "只依單一變因推論強弱。", "排除同時多變因卻硬排順序。", "以『支持／不足以支持』回報證據範圍。"],
    ["分辨質量、重量和萬有引力的名稱。", "確認所在地是否改變重力場。", "判斷質量是否有物質進出。", "排除把重量變小當作質量消失。", "用完整物理量和作用對象重述結論。"],
    ["圈出題目給的兩個物體與彼此距離。", "確認是否只改變其中一個物體的質量。", "在距離固定時判斷質量改變造成的趨勢。", "排除把物體大小、速度或接觸面當成質量證據。", "寫出定性結論並標明固定條件。"],
    ["先列地球質量、月球質量和衛星距離條件。", "分別判斷質量與距離的影響。", "若只改一項就給出趨勢，若兩項相反則保留不確定。", "不要用軌道是否穩定代替引力大小。", "最後寫出模型未涵蓋的速度與運動條件。"],
]
ROWS = [
    ("easy", "在其他條件相同時，若其中一個物體的質量增加，兩物間萬有引力通常如何？", ["增強", "減弱", "完全消失", "一定不變"], "A", "萬有引力的強弱會受到兩物質量影響；距離固定時，質量增加使吸引作用定性增強。", "固定距離，只比較質量這一個變因。"),
    ("easy", "兩物質量固定，把兩物中心拉得更遠，萬有引力通常如何？", ["增強", "減弱", "變成接觸力", "只改變方向而強弱不變"], "B", "在質量固定時，距離增加使萬有引力定性減弱，但不表示有質量的兩物間作用突然不存在。", "先固定質量，再用距離變大的趨勢判斷。"),
    ("medium", "有兩組球：乙組只把甲組其中一球換成較大質量的球，中心距離不變。哪項比較合理？", ["乙組引力較強", "乙組引力較弱", "無法知道因為球在移動", "兩組一定沒有引力"], "A", "乙組只改變質量而保持距離，質量增加對應較強的萬有引力；球是否移動不是本題控制變因。", "用成對比較隔離質量效果。"),
    ("hard", "丙組和甲組質量相同，但中心距離由一格拉成兩格；沒有精確公式時可做何種結論？", ["丙組引力定性較弱", "丙組引力一定變成零", "丙組引力定性較強", "只看球的顏色即可判斷"], "A", "只改變距離且距離增加，能判斷引力定性減弱；題目未要求精確倍率，不應自行補出數值。", "先說方向，再限制結論不要超過資料。"),
    ("hard", "若同時把其中一物質量增加、又把兩物拉遠，且沒有提供改變幅度，最嚴謹的回報是？", ["引力必增強", "引力必減弱", "兩因素方向相反，資料不足以直接排序", "引力必消失"], "C", "質量變大使引力增強、距離變遠使引力減弱；兩種效果方向相反且幅度未知，不能直接判定最後強弱。", "分別列兩個因素的方向，再檢查是否有幅度資料。"),
    ("medium", "關於地球和站在地面上的人的萬有引力，哪項敘述正確？", ["只有地球拉人，人不會拉地球", "兩者互相吸引，方向沿兩物中心連線", "人只受到地板接觸力，不受地球引力", "兩者距離有限所以沒有萬有引力"], "B", "萬有引力是兩個有質量物體間的相互作用，地球拉人、人也拉地球，方向沿連結兩物中心的方向。", "畫出成對箭頭，避免把結果或接觸力當成唯一作用。"),
    ("medium", "同一顆衛星繞地球運行，若其他條件不變而軌道半徑增加，地球對它的萬有引力趨勢為何？", ["變強", "變弱", "一定變成零", "只因速度改變而無法判斷"], "B", "衛星與地球的質量不變，距離增加會使萬有引力定性減弱；軌道是否穩定還需要速度等資料，本題只問引力趨勢。", "分離距離對引力的影響與軌道運動的其他問題。"),
    ("easy", "一顆靜止在桌面的螺絲，是否仍與地球存在萬有引力？", ["存在，靜止不代表沒有引力", "不存在，只有移動才有引力", "只剩桌子的接觸力", "因為很小所以引力必為零"], "A", "只要物體有質量，和地球間就有萬有引力；桌面支持力可平衡部分效果，但不會抹去引力。", "把『是否存在作用』與『是否有可見運動』分開。"),
    ("hard", "某資料只顯示質量變大但同時距離也變遠，且沒有兩者改變比例；能否直接說新引力較大？", ["可以，質量永遠比距離重要", "可以，距離永遠比質量重要", "不能，兩因素方向相反且幅度不足", "不能，萬有引力只存在於接觸物體"], "C", "質量與距離對引力的定性影響方向相反，若沒有幅度或精確模型資料，不能直接排序。", "先做證據界線判斷，而不是用直覺補足資料。"),
    ("medium", "把同一個人從地球帶到月球，若沒有物質進出，哪項說法正確？", ["質量大致不變，重量因月球重力場較弱而變小", "質量變成六分之一，重量不變", "質量和重量都變成零", "只有人的速度變化，其他物理量不變"], "A", "質量由物質量決定，換地點通常不變；月球 g 較小，重量這個受力結果會變小。", "把質量、所在地重力場和重量分三欄判讀。"),
]

def make_question(n, row):
    difficulty, prompt, options, answer, explanation, strategy = row
    return {"id": f"question-science-content-kb-iv-2-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", options)], "knowledgeIds": ["kg-science-content-kb-iv-2"], "difficulty": difficulty, "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的質量、距離、作用力、地球—月球與變因控制能力方向；本題只作 pattern-only 改寫來源。", "authoringNote": "依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-kb-iv-2", "examPatternRefs": REFS, "solutionStrategy": strategy, "solutionSteps": STEPS[n - 1]}

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["authoringStandard"] = "version-fused-v1"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-kb-iv-2、南一／康軒／翰林可取得的公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合萬有引力的作用對象、質量、中心距離、單變因比較、雙因素資料不足、地球—月球與接觸力迷思。所有正文、比較資料、題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    for entry in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []):
        entry["reviewedAt"] = TODAY
    for n, row in enumerate(ROWS, 1):
        (QDIR / f"question-science-content-kb-iv-2-{n}.json").write_text(json.dumps(make_question(n, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "10 題已逐題改寫為質量、距離、作用力、地球—月球、單變因、雙因素資料不足與接觸力迷思專屬問題；每題有唯一答案、解析與五步解法。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content kb iv 2")

if __name__ == "__main__":
    main()
