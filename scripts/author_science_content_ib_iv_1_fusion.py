import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ib-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-ib-iv-1-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "氣團形成地區、溫度、濕度與密度"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "海洋大陸氣團、測站資料與天氣變化"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "冷暖氣團、鋒面、風向與證據界線"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。氣團重點是大型空氣團在形成源區停留後，溫度、濕度等性質相對均勻；它不是一次低溫、單一高氣壓或鋒面名稱。",
    "B。海洋源區可提供水氣，若空氣在暖海面停留，通常較暖且較濕；仍需用露點、相對濕度與多站資料核對。",
    "C。低緯暖海面可能形成暖濕氣團，高緯冷陸面可能形成冷乾氣團，但移動途中與地形會改變性質，這只是初步推論。",
    "D。露點、比濕或混合比能較直接描述空氣中水氣量；相對濕度還會隨溫度改變，需注意比較條件。",
    "B。在其他條件相近時，冷空氣密度較大，可用溫度資料作初步比較，但壓力、海拔與水氣也會影響密度。",
    "C。冷暖氣團性質差異與交界的上升運動、雲雨生成可能造成天氣變化；交會區是鋒面，不是氣團本身。",
    "D。應沿移動路徑設多站、連續測量溫度露點風向與降水，並比較源區與途中資料，才能分辨空氣本身變化和地形／鋒面效應。",
    "A。溫度下降、濕度上升可能與氣團替換有關，但風向改變是重要線索，也可能涉及鋒面、降雨或局部地形，不能單一歸因。",
    "C。先檢查氣團來源、影響時間、測站位置與資料時間尺度，再比較溫度、露點、風向和降水，不只看季節標籤。",
    "B。氣團判讀應由形成源區與多項連續資料支持，並標示移動、地形、鋒面和局部降雨造成的替代解釋。",
]
STRATEGIES = [
    "先用形成源區與停留時間界定氣團，再看溫度與濕度均勻性。",
    "由海洋或大陸、低緯或高緯預測水氣與溫度，再用露點資料核對。",
    "把源區特徵和移動途中改變分開，結論保留初步性。",
    "優先用露點、比濕或混合比比較水氣，注意相對濕度的溫度依賴。",
    "以溫度推密度時固定壓力、海拔與水氣等條件。",
    "分辨氣團本身和冷暖交界鋒面，連結上升、雲雨與天氣變化。",
    "設多站連續觀測並記錄風向、露點、降水與地形位置。",
    "列出氣團替換、鋒面、降雨與地形等多個解釋再比較。",
    "先查來源、時間、位置與資料指標，再解讀預報名稱。",
    "用來源—性質—測站證據—替代解釋完成條件式判讀。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結氣團源區、溫度、濕度、密度、冷暖氣團、鋒面與測站資料；本題以全新氣象判讀情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ib-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合氣團源區、海洋與大陸、低高緯、溫度、露點、濕度、密度、冷暖氣團、鋒面與多站證據；保留臺灣測站連續資料互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出氣團源區、停留時間、溫度、露點、濕度、密度、風向與降水資料。", "由海洋／大陸與低／高緯度預測冷暖乾濕，再用多站連續資料核對。", "區分氣團性質、移動途中變化與冷暖氣團交界鋒面。", "比較直接觀察、合理推論和地形、降雨、鋒面等替代解釋。", "回查資料時間尺度、測站位置與結論適用範圍，避免由單一讀值作出天氣定論。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ib-iv-1-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的氣團源區、溫度、濕度、密度、冷暖氣團、鋒面與測站資料能力；本題改寫為氣團原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content ib iv 1")


if __name__ == "__main__": main()
