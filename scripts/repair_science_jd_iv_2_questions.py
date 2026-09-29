import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = [
    ("在 25°C 下，pH=3 與 pH=5 的兩杯水溶液相比，哪一杯氫離子濃度較大？", ["pH=3 的溶液，且約為 pH=5 的 100 倍", "pH=5 的溶液，且約為 100 倍", "兩者相同", "只看體積才能判斷"], "A", "pH 每降低 1，氫離子濃度約增加 10 倍，因此相差 2 個 pH 單位時約為 100 倍。", "先比較 pH 大小，再用每一單位 10 倍的關係換算。"),
    ("某溶液 pH=7，在 25°C 下最適合如何描述？", ["呈中性，氫離子與氫氧根離子濃度大致相等", "一定是強酸", "一定是強鹼", "完全沒有離子"], "A", "在 25°C 的常見判準中，pH=7 表示中性；中性不等於沒有離子。", "先確認溫度條件，再以 pH 7 的中性基準判斷。"),
    ("甲液 pH=2、乙液 pH=4，若兩者體積相同，哪項比較正確？", ["甲液氫離子濃度約為乙液的 100 倍", "乙液氫離子濃度約為甲液的 100 倍", "甲乙酸鹼性完全相同", "只憑顏色無法比較任何差異"], "A", "pH 相差 2，較低 pH 的甲液氫離子濃度約高 10² 倍。", "找出較低 pH 的溶液，計算相差的 pH 位數。"),
    ("用廣用指示劑測得樣品呈接近橙紅色，最合理的下一步是？", ["依比色範圍估計 pH，再用校正過的 pH 計交叉確認", "直接宣布樣品一定是鹽酸", "把顏色當成精確到小數點的 pH", "加入更多指示劑直到顏色更深"], "A", "指示劑提供範圍估計，不等於唯一物質鑑定；需要適當儀器與控制條件確認。", "區分半定量顏色判讀與精密測量的證據能力。"),
    ("若 pH 計在測量前沒有用標準緩衝液校正，最可能造成什麼問題？", ["讀值可能有系統偏差，難以確定測量準確度", "樣品會自動變成中性", "氫離子會全部消失", "只會讓溶液體積變大"], "A", "校正用來建立儀器讀值與已知 pH 的對應關係，未校正可能出現系統性偏差。", "先檢查儀器的基準，再判斷讀值是否能直接比較。"),
    ("將酸性溶液稀釋，且沒有加入其他物質，通常可預期 pH 如何變化？", ["pH 向中性方向移動，但不代表必定剛好等於 7", "pH 一定向 0 移動", "酸性一定變得更強", "pH 完全不會改變"], "A", "稀釋會降低氫離子濃度，使酸性減弱，pH 通常向中性方向移動；實際數值仍取決於濃度與體積。", "先判斷氫離子濃度變化，再連結 pH 方向，不過度推算精確值。"),
    ("甲、乙兩種酸的 pH 都是 3，但甲的體積比乙大三倍。下列哪項可由資料直接判斷？", ["兩者測量時的氫離子濃度相近，但總氫離子數不能只由 pH 判定", "甲的氫離子濃度是乙的三倍", "乙一定是強酸而甲一定是弱酸", "甲的 pH 應該是 9"], "A", "pH 反映濃度尺度；體積不同會影響總量，但不會單獨改變已測得的 pH。", "分清濃度、體積與總量三個不同物理量。"),
    ("甲 pH=3、乙 pH=5，若各取相同體積混合且忽略體積收縮，能否直接說混合液 pH=4？", ["不能直接取平均，需考慮氫離子濃度與混合後體積", "可以，pH 一定是兩者平均", "混合後一定變成 pH=7", "只要看兩杯顏色即可算出答案"], "A", "pH 是對數尺度，不能直接作算術平均；混合需先換算氫離子濃度再求混合後的濃度。", "先辨認 pH 的對數性質，再決定是否能直接平均。"),
    ("某指示劑在 pH 6 到 8 間變色，將它加入 pH=4 與 pH=10 的兩樣品，最合理的預期是？", ["兩者都可能呈現同一側的顏色，無法只靠它區分 pH=4 與 pH=10 的精確值", "兩者一定顯示完全不同的顏色", "都會顯示中性顏色", "指示劑能直接測出氫離子濃度"], "A", "樣品若都落在變色範圍之外，可能只呈現酸側或鹼側的端點顏色，不能取得精確 pH。", "確認樣品 pH 是否落在指示劑的有效變色區間。"),
    ("要比較兩種飲料的酸鹼強弱，哪項實驗設計最可靠？", ["用相同溫度、相同校正狀態的 pH 計測量多次，並記錄平均與變異", "只比較包裝顏色", "每種飲料用不同體積且只測一次", "先加糖直到味道相同"], "A", "控制溫度、儀器校正、樣品條件並重複測量，才能降低測量誤差並比較 pH。", "列出控制變因、重複測量與資料摘要三個品質條件。"),
]

PUBLIC_REFERENCES = [
    {"url": "https://www.dwm.kh.edu.tw/upload/344/104_64183/105-2-2%E8%87%AA%E7%84%B6%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "title": "高雄市立大灣國中 102 學年度上學期第一次段考二年級自然科試題", "year": "102"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/2-%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立國昌國民中學 114 學年度第二學期二年級自然與生活科技第二次段考", "year": "114"},
    {"url": "https://lgt.ntpc.edu.tw/TeachPlan_Detail_Upload.aspx?id=1500", "title": "新北市教育局數位教學平台：水溶液的酸鹼性公開教學活動", "year": "公開教學"},
]

TARGET_ANSWERS = "ABCDBCDACB"
for ref in PUBLIC_REFERENCES:
    ref.update({"subject": "science", "locator": ref["title"], "observedPattern": "僅研究公立學校公開試題與教育局教學活動的 pH 比較、指示劑判讀及實驗設計能力方向；未複製原題文字、選項、圖表或答案。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"})

for i, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = ROOT / "questions/science" / f"question-science-content-jd-iv-2-{i}.json"
    item = json.loads(path.read_text())
    correct = options[ord(answer) - 65]
    target = TARGET_ANSWERS[i - 1]
    distractors = [text for index, text in enumerate(options) if index != ord(answer) - 65]
    position = ord(target) - 65
    arranged = distractors[:position] + [correct] + distractors[position:]
    item.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(arranged)],
        "answer": {"value": target, "explanation": f"{explanation} 正確答案為選項 {target}：「{correct}」。"},
        "solutionStrategy": strategy,
        "solutionSteps": [
            "圈出題目中的 pH、氫離子濃度、體積、溫度或測量條件。",
            "先判斷 pH 的大小方向，必要時把 pH 差換成 10 的次方關係。",
            f"套用原理：{explanation}",
            f"排除混淆濃度、總量、顏色與精確測量的選項，答案為「{correct}」（選項 {target}）。",
            "回查是否忽略溫度、儀器校正、變色範圍或 pH 的對數尺度。",
        ],
        "examPatternRefs": PUBLIC_REFERENCES,
        "reviewStatus": "draft",
    })
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
