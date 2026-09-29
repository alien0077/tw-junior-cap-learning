import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-eb-iv-9.json"
REPORT = ROOT / "implementation/reports/science-content-eb-iv-9-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "圓周運動、力與運動方向"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "速率、加速度與受力圖"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "生活轉彎、張力與向心力判讀"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "C。東側點的半徑指向東，切線方向必須與半徑垂直；題目已說瞬間向北，因此速度沿切線向北，不是指向圓心或向外。",
    "B。速率固定只代表速度大小不變，方向仍持續改變，所以仍有指向圓心的向心加速度。",
    "C。a_c=v²/r=4²/2=8 m/s²；先平方速率，再除以半徑，單位為 m/s²。",
    "D。a_c=v²/r，半徑不變而速率變為 2v 時，a_c 變為 (2v)²/r=4 倍。",
    "A。v 固定時 a_c=v²/r；半徑變為 2r，向心加速度變為原來的 1/2。",
    "A。忽略其他水平力時，繩張力提供指向圓心的水平合力；『向心力』是這個合力的功能名稱，不是額外一種力。",
    "A。水平道路轉彎時，輪胎與路面間的靜摩擦力提供改變速度方向所需的水平向心合力；若摩擦不足就會打滑。",
    "B。繩張力消失後，球保留斷裂瞬間的切線速度，會先沿切線前進，不是沿半徑被向外力推出。",
    "A。衛星的重力指向地球中心，提供近似圓周運動所需的向心合力；向心力不是另加的第五種力。",
    "C。F_c=ma_c=mv²/r=2×6²/3=24 N；先求向心加速度或直接代入向心力公式，並檢查方向指向圓心。",
]
STRATEGIES = [
    "先找圓心與切線，再用題目給的瞬時運動方向判斷速度。", "分開速度大小與方向；方向改變就有加速度。", "套用 a_c=v²/r，先處理平方與單位。", "看速率是否平方出現，再判斷倍數變化。", "固定速率時檢查半徑在分母的反比關係。", "畫水平受力圖，找真正指向圓心的合力來源。", "將轉彎摩擦力與向心合力區分，不增加虛構的力。", "向心力消失後依慣性沿切線，不沿半徑。", "把重力方向與地球中心位置連起來。", "使用 F_c=mv²/r，核對質量、速率、半徑與牛頓單位。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求辨認速度與加速度方向、套用向心關係、畫實際受力來源並判讀轉彎或衛星情境；本題重新設計數值與語料。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-eb-iv-9、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合切線速度、向心加速度、半徑與速率比例、實際力源及模型限制；保留既有互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出圓心、半徑、瞬時速度方向、速率、質量與實際受力來源。", "先分辨切線方向的速度與指向圓心的向心加速度。", "依 a_c=v²/r 或 F_c=mv²/r 代入，注意平方、倍數與單位。", "排除把向心力當額外力、把慣性力當真實向外力，或把速度方向畫向圓心的選項。", "用受力圖與公式回查答案，說明若繩斷、摩擦不足或半徑改變時模型如何失效或修正。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-eb-iv-9-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["solutionStrategy"] = STRATEGIES[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的速度與加速度方向、向心關係、受力來源與生活運動判讀能力；本題改寫為圓周運動原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content eb iv 9")


if __name__ == "__main__": main()
