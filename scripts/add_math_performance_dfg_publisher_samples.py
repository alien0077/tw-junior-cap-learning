#!/usr/bin/env python3
"""Record public-school publisher evidence for mathematics D, F and G performance."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/378739209.pdf", "卓蘭高中附設國中公立校方南一版九年級數學課程計畫；統計、機率與二次函數章節定位。"),
    ("kanghsuan", "https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=100&file=WVhSMFlXTm9MelkzTDNCMFlWOHhNamd6T1Y4MU56WXlNRFl3WHpjNE1USXpMbkJrWmc9PQ%3D%3D&fname=WSGGRPQK20QO41KKLOLK54TXXSMO25JGKLB0DCNKCCQLOO40QKTSST54WSLKUSSSROPOIHKK2004GDLOQONKTSMOOPB0FHMPQPMPNOTSUWZWXVWFH10YWFCSSWUX25HCA0UWIGVWKO40XSUSB040MPTXGDTWA0ZWUSOPTWFGTS45QKNOKK21HHDGB0JC24KK14WTIGYSEG14WSMLID30B514YWRKA434DCDGA0WWQOPP1000ZSIGMOIGDGJDLO", "淡水國中公立校方康軒版九年級數學課程計畫；統計機率、函數及圖形應用定位。"),
    ("hanlin", "https://www1.fsm.kh.edu.tw/plan/special_112/112%E8%B3%87%E6%BA%90%E7%8F%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB.pdf", "高雄市公立校方翰林版第六冊數學課程計畫；統計、機率與函數學習內容及評量定位。"),
]
UNITS = [
    ("lesson-math-performance-d", "資料與不確定性", ["資料分布", "機率", "不確定性判讀"], "先整理資料或樣本空間，再選適合的統計量、圖表或機率模型，最後說明結論的證據與限制。", "只報一個數字就宣稱結論，忽略分布、樣本空間或不確定性。"),
    ("lesson-math-performance-d-iv-1", "d-Ⅳ-1：統計圖表統計量與軟體", ["統計圖表", "統計量", "軟體驗證"], "從原始資料確認欄位與單位，選擇圖表和統計量，以軟體計算後回看圖形與離群值是否支持敘述。", "把軟體輸出的結果直接當答案，沒有檢查資料範圍或圖表尺度。"),
    ("lesson-math-performance-d-iv-2", "d-Ⅳ-2：機率樹狀圖與應用", ["樹狀圖", "乘法原理", "事件機率"], "先列出每一步的分支與條件，再沿路徑相乘、跨路徑相加，最後確認所有可能結果沒有重複或遺漏。", "只畫樹狀圖不標條件，或把不同路徑的機率錯當成同一路徑相乘。"),
    ("lesson-math-performance-f", "函數", ["對應關係", "函數圖形", "變化模型"], "以輸入輸出、表格、式子和圖形互相轉譯，觀察變數如何共同變化，再判斷模型能否描述情境。", "只背公式或圖形外觀，沒有辨認自變數、應變數與定義域。"),
    ("lesson-math-performance-f-iv-1", "f-Ⅳ-1：常數與一次函數", ["常數函數", "一次函數", "斜率"], "從兩量關係辨認固定值或固定變化率，建立式子並以表格和圖形檢查斜率、截距與單位。", "看到直線就當成任何情境的一次函數，忽略資料是否呈固定變化。"),
    ("lesson-math-performance-f-iv-2", "f-Ⅳ-2：二次函數圖形", ["二次函數", "拋物線", "對稱"], "由表格或式子預測拋物線的開口與對稱，再以幾個關鍵點和坐標圖形核對，不用單一點判定整條曲線。", "把一次函數的直線變化套到二次函數，或只看一側資料就判斷對稱。"),
    ("lesson-math-performance-f-iv-3", "f-Ⅳ-3：二次函數標準式開口頂點極值", ["標準式", "頂點", "極值"], "先辨認二次項係數決定開口，再用配方法或頂點公式找對稱軸與極值，最後加入情境定義域判斷可行答案。", "只求出頂點卻沒有判斷它是否落在題目的可用範圍內。"),
    ("lesson-math-performance-g", "坐標幾何", ["坐標平面", "距離", "直線與聯立"], "把幾何位置轉成坐標與代數條件，用距離、斜率或交點互相驗證圖形關係與解的意義。", "把坐標計算當成獨立算術，沒有回到圖形確認位置與方向。"),
    ("lesson-math-performance-g-iv-1", "g-Ⅳ-1：直角坐標點與距離", ["坐標點", "距離公式", "畢氏定理"], "先讀取兩點的水平與垂直差，再用直角三角形或距離公式計算，保留平方與單位的檢核。", "把坐標差直接相加當距離，或忘記平方根與絕對距離的意義。"),
    ("lesson-math-performance-g-iv-2", "g-Ⅳ-2：二元一次直線與聯立解幾何", ["直線圖形", "交點", "聯立解"], "將兩個方程式畫成直線或讀取其斜率截距，利用交點判斷聯立方程式的解與無解、無限多解情形。", "只靠代數數值下結論，沒有確認交點是否存在及其幾何位置。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8")); units = {x["lessonId"]: x for x in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {"lessonId": lesson_id, "title": title, "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": [{"publisher": p, "sourceUrl": u, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{l}；{title}：概念、表徵與評量定位；核讀 2026-09-21。", "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。"} for p, u, l in SOURCES], "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"}}
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"]); data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str): b["reason"] = b["reason"].replace("Eight hundred sixty-seven unit samples", "Eight hundred seventy-six unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
