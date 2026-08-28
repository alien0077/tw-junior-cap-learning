"""替換數學學習表現總分類的泛用題，改為可觀察的數學推理與表徵任務。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/815/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E6%95%B8%E5%AD%B8%E9%A0%98%E5%9F%9F.pdf"

ITEMS = [
    ("解方程式 3x−7=11，x 的值為何？", ["6", "4", "9", "−6"], "A", "兩邊先加 7 得 3x=18，再除以 3 得 x=6。", "easy", "一元一次方程式的解題與驗算"),
    ("某校調查 40 位學生，其中 14 位騎腳踏車到校。若以此樣本估計比例，最簡分數為何？", ["7/20", "14/30", "3/10", "7/10"], "A", "比例為 14/40，約分除以 2 得 7/20。", "easy", "比例表徵與化簡"),
    ("直角三角形兩股長為 5 公分與 12 公分，斜邊長為何？", ["13 公分", "17 公分", "60 公分", "169 公分"], "A", "由畢氏定理，斜邊平方=5²+12²=169，所以斜邊為 13 公分。", "medium", "幾何關係與推理"),
    ("資料 2、4、7、7、10 的中位數與平均數分別為何？", ["7 與 6", "6 與 7", "7 與 7", "6 與 6"], "A", "排序後中央值為 7；總和 30 除以 5 得平均數 6。", "easy", "統計量計算與解讀"),
    ("擲一枚公平骰子一次，出現大於 4 的點數，其機率為何？", ["1/3", "1/2", "1/6", "2/3"], "A", "大於 4 的結果是 5、6，共 2 種；機率為 2/6=1/3。", "easy", "古典機率計算"),
    ("若函數 y=2x−3，當 x=4 時 y 為何？", ["5", "8", "11", "−5"], "A", "代入 x=4：y=2×4−3=5。", "easy", "函數代入與表示"),
    ("多項式 x²+7x+12 因式分解後為何？", ["(x+3)(x+4)", "(x+2)(x+6)", "(x−3)(x−4)", "(x+1)(x+12)"], "A", "尋找乘積 12 且和為 7 的兩數 3、4，因此為 (x+3)(x+4)。", "medium", "代數式結構與驗算"),
    ("等差數列 3、8、13、18、… 的第 12 項為何？", ["58", "63", "60", "55"], "A", "首項 3、公差 5；第 12 項=3+(12−1)×5=58。", "medium", "數列規律與一般項"),
    ("若 4 本筆記本共 120 元，單價相同，買 7 本需多少元？", ["210 元", "180 元", "280 元", "840 元"], "A", "每本 120÷4=30 元，7 本為 30×7=210 元。", "easy", "比例關係與解題表徵"),
    ("不等式 2x+1<9 的解為何？", ["x<4", "x>4", "x<5", "x>5"], "A", "兩邊減 1 得 2x<8，再除以正數 2，得到 x<4。", "medium", "不等式推理與符號方向"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "math" / f"question-math-learning-performance-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        options = options[shift:] + options[:shift]
        answer = chr(65 + ((4 - shift) % 4))
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(options)]
        data["difficulty"] = difficulty
        data["answer"] = {"value": answer, "explanation": explanation}
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科試題卷；研究數學解題、表徵與推理能力方向（{locator}）；另以官方數學課綱核對範圍（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, figures, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
