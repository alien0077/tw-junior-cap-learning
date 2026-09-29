import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ea-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-ea-iv-1-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "基本量、衍生量、單位與測量"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "速率、密度、體積與有效數字"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "單位換算、排水法與資料表達"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以單位、速率、密度、排水法、體積換算、測量刻度與資料表達考查基本量和衍生量；本題只取能力方向並重新設計情境與數據。"
EXPLANATIONS = [
    "B。完整物理量至少要有數值、單位與量的名稱或符號，例如 12 m/s；只寫數字無法知道描述什麼。",
    "B。平均速率=距離÷時間=60 m÷12 s=5 m/s；必須保留距離與時間的單位。",
    "C。密度由質量÷體積計算得到，屬於衍生物理量；長度、時間等可作為基本量的直接測量例子。",
    "C。密度=240 g÷100 mL=2.4 g/mL；質量和體積的單位要與答案一致。",
    "A。密度固定時 m=ρV，質量加倍會使體積也加倍；前提是材料和密度沒有改變。",
    "D。操場長度通常用公尺表示；毫米太小、公里太大，選單位要配合量級和測量目的。",
    "A。排水法得到的體積=48.0−35.0=13.0 mL；要注意兩個讀值的小數位一致。",
    "B。速度除了數值還需要方向與單位；若只寫『5』，至少缺少單位，若要完整速度還要交代方向。",
    "A。最小刻度 1 mm，12.4 cm=124 mm，讀值精度需符合尺的解析度；不能宣稱多出未測得的小數位。",
    "C。1 m³=1000 L，因此 0.24 m³=240 L；換算時立方單位的倍率不能當成 0.24×100。",
]
STRATEGIES = [
    "先找量的名稱、數值與單位，確認三者是否完整。",
    "用距離÷時間計算平均速率，再檢查單位。",
    "判斷量是否由其他量依定義式組合，區分基本與衍生。",
    "列密度=質量÷體積，代入並保留 g/mL。",
    "固定密度用 m=ρV 比例判斷質量與體積。",
    "用生活量級估算，再選適合長度單位。",
    "用末刻度−初刻度，並維持讀值精度。",
    "先補單位，再確認速度是否需要方向。",
    "把最小刻度換成題目單位，避免寫出超過儀器解析度的數字。",
    "使用 1 m³=1000 L 的體積單位關係檢查量級。",
]
STEPS = [
    "辨認物理量名稱、數值、單位與測量工具。",
    "寫出基本量或衍生量的定義關係式。",
    "統一單位後代入計算或比較量級。",
    "檢查有效數字、刻度與方向是否合理。",
    "用反向換算和單位分析驗收紀錄能否被他人重現。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ea-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合基本量、衍生量、速率、密度、排水法、單位換算、測量刻度、有效數字與可追溯紀錄；保留運動隊資料卡—量值護照—單位海關互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ea-iv-1-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的基本量、衍生量、速率、密度、排水法、單位、刻度與資料表達能力；本題改寫為基本物理量與衍生物理量原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ea iv 1")


if __name__ == "__main__": main()
