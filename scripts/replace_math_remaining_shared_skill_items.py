#!/usr/bin/env python3
"""Replace the last repeated-looking mathematics skill drills with contexts."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ITEMS = {
    "question-math-content-n-7-2-1.json": ("一個長方形花圃的面積為 72 平方公尺。72 的標準質因數分解式為何？", ["2²×3²", "2×3³", "2³×3", "3²×4"], "A", "72＝2×2×2×3×3，因此標準質因數分解式為 2²×3²。"),
    "question-math-content-n-7-1-3.json": ("84 張貼紙要平均分裝，先將 84 作標準質因數分解，結果為何？", ["2²×3×7", "2×3²×7", "2²×3²", "2×42"], "A", "84＝2×2×3×7，因此為 2²×3×7。"),
    "question-math-content-n-7-2-5.json": ("某批零件有 48 個。將 48 作標準質因數分解，哪一項正確？", ["2⁴×3", "2³×3²", "2²×3×4", "2×24"], "A", "48＝2×2×2×2×3，因此為 2⁴×3。"),
    "question-math-content-n-7-2-9.json": ("105 位參加者要依質因數規劃分組。105 的標準質因數分解式為何？", ["3×5×7", "3×5²×7", "2×3×5×7", "5×21"], "A", "105＝3×5×7，三個因數都是質數。"),
    "question-math-content-n-7-2-3.json": ("一個數字鎖的密碼提示是 90。90 的標準質因數分解式為何？", ["2×3²×5", "2²×3×5", "2×3×15", "9×10"], "A", "90＝2×3×3×5，因此為 2×3²×5。"),
    "question-math-content-n-7-2-2.json": ("180 顆螺帽要依質因數檢查包裝數量。180 的標準質因數分解式為何？", ["2²×3²×5", "2×3²×5²", "2³×3×5", "2²×3×15"], "A", "180＝2×2×3×3×5，因此為 2²×3²×5。"),
    "question-math-content-d-1.json": ("四天的借閱量分別為 8、12、15、5 本，平均每天借閱幾本？", ["10 本", "9 本", "11 本", "12 本"], "A", "總數 40 除以 4，平均為 10 本。"),
    "question-math-content-d-7-1-4.json": ("四次測量值為 12、18、15、9 公分，平均值為何？", ["13.5 公分", "14 公分", "12.5 公分", "15 公分"], "A", "總和為 54，54÷4＝13.5。"),
    "question-math-content-d-7-2-1.json": ("四位同學步行距離為 4、6、8、10 百公尺，平均距離為何？", ["7 百公尺", "6 百公尺", "8 百公尺", "9 百公尺"], "A", "總和 28 除以 4，平均為 7 百公尺。"),
    "question-math-content-d-7-2-5.json": ("四天回收量為 6、8、10、12 公斤，平均每天回收量為何？", ["9 公斤", "8 公斤", "10 公斤", "11 公斤"], "A", "總和 36 除以 4，平均為 9 公斤。"),
    "question-math-content-n-8-4-5.json": ("劇場座位號碼每排比前一排多 4 號：6、10、14、18、……，第 12 項為何？", ["50", "46", "54", "48"], "A", "第 12 項為 6＋(12−1)×4＝50。"),
    "question-math-learning-content-9.json": ("階梯高度記錄形成 5、9、13、17、……的等差數列，第 20 項為何？", ["81", "77", "85", "80"], "A", "首項 5、公差 4，第 20 項為 5＋19×4＝81。"),
    "question-math-learning-performance-8.json": ("某儲水槽每日增加 5 公升，累計量形成 3、8、13、18、……，第 12 項為何？", ["58", "53", "63", "60"], "A", "首項 3、公差 5，第 12 項為 3＋11×5＝58。"),
    "question-math-content-d-9-1-1.json": ("五次觀測值排序後為 3、5、7、9、11，代表中間位置的中位數為何？", ["7", "5", "9", "6"], "A", "五筆資料已排序，中間第 3 筆是 7。"),
    "question-math-content-d-7-2-2.json": ("五位選手成績為 3、5、7、9、12 分，中位數為何？", ["7", "5", "9", "8"], "A", "五筆資料已排序，中間第 3 筆是 7。"),
    "question-math-content-d-2.json": ("五天降雨量為 4、6、9、11、15 毫米，中位數為何？", ["9 毫米", "6 毫米", "11 毫米", "8 毫米"], "A", "五筆資料已排序，中間第 3 筆是 9 毫米。"),
    "question-math-content-n-8-3-7.json": ("圖形拼排數量依序為 1、4、9、16、……，若規律為平方數，第 6 項為何？", ["36", "25", "30", "49"], "A", "第 n 項為 n²，因此第 6 項是 6²＝36。"),
    "question-math-content-n-8-3-2.json": ("細菌數量模型依序為 2、4、8、16、……，每次乘以 2，第 5 項為何？", ["32", "24", "30", "64"], "A", "每項是前一項的 2 倍，第 5 項為 16×2＝32。"),
    "question-math-performance-n-iv-7-9.json": ("燈串每一段數量依序為 3、6、12、24、……，若每次加倍，第 6 項為何？", ["96", "72", "84", "192"], "A", "第 5 項為 48，第 6 項為 48×2＝96。"),
    "question-math-performance-n-iv-6-3.json": ("正方形面積為 80 平方公分時，邊長 √80 介於哪兩個連續整數之間？", ["8 與 9", "7 與 8", "9 與 10", "10 與 11"], "A", "因為 8²＝64＜80＜81＝9²，所以 √80 介於 8 與 9。"),
    "question-math-performance-n-5.json": ("某正方形面積為 50 平方公分，邊長 √50 介於哪兩個連續整數之間？", ["7 與 8", "6 與 7", "8 與 9", "5 與 6"], "A", "因為 7²＝49＜50＜64＝8²，所以 √50 介於 7 與 8。"),
    "question-math-performance-n-iv-5-1.json": ("正方形面積為 121 平方公分時，邊長 √121 為何？", ["11", "10", "12", "121"], "A", "11²＝121，因此 √121＝11。"),
    "question-math-content-n-8-1-1.json": ("一個正方形面積為 49 平方公分，若取正邊長，√49 為何？", ["7", "6", "8", "49"], "A", "7²＝49，因此算術平方根 √49＝7。"),
    "question-math-content-n-8-1-9.json": ("正方形地磚面積為 81 平方公分，邊長 √81 為何？", ["9", "8", "10", "81"], "A", "9²＝81，因此 √81＝9。"),
}


def main() -> None:
    changed = 0
    for filename, (prompt, options, answer, explanation) in ITEMS.items():
        path = ROOT / "questions" / "math" / filename
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)]
        data["answer"] = {"value": answer, "explanation": explanation}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-29"
        data.setdefault("provenance", {})["authoringNote"] = (
            "依官方課綱數學能力與公開會考／公立國中試題的能力方向獨立編寫；"
            "未複製原題文字、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"
        )
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    print(f"replaced {changed} remaining shared-skill mathematics questions")


if __name__ == "__main__":
    main()
