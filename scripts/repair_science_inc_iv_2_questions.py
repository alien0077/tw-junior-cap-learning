import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "questions/science"
DATA = [
    ("0.0000045 公尺用科學記號表示為？", ["4.5 × 10^-6 公尺", "4.5 × 10^6 公尺", "45 × 10^-4 公尺", "0.45 × 10^6 公尺"], "A", "小數點向右移 6 位可得到 4.5，因此原數為 4.5 × 10^-6 公尺。", "先數小數點移動位數，再決定指數正負。"),
    ("6.2 × 10^5 公尺等於多少公里？", ["620 公里", "62 公里", "6200 公里", "0.62 公里"], "A", "1 公里等於 10^3 公尺，因此 6.2 × 10^5 ÷ 10^3 = 6.2 × 10^2 = 620 公里。", "先寫出公尺與公里的換算倍率，再運算指數。"),
    ("下列哪個數值最大？", ["3 × 10^4", "8 × 10^3", "9 × 10^2", "7 × 10^1"], "A", "先比較指數，10^4 的量級大於 10^3、10^2 與 10^1，因此 3 × 10^4 最大。", "指數不同時先比量級，不要只看前面的係數。"),
    ("2.4 公尺等於多少毫米？", ["2400 毫米", "240 毫米", "24 毫米", "0.24 毫米"], "A", "1 公尺等於 1000 毫米，所以 2.4 × 1000 = 2400 毫米。", "確認公尺到毫米是乘以 10^3。"),
    ("若甲長度為 5 × 10^-3 m、乙長度為 2 × 10^-5 m，甲約是乙的幾倍？", ["250 倍", "25 倍", "2.5 倍", "0.004 倍"], "A", "(5 × 10^-3) ÷ (2 × 10^-5) = 2.5 × 10^2 = 250。", "係數相除，指數相減，最後整理成標準科學記號。"),
    ("科學記號的標準形式要求前面的係數通常？", ["大於或等於 1 且小於 10", "一定大於 100", "一定小於 0", "只能是整數 1"], "A", "標準科學記號寫成 a × 10^n，其中 1 ≤ a < 10，方便比較量級。", "先檢查係數是否落在 1 到 10 之間。"),
    ("3.0 cm 與 3 cm 的記錄差異主要表示？", ["有效數字或測量精度不同", "兩者必定相差 3 公分", "3.0 一定是錯誤單位", "小數點沒有任何意義"], "A", "3.0 cm 通常表示測量精度到十分位，3 cm 的有效數字與精度資訊較少。", "留意數值後的有效位數與儀器解析度。"),
    ("將 7.8 × 10^6 改寫成一般數字，結果是？", ["7,800,000", "780,000", "78,000,000", "0.0000078"], "A", "正指數 6 代表小數點向右移 6 位，得到 7,800,000。", "正指數向右移，並逐位檢查零的數量。"),
    ("將 9.1 × 10^-4 改寫成一般小數，結果是？", ["0.00091", "0.0091", "0.091", "9100"], "A", "負指數 4 代表小數點向左移 4 位，得到 0.00091。", "負指數向左移，先寫出零再放入有效數字。"),
    ("測量天文距離與細胞大小時，選擇不同單位的主要理由是？", ["讓數值落在較易讀、易比較的範圍並保留尺度意義", "改變物體真實大小", "讓所有誤差消失", "表示不同單位的物理量沒有關係"], "A", "適當單位能避免過多零位並清楚呈現尺度，但換單位不會改變物理量本身。", "分辨表示方式的改變與物理量本身的改變。"),
]
TARGET_ANSWERS = 'ABCDBCDACB'

for index, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = DATA_DIR / f"question-science-content-inc-iv-2-{index}.json"
    record = json.loads(path.read_text())
    correct_text = options[ord(answer) - 65]
    target = TARGET_ANSWERS[index - 1]
    position = ord(target) - 65
    distractors = [x for x in options if x != correct_text]
    arranged = distractors[:position] + [correct_text] + distractors[position:]
    record.update({"prompt": prompt, "options": [{"id": chr(65+i), "text": x} for i, x in enumerate(arranged)], "answer": {"value": target, "explanation": explanation + f" 正確答案為選項 {target}：「{correct_text}」。"}, "solutionStrategy": strategy, "solutionSteps": ["圈出數值、單位、指數與換算方向。", "先統一單位或判斷小數點移動方向。", f"套用原理：{explanation}", f"檢查係數、指數與有效位數，排除錯誤選項並保留「{correct_text}」。", f"回算答案「{correct_text}」確認數量級與原題相符。"], "reviewStatus": "draft"})
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
