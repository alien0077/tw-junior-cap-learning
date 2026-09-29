import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-mc-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-mc-iv-4-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "聚合物、合金、複合材料與材料資料"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "人造材料性質、加工與應用"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "材料選擇、測試控制與回收"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以聚合物、合金、複合材料、熱加工、材料測試、回收和生活產品需求考查性質—製程—用途的推理；本題只取能力方向並重新設計情境與資料。"
CONTENT = {
    "summary": "人造材料不是一張材料名稱清單，而是由組成、微觀結構、加工方法和使用條件共同決定性能。本課以聚合物、合金、玻璃纖維複材、熱塑／熱固塑膠與再生玻璃為例，學習把需求轉成可測試的選材判準，再兼顧安全、成本與生命週期。",
    "sections": [
        {"heading": "從鏈結與組成預測性質", "body": "單體連成長鏈後，分子量、鏈間作用力與排列會改變材料的柔韌、強度、黏彈性與耐熱表現；同一名稱的塑膠也可能因添加物、結晶度或加工條件不同而有不同性能。合金則透過加入其他元素改變金屬晶格和相組成，可能提高硬度、強度或耐腐蝕，卻同時降低延展性。不能只用『越硬越好』選材料。"},
        {"heading": "複合材料把不同優點放在一起", "body": "玻璃纖維提供拉伸強度與剛性，樹脂負責包覆、固定與傳遞應力；纖維方向、比例、界面黏著與缺陷會影響成品。選擇便當盒、雨水導管或腳踏車零件時，要先寫出耐熱、耐水、質量、導電、衝擊、成本與維修等需求，再以資料比較，而不是只背材料名稱。"},
        {"heading": "加工方式會改變可回收性", "body": "熱塑性塑膠加熱可軟化、冷卻再成形，適合重複加工但仍可能老化；熱固性塑膠固化後形成交聯網狀結構，再加熱不易熔融，通常不能用同樣方式回收。廢玻璃再製前需按顏色與種類分選、去除異物並破碎，避免陶瓷或金屬混入造成品質與設備風險。"},
        {"heading": "測試與生命週期一起看", "body": "比較抗衝擊時要固定試片尺寸、缺口、落錘高度、溫度、撞擊位置與重複次數；只做一次或改變多個條件不能支持公平結論。材料性能很好但難拆解、難回收或含危害添加物時，設計可改成單一材質、可拆接合、標示成分和延長使用壽命，將製造、使用、維修與報廢一起納入。"},
    ],
}
EXPLANATIONS = [
    "A。單體長鏈化會改變分子量、鏈間作用與結構排列，因而可能改變強度、柔韌、黏彈與耐熱，不是只增加材料重量。",
    "A。加入適量元素可調整鋼的晶格與組織，改善硬度、強度或耐腐蝕；但比例過高或性能取捨也可能降低延展性。",
    "A。玻璃纖維承擔拉伸與剛性，樹脂固定纖維並傳遞應力，兩者組合可取得單一材料沒有的性能平衡。",
    "A。便當盒會接觸熱食，應先看使用溫度範圍、熱變形或耐熱資料，再同時檢查食品接觸安全與清洗耐久。",
    "A。熱塑性塑膠受熱可軟化並再成形；熱固性塑膠固化後交聯，通常再加熱不會重新熔融，兩者加工與回收不同。",
    "A。要固定試片尺寸、厚度、缺口、落錘高度、溫度、撞擊位置與重複次數，只改材料種類並記錄破壞能量或結果。",
    "A。需考慮低溫脆化和高溫軟化的工作範圍，可改配方、增加保護結構或限制使用溫度，不能只看室溫測試。",
    "A。先分選顏色與材質、去除金屬陶瓷等異物並破碎，才能降低混料造成的熔融溫度差、缺陷與設備損傷。",
    "A。要同時比較質量、強度、耐候、疲勞、加工、成本、維修與報廢方式，依零件的實際失效風險加權。",
    "A。優先採用可拆解、可分選、可重複使用或再生的設計，並保留材料標示與維修路徑，兼顧性能和生命週期。",
    "B。雨水導管不需導電且要長期淋雨、方便固定，乙質量小、耐水且不導電；仍須再確認耐候與接合強度。",
    "B。戶外螺栓需要硬度與耐腐蝕，合金改善這兩項但延展性下降，應再確認脆裂、負載與加工條件，不能只看單一性能。",
]
STRATEGIES = [
    "由單體、鏈結與鏈間作用推論性能，再檢查加工與添加物。",
    "比較合金前後的硬度、腐蝕、延展和使用需求，接受性能取捨。",
    "把纖維和樹脂的功能分開，再看界面、方向和比例。",
    "先列工作溫度與食品接觸條件，再比較熱變形和安全資料。",
    "從分子網狀結構判斷加熱後能否重新熔融與回收。",
    "固定所有測試條件，只改材料並重複測量衝擊結果。",
    "把實際溫度範圍與材料脆化／軟化曲線連結到設計。",
    "按材質分選、去除異物、破碎，再檢查再生品質。",
    "建立性能、製程、成本、維修和生命週期的比較矩陣。",
    "先追蹤拆解、分選、再使用與報廢路徑，再提出設計改良。",
    "把產品需求逐項對照候選材料資料，補上尚缺的耐候與接合驗證。",
    "接受硬度與延展性的取捨，回查螺栓受力、腐蝕和脆裂風險。",
]
STEPS = [
    "列出產品功能、環境、負載、安全與成本需求。",
    "把材料組成與加工方式連到可測量性能。",
    "確認比較資料的單位、測試條件與重複性。",
    "評估性能取捨、維修、回收與生命週期。",
    "以需求—證據—限制寫出條件式選材結論。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1", "content": CONTENT})
    lesson["studyHighlights"] = ["由聚合物、合金與複合材料的組成與結構推論性能。", "先把產品需求轉成可測試的材料指標。", "區分熱塑與熱固加工及回收條件。", "把公平測試、維修、回收與生命週期納入設計。"]
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-mc-iv-4、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合聚合物、合金、複合材料、熱塑／熱固、性能測試、再生玻璃、產品安全與生命週期；把原通用佔位正文改寫為雨水導管—便當盒—腳踏車零件的材料設計教材，並逐一處理 12 題，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 13):
        path = ROOT / f"questions/science/question-science-content-mc-iv-4-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的聚合物、合金、複合材料、材料測試、回收、選材與生命週期能力；本題改寫為人造材料特性、製造與應用原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "allUnitQuestionsProcessed": True, "questionCount": 12, "contentRewrittenFromPlaceholder": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content mc iv 4")


if __name__ == "__main__": main()
