"""替換因式分解舊重複題組，保留 ID 並改為不同能力情境的原創題。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
AUTHORING = "參考公立國中公開段考與國中教育會考的代數式判讀能力方向，以全新數值、情境、選項與解析獨立改寫；未重製原題文字、圖表、選項或答案；待第二輪 AI／Terra 內容複核。"

ITEMS = [
    ("一個長方形的面積表示為 6x²＋9x，若其中一邊為 3x，另一邊可表示為何？", ["2x＋3", "2x＋9", "3x＋3", "6x＋3"], "A", "將 6x²＋9x 除以 3x，兩項分別得到 2x 與 3，因此另一邊是 2x＋3。", "medium"),
    ("18a²b－12ab² 的最大公因式為何？", ["6ab", "6a", "3ab²", "12ab"], "A", "18 與 12 的最大公因數是 6，兩項共同含有 a、b，所以最大公因式為 6ab。", "medium"),
    ("小安把 4x²－10x 寫成 2x(2x－5)。下列哪項可用來驗證這一步？", ["將括號展開後應得到 4x²－10x", "只檢查括號內兩項係數相加", "把 2x 改成 2", "確認答案看起來最簡短"], "A", "用分配律展開 2x(2x－5)，得到 4x²－10x，即可確認因式分解正確。", "easy"),
    ("完成等式 −3y(2y－7)＝−6y²＋＿＿，空格應填入什麼？", ["21y", "−21y", "14y", "−14y"], "A", "−3y 乘以 −7 得 21y，所以展開式為 −6y²＋21y。", "medium"),
    ("若 5m²＋15m＝5m(m＋3)，代入 m＝2 後，原式的值為何？", ["50", "70", "80", "100"], "A", "代入因式分解後的式子：5×2×(2＋3)＝50，所以原式的值為 50。", "medium"),
    ("將 −8p²＋12p 因式分解，哪一項正確？", ["−4p(2p－3)", "−4p(2p＋3)", "−4(2p²－3p)", "−2p(4p＋6)"], "A", "提出 −4p 後，−8p²÷(−4p)＝2p，12p÷(−4p)＝−3，因此為 −4p(2p−3)。", "hard"),
    ("下列哪一項是 7r(3r－2) 展開後的結果？", ["21r²－14r", "21r²－2r", "10r²−14r", "21r−14"], "A", "依分配律，7r×3r＝21r²，7r×(−2)＝−14r。", "easy"),
    ("若 12u³v＋8u²v²＝4u²v(3u＋2v)，下列哪個等式可檢查括號內第一項？", ["4u²v×3u＝12u³v", "4u²v×3u＝12u²v", "4u²v×3u＝7u³v", "4u²v×3u＝12uv"], "A", "外提出的 4u²v 乘以括號第一項 3u，正好得到 12u³v。", "medium"),
    ("多項式 9t²−24t 的因式分解中，提出 3t 後括號內應為何？", ["3t−8", "3t−24", "6t−8", "9t−8"], "A", "9t²÷3t＝3t，−24t÷3t＝−8，因此為 3t(3t−8)。", "easy"),
    ("下列哪個分解結果展開後等於 10z²＋25z？", ["5z(2z＋5)", "5(2z²＋25z)", "10z(z＋25)", "25z(2z＋5)"], "A", "5z(2z＋5) 展開為 10z²＋25z，且括號內已無可再提出的共同因數。", "medium"),
]

for index, (prompt, texts, answer, explanation, difficulty) in enumerate(ITEMS, 1):
    path = ROOT / "questions" / "math" / f"question-math-factorization-{index}.json"
    data = json.loads(path.read_text())
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(texts)],
        "difficulty": difficulty,
        "answer": {"value": answer, "explanation": explanation},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-29",
    })
    data["provenance"] = {
        "origin": "original",
        "license": "All rights reserved",
        "sourceUrl": SOURCE,
        "sourceLocator": "公立國中公開數學段考與 114 年國中教育會考；研究共同因式、分配律、代入驗算與錯誤辨識能力方向；本題為獨立改編。",
        "authoringNote": AUTHORING,
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

print(f"rewrote {len(ITEMS)} duplicate-prone factorization questions")
