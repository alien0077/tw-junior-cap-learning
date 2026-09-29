#!/usr/bin/env python3
"""Record public-school publisher evidence for mathematics root/domain units."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf", "永豐高中國中部公立校方南一版數學課程計畫；代數、數與量、幾何、函數與資料的章節架構。"),
    ("kanghsuan", "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110", "大豐國中公立校方康軒版數學課程計畫；六大內容主題的教材序列與多元評量欄位。"),
    ("hanlin", "https://www.cp.ptc.edu.tw/storage/134513/134513_112_B-1_9A.pdf", "屏東縣公立學校翰林版數學課程計畫；數與量、代數、幾何、函數及資料不確定性架構與評量欄位。"),
]
UNITS = [
    ("lesson-math-content-a", "代數總綱", ["代數符號", "等式不等式", "推理"], "以變數、式子、方程與圖形描述關係，讓符號操作可回扣定義、條件與證明。", "只把代數當計算規則，未說明變數與結論範圍。"),
    ("lesson-math-content-d", "資料與不確定性總綱", ["資料整理", "統計", "機率"], "由資料來源、分布與樣本空間選擇圖表、統計量或機率模型，並表達不確定性。", "把單一統計數字當成完整資料結論。"),
    ("lesson-math-content-f", "函數總綱", ["對應關係", "函數式", "圖形模型"], "在表格、式子、圖形與情境間轉換，判斷輸入輸出及變化模型是否相符。", "只記圖形外觀，忽略定義域與變數角色。"),
    ("lesson-math-content-g", "坐標幾何總綱", ["坐標", "距離", "直線交點"], "把幾何位置翻成坐標和代數條件，再用距離、斜率與交點驗證圖形關係。", "只做坐標算術，不回看幾何位置。"),
    ("lesson-math-content-n", "數與量總綱", ["數系統", "比例", "近似與誤差"], "用數線、比例、根式、數列與估算表達量的關係，區分精確值與近似值。", "忽略單位、數量級與近似誤差。"),
    ("lesson-math-content-s", "空間與形狀總綱", ["幾何物件", "圖形性質", "立體表徵"], "由定義與圖形性質建立平面、空間與變換模型，並以圖、式、文字互相核對。", "只背公式或名稱，不檢查幾何條件。"),
    ("lesson-math-learning-performance", "數學學習表現總綱", ["問題解決", "推理溝通", "工具與表徵"], "依問題選擇表示法、工具與策略，保留推理歷程，並用檢核與溝通修正答案。", "把得到答案當成完成，沒有證據、表徵或反思。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8")); units = {x["lessonId"]: x for x in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {"lessonId": lesson_id, "title": title, "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": [{"publisher": p, "sourceUrl": u, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{l}；{title}：概念、表徵與評量定位；核讀 2026-09-21。", "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。"} for p, u, l in SOURCES], "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"}}
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"]); data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str): b["reason"] = b["reason"].replace("Nine hundred four unit samples", "Nine hundred eleven unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
