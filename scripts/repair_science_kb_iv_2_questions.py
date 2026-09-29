import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "questions/science"
DATA = [
    ("萬有引力大小與兩物體質量的定性關係是？", ["質量越大，引力通常越大", "質量越大，引力必定越小", "質量與引力無關", "只有帶電物體才有萬有引力"], "A", "萬有引力與兩物體的質量都呈正相關，質量越大，其他條件相同時引力越大。", "先固定距離，再比較質量改變的方向。"),
    ("兩物體距離增加時，萬有引力通常如何變化？", ["變小", "變大", "永遠不變", "先變成電力"], "A", "萬有引力隨距離增加而減小，定量上與距離平方成反比。", "先判斷距離是分母中的影響因素。"),
    ("若兩物體距離加倍，其他條件不變，萬有引力約變為？", ["原來的 1/4", "原來的 1/2", "原來的 2 倍", "原來的 4 倍"], "A", "引力與距離平方成反比，距離變 2 倍時引力變為 1/(2^2)=1/4。", "將距離倍率平方後取倒數。"),
    ("地球與月球彼此互相吸引，哪項說法正確？", ["兩者互相施力，作用力與反作用力大小相等、方向相反", "只有地球吸引月球", "月球沒有質量所以不受力", "引力只存在地面"], "A", "萬有引力是相互作用，地球與月球互相施力，依牛頓第三定律大小相等、方向相反。", "辨認力的施力者與受力者是一對相互作用。"),
    ("太陽能使行星繞行，主要是因為？", ["太陽的巨大質量提供對行星的引力", "太陽風把行星固定在軌道上", "行星沒有質量", "行星只受月球引力"], "A", "太陽質量很大，對行星產生引力，使行星運動方向持續改變而形成軌道運動。", "把中心天體質量與軌道運動的方向改變連結。"),
    ("若將其中一物體質量加倍、距離不變，引力定性上會？", ["加倍", "減半", "變為 1/4", "不變"], "A", "萬有引力與任一物體質量成正比，單一質量加倍時引力也加倍。", "只改變一個質量因素，固定另一質量與距離。"),
    ("太空船遠離地球時，地球對它的引力通常？", ["隨距離增加而減小，但不會在有限距離突然變成零", "隨距離增加而無限變大", "只要離開大氣就完全沒有", "改變成磁力"], "A", "萬有引力作用範圍廣，距離越遠越弱，但在有限距離仍可視為存在。", "區分變弱與完全不存在。"),
    ("用小球模型研究距離對引力的影響時，哪項設計較公平？", ["固定兩球質量，只改變球心距離並保持測量方法一致", "同時改變球質量與距離", "只改變其中一球大小且不量距離", "只觀察球的顏色"], "A", "要檢驗距離因素，必須固定質量，只改變兩球間距離並一致量測結果。", "明確設定自變因為距離，其他條件保持不變。"),
    ("地球表面不同地點的重力加速度略有差異，不能直接推論為？", ["萬有引力定律失效", "地球形狀、自轉與地下密度分布會影響測量", "不同地點的測量值可能略不同", "需控制儀器與高度"], "A", "局部重力差異可由地球形狀、自轉和質量分布解釋，不代表萬有引力定律失效。", "把模型的理想化與真實地球的局部因素分開。"),
    ("比較兩顆行星受太陽引力時，哪組資料最重要？", ["行星質量、太陽質量與兩者距離", "只記錄行星顏色", "只知道行星名稱", "只測行星表面溫度"], "A", "引力大小取決於兩物體質量與距離，需取得這三類資料才能比較。", "從關係式找出所有必要變因，避免單一特徵推論。"),
]

TARGET_ANSWERS = 'ABCDBCDACB'

for index, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = DATA_DIR / f"question-science-content-kb-iv-2-{index}.json"
    record = json.loads(path.read_text())
    correct_text = options[ord(answer) - 65]
    target = TARGET_ANSWERS[index - 1]
    distractors = [text for option_index, text in enumerate(options) if option_index != ord(answer) - 65]
    position = ord(target) - 65
    arranged = distractors[:position] + [correct_text] + distractors[position:]
    record.update({"prompt": prompt, "options": [{"id": chr(65+i), "text": x} for i, x in enumerate(arranged)], "answer": {"value": target, "explanation": explanation + f" 正確答案為選項 {target}：「{correct_text}」。"}, "solutionStrategy": strategy, "solutionSteps": ["圈出質量、距離、引力、軌道或模型控制等關鍵詞。", "固定其他條件，判斷改變因素對引力的方向與倍率。", f"套用原理：{explanation}", f"排除混淆距離、質量或相互作用的選項，保留「{correct_text}」（選項 {target}）。", f"回查答案「{correct_text}」是否符合萬有引力的定性關係。"], "reviewStatus": "draft"})
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
