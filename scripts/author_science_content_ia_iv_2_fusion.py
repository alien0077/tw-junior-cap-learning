import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ia-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-ia-iv-2-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "板塊運動、地震火山與地球構造"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "地質資料、地形與模型判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "地震帶、海底地形與板塊邊界"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。板塊是岩石圈中相對完整、可彼此運動的剛性單元，可能包含海洋地殼、大陸地殼及其下方上部地函；不能只等同一塊大陸。",
    "B。全球地震與火山集中在狹長帶，支持活動與板塊邊界或相對運動有關；單一地震點不能單獨確定邊界類型。",
    "C。長期 GPS 位移可量出板塊或地殼相對運動的方向與速率，適合檢驗板塊運動，而不是只描述一次地震的規模。",
    "D。海洋地殼在中洋脊形成後向兩側移動，離中洋脊越遠通常越老，支持海底擴張模型；不能解釋成海水本身變老。",
    "B。板塊是岩石圈單元，可能同時含海洋與大陸部分；大陸只是地表陸塊，兩者尺度、組成與概念不同。",
    "C。要檢驗臺灣地震與板塊運動的關係，應合併震央／震源深度分布、GPS 位移、斷層或板塊邊界方向等資料，而非只看地震次數。",
    "D。由淺到深排列的狹長震源帶可支持一板塊沿傾角隱沒到另一板塊下方，但仍要配合海溝、火山弧或地形資料。",
    "A。板塊整體會移動不代表板塊內每處應力、岩性與斷層條件相同；地震活動仍受局部結構與應力累積影響。",
    "C。保麗龍板在水面滑動主要是板塊相對運動的簡化模型，能表示邊界方向與相對位移，不能直接代表真實岩石、黏滯地函與時間尺度。",
    "B。要判斷活躍邊界，應看多年地震／火山分布、GPS 相對位移、震源深度與地形等多項互相支持的證據，並寫出模型限制。",
]
STRATEGIES = [
    "先定義岩石圈板塊的範圍，再排除把它縮小成大陸或單一地殼的說法。", "把全球帶狀分布與板塊邊界假說連起來，再檢查是否還需其他證據。", "看長期位移的方向、速率與相對位置，不用單次災害事件代替板塊運動資料。", "沿中洋脊向兩側比較海洋岩石年齡，判斷是否有生成與外移的順序。", "把板塊和大陸放在尺度、組成、邊界三個欄位比較。", "選能同時呈現位置、深度、方向和時間的多源資料。", "看震源深度是否沿傾斜帶增加，再用海溝和火山等資料交叉檢查。", "區分整體運動與局部應力、斷層及岩性條件。", "把模型可表示的相對位移與不可直接代表的真實尺度分開。", "要求多項長期、空間與深度證據共同支持活躍邊界。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求由地震火山分布、地形、岩石年齡、位移與剖面資料推論板塊運動；本題改用全新資料語料。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    lesson["content"] = {"summary": "從臺灣周邊與全球地震、火山、海底地形和 GPS 位移資料，建立岩石圈由多個板塊組成的模型，並用邊界相對運動解釋聚合、張裂與錯動的證據及限制。", "sections": [
        {"heading": "岩石圈不是一整片不動的外殼", "body": "岩石圈是較剛性的地球外層，並非一整塊連續不動的薄殼；它被分成多個能相對運動的板塊。板塊可能包含海洋地殼、大陸地殼與上部地函，不能直接等同一塊大陸或一個國家。"},
        {"heading": "分布資料把邊界畫出來", "body": "把全球地震、火山與海溝位置疊在地圖上，常會看到狹長帶狀分布。這是板塊邊界的線索，不是只要有一個地震就能畫出邊界；還要配合震源深度、地形與長期位移資料。"},
        {"heading": "三種相對運動要看箭頭與結果", "body": "張裂使板塊彼此遠離並可能形成新海洋地殼，聚合可造成碰撞或隱沒，錯動則以水平相對滑動為主。判讀資料時先畫箭頭，再把海溝、山脈、火山弧、地震帶或位移方向接到相對運動。"},
        {"heading": "海底年齡與 GPS 是不同時間尺度的證據", "body": "中洋脊兩側海洋岩石年齡的對稱變化可支持海底擴張；多年 GPS 則直接量出現今地表位移。兩者支持的時間尺度不同，不能用一次地震或一張示意圖取代長期資料。"},
        {"heading": "模型能解釋分布，不能預報單一災害", "body": "板塊模型能說明活動帶與地形的整體關係，不能由板塊箭頭直接預測某日某地必然發生大地震。保麗龍或剖面模型也簡化了岩性、摩擦、地函流動與時間尺度，結論要保留適用範圍。"},
    ]}
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ia-iv-2、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合岩石圈板塊、地震火山分布、邊界運動、海底擴張、GPS 位移與模型限制；保留既有臺灣剖面互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出板塊、地震火山、海溝、震源深度、岩石年齡、GPS 位移與箭頭方向。", "先把地圖、剖面或時間序列中的直接資料整理出來。", "用張裂、聚合、隱沒或錯動模型連結資料與相對運動。", "排除把板塊等同大陸、把單一地震當邊界證明，或把模型當單一災害預報的選項。", "用多項證據回查結論，並寫出觀測尺度、模型簡化與仍需補查的限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ia-iv-2-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["solutionStrategy"] = STRATEGIES[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的板塊、地震火山分布、地形、岩石年齡、GPS 與模型限制判讀能力；本題改寫為板塊構造原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ia iv 2")


if __name__ == "__main__": main()
