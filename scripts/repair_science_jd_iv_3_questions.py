import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "questions/science"
DATA = [
    ("pH = 7 的水溶液通常呈現哪種性質？", ["中性", "酸性", "鹼性", "一定有毒"], "A", "在一般水溶液 pH 尺度中，pH 7 通常表示中性；pH 小於 7 偏酸，大於 7 偏鹼。", "先記住 pH 7 的基準，再比較數值大小。"),
    ("下列哪項 pH 值代表酸性較強？", ["pH 2", "pH 5", "pH 7", "pH 10"], "A", "pH 越小表示酸性通常越強，pH 2 比 pH 5、7 與 10 更酸。", "先判斷 pH 位於 7 的哪一側，再比較遠近。"),
    ("廣用指示劑的主要用途是？", ["由顏色變化粗略判斷溶液酸鹼性或 pH 範圍", "精確測量溶液質量", "直接測量溶液溫度", "把酸完全變成水"], "A", "廣用指示劑在不同 pH 範圍呈現不同顏色，可用來估計酸鹼性，但精度通常不如 pH 計。", "區分粗略範圍判斷與精密數值測量。"),
    ("使用 pH 計測量溶液前，最重要的準備之一是？", ["依規範用標準液校正並以蒸餾水沖洗電極", "把電極擦到完全乾燥且不校正", "只看顯示器外觀", "將不同溶液混在同一容器不清洗"], "A", "pH 計需以標準液校正，電極也要適當清洗，才能降低殘液與校正造成的誤差。", "先處理儀器校正，再處理樣品交叉污染。"),
    ("比較兩種飲料酸鹼性時，哪項做法較公平？", ["使用相同溫度、相同體積與校正後的儀器，重複測量並清洗電極", "一杯用指示劑、一杯用未校正 pH 計", "只挑顏色最鮮豔的結果", "每次改變溫度且不記錄"], "A", "一致的溫度、體積、儀器狀態與重複測量可提高比較的公平性與可靠度。", "固定樣品與儀器條件，再比較讀值。"),
    ("若廣用指示劑呈現偏紅色，通常表示溶液？", ["偏酸性", "偏鹼性", "必為純水", "沒有任何離子"], "A", "廣用指示劑在酸性範圍常呈紅、橙或黃等色系，實際判讀仍應依試紙或指示劑色表。", "將觀察顏色與標準色表的 pH 範圍配對。"),
    ("pH 3 與 pH 4 的溶液相比，若以氫離子濃度概念判斷，pH 3 約？", ["比 pH 4 高 10 倍", "比 pH 4 低 10 倍", "完全相同", "只差 1 倍"], "A", "pH 每降低 1，氫離子濃度約增加 10 倍，因此 pH 3 約是 pH 4 的 10 倍酸性濃度尺度。", "注意 pH 是對數尺度，差 1 不代表只差 1 倍。"),
    ("測量高濃度酸液後要再測量中性水，哪項最能避免污染？", ["充分沖洗電極並依規範處理，再測量空白或標準液確認", "直接把電極插入水中", "只用紙巾擦拭電極尖端", "把兩種溶液混合後再讀值"], "A", "酸液殘留會改變下一樣品讀值，需清洗並用適當檢查確認儀器狀態。", "依樣品順序與清洗步驟控制交叉污染。"),
    ("若指示劑顏色落在兩個色階之間，最合理的記錄是？", ["記為約略 pH 範圍並註明判讀不確定性", "硬寫成精確到小數點後三位", "直接當成 pH 7", "忽略顏色差異"], "A", "指示劑顏色判讀具有範圍與主觀不確定性，應記錄約略範圍而非誇大精度。", "讓記錄精度不超過工具與色表的解析能力。"),
    ("酸鹼中和實驗中，加入鹼液後 pH 接近 7，最合理的解釋是？", ["酸與鹼反應使溶液酸鹼性趨近中性，但仍需以測量確認", "所有物質都消失", "pH 計必然壞掉", "顏色改變就代表溫度為零"], "A", "酸鹼反應可使溶液的酸鹼性趨近中性，但實際 pH 需依濃度、體積與測量結果判斷。", "區分化學反應的推論與儀器實測證據。"),
]

TARGET_ANSWERS = "ABCDBCDACB"

for index, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = DATA_DIR / f"question-science-content-jd-iv-3-{index}.json"
    record = json.loads(path.read_text())
    correct_text = options[ord(answer) - 65]
    target = TARGET_ANSWERS[index - 1]
    distractors = [text for option_index, text in enumerate(options) if option_index != ord(answer) - 65]
    position = ord(target) - 65
    arranged = distractors[:position] + [correct_text] + distractors[position:]
    record.update({"prompt": prompt, "options": [{"id": chr(65+i), "text": x} for i, x in enumerate(arranged)], "answer": {"value": target, "explanation": explanation + f" 正確答案為選項 {target}：「{correct_text}」。"}, "solutionStrategy": strategy, "solutionSteps": ["圈出 pH 數值、顏色、指示劑、pH 計或校正等關鍵詞。", "先用 pH 7 基準判斷酸鹼，再考慮工具精度與污染。", f"套用原理：{explanation}", f"排除誇大精度或忽略校正的選項，保留「{correct_text}」（選項 {target}）。", f"回查答案「{correct_text}」是否符合 pH 定義與實驗證據。"], "reviewStatus": "draft"})
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
