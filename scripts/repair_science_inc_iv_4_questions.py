import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "questions/science"
DATA = [
    ("地圖比例尺 1:50,000 表示圖上 1 cm 代表實際多少？", ["500 m", "50 m", "5 km", "50 km"], "A", "1:50,000 表示 1 cm 對應 50,000 cm，換算為 500 m。", "先將圖上距離乘比例，再把公分換成公尺。"),
    ("若模型比例為 1:100，真實長度 3 m 的模型長度是多少？", ["3 cm", "30 cm", "0.3 cm", "300 cm"], "A", "模型長度 = 3 m ÷ 100 = 0.03 m = 3 cm。", "先用比例除以縮小倍數，再統一長度單位。"),
    ("圖上兩地距離 4 cm，比例尺為 1:25,000，實際距離為？", ["1 km", "100 m", "10 km", "250 m"], "A", "4 × 25,000 = 100,000 cm = 1,000 m = 1 km。", "圖上距離乘比例，再連續換算單位。"),
    ("若照片中昆蟲長 6 cm，旁邊標準尺顯示真實長度 2 mm，放大倍率約為？", ["30 倍", "3 倍", "300 倍", "12 倍"], "A", "6 cm = 60 mm，60 ÷ 2 = 30，因此影像約放大 30 倍。", "先將兩者換成同一單位，再用影像長度除以真實長度。"),
    ("把地圖長度與實際距離畫成圖表時，哪項最重要？", ["標示單位、比例或座標尺度，避免只比較圖形長短", "只使用不同單位而不標示", "刪除所有刻度", "讓每個物體都畫成同樣大小"], "A", "圖表必須說明單位與尺度，讀者才能把圖形長度轉回實際量值。", "先檢查軸線、單位與比例，再解讀圖形。"),
    ("若模型將所有長度縮小 10 倍，面積應縮小為原來的？", ["1/100", "1/10", "1/1000", "10 倍"], "A", "長度倍率為 1/10 時，面積倍率為 (1/10)^2 = 1/100。", "面積涉及兩個長度方向，要將長度比例平方。"),
    ("若模型長度縮小 10 倍，體積應縮小為原來的？", ["1/1000", "1/100", "1/10", "10 倍"], "A", "體積倍率為 (1/10)^3 = 1/1000，因為長、寬、高三個方向都縮放。", "體積比例是長度比例的三次方。"),
    ("用不同大小圓形代表不同天體時，要避免誤解，最需要標示？", ["圓形代表的量是直徑、半徑或其他指標，以及比例尺", "只標示顏色", "只標示天體名稱而不說尺度", "把示意圖當成真實照片"], "A", "圖示中的大小可能代表直徑、半徑或相對量，需標示定義與比例，才能正確解讀。", "先確認圖形大小所代表的物理量與比例關係。"),
    ("比例尺圖上量距若使用彎曲河道，較適當的做法是？", ["沿河道分段量測後加總，並記錄估計誤差", "只量兩端直線距離並稱為河道長度", "任意拉直地圖", "不需單位"], "A", "彎曲路徑應沿路線分段量測並加總，直線距離是另一種不同的量。", "先定義要量的路徑，再選與路徑相符的方法。"),
    ("比較兩個模型的尺度是否一致，最可靠的做法是？", ["用同一實際量與同一模型量計算比例，再比較比例值", "只看模型外觀", "只比較顏色深淺", "不需要知道實際尺寸"], "A", "模型比例 = 模型量 ÷ 實際量，用相同定義計算才能判斷兩模型是否同尺度。", "建立相同的比例公式，再比較結果。"),
]
TARGET_ANSWERS = 'ABCDBCDACB'

for index, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = DATA_DIR / f"question-science-content-inc-iv-4-{index}.json"
    record = json.loads(path.read_text())
    correct_text = options[ord(answer) - 65]
    target = TARGET_ANSWERS[index - 1]
    position = ord(target) - 65
    distractors = [x for x in options if x != correct_text]
    arranged = distractors[:position] + [correct_text] + distractors[position:]
    record.update({"prompt": prompt, "options": [{"id": chr(65+i), "text": x} for i, x in enumerate(arranged)], "answer": {"value": target, "explanation": explanation + f" 正確答案為選項 {target}：「{correct_text}」。"}, "solutionStrategy": strategy, "solutionSteps": ["圈出圖上量、實際量、比例、縮放次方或圖表單位。", "統一長度單位並寫出比例公式。", f"套用原理：{explanation}", f"檢查比例方向、面積或體積次方與單位，保留「{correct_text}」。", f"回算答案「{correct_text}」確認模型與實物的尺度關係一致。"], "reviewStatus": "draft"})
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
