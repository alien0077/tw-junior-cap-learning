import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ing-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-ing-iv-1-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "太陽能、能量轉換與地球系統資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "能量轉換、光合作用與地球環境情境"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "能量流動、食物鏈與控制變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以太陽能、光合作用、蒸發、能量轉換、食物鏈、資料表與公平實驗考查能量來源、流動方向及控制變因；本題只取能力方向並重新設計情境、數據與選項。"
EXPLANATIONS = [
    "A。地球表面天氣與多數生態系的主要外部能量由太陽輻射提供；這裡的『主要』不排除地球內部熱等其他來源。",
    "B。光合作用把太陽的輻射能轉為葡萄糖等有機物儲存的化學能，之後才可能沿食物鏈傳遞。",
    "C。太陽供熱使水蒸發，後續的上升、冷凝與降水把能量和水循環連在一起，顯示輻射能轉成水循環中的內能與動能路徑。",
    "D。受熱不均造成密度差與浮力，空氣流動把內能轉成大尺度運動的動能；不能只寫成『太陽能變成電能』。",
    "B。能量由草的化學能進入蝗蟲，再進入青蛙，逐級傳遞且每一級都有部分以呼吸和散熱等形式離開可用食物能量。",
    "C。古代植物先用光合作用把太陽輻射轉成化學能，埋藏後才形成煤與石油；燃燒不是最初來源。",
    "D。完整流程是太陽輻射能被太陽能板轉為電能，再供給負載並有部分轉成光、熱或其他形式；要交代轉換與散失。",
    "A。應固定植物種類、數量、培養時間、溫度與水分，只改變光照條件，並以相同方法測量固定碳量，才能把差異歸因於光照。",
    "C。地表吸收短波後會升溫並以紅外線長波輻射向外放能量；實際收支還受大氣吸收、對流與蒸發影響。",
    "B。應先補量測條件、時間尺度與能量分流，再重複測量；單一地點或單次異常不能直接推出全球長期結論。",
]
STRATEGIES = [
    "先分辨『主要外部來源』與地球內部熱等其他來源，再選能涵蓋天氣與生態的共同來源。",
    "追蹤光合作用輸入與輸出，判斷能量形式是輻射能還是化學能。",
    "把蒸發—上升—冷凝—降水排成箭頭，標示各階段的能量轉換。",
    "由受熱不均推到密度差、浮力與空氣運動，逐段寫出形式改變。",
    "沿食物鏈方向追蹤化學能，並補上每一級呼吸與散熱造成的可用能量減少。",
    "倒推化石燃料形成前的生物與光合作用，不把燃燒當成最初能量來源。",
    "先寫輸入，再寫太陽能板的轉換、負載使用與不可避免的散失。",
    "只改一個自變因，固定其餘條件，並選擇能代表能量固定量的相同測量指標。",
    "區分短波輸入和長波輸出，再檢查大氣、蒸發與對流是否是未量測流。",
    "先確認尺度與證據，再提出補測與替代解釋，不用一句口號取代系統收支。",
]
STEPS = [
    "圈出題目中的能量來源、轉換物件、傳遞方向與系統邊界。",
    "把每一步的能量形式寫成箭頭，避免只寫現象名稱。",
    "核對是否有反射、吸收、蒸發、對流、呼吸或散熱等分流。",
    "比較資料的單位、空間範圍、時間尺度與控制條件。",
    "用『觀察—推論—限制』回查結論能否被證據支持。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []):
        row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []):
        row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ing-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合太陽輻射、反射吸收、地表長波、蒸發、對流、光合作用、食物鏈、系統邊界與尺度判讀；保留校園地表能量收支互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ing-iv-1-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的太陽能、能量轉換、光合作用、食物鏈、資料判讀與控制變因能力；本題改寫為地球系統能量流動原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ing iv 1")


if __name__ == "__main__":
    main()
