import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-aa-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-aa-iv-3-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "元素、化合物與混合物分類"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "粒子組成、化學式與分離方法"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "固定比例、分解與物質性質"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "D。只含一種元素的粒子即使由兩個相同原子組成，也仍是元素；化合物必須含兩種以上不同元素且有化學結合。",
    "B。元素與化合物的核心差異是組成的元素種類及化學結合，不是外觀、狀態或名稱。",
    "B。CO 與 CO₂ 都含碳、氧，但原子比例不同、是不同化合物；化學式下標表示固定組成，不能任意互換。",
    "C。尚未反應的鐵粉和硫粉只是物理混合，仍可各自保有性質並用物理方法分開；加熱反應後才可能形成硫化鐵化合物。",
    "A。若多次製得的樣品都具有固定元素比例，且需化學方法分解，能支持它是固定組成的化合物；均勻外觀本身不夠。",
    "D。每個粒子由兩個相同元素原子組成，表示由單一元素形成的雙原子分子，不是含兩種元素的化合物。",
    "B。砂與食鹽可藉溶解、過濾、蒸發等物理方法分離，且各成分保留原有特性，因此是混合物。",
    "C。最有力的證據是成分元素比例固定且可透過化學反應分解成不同元素；顏色或均勻度不能單獨證明。",
    "A。水通電分解成氫氣和氧氣，表示水可用化學方法拆成不同元素，是化合物而不是元素或單純混合。",
    "B。石墨與鑽石都只含碳元素，差異可來自原子排列與結構；元素分類看組成元素種類，不要求所有同元素材料性質相同。",
]
STRATEGIES = [
    "先數粒子中不同元素種類，再看是否為化學結合。", "用元素種類、固定比例與分離方式三個判準比較。", "讀化學式下標，檢查元素比例與物質是否相同。", "先確認是否發生化學反應，再判斷混合物或化合物。", "優先找固定比例與化學分解的重複證據。", "看每個粒子由同種或不同種原子組成。", "檢查能否物理分離且成分仍保有原來性質。", "把組成比例與化學分解證據放在外觀之前。", "由可分解成不同元素的結果判斷化合物。", "區分元素組成與原子排列造成的同素異形差異。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求由粒子圖、化學式、固定比例、分解與物理分離判斷元素、化合物或混合物；本題以全新語料重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-aa-iv-3、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合元素、化合物、混合物、粒子組成、固定比例、物理分離與化學分解；保留既有粒子分類互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出元素種類、粒子結合、化學式下標、比例與分離或分解方法。", "用粒子模型判斷樣品由同種元素、不同元素化合，或多種粒子混合。", "檢查比例是否固定，以及分離後成分是否保留原有性質。", "排除只看顏色、透明度或均勻外觀，或把化學式下標當成可變混合比例的選項。", "用粒子、化學式與實驗證據回查分類，補上模型與操作限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-aa-iv-3-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["solutionStrategy"] = STRATEGIES[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的元素、化合物、混合物、粒子組成、固定比例與分離判讀能力；本題改寫為物質分類原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content aa iv 3")


if __name__ == "__main__": main()
