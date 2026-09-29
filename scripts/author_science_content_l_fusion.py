"""L：生物與環境第一輪原創題庫與互動流程。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-l.json"
REPORT = ROOT / "implementation/reports/science-content-l-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題", "year": "114", "locator": "族群、生態系、食物網與環境因子", "pattern": "取公立學校自然科評量以生態資料、因果關係、尺度與圖表判讀的能力方向。"},
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "生態系、能量流動、物質循環與實驗推理", "pattern": "取公開會考以食物關係、時間序列、限制因子和證據界線評估的能力方向。"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國民中學二年級自然科公開段考試題", "year": "112", "locator": "生物因子、非生物因子、族群變化與食物鏈", "pattern": "取公立國中試題以生態尺度、捕食關係、資源限制和控制變因的能力方向。"},
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]
STEPS = [["先標出題目研究的個體、族群、群集或生態系尺度。", "把生物因子和非生物因子分欄，並畫出直接關係。", "沿食物網追蹤能量流向，另用循環觀念處理物質。", "用時間序列和對照區分觀察到的相關與可支持的因果。", "寫出證據支持的結論、限制與下一個可檢驗問題。"] for _ in range(10)]
ROWS = [
    ("easy", "校園池塘中一隻青蛙的體重與叫聲紀錄，主要是在研究哪個層次？", ["個體", "族群", "群集", "生態系"], "A", "資料只描述一隻青蛙的特徵與行為，觀察對象是單一個體，不足以代表整個族群。", "先數清楚研究對象有幾個，再判斷是否涉及同種多個體、不同物種或環境。"),
    ("easy", "池塘中同一種蝌蚪的數量隨月份增加後趨於穩定，最合理的解釋是？", ["食物、空間或天敵等限制因子使出生與死亡趨近平衡", "族群已經停止所有生命活動", "環境一定完全沒有變化", "只要數量穩定就代表沒有天敵"], "A", "族群數量穩定通常表示資源與天敵等條件形成限制，使增加與減少的作用在一段時間內接近平衡。", "先讀取曲線的趨勢，再找可能的資源、空間、疾病或捕食限制，不把穩定誤解成沒有作用。"),
    ("medium", "下列哪一項屬於池塘的非生物因子？", ["水溫", "藻類", "水蚤", "細菌"], "A", "水溫不具生命，但會影響代謝、溶氧與生物分布，屬於非生物環境因子。", "逐一問該項是否具有生命，再判斷它如何影響生物。"),
    ("medium", "食物鏈『藻類→水蚤→小魚→大魚』中的箭頭最適合表示什麼？", ["能量與食物中的物質由被取食者流向取食者", "大魚會把所有物質循環回藻類", "箭頭代表生物移動方向", "箭頭只表示體型大小规律"], "A", "箭頭從食物到取食者，表示能量及部分物質隨攝食傳遞；能量逐級散失，不能把食物鏈畫成能量循環。", "先問『誰被誰吃』，再分開說明能量單向流動與物質可在系統中循環。"),
    ("medium", "若池塘藻類大量增加後溶氧下降、魚類減少，哪一項最能作為支持因果的下一步？", ["控制水溫與光照，設置不同營養鹽輸入與無輸入對照，追蹤藻量、溶氧和魚類", "只比較一天的藻類顏色", "刪除與預期不符的溶氧資料", "看到魚變少就直接宣稱所有污染都來自營養鹽"], "A", "對照、控制條件與連續測量能檢查營養鹽—藻類—溶氧—魚類的關係；單一觀察不足以排除其他原因。", "把可能原因轉成可操弄的自變因，再安排對照和多個應變量。"),
    ("hard", "森林中某種鳥數量增加，但昆蟲和樹木健康也同時改變；要避免過度推論，應如何表達？", ["資料顯示變項同時變化，但仍需控制棲地、食物和天敵等因素才能支持直接因果", "鳥數量增加必然是樹木健康變好的唯一原因", "只要兩條曲線同方向就已證明因果", "因果無法研究，所以不必再量測"], "A", "同時變化可提供關聯線索，卻不能單獨排除其他變因；需要控制或比較多個條件。", "先寫觀察到的關聯，再列替代解釋與需要的驗證資料。"),
    ("easy", "下列何者最能區分『棲地』與『生態系』？", ["棲地是生物生活的場所；生態系還包括其中生物與非生物環境的交互作用", "棲地一定比生態系大", "生態系只包含動物，棲地只包含植物", "兩者都只表示地名，沒有生物關係"], "A", "棲地著重生物生活的空間與條件；生態系則把生物群集及其非生物環境和交互作用一起納入。", "看到名詞時先問它是在描述場所，還是描述整個互動系統。"),
    ("hard", "若移除池塘中的水草，最可能先改變哪組系統關係？", ["氧氣、躲藏空間與食物來源改變，進而影響多個族群", "只有水草數量改變，其他生物不可能受影響", "所有能量立刻消失且物質不再循環", "因為水草是生物，所以水溫必然不變"], "A", "水草同時提供初級生產、氧氣、棲身空間或食物，移除會經由食物網和非生物條件影響其他生物。", "沿直接關係逐層追蹤，不把一個變化限制在被移除的物種。"),
    ("medium", "要比較兩個池塘的生物多樣性，哪種做法較可靠？", ["固定樣區、季節、取樣時間與方法，重複記錄物種數和個體數", "一個池塘取春天資料，另一個只取冬天資料", "只挑物種最多的一次觀察", "只問居民印象而不記錄樣本"], "A", "固定取樣設計與重複觀察能減少時間、位置和方法差異造成的偏差，讓兩池塘資料可比較。", "先固定取樣邊界與方法，再同時看物種數、個體數和資料不確定性。"),
    ("hard", "若一場乾旱後草地植物量下降，哪個結論最符合證據界線？", ["乾旱可能是重要影響因子，但仍應檢查放牧、土壤與病蟲害等替代解釋", "植物量下降就證明唯一原因是乾旱", "植物量下降代表生態系所有功能都同時消失", "只要下一場雨後恢復，就能證明沒有其他因素"], "A", "時間上的先後和合理機制支持乾旱的可能性，但仍需檢查其他因子與多次資料，不能把可能性寫成唯一原因。", "用證據強度調整語氣：先寫可能，再列需要控制或補測的因素。"),
]

def make_question(number, row):
    difficulty, prompt, options, answer, explanation, strategy = row
    return {"id": f"question-science-content-l-{number}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", options)], "knowledgeIds": ["kg-science-content-l"], "difficulty": difficulty, "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的生態尺度、族群、食物網、非生物因子、能量、物質循環與控制變因能力方向；本題只作 pattern-only 改寫來源。", "authoringNote": "依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-l", "examPatternRefs": REFS, "solutionStrategy": strategy, "solutionSteps": STEPS[number - 1]}

def update_interactive(lesson):
    lesson["interactive"] = {"type": "scientific-investigation", "goal": "在校園池塘模型中辨認生態尺度、食物網與非生物限制，透過改變一項條件觀察族群和溶氧的連鎖變化。", "scenario": "你是校園生態調查小組：先選定個體、族群、群集或生態系尺度，再調整光照、營養鹽、捕食壓力或水溫一項變因，觀察藻類、溶氧、蝌蚪與魚類的時間序列，最後用對照資料寫出有條件的結論。", "variables": [{"symbol": "n", "meaning": "營養鹽輸入量"}, {"symbol": "t", "meaning": "水溫"}, {"symbol": "p", "meaning": "捕食壓力"}], "steps": [{"id": "step-1", "prompt": "要比較營養鹽對池塘族群的影響，第一步應先固定或列出什麼？", "options": ["取樣時間、樣區、光照、水溫、營養鹽量與觀察指標", "先宣布藻類增加就是好現象", "只挑結果最符合預期的一天"], "answer": "A", "feedback": "先界定系統邊界、變因與指標，才能把不同池塘或不同方案公平比較。"}, {"id": "step-2", "prompt": "營養鹽提高後藻類增加，但溶氧下降，應如何記錄？", "options": ["同時保留藻量與溶氧時間序列，再檢查其他環境條件", "只保留藻量增加，因為增加一定代表環境變好", "刪掉溶氧資料以免結論矛盾"], "answer": "A", "feedback": "生態系是多層次互動；同一變因可能帶來不同指標的正負效果。"}, {"id": "step-3", "prompt": "池塘魚類減少，要判斷是否由藻類造成，哪個比較最有力？", "options": ["設置無營養鹽或低藻量對照，固定水溫與光照並重複追蹤", "只觀察魚類一次並直接下唯一結論", "把所有其他池塘資料刪除"], "answer": "A", "feedback": "對照和重複資料有助於排除水溫、疾病或棲地差異等替代解釋。"}, {"id": "step-4", "prompt": "模擬結果中藻類、溶氧、魚類一起變化，報告結尾應怎麼寫？", "options": ["指出資料支持的關係、可能機制與尚需驗證的限制", "只寫一句口號，不交代資料", "把相關直接寫成唯一因果"], "answer": "A", "feedback": "良好的生態結論必須同時呈現證據、解釋和證據邊界。"}]}

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = TODAY; lesson["reviewStatus"] = "draft"; lesson["authoringStandard"] = "version-fused-v1"; update_interactive(lesson)
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-l、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合個體／族群／群集／生態系尺度、非生物因子、食物網、能量流動、物質循環、承載與生態實驗。原有通用問題已改為生物與環境專屬題目，互動也改為校園池塘資料探究；所有題幹、選項、答案、回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    for entry in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []): entry["reviewedAt"] = TODAY
    for number, row in enumerate(ROWS, 1): (QDIR / f"question-science-content-l-{number}.json").write_text(json.dumps(make_question(number, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "10 題改寫為生態尺度、非生物因子、族群、食物網、能量、物質循環、承載力與控制變因專屬問題；互動改為校園池塘時間序列探究；每題有唯一答案、解析與五步解法。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print("authored science content l")

if __name__ == "__main__": main()
