import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = [
    ("光線對平面鏡的法線入射角為 35°，反射角是多少？", ["35°", "55°", "70°", "145°"], "A", "反射定律指出反射角等於入射角，兩者都以法線為基準測量。", "先確認角度是相對法線，再直接套用反射定律。"),
    ("一條光線與鏡面夾 20°，它與法線的入射角是多少？", ["20°", "70°", "90°", "160°"], "B", "鏡面與法線互相垂直，因此光線與法線的角度為 90°−20°=70°。", "先辨認題目給的是鏡面角還是法線角，再用互餘角換算。"),
    ("光由空氣斜射入玻璃時，若玻璃中的光速較慢，折射線通常如何偏折？", ["向法線偏折", "向界面偏折且遠離法線", "完全不改變方向", "沿界面平行前進"], "A", "光進入光速較慢的介質時，折射線通常向法線偏折；正向入射則不產生方向偏折。", "比較兩介質中的光速，再判斷折射線靠近或遠離法線。"),
    ("光由玻璃斜射向空氣，若入射角逐漸增大，可能在何種條件下發生全反射？", ["入射角大於臨界角且光由較慢介質射向較快介質", "任何入射角都一定全反射", "光由空氣射入玻璃且入射角很小", "只要光是白光就會全反射"], "A", "全反射需要光由折射率較大、光速較慢的介質射向較小、光速較快的介質，且入射角超過臨界角。", "先確認入射方向與介質，再檢查入射角是否超過臨界角。"),
    ("把鉛筆斜插入水中，從水面上方觀察時看似彎折，最合理的原因是？", ["光由水到空氣時折射，眼睛沿折射光反向延伸形成錯覺", "鉛筆在水中真的被折斷", "水把鉛筆的質量改變", "反射定律使鉛筆發光"], "A", "水與空氣的光速不同，光離開水面時改變方向，眼睛通常沿直線反向推回而產生位置偏差。", "追蹤光從哪個介質到哪個介質，再分辨實物位置與視覺位置。"),
    ("平面鏡前物體距鏡面 40 cm，鏡中虛像距鏡面多遠？", ["20 cm", "40 cm", "80 cm", "無法形成像"], "B", "平面鏡成像時，像與物到鏡面的距離相等，因此虛像在鏡後 40 cm。", "使用平面鏡的等距成像規律，不把物像距誤當成鏡面距離。"),
    ("平面鏡保持不動，若物體向鏡面移近 10 cm，物像間距會如何改變？", ["減少 10 cm", "減少 20 cm", "增加 10 cm", "不變"], "B", "物與像會同時各向鏡面靠近 10 cm，因此物像間距減少 20 cm。", "畫出物、鏡、像三者位置，再追蹤兩側距離同時變化。"),
    ("下列哪個現象最能說明光在不同透明介質交界處可能同時反射與折射？", ["雷射斜射玻璃板時，界面可見反光且玻璃內有改變方向的光線", "黑紙吸收所有光", "物體沒有光照仍可見", "聲音繞過牆角"], "A", "斜射透明介面時，一部分光可被反射，另一部分進入另一介質並折射，方向改變。", "找出同時包含反射光與折射光的觀察證據。"),
    ("若光線正向射入另一透明介質，哪項敘述較正確？", ["光速可能改變，但理想情況下傳播方向不偏折", "一定發生全反射", "反射角必大於入射角", "光會沿界面前進"], "A", "正向入射時入射角為 0°，折射線沿原方向前進；但光速仍可能因介質不同而改變。", "把方向變化與光速變化分開判斷，不因沒有偏折就認為沒有折射。"),
    ("要比較兩種透明材料的折射效果，哪項設計最能支持結論？", ["固定入射角與光源，量測多次入射角和折射角並記錄材料、溫度", "每次更換入射角且只憑肉眼描述", "只比較材料顏色", "只測一種材料後推論所有材料"], "A", "控制入射條件、重複測量並記錄環境與材料，才能公平比較折射角或折射率。", "先列控制變因，再確認資料是否可重複且能直接比較。"),
]

TARGET_ANSWERS = 'ABCDBCDACB'

PUBLIC_REFERENCES = [
    {"url": "https://www.nhjh.tp.edu.tw/uploads/1675416610965nINWfUhq.pdf", "title": "臺北市立內湖國民中學 111 學年度第一學期第二次定期考查八年級理化科試題", "year": "111"},
    {"url": "https://bsjh.hcc.edu.tw/var/file/21/1021/attach/11/pta_310375_8225733_72482.pdf", "title": "新竹縣立寶山國中八年級理化補考試題", "year": "公開資料"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國中 112 學年度第一學期第二次段考二年級自然科試題", "year": "112"},
]
for ref in PUBLIC_REFERENCES:
    ref.update({"subject": "science", "locator": ref["title"], "observedPattern": "僅研究公立學校公開試題的反射角、折射方向、平面鏡成像與實驗判讀能力方向；未複製原題文字、選項、圖表或答案。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"})

for i, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = ROOT / "questions/science" / f"question-science-content-ka-iv-8-{i}.json"
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
            "圈出題目中的法線、鏡面、入射角、介質與光速條件。",
            "先判斷角度基準或光線跨越介面的方向。",
            f"套用原理：{explanation}",
            f"排除把鏡面角、法線角或物像距混淆的選項，答案為「{correct}」（選項 {target}）。",
            "回查是否同時考慮反射、折射、介質與控制變因，而非只看現象名稱。",
        ],
        "examPatternRefs": PUBLIC_REFERENCES,
        "reviewStatus": "draft",
    })
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
