import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = [
    ("在白光照射下，紅色紙張看起來呈紅色，最合理的解釋是？", ["紙張主要反射紅光並吸收較多其他色光", "紙張自己發出紅光", "紙張吸收全部紅光", "眼睛把所有顏色都變成紅色"], "A", "不發光物體的顏色主要由進入眼睛的反射或透射光決定，紅紙主要反射紅光。", "先確認光源是白光，再判斷物體選擇性反射哪些色光。"),
    ("紅色物體只用綠光照射時，看起來可能接近黑色，主要原因是什麼？", ["物體缺少可被它有效反射的紅光，反射進眼睛的光很少", "綠光會自動變成紅光", "物體一定會發出黑光", "眼睛失去辨色能力"], "A", "紅色物體在白光下看紅，是因為反射紅光；若入射光只有綠光，能反射回眼睛的光可能很少。", "先列出入射光中有哪些顏色，再檢查物體能反射哪些顏色。"),
    ("白色紙張在白光下看起來白，最適合的模型是？", ["可見光多種色光皆有較強反射，混合光進入眼睛形成白色感覺", "白紙只反射紅光", "白紙吸收所有色光", "白紙自身不需光也會發白光"], "A", "理想白色表面對可見光各色反射較均勻，混合反射光進入眼睛形成白色外觀。", "比較白色物體對各色入射光的反射範圍，而非只看一種色光。"),
    ("黑色物體在白光下看起來黑，最合理的近似說法是？", ["可見光被吸收較多，反射到眼睛的光較少", "黑色物體反射所有色光", "黑色物體一定沒有任何溫度", "黑色是由只反射藍光造成"], "A", "黑色表面通常吸收較多可見光，反射光少，因此眼睛接收到的光較少。", "將看到的顏色與反射光量、吸收光量連結。"),
    ("藍色紙張在紅光與藍光同時照射下，最可能呈現什麼顏色？", ["藍色或偏藍，因為它主要反射藍光", "一定呈紅色，因為紅光先到達", "一定呈黑色，因為兩種光會互相抵消", "透明無色"], "A", "藍紙主要反射藍光，紅光通常被吸收較多；混合入射光中仍有藍光可被反射。", "逐一檢查物體對每種入射色光的反射與吸收。"),
    ("用紅、綠、藍三種光混合調整顯示器顏色，這與紙張顏色判讀最大的差異是？", ["顯示器是發光混色，紙張主要是選擇性反射入射光", "兩者都完全不需要光源", "紙張會主動發出三原色", "顯示器只靠吸收光線成像"], "A", "顯示器以不同強度的光直接進入眼睛；紙張顏色則依光源與表面的選擇性反射而變化。", "先辨認物體是自發光還是反射光，再選擇適用的顏色模型。"),
    ("要研究不同色光對黃色紙張外觀的影響，哪項設計較合理？", ["固定紙張、觀察角度與亮度，逐一更換紅、綠、藍光並記錄反射結果", "每次同時改變紙張與光源", "只在黑暗中觀察而不提供光源", "只記錄紙張原本名稱"], "A", "控制紙張與觀察條件、逐一改變入射色光，才能比較選擇性反射造成的外觀差異。", "列出控制變因與自變因，再設定可觀察的反射色結果。"),
    ("同一件衣服在商店白光與舞台藍光下看起來顏色不同，最主要的原因是？", ["入射光光譜改變，衣服能反射的色光組成也隨之改變", "衣服的分子一定在短時間內變色", "眼睛只在舞台上能看到藍色", "藍光會把所有物體染成永久藍色"], "A", "物體呈色取決於入射光與表面選擇性反射的共同結果，更換光源會改變進入眼睛的反射光。", "把光源條件與物體反射特性分開，再合併判讀觀察結果。"),
    ("攝影棚用色卡校正相機時，為什麼要固定光源色溫？", ["避免光源本身的光譜改變色卡反射結果，才能比較相機記錄的差異", "讓色卡自己發光", "使所有物體都只反射白光", "增加鏡頭焦距"], "A", "色卡反射的光會受光源光譜影響，固定色溫能降低外部變因並改善顏色判讀。", "確認光源是顏色實驗的重要控制變因。"),
    ("若某表面從不同角度觀察會呈現不同色澤，最謹慎的解釋是？", ["可能有微結構造成方向選擇性的反射，仍需改變角度與光源做測試", "一定是染料完全變色", "只要看到變色就能確定化學反應", "角度不可能影響反射光"], "A", "有些表面色澤來自微結構造成的方向性反射，應以角度、光源與光譜資料進一步檢驗。", "把觀察現象轉成可控制的角度與光源實驗，不過度推論成因。"),
]

PUBLIC_REFERENCES = [
    {"url": "https://www.nhjh.tp.edu.tw/uploads/1675416610965nINWfUhq.pdf", "title": "臺北市立內湖國民中學 111 學年度第一學期第二次定期考查八年級理化科試題", "year": "111"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國中 112 學年度第一學期第二次段考二年級自然科試題", "year": "112"},
    {"url": "https://www.ykjh.tn.edu.tw/modules/tad_uploader/index.php?cat_sn=103&cfsn=1010&name=111%E5%AD%B8%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%28%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6%29%E8%A3%9C%E8%80%83-%E9%A1%8C%E5%BA%AB.pdf&op=dlfile", "title": "臺南市立永康國中 111 學年度第一學期八年級自然科補考題庫", "year": "111"},
]
for ref in PUBLIC_REFERENCES:
    ref.update({"subject": "science", "locator": ref["title"], "observedPattern": "僅研究公立學校公開課程與試題的色光、物體選擇性反射、光源改變與顏色判讀能力方向；未複製原題文字、選項、圖表或答案。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"})

TARGET_ANSWERS = 'ABCDBCDACB'

for i, (prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    path = ROOT / "questions/science" / f"question-science-content-ka-iv-11-{i}.json"
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
            "圈出光源顏色、物體表面、反射光與觀察者看到的顏色。",
            "先列出入射光包含哪些色光，再判斷表面選擇性反射與吸收。",
            f"套用原理：{explanation}",
            f"排除把光源色、物體色與自發光混淆的選項，答案為「{correct}」（選項 {target}）。",
            "回查是否固定光源、角度與觀察條件，並把現象與證據範圍分開。",
        ],
        "examPatternRefs": PUBLIC_REFERENCES,
        "reviewStatus": "draft",
    })
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n")
print(f"rewrote {len(DATA)} questions")
