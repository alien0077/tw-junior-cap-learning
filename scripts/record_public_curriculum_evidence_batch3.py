#!/usr/bin/env python3
"""Record page-located public-school curriculum evidence without status promotion."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-07"
MATH_URL = "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/909260305.pdf"
SCIENCE_URL = "https://www.cp.ptc.edu.tw/storage/134542/134542_114_C-1_8A.pdf"

MATH_ROWS = {
    "lesson-math-content-a-8-2": ("A-8-2：多項式的意義", "PDF p.1 / extracted lines 44-64; second week 1-1 乘法公式, A-8-2 names polynomial, terms, coefficients, constant term, degree and ascending/descending order; listed assessment includes oral response, discussion, homework, operation and paper test", "由乘法公式轉入多項式詞彙與項次表示，並將符號辨認接到紙筆與口頭說明。", "以項次標記、升降冪排列與文字／符號互換作為表徵；本 lesson 另用原創分類卡與反例。"),
    "lesson-math-content-a-8-3": ("A-8-3：多項式的四則運算", "PDF p.1 / extracted lines 65-84; third week 1-2 and lines 89-108; A-8-3 includes horizontal/vertical addition and subtraction, multiplication up to degree three and division by a quadratic polynomial; listed assessment includes oral response, discussion, homework, operation and paper test", "課程計畫把多項式加減先於乘除，並明列直式、橫式與最高三次乘積的範圍。", "以同類項合併、分配律與直式對齊建立運算表徵；本 lesson 另加符號錯位診斷與自編資料題。"),
    "lesson-math-content-a-8-4": ("A-8-4：因式分解", "PDF p.3 / extracted lines 320-340; chapter 3 precedes chapter 4 and A-8-4 defines factors and factorization of a quadratic polynomial; listed assessment includes oral response, discussion, homework, operation and paper test", "課程計畫把因式分解放在一元二次方程式之前，先建立因式與二次式分解的意義。", "以乘法展開與反向分解互檢，並把等式兩邊的形式轉換連到驗算。"),
    "lesson-math-content-a-8-5": ("A-8-5：因式分解的方法", "PDF p.3 / extracted lines 287-318; A-8-5 is taught through common-factor extraction, multiplication identities and cross multiplication, with a paper test and operation/discussion signals", "公開計畫列出提公因式、乘法公式與十字交乘三種方法，並安排連續週次與紙筆評量。", "以先觀察共同因式、再選公式或十字交乘的決策表呈現方法差異。"),
    "lesson-math-content-a-8-6": ("A-8-6：一元二次方程式的意義", "PDF p.3 / extracted lines 320-340; A-8-6 names the equation, its solution and forming an equation from a concrete situation", "課程計畫把具體情境列式與解的意義放在解法之前，形成建模到驗算的順序。", "以面積或數量情境建立未知數、等式與解的對應，並檢查不合限制的根。"),
    "lesson-math-content-a-8-7": ("A-8-7：一元二次方程式的解法與應用", "PDF p.3-4 / extracted lines 345-429; A-8-7 includes factorization, completing the square, formula solution, applications and calculator approximation, with oral, discussion, homework, operation and paper-test signals", "公開計畫明列三種解法、應用問題與近似值工具，並延伸到第十八、十九週的情境應用。", "以方法選擇、根的限制與代回驗算組織多步解題，而不把公式代入當成唯一理解。"),
}

def add_version_record(lesson: dict, publisher: str, edition: str, url: str, locator: str, concepts: list[str], representation: str, evidence: str) -> None:
    marker = f"{url}；{locator}"
    if any(r.get("sourceLocator") == marker for r in lesson.get("versionResearch", [])):
        return
    lesson.setdefault("versionResearch", []).append({"publisher": publisher, "edition": edition, "sourceType": "public-web", "sourceLocator": marker, "reviewedAt": DATE, "findings": {"concepts": concepts, "representations": [representation], "examplesOrEvidence": [evidence], "misconceptions": ["課程計畫只支持範圍與教學活動定位，不能替代完整教材內容或逐題答案核對。"], "assessmentEmphasis": ["公開計畫列出的口頭、討論、操作、作業與紙筆評量被記為評量線索，不被宣稱為出版社題目。"]}, "licenseBoundary": "僅記錄公立學校公開課程計畫的頁碼、概念與活動定位；不複製教材、學習單、題目、答案、圖片或版面，lesson 維持 draft。"})

def main() -> None:
    changed = []
    for lesson_id, (title, locator, concept, representation) in MATH_ROWS.items():
        path = next((ROOT / "lessons/math").glob(f"{lesson_id}.json"))
        data = json.loads(path.read_text(encoding="utf-8"))
        add_version_record(data, "nani", "南一版八年級數學公開校方課程計畫交叉證據", MATH_URL, locator, [concept, "計畫同時列出單元週次、學習表現、學習內容與評量方式。"], representation, "卓蘭高中附設國中公開計畫標示南一版教科書、教師手冊、學習單與紙筆／操作評量；本課內容仍完全自編。")
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append({"lessonId": lesson_id, "sourceUrl": MATH_URL, "locator": locator})

    path = ROOT / "lessons/science/lesson-science-content-bc-iv-4.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    add_version_record(data, "kanghsuan", "屏東縣公立學校八年級校本自然課程計畫交叉證據", SCIENCE_URL, "PDF p.9 / extracted lines 353-370; Bc-Ⅳ-2 respiration, Bc-Ⅳ-3 photosynthesis, Bc-Ⅳ-4 factors and inquiry; performance emphasizes planned observation, safe operation, qualitative observation and numerical measurement", ["Bc-Ⅳ-4 明列日光、二氧化碳與水分等因素可透過探究實驗驗證。", "同頁把光合作用與呼吸作用的能量轉換並列，提供概念邊界。"], "以校園觀察、採樣、實作與量測紀錄把生命概念連到可驗證的探究流程。", "公開計畫列有觀察、採樣、實作、數值量測與小組發表；本 lesson 改寫為原創變因控制與證據判讀，不重製活動文字。")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    changed.append({"lessonId": data["id"], "sourceUrl": SCIENCE_URL, "locator": "PDF p.9 / extracted lines 353-370"})

    report = {"updatedAt": DATE, "scope": "three lesson-level public-school curriculum evidence records; no global publisher status promotion", "changedLessons": changed, "sourceBoundary": "School course plans identify scope, sequence, representations and assessment signals only. They do not prove access to full publisher chapters and do not authorize reproduction.", "status": "chapter-level-recorded-pending-fusion-review"}
    out = ROOT / "implementation/reports/public-curriculum-evidence-batch3.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"changedLessons": len(changed), "status": report["status"], "report": str(out)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
