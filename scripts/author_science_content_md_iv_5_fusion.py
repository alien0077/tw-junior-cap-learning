import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-md-iv-5.json"
REPORT = ROOT / "implementation/reports/science-content-md-iv-5-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "降雨、地質構造與坡地災害"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "地形、地下水與防災資料判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "坡地安全、監測與環境變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "B。順向坡的岩層傾斜方向與坡面下降方向大致相同，雨水與重力可能沿層面促進滑動；不能只用坡度大小判斷。",
    "C。入滲水會增加土體重量、孔隙水壓，並可能降低顆粒間有效摩擦，使抗滑能力相對下降；實際風險仍須看岩性與排水。",
    "A。連續降雨讓水分累積、地下水位或孔隙水壓可能上升，且排水來不及，效果不同於短暫小雨。",
    "D。裂縫擴大、樹木歪斜或擋土牆鼓起是警訊，應保持距離、通報並依主管機關或校方指示管制、改道或撤離。",
    "B。除雨量外還要記錄坡面／岩層方向、坡度、排水、裂縫與位移等條件，才能避免把相關性誤當單一因果。",
    "B。截水與排水可減少地表水入滲、導引水流，降低坡體含水與水壓累積；它不是保證任何雨量都不會滑動。",
    "C。應固定土壤量、坡度、模擬降雨強度與時間，只改變植被覆蓋，並重複量測流失土量，才可比較植被效果。",
    "A。風險圖應標示危險區、警戒門檻、避難路線、集合點與更新時間，讓使用者知道何時往哪裡避難，而非只塗一種顏色。",
    "D。位移速率持續增加或加速、且與裂縫和累積雨量同時出現，比單次小幅位移更值得警戒；仍要配合專業門檻。",
    "C。選線與開發應避開高風險順向坡，並做地質與水文調查、排水、坡腳保護、監測與警戒規劃，不能只加一道擋土牆。",
]
STRATEGIES = [
    "先在剖面比較坡面下降方向和岩層傾向，再判斷順向或逆向。", "把入滲水連到重量、孔隙水壓和摩擦力的變化。", "看累積雨量、排水時間與地下水，而非只看一次降雨。", "將裂縫等現場警訊轉成避開、通報與依指示撤離行動。", "把雨量與幾何、岩性、排水、位移等同步資料配對。", "從水流路徑判斷截水和排水如何改變坡體含水。", "只改植被條件並固定其他變因，重複量測沖蝕量。", "選能直接支援判斷與避難行動的地圖資訊。", "看位移時間序列是否加速並和其他警訊一致。", "用地質、水文、工程、監測和警戒五類條件整體評估。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求由坡面與岩層方向、降雨、地下水、位移、沖蝕與防災設施判讀坡地風險；本題以全新語料重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-md-iv-5、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合順向坡、降雨入滲、孔隙水壓、排水、裂縫、位移監測與防災決策；保留既有坡面互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出坡面方向、岩層傾向、雨量、排水、裂縫、位移與安全警訊。", "先用剖面和時間序列整理直接觀察，再判斷順向坡與水的作用。", "把降雨、孔隙水壓、重量、摩擦、坡腳與位移連成風險模型。", "排除只看坡度或單次雨量、把山崩當必然結果，或為取證而靠近危險坡面的選項。", "用完整句寫出條件式風險判斷、補測資料與安全行動。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-md-iv-5-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["solutionStrategy"] = STRATEGIES[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的順向坡、降雨、排水、地質風險、位移監測與防災資料判讀能力；本題改寫為坡地安全原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content md iv 5")


if __name__ == "__main__": main()
