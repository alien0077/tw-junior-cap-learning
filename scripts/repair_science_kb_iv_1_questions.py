import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "questions/science"
DATA = [
    ("質量與重量的主要差異是？", ["質量表示物體含有物質的多寡，重量是物體受重力作用的力", "質量只存在液體，重量只存在固體", "兩者永遠使用相同單位", "重量與重力無關"], "A", "質量是物體物質多寡的量，重量是重力對物體施加的力，兩者概念與單位不同。", "先判斷題目問物質多寡還是受力大小。"),
    ("在地球表面，物體重量 W、質量 m 與重力加速度 g 的關係為？", ["W = mg", "W = m/g", "W = g/m", "W = m + g"], "A", "重量是重力造成的力，關係式為 W = mg；在地球表面 g 約為 9.8 N/kg。", "先寫公式，再確認各物理量與單位。"),
    ("同一物體帶到月球，哪項通常不變？", ["質量", "重量", "重力加速度", "彈簧秤讀值"], "A", "物體所含物質沒有因地點改變，因此質量近似不變；月球重力較小，重量會改變。", "區分物體本身的量與所在地的重力場。"),
    ("若物體質量為 2 kg，在 g = 10 N/kg 的地方重量約為？", ["20 N", "5 N", "2 N", "0.2 N"], "A", "W = mg = 2 kg × 10 N/kg = 20 N。", "代入 W = mg，檢查 kg 與 N/kg 會得到 N。"),
    ("測量物體質量通常使用天平，測量重量通常使用？", ["彈簧秤", "量筒", "溫度計", "直尺"], "A", "天平透過比較質量測量質量，彈簧秤則利用彈性形變量測力，可讀取重量。", "依儀器測量的物理量配對。"),
    ("若兩物體在同一地點質量相同，則其重量通常？", ["相同", "一定一個為零", "與質量完全無關", "只能用公尺表示"], "A", "同一地點 g 近似相同，W = mg；質量相同則重量也相同。", "先確認地點相同，再比較公式中的 m 與 g。"),
    ("用彈簧秤比較不同質量物體時，哪項做法較公平？", ["同一地點、同一彈簧秤校零並垂直懸掛", "每次使用不同刻度且不歸零", "改變地點後不記錄 g", "只看物體顏色"], "A", "校零、同一儀器與垂直懸掛可降低系統差異，固定地點則使重力條件一致。", "先控制儀器、姿勢與地點，再比較讀值。"),
    ("太空人進入近似失重狀態時，哪項說法較合理？", ["質量仍存在，但表觀重量可能接近零", "物體質量完全消失", "重力定律不再存在", "天平一定能直接量出原質量"], "A", "失重常指支持力或表觀重量很小，不代表物體含有的物質消失。", "分開判斷質量、重力與支持力的概念。"),
    ("若同一物體在兩地彈簧秤讀值不同，最可能要檢查哪項？", ["兩地重力加速度是否不同，以及儀器是否校正", "物體的原子數每天改變", "直尺刻度是否變長", "液體沸點是否相同"], "A", "重量取決於 m 與當地 g，地點不同可能造成讀值差異，也需排除儀器校正問題。", "由 W = mg 找出可能改變的因素，再檢查儀器。"),
    ("若實驗想驗證重量與質量成正比，哪種資料最有力？", ["固定地點量測多個物體的質量與重量，繪圖後檢查 W/m 是否近似固定", "只測一個物體一次", "只比較物體大小外觀", "不記錄單位與儀器解析度"], "A", "在固定 g 下，W 與 m 應成正比；多組資料與比例或圖線可檢驗此關係。", "建立多組配對資料，再檢查比例與控制條件。"),
]

TARGET_ANSWERS = 'ABCDBCDACB'

for index, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = DATA_DIR / f"question-science-content-kb-iv-1-{index}.json"
    record = json.loads(path.read_text())
    correct_text = options[ord(answer) - 65]
    target = TARGET_ANSWERS[index - 1]
    distractors = [text for option_index, text in enumerate(options) if option_index != ord(answer) - 65]
    position = ord(target) - 65
    arranged = distractors[:position] + [correct_text] + distractors[position:]
    record.update({"prompt": prompt, "options": [{"id": chr(65+i), "text": x} for i, x in enumerate(arranged)], "answer": {"value": target, "explanation": explanation + f" 正確答案為選項 {target}：「{correct_text}」。"}, "solutionStrategy": strategy, "solutionSteps": ["圈出質量、重量、重力加速度、儀器或公式等關鍵詞。", "判斷物理量定義、單位與所在地重力條件。", f"套用原理：{explanation}", f"排除混淆質量、重量或儀器用途的選項，保留「{correct_text}」（選項 {target}）。", f"回查答案「{correct_text}」是否符合公式、單位與實驗控制。"], "reviewStatus": "draft"})
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
