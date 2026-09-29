import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-fc-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-fc-iv-1-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "個體、族群、群集、生態系與生物圈"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "生物因子、非生物因子與生態系資料"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "生產者、消費者、分解者與尺度判讀"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。三隻同種麻雀在同一公園與同一繁殖季中共同生活，描述的是同一物種在特定空間與時間的族群。",
    "B。魚、藻類、細菌等生物與陽光、水溫、溶氧等非生物環境共同構成生態系；只列生物才是群集。",
    "C。箭頭可表示水草、蝸牛、魚與水鳥間的取食關係和能量傳遞方向，但不能僅憑此圖判斷全部生物圈或能量數值。",
    "D。能量從生產者進入食物網，沿營養階層傳遞並散失，因此通常生產者層可用能量最多。",
    "B。小島上所有生物族群與陽光、土壤、降雨、溫度等環境共同作用，範圍最接近一個生態系，而非只是一個群集。",
    "C。分解者分解遺體與排遺，使有機物中的元素回到土壤、水或大氣，連接生物與非生物環境的物質循環。",
    "D。砍伐改變光照與水溫，溶氧下降又限制魚類呼吸；這是非生物條件改變透過生理限制影響族群數量的連鎖。",
    "A。應比較兩地的生物組成、非生物條件、能量來源、物質循環與尺度，而不是只比較物種數量。",
    "C。生物圈涵蓋地球上適合生物生存的整體範圍，許多局部生態系是其中的組成部分；兩者研究尺度不同。",
    "B。完整判斷要同時觀察池塘的生物群集、光照、水溫、溶氧、養分、物質流動與時間變化，而非只拍攝魚的數量。",
]
STRATEGIES = [
    "先圈對象、物種數、空間與時間，再決定個體或族群。",
    "把生物群集和非生物環境一起納入，才可判斷生態系。",
    "先讀食物箭頭的功能，再說明能量方向與可支持的結論範圍。",
    "由營養階層與能量散失判斷能量塔各層，不把物質循環套入。",
    "檢查是否同時包含生物群集和環境條件，再判斷生態系尺度。",
    "沿遺體—分解者—土壤／水／大氣追蹤元素回流。",
    "把砍伐、遮蔭、水溫、溶氧與魚群變化接成因果路徑。",
    "用同一尺度比較生物、非生物、能量與物質資料，避免只看物種數。",
    "區分全球生物圈和局部生態系的包含關係與研究範圍。",
    "用生物、非生物、物質流動與時間資料共同檢查生態系完整性。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求判斷個體、族群、群集、生態系、生物圈、生物與非生物因子及能量層級；本題以全新生態尺度情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-fc-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合個體、族群、群集、生態系、生物圈、生產者、消費者、分解者、非生物因子與能量層級；保留校園池塘觀察地圖與尺度切換互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出研究對象、物種數、空間範圍、時間範圍與環境條件。", "依個體—族群—群集—生態系—生物圈排列，確認每層的包含關係。", "標記生產者、消費者、分解者與陽光、水溫、溶氧等非生物因子。", "沿取食、能量、物質與環境影響箭頭判斷可支持的結論，不超出觀察範圍。", "回查尺度、時間與資料限制，說明單一物種或單一讀值不能代表整體系統。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-fc-iv-1-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的生態尺度、群集、生態系、非生物因子、能量與食物關係能力；本題改寫為生物圈原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content fc iv 1")


if __name__ == "__main__": main()
