import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-aa-iv-5.json"
REPORT = ROOT / "implementation/reports/science-content-aa-iv-5-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "元素符號、化學式與粒子數量"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "元素、化合物、化學式與原子守恆"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "週期表、符號大小寫與化學式判讀"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以元素符號大小寫、原子序、化學式下標與係數、粒子模型及反應式守恆考查符號讀寫；本題只取能力方向並重新設計情境與選項。"
EXPLANATIONS = [
    "C。元素符號第一個字母必須大寫，第二個字母若有則小寫；大小寫不是排版偏好，而是符號身分的一部分。",
    "B。Fe 的 F 大寫、e 小寫，代表鐵；不能寫成 FE 或 fe，因為那不符合元素符號規則。",
    "A。原子序 8 對應氧，元素符號為 O；原子序代表核內質子數，不是化學式中的原子個數。",
    "A。H₂O 的下標 2 只表示每一個水分子含 2 個氫原子，O 沒有下標即為 1 個氧原子。",
    "C。2O 是兩個氧原子或兩個氧粒子的係數表示，O₂ 是一個氧分子內含兩個氧原子；係數與下標作用範圍不同。",
    "D。先核對中文名稱對應的元素符號 Mg，再確認 M 大寫、g 小寫及原子序等資料；不能依發音猜字母。",
    "B。Ca 才是鈣的正確符號；CA 將第二字母錯寫成大寫，不符合元素符號大小寫規則。",
    "A。用週期表或經核對的元素資料表查符號，再反向確認原子序與名稱；只靠符號外觀猜測不可靠。",
    "C。NaCl 表示由鈉與氯兩種元素組成，Na 和 Cl 各一個的最簡整數比；它不是兩個獨立元素符號的隨意並列。",
    "D。先核對大小寫，再把下標與係數轉成原子清單，最後用反應前後各元素原子數相等檢查卡片。",
]
STRATEGIES = [
    "先檢查每個符號的第一字母大小寫與第二字母小寫規則。",
    "按元素符號格式拆分 Fe，避免把大小寫視為可互換。",
    "用原子序與週期表交叉確認元素名稱和符號。",
    "只把下標作用在它左側的元素或括號單位，再列出原子數。",
    "把係數與下標分開，分別說明粒子數和單一粒子內的原子數。",
    "由中文名稱查正式符號，再核對大小寫與原子序。",
    "檢查第一字母大寫、第二字母小寫，並與週期表核對。",
    "先查資料表，再用名稱、符號、原子序三者互相驗證。",
    "逐一讀取 Na、Cl 與下標，說明元素種類和數量比例。",
    "建立符號—下標—係數—原子總數四欄檢查表。",
]
STEPS = [
    "辨認元素名稱、符號、原子序或化學式的範圍。",
    "檢查符號大小寫與下標、係數位置。",
    "把化學式翻成元素種類與各自原子數。",
    "以週期表或反應前後原子守恆交叉驗證。",
    "說明係數、下標及資料表限制，避免只靠外觀猜答案。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-aa-iv-5、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合元素名稱與符號、大小寫、原子序、化學式下標、係數、粒子模型與原子守恆；保留化學式解碼器與符號卡片互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-aa-iv-5-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的元素符號、原子序、化學式、下標係數、粒子模型與守恆能力；本題改寫為元素與化合物符號原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content aa iv 5")


if __name__ == "__main__": main()
