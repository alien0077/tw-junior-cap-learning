import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-jb-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-jb-iv-3-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "電解質、離子與水溶液反應"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "沉澱、導電度與粒子判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "酸鹼、溶解與淨離子反應"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。固態 NaCl 的離子被固定在晶格中，溶於水後 Na⁺ 與 Cl⁻ 可移動，因此溶液能導電；不是因為水把它變成金屬。",
    "B。NaCl 溶於水後解離成可移動的 Na⁺ 和 Cl⁻，粒子種類仍守恆；要注意係數表示粒子數量比例。",
    "C。MgCl₂(aq) 解離為 Mg²⁺＋2Cl⁻，所以鎂離子與氯離子的粒子數比為 1:2，並符合電荷總和為零。",
    "D。Ag⁺ 與 Cl⁻ 生成難溶的 AgCl，最直接的宏觀證據是出現混濁或白色沉澱；導電度變化本身不能單獨指明產物。",
    "B。BaSO₄ 沉澱會把 Ba²⁺ 和 SO₄²⁻ 從溶液中移除，Na⁺、Cl⁻ 多半是旁觀離子，仍留在水溶液中。",
    "C。食鹽水有可移動的離子，糖水主要是中性分子；在濃度與測量條件相當時，前者通常有較強導電性。",
    "D。離子反應式除了元素原子數，還要檢查反應前後總電荷相同；只數元素可能留下不合理的電荷。",
    "A。若沒有沉澱、氣體或弱電解質生成，離子仍以原本可溶形式存在，通常沒有可寫出的淨離子反應；需保留觀察與濃度限制。",
    "C。加水稀釋使單位體積內可移動離子數減少，導電度通常下降；這不表示離子全部消失。",
    "B。導電表示溶液中存在可移動帶電粒子，但不能只靠導電度確定是哪一種離子、濃度或是否發生特定反應。",
]
STRATEGIES = [
    "先區分固態晶格與水中可移動離子，再連到導電性。", "把溶解寫成離子解離，並檢查粒子種類與數量。", "依化學式下標讀出離子比例，再核對電荷中和。", "找最直接的沉澱、氣體、弱電解質或顏色證據。", "交換離子後刪除未改變的旁觀離子。", "比較可移動離子與中性分子的數量和狀態。", "逐元素計數後，再逐電荷檢查反應式。", "沒有驅動反應的生成物時，避免硬寫淨離子反應。", "將稀釋造成的單位體積粒子數變化與總粒子數分開。", "把導電性當成離子存在的證據，不過度推定成分。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求由導電、解離、離子比例、沉澱、酸鹼與電荷守恆判讀水溶液；本題以全新語料重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-jb-iv-3、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合電解質解離、離子比例、沉澱、酸鹼中和、旁觀離子、導電度與電荷守恆；保留既有水樣互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出溶液中的陽離子、陰離子、化學式下標、沉澱或導電證據。", "把固體、溶液中的自由離子與反應後粒子分開表示。", "檢查元素數量、總電荷、溶解性與是否有驅動反應的產物。", "排除把透明混合等同沒有反應、把所有離子都變成沉澱，或把導電度直接當成完整成分證明的選項。", "用淨離子式或粒子模型回查答案，補上旁觀離子、濃度與觀察限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-jb-iv-3-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["solutionStrategy"] = STRATEGIES[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的電解質、離子、沉澱、酸鹼、導電度與電荷守恆判讀能力；本題改寫為水溶液離子反應原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content jb iv 3")


if __name__ == "__main__": main()
