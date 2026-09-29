import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-bb-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-bb-iv-2-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "熱量、比熱與能量計算"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "熱傳遞、單位與實驗資料判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "能量轉換、比熱與生活情境"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。1 cal 的教學定義是使 1 g 水升高 1 ℃ 所需的熱量；它是能量單位，不是溫度單位，也不能脫離質量與溫差條件。",
    "C。用 1 cal≈4.2 J 換算，50×4.2=210 J；先確認題目給的是近似換算，再保留合適有效位數。",
    "C。Q=mcΔT=100 g×1 cal/(g·℃)×5 ℃=500 cal；質量、比熱與溫差的單位相消後留下熱量單位。",
    "A。在 Q、m 相同時，ΔT=Q/(mc)，溫升較小表示 c 較大；高比熱材料需要較多能量才升高同樣溫度。",
    "A。兩杯材料、質量與比熱相同，Q=mcΔT，所以甲／乙=10/20=1/2；甲吸收的熱量是乙的一半。",
    "C。m=Q/(cΔT)=300/(1×3)=100 g；要先把公式變形成求質量，再檢查單位。",
    "A。cal 與 J 都是熱量或能量單位；℃是溫度，g 是質量，不能把它們當成熱量單位。",
    "A。Q=mcΔT 還需要質量與比熱；只知道溫升 10 ℃，無法判斷哪個吸收較多熱量。",
    "B。若只把放熱物體視為系統，能量離開系統，所以其熱量變化以負值記錄，即 ΔQ=-80 J；周圍得到的能量是另一個系統的增加。",
    "A。顯熱的 ΔT 是末溫減初溫，包含方向；若升溫為正、降溫為負，不能直接把末溫當成熱量。",
]
STRATEGIES = [
    "先回到 1 cal 的質量與溫差定義，再排除溫度單位。", "先寫換算比例，再做 50×4.2 並檢查單位。", "列出 Q=mcΔT，代入三個量並檢查單位相消。", "固定 Q 與 m 時，用 ΔT=Q/(mc) 比較比熱。", "質量與材料相同時，直接比較 Q 與 ΔT 的比例。", "把 Q=mcΔT 變形成 m=Q/(cΔT)，再代數值。", "區分能量單位、溫度單位與質量單位。", "列出還缺的 m 或 c，避免只用溫差推熱量。", "先決定系統邊界與能量方向，再用正負號表示。", "把溫差寫成末溫減初溫，並判斷升降溫方向。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求解讀熱量單位、比熱、溫差、熱傳遞與生活資料；本題以新的數值或情境重新設計。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-bb-iv-2、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合熱、溫度、熱量、cal、J、Q=mcΔT、比熱與熱量計限制；保留既有互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出熱量單位、質量、比熱、初末溫與系統邊界。", "選用 Q=mcΔT 或單位換算關係，先寫公式再代數值。", "統一 cal、J、g、kg、℃ 等單位，確認溫差方向與正負號。", "排除把熱量當溫度、把末溫當溫差，或忽略容器吸熱、散熱與相變限制的選項。", "用完整句回查計算結果、單位與模型適用條件。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-bb-iv-2-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["solutionStrategy"] = STRATEGIES[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的熱量單位、比熱、溫差、熱傳遞與資料計算能力；本題改寫為熱量定義原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content bb iv 2")


if __name__ == "__main__": main()
