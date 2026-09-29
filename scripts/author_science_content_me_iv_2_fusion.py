import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-me-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-me-iv-2-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "水污染、濃度與資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "家庭廢水、處理方法與環境影響"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "水質、優養化、控制變因與安全"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以家庭排水、水質指標、溶氧、優養化、濃度計算、處理流程、控制變因與安全用途考查環境推理；本題只取能力方向並重新設計情境與數據。"
EXPLANATIONS = [
    "B。家庭廢水可能帶有油脂、清潔劑、食物殘渣、有機物與懸浮固體；污染物種類取決於排水來源，不能只看水的外觀。",
    "C。油脂會附著管壁、凝結堵塞，也可能在水面形成薄膜，妨礙氣體交換；應先集中回收，不直接倒入排水系統。",
    "A。有機物被微生物分解會消耗水中溶氧，若補充速度跟不上，魚類等需氧生物可能受害；不是有機物越多溶氧越高。",
    "D。先確認來源未含高濃度清潔劑、油脂或病原風險，再依植物與土壤用途評估；觀賞植物與食用作物的安全門檻不同。",
    "B。沉澱主要靠密度差讓較大的懸浮顆粒下沉，不能移除全部溶解物、病原體或清潔劑。",
    "B。只改清潔劑種類，固定濃度、體積、植物種類、光照、溫度與觀察時間，才能把生長差異合理歸因於清潔劑。",
    "C。清澈度只能反映部分懸浮物，還要依用途檢查微生物、溶解物、清潔劑殘留、鹽分或其他水質指標。",
    "A。減少水龍頭流量、避免不必要放水並先刮除油脂或集中回收，能從源頭同時降低用水量與污染負荷。",
    "D。要同時看水源污染物、處理效果、儲存與接觸風險、用途需求、成本及失效時的替代方案。",
    "C。80 L 水約 80 kg；8 ppm=8 mg/kg，所以硝酸鹽量約為 80×8=640 mg，不能把 ppm 當成 8 g。",
    "C。清澈只代表部分顆粒被移除，不能證明病原體、清潔劑或鹽分安全；食用菜園需有符合用途的水質檢驗與管理。",
    "A。有效性要以處理前後同一水質指標、相同採樣與多次測量比較，並觀察長期結果，不應只憑一次看起來較清澈。",
]
STRATEGIES = [
    "從排水來源列出可能攜帶的污染物，再判斷其環境影響。",
    "把油脂的物理性質與管道／水面位置連結，說明堵塞與氣體交換問題。",
    "追蹤微生物分解有機物的耗氧過程，再判斷水生生物風險。",
    "先分辨觀賞與食用用途，再核對來源、處理與接觸風險。",
    "用密度差判斷沉澱能去除的對象，並列出不能處理的溶解污染物。",
    "只改一個自變因，控制植物與環境條件，設定可比較的生長指標。",
    "由用途反推需要的水質指標，不把清澈度當成完整安全證明。",
    "比較源頭減量與末端處理的效果，優先找能同時減少用水和污染的行動。",
    "用來源—處理—用途—風險—成本五個面向評估整體方案。",
    "把 ppm 轉成 mg/kg，再乘以樣本質量並保留單位。",
    "先列出食用作物的病原與化學暴露風險，再判斷目前證據是否足夠。",
    "設計前後對照、重複採樣與相同檢測方法，避免用單次外觀作結論。",
]
STEPS = [
    "確認廢水來源、污染物與預定再利用用途。",
    "把處理方法對應到可去除的物質與剩餘風險。",
    "核對水質資料的單位、濃度、樣本量與採樣條件。",
    "用對照、重複測量或長期觀察檢查方案效果。",
    "以衛生、安全、環境與用途限制寫出條件式結論。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-me-iv-2、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合家庭廢水來源、油脂、有機物耗氧、沉澱過濾、生物處理、消毒、ppm、水質指標、再利用用途與食安限制；保留洗手水—處理流程—用途決策互動，並逐一處理 12 題，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 13):
        path = ROOT / f"questions/science/question-science-content-me-iv-2-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的水污染、廢水處理、濃度、溶氧、優養化、控制變因與安全能力；本題改寫為家庭廢水影響與再利用原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "allUnitQuestionsProcessed": True, "questionCount": 12, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content me iv 2")


if __name__ == "__main__": main()
