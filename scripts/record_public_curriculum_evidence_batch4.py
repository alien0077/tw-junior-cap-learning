#!/usr/bin/env python3
"""Record page-located public-school curriculum evidence for grade 7 math."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-07"
URL = "https://www.nkjh.tyc.edu.tw/sites/default/files/2021-04/%E2%97%8F6-2-3%E6%95%B8%E5%AD%B8.pdf"

ROWS = {
    "lesson-math-content-a-7-1": ("A-7-1：代數符號", "PDF p.1 lines 59-60", "以代數符號表徵交換律、分配律、結合律，並處理一次式化簡、同類項與生活情境記錄。"),
    "lesson-math-content-a-7-2": ("A-7-2：一元一次方程式的意義", "PDF p.1 lines 61-62", "從具體情境列出一元一次方程式，並區分方程式與其解。"),
    "lesson-math-content-a-7-3": ("A-7-3：一元一次方程式的解法與應用", "PDF p.1 lines 63-64", "課程計畫明列等量公理、移項、驗算與應用問題，形成解題順序。"),
    "lesson-math-content-n-7-1": ("N-7-1：100 以內的質數", "PDF p.1 lines 65-65", "以質數、合數定義與篩法作為可操作的判別活動。"),
    "lesson-math-content-n-7-2": ("N-7-2：質因數分解的標準分解式", "PDF p.1 lines 66-67", "由質因數分解連到因數與倍數問題，而非只背分解格式。"),
    "lesson-math-content-n-7-3": ("N-7-3：負數與四則混合運算", "PDF p.1 lines 68-69", "用正負表徵生活量，再進入含分數、小數的四則混合運算。"),
    "lesson-math-content-n-7-4": ("N-7-4：數的運算規律", "PDF p.1 lines 70-71", "以交換、結合、分配律及負號分配式整理運算規律。"),
    "lesson-math-content-n-7-5": ("N-7-5：數線", "PDF p.1 lines 72-75", "在含負數數線上比較大小、理解絕對值，並以兩點差的絕對值表距離。"),
    "lesson-math-content-n-7-6": ("N-7-6：指數的意義", "PDF p.1 lines 76-77", "從非負整數次方、零次方與同底數比較建立指數表徵。"),
    "lesson-math-content-n-7-7": ("N-7-7：指數律", "PDF p.1 lines 78-81", "以數字例呈現同底數乘除、冪的冪及乘積的冪，並標出指數條件。"),
    "lesson-math-content-n-7-8": ("N-7-8：科學記號", "PDF p.2 lines 82-83", "用科學記號表達很大或很小的正數，並連到大小比較。"),
    "lesson-math-content-s-7-1": ("S-7-1：簡單圖形與幾何符號", "PDF p.2 lines 84-85", "以點、線、線段、射線、角、三角形及其符號建立幾何語言。"),
    "lesson-math-content-s-7-2": ("S-7-2：三視圖", "PDF p.2 lines 86-87", "限制在 3×3×3 正方體堆疊且不挖空，讓視圖判讀具有明確邊界。"),
    "lesson-math-content-s-7-3": ("S-7-3：垂直", "PDF p.2 lines 88-88", "連結垂直符號、中垂線與點到直線距離的意義。"),
    "lesson-math-content-s-7-4": ("S-7-4：線對稱的性質", "PDF p.2 lines 89-90", "比較對稱線段、角與對稱點連線，辨認垂直平分關係。"),
    "lesson-math-content-s-7-5": ("S-7-5：線對稱的基本圖形", "PDF p.2 lines 91-91", "以等腰三角形、正方形、菱形、箏形及正多邊形觀察對稱軸。"),
    "lesson-math-content-a-7-4": ("A-7-4：二元一次聯立方程式的意義", "PDF p.6 lines 271-273", "由具體情境列出二元一次方程式與聯立方程式，並解釋解的意義。"),
    "lesson-math-content-a-7-5": ("A-7-5：二元一次聯立方程式的解法與應用", "PDF p.6 lines 274-275", "並列代入消去法、加減消去法與應用問題，支援方法比較。"),
    "lesson-math-content-a-7-6": ("A-7-6：二元一次聯立方程式的幾何意義", "PDF p.6 lines 276-278", "把方程式視為直線圖形，聚焦兩直線相交且只有一個交點的情況。"),
    "lesson-math-content-a-7-7": ("A-7-7：一元一次不等式的意義", "PDF p.6 lines 279-280", "從具體情境列出不等式，將不等號與範圍語言連結。"),
    "lesson-math-content-a-7-8": ("A-7-8：一元一次不等式的解與應用", "PDF p.6 lines 281-282", "在數線標示解集並處理應用問題，明確要求範圍表徵。"),
    "lesson-math-content-d-7-1": ("D-7-1：統計圖表", "PDF p.6 lines 283-285", "由生活數據整理直方圖、長條圖、圓形圖、折線圖與列聯表，必要時用工具輔助。"),
    "lesson-math-content-d-7-2": ("D-7-2：統計數據", "PDF p.6 lines 286-287", "比較平均數、中位數與眾數，並以計算機的統計功能支援較長資料。"),
    "lesson-math-content-g-7-1": ("G-7-1：平面直角坐標系", "PDF p.6 lines 288-289", "用坐標系、方位與距離標定位置，並熟悉橫軸、縱軸與象限。"),
    "lesson-math-content-n-7-9": ("N-7-9：比與比例式", "PDF p.6 lines 290-291", "從比、比例式、正比與反比的基本運算進入生活應用，並要求情境有意義。"),
}

def main() -> None:
    changed = []
    for lesson_id, (title, locator, concept) in ROWS.items():
        path = ROOT / "lessons/math" / f"{lesson_id}.json"
        if not path.exists():
            raise FileNotFoundError(path)
        data = json.loads(path.read_text(encoding="utf-8"))
        marker = f"{URL}；{locator}"
        existing = next((row for row in data.get("versionResearch", []) if row.get("sourceLocator") == marker), None)
        if existing is not None:
            concepts = existing.setdefault("findings", {}).setdefault("concepts", [])
            if concepts:
                concepts[0] = f"{title} 的學習範圍與課程定位"
            else:
                concepts.append(f"{title} 的學習範圍與課程定位")
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        else:
            data.setdefault("versionResearch", []).append({
                "publisher": "hanlin",
                "edition": "翰林版國中數學七年級公開校方課程計畫交叉證據",
                "sourceType": "public-web",
                "sourceLocator": marker,
                "reviewedAt": DATE,
                "findings": {
                    "concepts": [f"{title} 的學習範圍與課程定位", concept, "此為學校課程計畫的範圍與順序證據，不等同完整出版社章節。"],
                    "representations": ["依單元的符號、圖形、數線、資料表徵或情境列式進行原創融合。"],
                    "examplesOrEvidence": ["南崁國中公開課程計畫列出學習內容、目標、評量與教材資源；本 lesson 不複製其教材或題目。"],
                    "misconceptions": ["公開課程計畫不能單獨證明學生已理解，也不能替代本單元的內容審查。"],
                    "assessmentEmphasis": ["計畫列出的紙筆、小組討論、口頭回答與作業僅作為評量線索。"],
                },
                "licenseBoundary": "僅保存公立學校公開課程計畫的 URL、頁碼與概念定位；不複製出版社教材、學習單、題目、答案、圖片或版面，lesson 維持 draft。",
            })
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append({"lessonId": lesson_id, "sourceUrl": URL, "locator": locator})
    report = {
        "updatedAt": DATE,
        "scope": "七年級數學 25 個 lesson-level public-school curriculum evidence records; no publisher status promotion",
        "changedLessons": changed,
        "sourceBoundary": "南崁國中課程計畫明列翰林版七上教材與七年級學習內容；本批只使用可追溯的課綱範圍、順序與評量線索，未複製教材或試題。",
        "status": "chapter-level-recorded-pending-fusion-review",
    }
    out = ROOT / "implementation/reports/public-curriculum-evidence-batch4.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"changedLessons": len(changed), "status": report["status"], "report": str(out)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
