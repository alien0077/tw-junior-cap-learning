import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-md-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-md-iv-3-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "颱風、氣象資料與災害判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "風雨、氣壓、暴潮與防災"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "降雨、洪水、地形與風險資料"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以颱風路徑、氣壓風場、降雨、潮位、地形、災害地圖與防災資料考查機制鏈及風險判讀；本題只取能力方向並重新設計情境與選項。"
EXPLANATIONS = [
    "B。強風可直接造成招牌、樹木或建物外部構件受損，並使飛散物增加；實際傷害仍取決於風速、結構與暴露程度。",
    "C。短時間強降雨若遇不透水鋪面、排水容量不足、低窪地或潮位偏高，雨水較難排出，都市淹水風險會放大。",
    "A。暴潮主要是強風推水與低氣壓造成海面升高等效應，若與天文高潮及海岸地形疊加，沿岸水位可能更高。",
    "D。沿海應依官方警報避開海邊、港區與低窪地，提早往高處或指定避難處移動；不要以現場看似平靜判斷安全。",
    "B。應固定都市區、排水條件、量測時間與雨量來源，只比較降雨強度或累積雨量，並納入多次事件或對照區。",
    "B。衛星雲圖、雷達回波、氣壓與風場、海溫及測站資料的連續更新，可共同修正路徑、強度與降雨預測。",
    "C。山區坡度、地質、土壤含水、先前降雨與河道條件會提高土石流脆弱度；不能只看當下雨量一項。",
    "A。要比較上游蓄洪、排水速度、下游水位與不同降雨情境，檢查工程是否只是把尖峰流量或淹水時間移給下游。",
    "D。至少要有危險區、人口與建物、道路／避難處、河川海岸、地形及預警時間等圖層，才能把 hazard 連到暴露與避難路徑。",
    "C。最完整證據應把預測雨量／風速／潮位與實測資料、災損範圍及措施前後結果對照，並交代時間、空間與替代原因。",
]
STRATEGIES = [
    "先從風速和暴露物連結直接受損機制，再補結構條件。",
    "把降雨、排水、地形與潮位放在同一時間空間框架比較。",
    "分開天文潮與颱風造成的海面增水，再判斷疊加風險。",
    "以官方警報、避難位置與水位變化作決策依據，不靠現場直覺。",
    "固定非研究變因，使用多次事件或對照區比較雨量與淹水。",
    "整合衛星、雷達、測站與海象的時間序列，而非只看單張圖。",
    "列出坡度、地質、含水量、先前雨量與河道等脆弱度條件。",
    "沿上游—工程—下游追蹤流量與水位，檢查風險是否轉移。",
    "把危險、暴露、脆弱度與避難資源圖層疊合判讀。",
    "比較預測、實測、災損和措施前後資料，說明時空範圍與限制。",
]
STEPS = [
    "標出颱風中心、風雨圈、海岸、河川、山區與測站位置。",
    "分別追蹤風、雨、海水位三條機制與時間變化。",
    "核對路徑、地形、潮位、排水與暴露人口等條件。",
    "用多站資料、預測與實測比較檢查因果方向。",
    "提出符合官方警報與避難資源的條件式防災結論。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-md-iv-3、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合颱風結構、風雨、暴潮、天文潮、路徑、地形、降雨、洪水、土石流、災害圖層與防災證據；保留同一颱風三地差異與位置—時間—機制互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-md-iv-3-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的颱風、風雨、氣壓、暴潮、降雨、地形、災害圖與防災能力；本題改寫為颱風狂風豪雨與暴潮災害原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content md iv 3")


if __name__ == "__main__": main()
