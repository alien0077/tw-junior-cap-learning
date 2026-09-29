#!/usr/bin/env python3
"""Record public-school publisher evidence for mathematics algebra performance A."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf", "桃園市立永豐高中國中部公立校方七年級數學課程計畫；南一版代數章節與評量欄位。"),
    ("kanghsuan", "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110", "新北市立大豐國民中學公立校方康軒版數學課程計畫；代數表徵、操作活動與多元評量欄位。"),
    ("hanlin", "https://www.cp.ptc.edu.tw/storage/134513/134513_112_B-1_9A.pdf", "屏東縣公立學校翰林版數學課程計畫；代數概念、解題表徵與情境評量欄位。"),
]
UNITS = [
    ("lesson-math-performance-a", "代數", ["代數符號", "等式與不等式", "推理與證明"], "從文字條件、圖表或數量關係建立代數表達，再以等值變形、反例或回代說明結論。", "把符號運算當成脫離情境的規則，沒有交代變數與結論範圍。"),
    ("lesson-math-performance-a-iv-1", "a-Ⅳ-1：符號文字表達概念運算推理證明", ["符號表達", "文字轉式", "推理證明"], "將定義、數量關係和限制條件寫成符號式，逐步標註每次變形的理由，最後用反例或回代檢查推理。", "只寫算式不說明等值依據，或把一個例子誤當成普遍證明。"),
    ("lesson-math-performance-a-iv-2", "a-Ⅳ-2：一元一次方程", ["等式性質", "未知數", "回代"], "先用題意界定未知數與單位，再利用等式性質隔離未知數，回到原題檢核數值與語意是否一致。", "移項只背變號，未理解兩邊同加減或同乘除的等值操作。"),
    ("lesson-math-performance-a-iv-3", "a-Ⅳ-3：一元一次不等式", ["不等式", "解集", "數線"], "保留不等號方向的條件，處理負數乘除時特別檢查方向，再用數線和原情境界定解集。", "照搬方程式移項規則，負數乘除後忘記反轉不等號。"),
    ("lesson-math-performance-a-iv-4", "a-Ⅳ-4：二元一次聯立", ["聯立方程式", "代入消去", "共同解"], "從兩個條件建立兩式，依係數與未知數選代入或加減消去，取得共同解後同時回代兩式。", "只解出一個變數就停止，或得到數值後沒有確認兩個條件都滿足。"),
    ("lesson-math-performance-a-iv-5", "a-Ⅳ-5：多項式四則與乘法公式", ["多項式", "同類項", "乘法公式"], "先依次數與變數排列，再辨認同類項、分配律與乘法公式，最後以代值或展開反查結果。", "把不同次數的項合併，或套用公式時沒有確認兩項與符號位置。"),
    ("lesson-math-performance-a-iv-6", "a-Ⅳ-6：一元二次方程", ["二次方程", "因式分解", "解的檢核"], "先整理成標準形式，再依可因式分解、配方法或公式選擇策略，列出所有候選解並回代篩選。", "找到一個根就停止，或忽略整理標準式後常數與係數造成的限制。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {item["lessonId"]: item for item in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [{
                "publisher": publisher, "sourceUrl": url,
                "sourceKind": "public-school-course-plan-identifying-publisher-material",
                "locator": f"{locator}；{title}：概念、表徵與評量定位；核讀 2026-09-21。",
                "accessedAt": "2026-09-21", "observedConcepts": [title, *core],
                "observedRepresentations": [representation], "observedAssessment": [assessment],
                "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。",
            } for publisher, url, locator in SOURCES],
            "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"},
        }
    data["units"] = sorted(units.values(), key=lambda item: item["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Eight hundred sixty unit samples", "Eight hundred sixty-seven unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
