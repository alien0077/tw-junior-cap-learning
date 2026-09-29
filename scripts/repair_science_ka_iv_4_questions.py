import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = [
    ("空氣中聲速取 340 m/s，在山谷喊話後 2.0 s 聽到回聲，喊話者到反射面的距離約為多少？", ["340 m", "170 m", "680 m", "85 m"], "B", "聲音往返總路程為 340×2.0=680 m，單程距離為 680÷2=170 m。", "先算聲波往返路程，再除以二得到單程距離。"),
    ("聲納發出超聲波，0.80 s 後收到海底回波；若水中聲速為 1500 m/s，海深約為多少？", ["300 m", "600 m", "1200 m", "1875 m"], "B", "回波往返路程為 1500×0.80=1200 m，海底深度是單程距離 1200÷2=600 m。", "辨認回波時間包含去程與回程，再除以二。"),
    ("要用回聲測量牆面距離，最需要知道哪項資料？", ["聲速與發聲到接收回波的時間", "牆面顏色與高度", "聲音的音色而不需時間", "只要知道喇叭大小"], "A", "距離由聲速與往返時間決定，公式為距離=聲速×時間÷2；其他特徵不能直接替代時間資料。", "找出測距公式中的聲速、時間與往返修正。"),
    ("同一個房間內，牆面加上吸音材料後回聲變弱，最合理的解釋是？", ["材料吸收部分聲能，反射回接收者的聲能減少", "聲速變成零", "聲波不再需要介質", "反射定律被改寫"], "A", "吸音材料可把部分聲能轉成材料內部的熱或其他形式，減少規則反射回來的聲能。", "把回聲音量變化連結到反射能量，而不是聲波是否存在。"),
    ("蝙蝠利用超聲波尋找障礙物時，最主要依據哪項資訊？", ["回波返回的時間與強弱等特徵", "障礙物的顏色", "空氣的味道", "回波的文字內容"], "A", "回波時間可估算距離，強弱與波形也可提供表面或方向的線索。", "先找出反射波可攜帶的時間、強度與波形資訊。"),
    ("同一聲源在空氣與水中傳播，若兩種介質的聲速不同，使用回波測距時最需要注意什麼？", ["必須使用對應介質的聲速，不能直接套用空氣中的 340 m/s", "所有介質都用 340 m/s", "水中沒有聲波反射", "只要測音量就能算距離"], "A", "聲速受介質種類、狀態、密度與溫度影響，測距公式必須採用當地介質的聲速。", "先辨認傳播介質，再選擇正確聲速與測距公式。"),
    ("若回波訊號受到多個牆面反射而出現數個峰值，如何較可靠地判斷距離？", ["辨認各峰值的到達時間，配合聲速與反射面位置分別計算", "只取音量最大的峰值且不看時間", "把所有峰值時間相加", "只觀察發射器外觀"], "A", "不同反射面會產生不同回波時間，需逐一分析峰值與幾何位置，不能只依音量判斷。", "把複數回波拆成各自的時間訊號，再逐一套用公式。"),
    ("以聲波反射檢查牆內裂縫時，哪項改進最能提高判讀可信度？", ["固定探頭位置與耦合條件，重複測量並與無裂縫樣本比較", "每次任意更換探頭角度", "只測一次並挑選最明顯結果", "忽略材料厚度與聲速"], "A", "控制探頭、接觸與材料條件並設置比較基準，才能把回波差異與裂縫訊號區分開。", "先建立基準樣本，再控制量測條件與重複性。"),
    ("醫療超音波影像能形成不同回波亮度，最合理的概念是？", ["不同組織界面對聲波的反射與傳播差異可形成回波對比", "人體內只有一種聲速", "影像完全由可見光反射形成", "超音波不會與組織互動"], "A", "組織的聲學性質與界面會影響反射、散射與回波時間，儀器再將訊號轉成影像。", "把回波訊號與組織界面、時間及強度的差異連結。"),
    ("要比較兩種牆面材料的聲波反射能力，哪項實驗設計較好？", ["固定聲源、入射角、距離與頻率，量測回波時間與強度並重複多次", "只比較牆面顏色", "每種材料用不同距離與不同音量", "只憑耳朵判斷一次"], "A", "控制入射條件與幾何位置，並重複量測時間與強度，才能公平比較反射效果。", "列出控制變因、應變量與重複測量方式。"),
]

PUBLIC_REFERENCES = [
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國民中學 112 學年度第一學期第二次段考二年級自然科試題", "year": "112"},
    {"url": "https://www.jhsh.ntpc.edu.tw/var/file/0/1000/attach/77/pta_22725_1030925_35628.pdf", "title": "新北市立錦和高級中學 113 學年度第二學期國中部八年級自然科補考題庫", "year": "113"},
    {"url": "https://www.nhjh.tp.edu.tw/uploads/1706771265834881MiQIe.pdf", "title": "臺北市立內湖國中 112 學年度第一學期第二次段考八年級自然科學試題", "year": "112"},
]

TARGET_ANSWERS = 'ABCDBCDACB'
for ref in PUBLIC_REFERENCES:
    ref.update({"subject": "science", "locator": ref["title"], "observedPattern": "僅研究公立學校公開試題的回聲、聲波反射、超聲波與測量應用能力方向；未複製原題文字、選項、圖表或答案。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"})

for i, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = ROOT / "questions/science" / f"question-science-content-ka-iv-4-{i}.json"
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
            "圈出聲速、回波時間、介質、反射面與測量用途。",
            "先確認時間是否包含去程與回程，再選用對應介質聲速。",
            f"套用原理：{explanation}",
            f"排除把音量、音色或單程路徑誤當距離公式的選項，答案為「{correct}」（選項 {target}）。",
            "回查是否控制幾何位置、介質與量測誤差。",
        ],
        "examPatternRefs": PUBLIC_REFERENCES,
        "reviewStatus": "draft",
    })
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
