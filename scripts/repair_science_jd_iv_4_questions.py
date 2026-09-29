import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = [
    ("在相同溫度下，某水溶液的 [H⁺] 大於 [OH⁻]，最合理的判斷是？", ["溶液呈酸性", "溶液呈鹼性", "一定是純水", "完全沒有離子"], "A", "酸性水溶液中氫離子濃度大於氫氧根離子濃度；判斷酸鹼性要比較兩者而非只看是否含有某一種離子。", "先比較 [H⁺] 與 [OH⁻]，再對照酸性、中性與鹼性的定義。"),
    ("若在 25°C 純水中加入少量氫氧化鈉且完全溶解，哪項變化最合理？", ["[OH⁻] 增加、[H⁺] 相對降低，溶液呈鹼性", "[H⁺] 與 [OH⁻] 都變成零", "[H⁺] 增加而溶液變酸", "水分子全部變成氫氣"], "A", "氫氧化鈉在水中提供氫氧根離子，使 [OH⁻] 增加並使溶液偏鹼。", "找出加入物質提供的離子，再判斷兩種離子濃度的相對變化。"),
    ("酸鹼中和的核心離子反應可用哪個式子表示？", ["H⁺ + OH⁻ → H₂O", "Na⁺ + Cl⁻ → H₂O", "H₂O → H⁺ + OH⁻ 且一定完全消失", "O₂ + H₂ → NaCl"], "A", "酸中的氫離子與鹼中的氫氧根離子反應生成水，是酸鹼中和的核心概念。", "先找出酸與鹼在水中提供的主要離子，再配平生成物。"),
    ("若一杯溶液含有 0.020 mol 的 H⁺，理想中和需要多少 mol 的 OH⁻？", ["0.010 mol", "0.020 mol", "0.040 mol", "只要一滴即可"], "B", "H⁺ 與 OH⁻ 以 1:1 反應生成水，因此需要 0.020 mol OH⁻ 才能完全中和。", "讀出中和反應的莫耳比，再將 H⁺ 的量按 1:1 對應。"),
    ("將酸性溶液加水稀釋但沒有加入鹼，哪項敘述較正確？", ["[H⁺] 通常降低，酸性減弱，但不代表一定變成中性", "[OH⁻] 一定變成零", "[H⁺] 一定增加", "只要加水就一定發生中和"], "A", "稀釋降低氫離子濃度，使酸性減弱；水本身不是提供足量 OH⁻ 的中和反應物。", "區分稀釋造成濃度改變與酸鹼中和造成離子反應。"),
    ("兩杯溶液 pH 相同但體積不同，能否直接判斷兩杯含有相同莫耳數的 H⁺？", ["不能；pH 主要反映濃度，總莫耳數還需知道體積", "可以，pH 就是總莫耳數", "體積越大 pH 必定越高", "只看顏色即可確定總量"], "A", "pH 與氫離子濃度相關，總量還要乘上體積；相同 pH 不代表相同總莫耳數。", "分清濃度與總量，再確認是否提供體積資料。"),
    ("要研究不同酸鹼溶液導電度與離子濃度的關係，哪項設計較適當？", ["控制體積、溫度與電極，改變濃度並重複測量導電度", "每組使用不同電極與不同溫度", "只看溶液顏色", "加入不同種類糖再比較"], "A", "導電度會受離子種類、濃度、溫度與電極條件影響，需控制條件並重複測量。", "先列出影響導電度的變因，再只改變研究中的濃度。"),
    ("混合等體積、等濃度的強酸與強鹼後接近中性，最需要確認什麼？", ["酸與鹼提供的 H⁺、OH⁻ 莫耳數是否相等，以及體積與濃度條件", "只看兩杯顏色是否相同", "只看容器大小", "假設所有酸鹼的反應比都相同而不看化學式"], "A", "中和是否完全取決於可反應 H⁺ 與 OH⁻ 的量及化學計量關係，不能只靠顏色或體積判定。", "先換算兩種離子的莫耳數，再依反應比判斷剩餘離子。"),
    ("若升高溫度後純水的 pH 不再恰好是 7，最謹慎的解釋是？", ["中性條件仍是 [H⁺]=[OH⁻]，但水的離子積與 pH 中性值可能隨溫度改變", "所有中性溶液永遠只有 pH=7", "溫度會把水變成強酸", "pH 與溫度完全無關"], "A", "pH=7 是 25°C 常用的中性基準；溫度改變會影響水的自解離平衡，中性仍以兩種離子濃度相等判定。", "先區分固定數值基準與中性的定義，再考慮溫度影響。"),
    ("某酸鹼實驗中同時改變濃度、體積與溫度，結果顯示 pH 改變；主要問題是什麼？", ["無法判定是哪一個變因造成結果，因為缺少單一變因控制", "變因越多越能證明因果", "pH 測量不需要校正", "溫度、體積與濃度永遠互不影響"], "A", "多個變因同時改變會造成混淆，需固定其他條件或分開設計實驗才能判斷因果。", "列出所有變因，確認是否只有一個自變因。"),
]

PUBLIC_REFERENCES = [
    {"url": "https://www.dam.kh.edu.tw/upload/68/101_28414/%E4%BA%8C%E5%B9%B4%E7%B4%9A%E7%AC%AC2%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf", "title": "高雄市立大社國中 111 學年度第二學期第二次段考自然科試卷", "year": "111"},
    {"url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/22%E4%BA%8C%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/2%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%87%AA%E7%84%B6/107-2-2-2%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6%E7%A7%91%E8%A9%A6%E5%8D%B7.pdf", "title": "高雄市立小港國民中學 107 學年度第二學期第二次段考二年級自然科", "year": "107"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6_1.pdf", "title": "高雄市立國昌國民中學 109 學年度第二學期第二次段考二年級自然科", "year": "109"},
]
for ref in PUBLIC_REFERENCES:
    ref.update({"subject": "science", "locator": ref["title"], "observedPattern": "僅研究公立學校公開試題的氫離子、氫氧根離子、酸鹼中和與實驗判讀能力方向；未複製原題文字、選項、圖表或答案。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"})

TARGET_ANSWERS = "ABCDBCDACB"

for i, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = ROOT / "questions/science" / f"question-science-content-jd-iv-4-{i}.json"
    item = json.loads(path.read_text())
    correct = options[ord(answer) - 65]
    target = TARGET_ANSWERS[i - 1]
    distractors = [text for option_index, text in enumerate(options) if option_index != ord(answer) - 65]
    position = ord(target) - 65
    arranged = distractors[:position] + [correct] + distractors[position:]
    item.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(arranged)],
        "answer": {"value": target, "explanation": f"{explanation} 正確答案為選項 {target}：「{correct}」。"},
        "solutionStrategy": strategy,
        "solutionSteps": [
            "圈出題幹中的 H⁺、OH⁻、濃度、體積、溫度與中和條件。",
            "先比較兩種離子或換算其莫耳數，再判斷酸鹼性與反應剩餘。",
            f"套用原理：{explanation}",
            f"排除把濃度與總量、稀釋與中和或 pH 與固定溫度基準混淆的選項，答案為「{correct}」（選項 {target}）。",
            "回查是否控制濃度、體積、溫度、儀器與化學計量條件。",
        ],
        "examPatternRefs": PUBLIC_REFERENCES,
        "reviewStatus": "draft",
    })
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
