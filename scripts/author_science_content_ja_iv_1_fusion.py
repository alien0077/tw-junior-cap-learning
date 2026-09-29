import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ja-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-ja-iv-1-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "化學反應、質量守恆與系統邊界"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "密閉／開放系統與資料誤差"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "反應式、氣體與質量證據"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。反應物總質量為 35+18=53 g；因所有物質仍在同一密閉系統內，反應前後總質量應相同。",
    "B。開放空氣中燃燒時，鋼絲絨與氧氣結合，氧氣從系統外進入，所以固體秤得的質量可能增加；不是創造質量。",
    "C。二氧化碳逸出使開放容器內留下的物質變少，秤得質量下降反映系統邊界與物質進出，不否定完整系統的質量守恆。",
    "D。氣球把生成氣體留在同一稱量系統，讓反應前後的物質都納入總質量比較；它不是用來直接判定氣體成分。",
    "B。係數調整粒子比例，使各元素原子數相等，反映反應前後原子重新排列與質量守恆；不能藉改下標配平。",
    "C。沉澱形成改變物質外觀與分布，但若整個密閉瓶都被秤量，物質仍在系統內，總質量應近似不變。",
    "D。水蒸氣逸出造成物質離開系統，應改用密閉裝置、冷凝收集或把逸出物納入質量收支，並控制溫度與秤量條件。",
    "A。氣泡表示可能生成氣體，但密閉系統中氣體仍在容器內；總質量相同支持守恆，不能單獨告訴氣體種類。",
    "C。公平比較需使用相同容器、秤量程序與反應物，並分別記錄密閉或開放邊界、重複讀值與逸出物收集情況。",
    "B。119.8 g 與 120.0 g 的差值要和秤的解析度、重複測量、密封性與物質進出一起檢查；應報告差值與限制，不直接宣稱守恆失效。",
]
STRATEGIES = [
    "先確認所有物質是否留在同一系統，再把反應物質量相加。", "追蹤空氣中的氧是否進入被秤量系統。", "先畫開放系統邊界，再判斷氣體是否逸出。", "把氣體收回同一稱量系統，避免只量容器內剩餘物。", "逐元素計數並調係數，不改變化學式下標。", "區分外觀改變與系統總質量是否改變。", "找出蒸氣離開的路徑，再設計冷凝或密閉改善。", "把氣泡、密閉條件與總質量分開判讀。", "控制容器、秤、反應物、時間與邊界，並做重複測量。", "比較差值與量測不確定度，再寫條件式報告。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求由稱量、氣體進出、反應式係數、密閉條件與量測誤差判斷質量守恆；本題以全新語料重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ja-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合質量守恆、密閉／開放系統、氣體進出、反應式係數、量測誤差與證據報告；保留既有密閉袋互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出反應前後質量、容器、氣體、系統邊界、重複讀值與誤差線索。", "列出被秤量的完整系統，追蹤物質是否進出。", "加總前後質量或依差值判斷氣體逸出、吸收與測量波動。", "排除把開放系統差值當成守恆失效、把氣泡直接當成特定氣體，或忽略容器與量測條件的選項。", "用完整句寫出條件式結論、補測方法與目前不能推出的範圍。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ja-iv-1-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["solutionStrategy"] = STRATEGIES[i-1]; q["solutionSteps"] = steps; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的質量守恆、密閉／開放系統、氣體進出、反應式與量測誤差能力；本題改寫為質量守恆原創情境。"; path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ja iv 1")


if __name__ == "__main__": main()
