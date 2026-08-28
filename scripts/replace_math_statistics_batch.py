#!/usr/bin/env python3
"""Replace the generic statistics questions with independently authored data items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = json.loads((ROOT / "curriculum/math/performance-d-iv-1.json").read_text())
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CAP_SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
LESSON_ID = "lesson-math-performance-d-iv-1"
KG_ID = "kg-math-performance-d-iv-1"

items = [
    ("某組資料為 4、6、8、8、9，這組資料的平均數為何？", ["7", "6", "8", "9"], "總和為 35，共 5 筆資料，所以平均數為 35 ÷ 5＝7。"),
    ("某組資料由小到大排列為 12、15、17、20、24、28、31，其中位數為何？", ["20", "17", "24", "15"], "共有 7 筆資料，中間第 4 筆是 20，因此中位數為 20。"),
    ("資料 18、12、25、20、16 的全距為何？", ["13", "7", "12", "25"], "最大值 25 減最小值 12，得到全距 13。"),
    ("某社團記錄每天借閱本數如下：借閱本數 1、2、3、4 本的次數分別為 2、3、4、1，平均每天借閱幾本？", ["2.4", "2", "2.5", "3"], "加權總和為 1×2＋2×3＋3×4＋4×1＝24，總次數為 10，所以平均數為 2.4。"),
    ("資料由小到大為 8、10、12、14、16、18、20、22，採上下半部中位數定義四分位數，Q1＋Q2＋Q3 為何？", ["45", "42", "46", "48"], "Q1＝(10＋12)÷2＝11，Q2＝(14＋16)÷2＝15，Q3＝(18＋20)÷2＝19，總和為 45。"),
    ("一個盒狀圖的五數摘要為最小值 52、Q1 60、中位數 68、Q3 75、最大值 91，下列何者正確？", ["資料的中位數是 68", "資料的全距是 23", "至少四分之三資料大於 75", "資料一定包含 68 分"], "盒狀圖直接標示中位數為 68；全距是 91－52＝39，且四分位數不代表一定有資料等於該數值。"),
    ("某班身高分組次數為 140～150 公分 2 人、150～160 公分 5 人、160～170 公分 7 人、170～180 公分 6 人，Q3 所在組別為何？", ["170～180 公分", "150～160 公分", "160～170 公分", "140～150 公分"], "共有 20 人，Q3 位於第 15、16 筆附近；累積到 160～170 公分為 14 人，因此 Q3 落在 170～180 公分組。"),
    ("甲、乙兩班人數相同，盒狀圖顯示甲班中位數 72 分、乙班中位數 68 分。下列何者必定正確？", ["甲班成績的中位數高於乙班", "甲班超過 80 分的人一定比較多", "甲班平均數一定高於乙班", "甲班最高分一定高於乙班"], "中位數已明確給出 72＞68；僅憑中位數不能必然推出平均數、最高分或超過某分數的人數。"),
    ("若試算表將 10 筆成績放在 B2 到 B11，要計算其中位數，哪個公式最適當？", ["=MEDIAN(B2:B11)", "=AVERAGE(B2:B11)", "=MAX(B2:B11)-MIN(B2:B11)", "=COUNT(B2:B11)"], "MEDIAN 函數用來求中位數；AVERAGE 求平均數，MAX－MIN 求全距，COUNT 計算資料筆數。"),
    ("某長條圖的縱軸只從 80 分開始，三組數值為 88、90、92。解讀這張圖時，哪一項最可靠？", ["應讀取座標標示的實際數值，不能只用柱高目測差距", "最高的柱一定代表人數最多", "柱高差兩倍就表示數值差兩倍", "縱軸從 80 開始表示 80 分以下沒有資料"], "截斷縱軸會放大視覺差異；判讀時應依座標刻度讀取 88、90、92 等實際數值，不能把柱高直接當成比例。"),
]

target_indices = [3, 2, 1, 0, 3, 2, 1, 0, 3, 2]
for i, (prompt, options, explanation) in enumerate(items, start=1):
    target = target_indices[i - 1]
    shift = (4 - target) % 4
    rotated = options[shift:] + options[:shift]
    path = ROOT / f"questions/math/question-math-performance-d-iv-1-{i}.json"
    data = {
        "id": f"question-math-performance-d-iv-1-{i}",
        "subject": "math",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(rotated)],
        "knowledgeIds": [KG_ID],
        "difficulty": ("easy", "medium", "hard")[(i - 1) % 3],
        "answer": {"value": chr(65 + target), "explanation": explanation},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考直方圖、盒狀圖、四分位數、次數分配與資料判讀題型；另參考 114 年國中教育會考數學科；本題使用全新數值、情境與選項，非原題重製。",
            "authoringNote": "統計單元實質改寫；已重新計算答案與解析，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(f"replaced {len(items)} statistics questions")
