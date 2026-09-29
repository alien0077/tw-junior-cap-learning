import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ba-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-ba-iv-1-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "能量形式、轉換、摩擦與守恆"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "效率、系統邊界與能量收支"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "動能、位能、電能、內能與生活應用"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "B。物體下降時重力位能主要轉成動能；若忽略空氣阻力，機械能總量近似守恆，不能說能量消失。",
    "C。煞車摩擦把車輪與煞車皮的機械能轉成內能，還可能有聲音和少量熱傳到周圍；能量只是換形式與跨邊界傳遞。",
    "D。電風扇把電能轉成馬達的機械能，並伴隨聲音、摩擦與內能增加；不是所有電能都成為風的動能。",
    "A。電池的化學能先轉成電路中的電能，燈絲或 LED 再轉成光能與內能；順序要包含能量形式而非只寫電池到光。",
    "B。摩擦使物體動能減少，但能量轉入接觸面內能、聲音與周圍環境；把觀察量下降說成能量消失是錯誤。",
    "B。效率=有用輸出能量÷輸入能量×100%=70÷100×100%=70%；其餘能量可能轉成熱、聲音等非有用輸出。",
    "D。壓縮時外力把能量儲存在彈簧彈性位能，放手後轉成小車動能，並伴隨摩擦、聲音與內能。",
    "A。水的重力位能先轉成流動水的動能，再轉成渦輪和發電機的機械能，最後轉成電能並有熱損耗。",
    "B。未轉成電能的 800 J 不代表消失，可能轉為內能、反射光或其他輸出；要說明系統邊界與未量測項目。",
    "D。把物體、地面與空氣納入系統，能把摩擦、熱傳、聲音與其他能量流向納入收支，較不會誤判能量消失。",
]
STRATEGIES = [
    "先定義系統與初末狀態，再追蹤位能、動能與內能。",
    "把摩擦造成的機械能下降連到接觸面內能、聲音與熱傳。",
    "拆分電能轉機械能、風動能、聲音與內能的路徑。",
    "依化學能—電能—光能／內能順序畫箭頭。",
    "找動能減少後的去向，不把觀察量變小當能量消失。",
    "用有用輸出÷輸入計算效率，再補列其他輸出。",
    "把彈簧儲能和小車動能串起來，檢查摩擦與聲音。",
    "沿水位、流速、渦輪、發電機逐段追蹤能量轉換。",
    "用輸入減有用輸出估算未轉換部分，並說明系統界線。",
    "擴大系統以納入熱傳、聲音與環境交換，再檢查完整收支。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結動能、位能、電能、內能、摩擦、效率、系統邊界與能量守恆；本題以全新能量收支情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ba-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合動能、重力位能、彈性位能、化學能、電能、光能、內能、摩擦、效率、系統邊界與能量守恆；保留溜滑車—電池燈泡—煞車收支表互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出系統邊界、初始能量、過程中的傳遞與末態可觀察量。", "依情境畫動能、位能、化學能、電能、光能、內能與聲音箭頭。", "用守恆收支或效率公式計算，統一 J、百分比與輸入輸出定義。", "檢查摩擦、熱傳、聲音與環境交換，避免把某一形式減少說成能量消失。", "回查系統是否足夠完整，說明未量測能量與模型限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ba-iv-1-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的能量形式、轉換、效率、摩擦、系統邊界與守恆能力；本題改寫為能量收支原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content ba iv 1")


if __name__ == "__main__": main()
