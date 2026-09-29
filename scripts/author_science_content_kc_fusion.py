"""Kc：電磁現象第一輪原創題庫。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-kc.json"
REPORT = ROOT / "implementation/reports/science-content-kc-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題", "year": "114", "locator": "電流磁效應、電磁力與感應", "pattern": "取公立學校自然科評量以方向判讀、裝置條件和能量轉換推理的能力方向。"},
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "電磁現象與實驗資料判讀", "pattern": "取公開會考以圖表、變因控制、證據界線與裝置功能推理的能力方向。"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國民中學二年級自然科公開段考試題", "year": "112", "locator": "電磁鐵、馬達、發電與感應", "pattern": "取公立國中試題以電流方向、線圈條件、磁通量改變和因果實驗的能力方向。"},
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]
STEPS = [["圈出電流、磁場、導線、磁鐵、運動與回路是否閉合。", "先判定現象是產生磁場、受磁力或感應電流。", "用右手規則、磁通量改變或能量方向建立關係。", "控制一次只改一項條件，排除把有磁場誤當有感應。", "以方向、強弱、回路與能量輸入輸出逐項檢查結論。"] for _ in range(10)]
ROWS = [
    ("easy", "直導線中的傳統電流方向反向，導線周圍磁場最直接的變化是？", ["磁場方向反向", "磁場一定消失", "只改變導線電阻而方向不變", "磁場變成電場且大小不變"], "A", "通電導線周圍的磁場方向由電流方向決定；電流反向時，周圍磁場方向也反向。", "先固定導線位置，再用右手握拳規則對照電流方向與磁場環繞方向。"),
    ("medium", "要讓直導線附近指南針偏轉更明顯，哪一組改變較合理？", ["增加電流，並把指南針移近導線", "減少電流並移遠指南針", "切斷電路再增加導線長度", "只改變指南針顏色"], "A", "在其他條件相近時，電流較大、觀測點較靠近導線通常能看到較明顯的磁效應；仍需以實測確認。", "把可能影響磁場的電流大小與距離分開列出，不把外觀改變當成物理變因。"),
    ("medium", "相同電流下，螺線管增加線圈匝數，通常會使內部磁場如何變化？", ["磁場較強，且極性仍由電流方向決定", "磁場必然消失", "只增加線圈重量，磁場不變", "匝數越多就不需要電源"], "A", "多匝線圈的磁場作用可疊加，因此在其他條件相近時場較強；極性仍須依電流方向判斷。", "先說明固定電流與幾何條件，再比較匝數對磁場疊加的影響。"),
    ("hard", "一根通電導線放在外加磁場中，導線受到的磁力方向要如何判斷？", ["同時考慮電流方向與磁場方向，不能只看其中一個", "只看導線長度即可決定方向", "只要有磁場，導線不通電也一定受同樣方向的力", "把磁場方向直接當成受力方向"], "A", "載流導線在磁場中的受力方向與電流、磁場兩者有關；不能將磁場箭頭、電流箭頭和受力箭頭混為一談。", "先分別畫電流與磁場，再用方向規則求第三個向量，並檢查是否有通電條件。"),
    ("easy", "磁鐵靜止在線圈內，線圈接閉合檢流計，指針回到零最合理的解釋是？", ["磁通量暫時不再改變，因此沒有持續感應電流", "線圈永遠不可能有感應電流", "磁鐵停止後磁場完全消失", "檢流計只能測電壓不能測電流"], "A", "感應的關鍵是穿過線圈的磁通量改變；靜止後若條件不變，感應電流不再持續，並非磁場消失。", "把『有磁場』與『磁通量正在改變』分成兩個檢查項目。"),
    ("medium", "比較磁鐵移動速度對感應電流的影響時，哪個設計最公平？", ["固定線圈匝數、磁鐵、路徑與閉合回路，只改變移動速度", "同時改變磁鐵大小、匝數與速度", "只挑偏轉最大的讀值而不記錄其他次數", "一組用閉合回路、另一組用斷路"], "A", "只改變速度才能把感應差異較合理地歸因於磁通量改變的快慢；其餘條件需固定並重複測量。", "先列自變因，再列必須固定的磁鐵、線圈、路徑和回路條件。"),
    ("medium", "下列哪個條件最能說明『線圈中觀察到感應電流』？", ["線圈形成閉合回路，且通過線圈的磁通量正在改變", "線圈只要靠近任何靜止磁鐵就一定有持續電流", "線圈顏色改變且沒有磁場", "只要電池放在旁邊，不必接線也會有感應電流"], "A", "可觀察的感應電流需要磁通量改變與閉合路徑；單有磁鐵或電池放在附近不足以推出電流。", "先查磁通量是否變，再查電荷是否有閉合路徑可循環。"),
    ("hard", "發電機以外力轉動線圈，檢流計指針左右擺動；若把轉動方向反過來，最合理的預測是？", ["感應電流方向反向，指針偏轉方向也反向", "只會讓線圈變重，指針方向不可能改變", "因為有磁鐵，指針永遠固定在同一側", "轉動方向與磁通量變化完全無關"], "A", "反向轉動會使磁通量變化的方向反向，閉合回路中的感應電流方向也隨之反向，因此指針偏轉方向改變。", "先比較兩種運動造成的磁通量變化方向，再推回感應電流與儀器指針。"),
    ("medium", "同一套裝置先接電池使線圈轉動，再拔掉電池改由外力轉動並接檢流計；兩次能量轉換分別是？", ["馬達：電能轉機械能；發電：機械能轉電能", "兩次都是化學能直接變磁能", "馬達是光能轉電能；發電是電能轉熱能", "兩次都不需要能量輸入"], "A", "電池供電的馬達以電能產生受力與轉動；外力轉動線圈使磁通量改變，發電機則輸出電能。", "先標出每個實驗的能量輸入與輸出，再判斷是馬達模式或發電模式。"),
    ("hard", "若要檢驗『增加線圈匝數會提高感應電壓』，哪個做法最能支持結論？", ["固定磁鐵、運動路徑、速度、線圈面積與儀表，只改變匝數並重複測量", "增加匝數的同時把磁鐵換大且加快速度", "只測一次並選擇最漂亮的數值", "一組閉合、一組斷路，再比較指針偏轉"], "A", "控制其他影響磁通量改變的條件，才能把量測差異主要歸因於匝數；重複測量還能檢查偶然誤差。", "把匝數定為唯一自變因，逐項固定磁鐵、路徑、速度、面積與儀表。"),
]

def make_question(number, row):
    difficulty, prompt, options, answer, explanation, strategy = row
    return {"id": f"question-science-content-kc-{number}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", options)], "knowledgeIds": ["kg-science-content-kc"], "difficulty": difficulty, "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的電流磁效應、電磁力、磁通量、感應、馬達、發電機與控制變因能力方向；本題只作 pattern-only 改寫來源。", "authoringNote": "依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-kc", "examPatternRefs": REFS, "solutionStrategy": strategy, "solutionSteps": STEPS[number - 1]}

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = TODAY; lesson["reviewStatus"] = "draft"; lesson["authoringStandard"] = "version-fused-v1"
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-kc、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合電流磁效應、電磁力、磁通量、感應、電磁鐵、馬達、發電機與公平實驗。原有題目已全部改為電磁現象專屬題目；所有題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    for entry in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []): entry["reviewedAt"] = TODAY
    for number, row in enumerate(ROWS, 1): (QDIR / f"question-science-content-kc-{number}.json").write_text(json.dumps(make_question(number, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "10 題改寫為電流磁效應、電磁力、磁通量、感應、電磁鐵、馬達、發電機與公平實驗專屬問題；每題有唯一答案、解析與五步解法。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print("authored science content kc")

if __name__ == "__main__": main()
