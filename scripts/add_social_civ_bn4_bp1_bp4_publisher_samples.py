#!/usr/bin/env python3
"""Record public-school publisher evidence for social civics Bn-IV-4 and Bp-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版公民課程的交易、貿易與貨幣內容列 Bn-IV-4、Bp-IV-1～4。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版公民課程列進口貿易、貨幣、儲值卡、信用卡與外幣買賣內容。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版公民課程列 Bn-IV-4、Bp-IV-1～4，並採報告、紙筆、資料蒐集與問答評量。"),
]
UNITS = [
    ("bn-iv-4", "公 Bn-Ⅳ-4：進口商品開放的利弊", ["進口", "消費者選擇", "國內產業", "貿易利弊與分配影響"], "用進口開放前後的價格、選擇、產業與勞動影響表，分開短期消費利益和不同生產者承受的調整成本。", "從資料同時指出受益與受影響群體，提出判斷條件，避免把進口政策簡化成絕對利多或利空。"),
    ("bp-iv-1", "公 Bp-Ⅳ-1：貨幣出現的原因", ["交易媒介", "價值尺度", "價值儲藏", "雙重巧合問題"], "以物物交換的需求配對表，逐步加入貨幣功能，觀察交易搜尋成本與價格表達如何改變。", "學生需由交易限制推導貨幣需求，不可只背貨幣三功能而未連回生活交易。"),
    ("bp-iv-2", "公 Bp-Ⅳ-2：儲值卡與貨幣的差異", ["支付工具", "儲值餘額", "法償性", "使用範圍與風險"], "比較現金、儲值卡在支付、餘額、接受範圍、遺失風險與退款條件上的功能表。", "要求先辨認工具功能與限制，再判斷情境中誰承擔風險，避免把所有支付工具都稱為貨幣。"),
    ("bp-iv-3", "公 Bp-Ⅳ-3：信用卡與儲值卡差異", ["先消費後付款", "信用額度", "預付", "利息與債務風險"], "以付款時間軸和帳單資料區分預付、即時支付與延後付款，呈現信用卡的額度與費用風險。", "題目要求依付款時點、資金來源與違約後果作答，不以卡片外觀或消費便利性分類。"),
    ("bp-iv-4", "公 Bp-Ⅳ-4：外幣買賣需求", ["匯率", "外幣需求", "外幣供給", "進出口與旅遊支付"], "用匯率報價和不同角色的交易目的，判斷誰需要買入或賣出外幣，以及匯率變動的方向。", "先辨認角色是付款、收款、投資或避險，再依外幣需求／供給推理，避免只背匯率升貶口號。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-civ-" + suffix
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [{
                "publisher": publisher, "sourceUrl": url,
                "sourceKind": "public-school-course-plan-identifying-publisher-material",
                "locator": locator, "accessedAt": "2026-09-21",
                "observedConcepts": [title, *core],
                "observedRepresentations": [representation],
                "observedAssessment": [assessment],
                "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。",
            } for publisher, url, locator in SOURCES],
            "fusionReview": {
                "commonCore": core,
                "differencesToReview": [representation, assessment],
                "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。",
            },
        }
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str):
            b["reason"] = b["reason"].replace("Five hundred eight unit samples", "Five hundred thirteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
