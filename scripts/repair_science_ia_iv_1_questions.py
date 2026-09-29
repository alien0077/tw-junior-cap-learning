import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "questions/science"
DATA = [
    ("岩石在原地裂解或分解，但沒有被搬走，這種作用稱為？", ["風化", "侵蝕", "沉積", "成岩"], "A", "風化是岩石在原地受到物理或化學作用而破碎、分解；搬運與移除則屬侵蝕相關過程。", "先判斷物質是否仍留在原地。"),
    ("河流把砂粒帶往下游，主要包含哪個地表作用？", ["搬運", "風化", "隆起", "凝結"], "A", "砂粒由水流帶離原位置並移向下游，這是河流的搬運作用。", "追蹤沉積物的位置是否改變。"),
    ("河流流速變慢時，較可能發生什麼？", ["較大或較重顆粒沉積", "所有沉積物都上升到空中", "岩石立即熔化", "侵蝕必定增加"], "A", "流速降低使搬運能力減弱，較大的顆粒可能先沉積在河床或河口。", "把流速與水流搬運能力連結。"),
    ("海蝕平台主要是海浪長期作用於哪種位置形成？", ["海岸岩壁或基部", "高空雲層", "地核內部", "沙漠地下深處"], "A", "海浪反覆撞擊海岸岩壁基部，造成侵蝕與崩落，逐漸形成較平坦的海蝕平台。", "先定位作用介質與地貌所在位置。"),
    ("板塊聚合邊界常見的地表結果是？", ["造山、地震或火山活動增加", "河流完全停止", "所有地層變成水平", "潮汐消失"], "A", "板塊互相推擠或隱沒可造成地殼變形、地震與火山活動，並形成山脈或火山帶。", "把板塊運動方向與地殼變形結果配對。"),
    ("研究降雨對坡面沖蝕的影響時，哪項設計較能支持因果判斷？", ["固定坡度與土壤，改變降雨強度並量測流失土砂量", "同時改坡度、土壤與降雨且只看照片", "只挑一場豪雨觀察", "不量測流失量"], "A", "固定其他條件、只改變降雨強度並量測土砂量，才能比較降雨對沖蝕的影響。", "找出自變因、控制變因與可量化的應變因。"),
    ("冰川搬運並磨蝕地表，最可能留下哪種證據？", ["擦痕、磨圓岩屑或 U 形谷", "珊瑚礁必然生長", "沙丘只向上移動", "地層完全沒有變化"], "A", "冰體移動可刮磨基岩並搬運岩屑，擦痕、冰磧物與 U 形谷都是常見地貌證據。", "由搬運介質的形狀與運動方式推測地貌。"),
    ("風力搬運砂粒時，較常形成哪種地貌？", ["沙丘或風蝕地形", "深海海溝必然形成", "珊瑚礁島", "冰斗"], "A", "乾燥地區的風可搬運與堆積砂粒形成沙丘，也可能磨蝕岩石形成風蝕地形。", "辨認風的搬運物與堆積環境。"),
    ("地震後河道堵塞形成堰塞湖，這反映哪種地球作用連鎖？", ["內營力造成崩塌，外營力與地形共同改變水流", "只有月相造成湖泊", "水蒸氣直接變成山脈", "潮汐使所有河道上升"], "A", "地震是內營力事件，可誘發崩塌；崩塌物阻塞河道後又改變水流與沉積，形成連鎖作用。", "依事件先後排列內營力、崩塌與水文結果。"),
    ("判斷某河口三角洲由河流沉積形成，哪組證據最有力？", ["上游帶來的沉積物在河口流速降低處呈扇狀堆積", "河口附近沒有任何沉積物", "只有海水溫度升高", "只看到一次閃電"], "A", "河流進入較寬廣水域後流速降低，沉積物在河口堆積並逐步向外伸展，符合三角洲形成機制。", "把沉積物來源、流速變化與地貌形狀串起來。"),
]
TARGET_ANSWERS = "ABCDBCDACB"

for index, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = DATA_DIR / f"question-science-content-ia-iv-1-{index}.json"
    record = json.loads(path.read_text())
    correct_text = options[ord(answer) - 65]
    target = TARGET_ANSWERS[index - 1]
    position = ord(target) - 65
    distractors = [x for x in options if x != correct_text]
    arranged = distractors[:position] + [correct_text] + distractors[position:]
    record.update({"prompt": prompt, "options": [{"id": chr(65+i), "text": x} for i, x in enumerate(arranged)], "answer": {"value": target, "explanation": explanation + f" 正確答案為選項 {target}：「{correct_text}」。"}, "solutionStrategy": strategy, "solutionSteps": ["圈出地貌、作用、介質與事件順序等關鍵詞。", "判斷物質是否風化、搬運、侵蝕或沉積，以及作用力來源。", f"套用原理：{explanation}", f"排除與作用位置或證據不符的選項，保留「{correct_text}」。", f"回查答案「{correct_text}」是否同時符合作用機制與地貌證據。"], "reviewStatus": "draft"})
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
