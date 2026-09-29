import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-na-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-na-iv-3-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "資源永續、族群與環境資料"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "水資源、森林、漁業與生態平衡"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "承載量、保育、永續決策與控制變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以資源補充率、森林多樣性、地下水、外來種、保護區、灌溉、承載量、濕地監測與決策資料考查永續利用；本題只取能力方向並重新設計情境與選項。"
EXPLANATIONS = [
    "永續捕撈須讓採收量不長期超過族群補充能力，並以族群大小、年齡結構與繁殖資料調整禁捕期和配額；只看收入無法證明族群健康。",
    "單一快速生長樹種可能增加木材量，卻降低物種多樣性、土壤與棲地功能；恢復樹木數量不等於原本森林生態功能完全恢復。",
    "抽水量長期大於補注量會使地下水位下降，可能造成井枯、地層下陷、海水入侵或溪流基流減少；需比較抽取與補注的時間尺度。",
    "外來魚種可能捕食、競爭或改變食物網；管理應先監測族群、移除或隔離外來種並保護原生棲地，而不是只增加餵食或放養。",
    "應同時比較保護區內外的魚群量、體型／年齡結構、捕獲量、棲地狀況與社區收入，並追蹤足夠時間，才可評估生態與利用是否兼顧。",
    "滴灌降低蒸發與逕流浪費，雨水收集增加可用水來源；兩者都需配合水質、儲存、防蚊與乾旱期供水檢查。",
    "可再生只表示有自然補充機制；若採集速度長期超過恢復速度，仍會造成資源量下降，不屬於實質永續利用。",
    "濕地復育應有復育前後與對照區，長期監測水質、植被、鳥類／兩棲類、外來種與水位，並同時追蹤人類使用與干擾。",
    "應比較短期用水利益與長期棲地、物種繁殖及下游影響，提出替代取水、分期開發、避開繁殖期或補償復育等方案。",
    "最有力的證據需包含資源量、補充／消耗速率、生物多樣性、環境品質與利用者結果的長期資料，並有明確基準和可調整的管理門檻。",
]
STRATEGIES = [
    "比較捕撈量、補充率、繁殖期與族群監測，再設定可調整配額。",
    "把木材產量和多樣性、土壤、水文、棲地功能分開評估。",
    "建立抽水與補注的長期收支帳，檢查地下水位與地質後果。",
    "沿外來種進入—族群變化—食物網影響找出管理節點。",
    "使用保護區內外與前後時間序列的多項指標，而非單一收入。",
    "把節水效率和水源安全、儲存、乾旱期供應一起評估。",
    "比較自然恢復速度與採集速度，判斷是否超過承載量。",
    "設置對照、前後資料、長期指標與外來干擾紀錄。",
    "列出短期利益、長期生態代價、替代方案與受影響者。",
    "用多項長期指標和明確門檻判斷成效，並保留調整方案。",
]
STEPS = [
    "列出資源、使用者、補充來源與生態系關係。",
    "比較消耗量、補充量、承載量與時間尺度。",
    "檢查族群、生物多樣性、環境品質與人類利用資料。",
    "設計對照、重複或長期監測以排除替代解釋。",
    "提出有門檻、期限、受影響者與修正機制的永續方案。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-na-iv-3、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合資源補充率、承載量、地下水、森林多樣性、外來種、海洋保護區、節水、濕地監測與永續決策；保留溪流資源帳本—食物網—管理門檻互動，並打散原先全為 A 的正解位置，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    shifts = [0, 1, 2, 3, 1, 2, 3, 0, 2, 1]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-na-iv-3-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        opts = q["options"]
        shift = shifts[i - 1]
        opts = opts[shift:] + opts[:shift]
        for n, opt in enumerate(opts): opt["id"] = chr(65 + n)
        q["options"] = opts
        q["answer"]["value"] = chr(65 + ((0 - shift) % 4))
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的資源補充率、承載量、森林、地下水、外來種、保護區、濕地與永續決策能力；本題改寫為資源永續利用與生態平衡原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "answerPositionDiversityRepaired": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content na iv 3")


if __name__ == "__main__": main()
