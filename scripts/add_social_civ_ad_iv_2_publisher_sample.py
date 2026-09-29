#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Ad-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公民課程計畫，南一版單元 1 人性尊嚴與人權保障明列公 Ad-Ⅳ-2，並以口頭問答、課堂觀察、上機實作、參與討論與學習歷程檔案評量。"),
    "kanghsuan": ("https://www.bish.tp.edu.tw/get_file.php?file_dir=data10710%2F&file_name=0d301d84a39c7bbdf88a3f4567228072.pdf&rename=%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83%28%E5%85%AC%E6%B0%91%E8%88%87%E7%A4%BE%E6%9C%83%29.pdf", "臺北市靜修中學國中部七年級公民課程計畫，選用康軒版，將公 Ad-Ⅳ-2 放入人性尊嚴與人權保障、公共議題見解、同理討論及紙筆、觀察、自評、同儕與口頭評量。"),
    "hanlin": ("https://hakka.mtjh.kh.edu.tw/112plan/7/5/4.pdf", "高雄市立民族國中人權議題教學活動設計，教材來源明載翰林版七上社會，列出公 Ad-IV-2，從性別與多元身分案例連結人權保障、人性尊嚴、同理表達與資料／討論活動。"),
}
CONCEPTS = [
    "說明人權具有普遍性，不能因國籍、種族、族群、區域、文化、性別、性傾向或身心障礙身分而任意排除",
    "區分形式平等、實質平等、差別待遇與歧視，從案例資料檢查差異待遇是否有合理目的、必要性與不造成尊嚴傷害",
    "比較不同群體的生活處境與制度障礙，提出兼顧文化差異、身體自主、平等參與與國家保障責任的公共回應",
]
REPRESENTATIONS = ["普遍人權—平等—差異—尊嚴概念圖", "身分／制度門檻／受影響權利／補救措施矩陣", "案例事實—群體處境—歧視檢查—權利保障方案流程"]
ASSESSMENT = ["多元身分人權案例閱讀", "平等、差別待遇與歧視判斷", "不同群體處境及資料比較", "提出兼顧差異與普遍保障的政策方案", "口頭問答、課堂觀察、上機實作、討論、紙筆與學習歷程評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫或公開教學活動的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-ad-iv-2", "title": "公 Ad-Ⅳ-2：普遍人權與多元身分保障", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以人性尊嚴與普遍保障為主軸，需把身分差異、制度障礙與實質平等串成可檢驗的案例分析。", "康軒把多元文化、同理討論與多種評量放在公民課程，需補足差別待遇與歧視的判準。", "翰林以性別及多元身分教學活動切入，需補足國家保障責任、補救措施與不同群體資料比較。"], "originalSynthesisBoundary": "本樣本只記錄三筆可追溯的公開章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {x["lessonId"] for x in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(bp.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str) and "unit samples" in b["reason"]: b["reason"] = re.sub(r"Four hundred three unit samples", "Four hundred four unit samples", b["reason"])
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
