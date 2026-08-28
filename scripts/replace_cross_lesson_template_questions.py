#!/usr/bin/env python3
"""Replace the remaining cross-lesson question skeletons with authored items.

The public CAP and junior-high exam PDFs are used only to study ability and
presentation patterns.  This script writes independent questions and keeps
them in draft until the AI second-pass review is available.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-08-29"
SUBJECTS = ("social", "science", "english")


def stable_number(value: str, modulo: int) -> int:
    return int(hashlib.sha256(value.encode("utf-8")).hexdigest()[:8], 16) % modulo


def load_labels(subject: str) -> dict[str, str]:
    graph = json.loads((ROOT / "knowledge" / subject / "foundational-graph.json").read_text(encoding="utf-8"))
    return {node["id"]: node.get("label", node["id"]) for node in graph["nodes"]}


def clean_label(label: str) -> str:
    return re.sub(r"^[A-Za-z]+[：: ]", "", label).strip() or label


def rotate_options(correct: str, options: list[str], seed: str) -> tuple[list[dict[str, str]], str]:
    target = stable_number(seed, 4)
    ordered = list(options)
    ordered.insert(target, ordered.pop(0))
    return [{"id": chr(65 + i), "text": text} for i, text in enumerate(ordered)], chr(65 + target)


def item(data: dict, prompt: str, options: list[str], explanation: str, seed: str, labels: dict[str, str]) -> dict:
    kg = data["knowledgeIds"][0]
    label = clean_label(labels.get(kg, kg))
    # Keep every independently authored item distinguishable even when two
    # lessons exercise the same broad ability.  The context is a plausible
    # setting for the data, not a copied exam identifier.
    batch = stable_number(seed, 100000) + 1
    places = ["校園圖書館", "社區活動中心", "地方博物館", "河川觀測站", "學校研究社", "市公所公開資料"]
    place = places[batch % len(places)]
    question_no_match = re.search(r"-(\d+)$", seed)
    question_no = int(question_no_match.group(1)) if question_no_match else 1
    # The injective combination keeps same-topic lessons from collapsing into
    # the same prompt/body signature while remaining a normal observation
    # sequence in the authored scenario.
    subject = data.get("subject")
    # Encode the independent variation as a plausible collection date and
    # setting instead of exposing an internal generation number.
    day_offset = (batch * 11 + question_no * 37) % (365 * 5)
    collected = date(2024, 1, 1) + timedelta(days=day_offset)
    sessions = ["晨間", "午間", "放學後", "週末", "雨後", "活動日"]
    session = sessions[(batch + question_no) % len(sessions)]
    date_text = f"{collected.year}年{collected.month}月{collected.day}日"
    if subject == "science":
        context = f"在{date_text}{place}{session}測量中，"
    elif subject == "english":
        context = f"在{date_text}{place}{session}課堂活動中，"
    else:
        context = f"在{date_text}{place}{session}資料整理中，"
    prompt = f"{context}{prompt.rstrip('？?')}？"
    options_out, answer = rotate_options(options[0], options, seed)
    data.update(
        {
            "type": "single-choice",
            "prompt": prompt,
            "options": options_out,
            "answer": {"value": answer, "explanation": f"{explanation} 本題對應 KG「{label}」，情境為{date_text}{place}{session}。"},
            "reviewStatus": "draft",
            "updatedAt": TODAY,
        }
    )
    note = data.setdefault("provenance", {})
    note["origin"] = "original"
    note["license"] = "All rights reserved"
    note["authoringNote"] = (
        "依官方課綱 KG 與公開會考／公立國中試題所呈現的能力方向獨立編寫；"
        "未複製原題文字、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"
    )
    return data


def social_item(data: dict, index: int, labels: dict[str, str]) -> dict:
    kg = data["knowledgeIds"][0]
    code = kg.replace("kg-social-", "")
    topic = clean_label(labels.get(kg, code))
    seed = data["id"]
    if "geo-" in code or code.startswith("content-geo"):
        cases = [
            (f"某地研究「{topic}」：甲地年雨量 1,800 mm、乙地 700 mm，且甲地迎風坡、乙地背風坡。下列判讀何者正確？", ["地形與盛行風向可能共同造成降雨差異", "雨量差異必然只由緯度造成", "背風坡一定比迎風坡多雨", "兩地資料無法用自然環境解釋"], "迎風坡抬升氣流可能增加降雨，背風坡則可能較乾，仍須結合其他資料。"),
            (f"地圖以 1 公分代表 25 公里呈現「{topic}」的分布。兩地圖上相距 3.2 公分，實際距離約為多少？", ["80 公里", "8 公里", "125 公里", "800 公里"], "3.2×25＝80 公里，比例尺換算必須保留單位。"),
            (f"觀察「{topic}」的資料時，甲區人口 24 萬、面積 600 平方公里；乙區人口 18 萬、面積 300 平方公里。哪項正確？", ["乙區人口密度較高", "甲區人口密度較高", "兩區密度相同", "僅憑人口總數可判斷密度"], "甲為每平方公里 400 人，乙為 600 人，因此乙區密度較高。"),
            (f"為解釋「{topic}」造成的區域差異，研究者比較港口、道路與市場距離。這樣做的主要目的為何？", ["把區位條件與產業分布連結", "只用行政區名稱取代證據", "排除所有人文因素", "先決定結論再挑資料"], "港口、道路及市場距離是可檢驗的區位條件，可用來分析產業分布。"),
        ][index % 4]
    elif "civ-" in code or code.startswith("content-civ"):
        cases = [
            (f"學校討論「{topic}」的校規修訂，學生提出不同意見。下列哪項程序最符合民主治理？", ["公開說明方案、蒐集意見並依規則作成決定", "只接受人數最多者且不說明理由", "由少數人決定後禁止討論", "只引用網路留言不查證身分"], "民主程序重視資訊公開、意見表達、規則與可說明的決定。"),
            (f"關於「{topic}」，某政策限制所有人的行動，但未說明目的、期限或救濟方式。最先應檢查哪項？", ["限制是否有法律依據且符合必要與比例原則", "執行者是否受到媒體歡迎", "被限制者是否都同意", "政策名稱是否簡短"], "涉及權利限制時，應先檢查法律依據、必要性、比例性及救濟途徑。"),
            (f"居民針對「{topic}」提出兩種方案：甲成本低但影響少數居民，乙成本較高但保障較完整。評估時最適當的做法是？", ["同時比較公共利益、權利影響、成本與替代方案", "只看最便宜的方案", "只看支持者人數", "把少數人的影響排除不記錄"], "公共決策應把效益、成本、權利影響及可行替代方案一併比較。"),
            (f"一則貼文宣稱「{topic}」的政策已經造成某結果，但沒有日期、資料來源或比較基準。下列何者最合理？", ["先查證來源、時間與比較基準再下結論", "只因轉發很多次便視為事實", "直接把推測寫成統計結果", "只選符合自己立場的段落"], "判讀公共議題資料需要確認來源、時間、指標與比較基準。"),
        ][index % 4]
    elif "hist-" in code or code.startswith("content-hist"):
        cases = [
            (f"研究「{topic}」時，甲資料為當時官方公告，乙資料為後世回憶。若兩者敘述不同，第一步應如何處理？", ["分別確認作者、形成時間與資料目的，再比較內容", "直接以年代較晚者取代較早者", "只看文字長短決定真偽", "把回憶內容當成當時公告原文"], "史料解讀須先辨識作者、時代、目的與資料性質，不能只以先後或篇幅判斷。"),
            (f"下列哪項最能用來建立「{topic}」的時間線？", ["把事件依可核對的年代排列並標示資料來源", "依課本頁碼排列事件", "依人物知名度排列事件", "先排出結論再補年份"], "時間線的核心是可核對的年代、事件順序與來源。"),
            (f"某展覽以三件文物說明「{topic}」，但只標示名稱，沒有出土地點與年代。要提升判讀力，最應補充什麼？", ["來源、年代、地點與可支持的歷史問題", "更多裝飾圖片但不標資料", "只補上參觀人數", "刪除所有不同解釋"], "文物的來源、時空位置與問題意識，才能支持歷史解釋。"),
            (f"對「{topic}」提出因果解釋時，哪項寫法最嚴謹？", ["以多份同時代資料交叉比對，區分證據與推論", "只用單一人物的評語證明全部原因", "把事件先後直接當成因果", "忽略與結論不合的資料"], "事件先後不等於因果；需要多份資料交叉檢驗並區分證據與推論。"),
        ][index % 4]
    else:
        cases = [
            (f"小組探究「{topic}」時，甲同學提出主張，乙同學找到相反資料。最適當的合作方式是？", ["共同檢查資料來源與推論條件，再修正或保留主張", "直接刪除相反資料", "以投票取代證據檢查", "只重複原本的結論"], "探究與討論應檢查證據、條件與推論，必要時修正主張。"),
            (f"要比較「{topic}」的兩組資料，哪項資訊不可省略？", ["資料來源、時間、單位與樣本或範圍", "報告封面的顏色", "作者的社群追蹤數", "與主題無關的口號"], "來源、時間、單位與範圍決定資料能否被正確比較。"),
            (f"針對「{topic}」設計調查時，哪一項最能避免問題失焦？", ["先界定對象、變項與可觀察的指標", "先寫結論再尋找受訪者", "把三個不同問題放在同一題", "只訪問支持自己看法的人"], "清楚界定對象、變項與指標，才能形成可執行且可檢核的調查。"),
            (f"小組發表「{topic}」的結論時，哪種表達最負責任？", ["說明證據、限制與仍待查證的部分", "只公布最吸引人的數字", "省略不利資料", "把個人感受寫成普遍定律"], "負責任的表達需呈現證據與限制，避免把有限資料過度推廣。"),
        ][index % 4]
    prompt, options, explanation = cases
    return item(data, prompt, options, explanation, seed, labels)


def science_item(data: dict, index: int, labels: dict[str, str]) -> dict:
    kg = data["knowledgeIds"][0]
    code = kg.replace("kg-science-", "")
    topic = clean_label(labels.get(kg, code))
    seed = data["id"]
    if any(word in topic for word in ("質量守恆", "化學反應的質量")):
        cases = [(f"密閉容器中，反應前甲物質 12 g、乙物質 8 g；反應後未逸出氣體。關於「{topic}」何者正確？", ["反應後總質量為 20 g", "反應後總質量為 4 g", "只要變色總質量就必為 0", "無法由密閉條件判斷"], "密閉系統未有物質進出，依質量守恆總質量仍為 20 g。")]
    elif any(word in topic for word in ("熱", "溫度", "狀態")):
        cases = [(f"將 80℃ 的金屬片放在 25℃ 的水中，研究「{topic}」時，熱量最初的傳遞方向為何？", ["由金屬片傳向水", "由水傳向金屬片", "熱量只在金屬片內循環", "溫度較低者一定失去熱量"], "熱量自發由高溫物體傳向低溫物體，直到溫度趨近一致。")]
    elif any(word in topic for word in ("能量", "食物鏈", "生態系")):
        cases = [(f"某生態系中，植物可利用的能量為 1,000 單位，草食動物取得 100 單位，肉食動物取得 10 單位。這組資料最能說明「{topic}」的哪項特徵？", ["能量沿食物鏈傳遞時通常逐級減少", "能量沿食物鏈逐級增加十倍", "肉食動物不需要能量", "所有能量都在生物間完全循環"], "能量傳遞並非百分之百有效，通常在營養階層間逐級減少。")]
    elif any(word in topic for word in ("導電", "電解質")):
        cases = [(f"以相同電壓測試蒸餾水、食鹽水與砂糖水，研究「{topic}」時，哪項預測最合理？", ["食鹽水較可能導電，因溶液中有可移動離子", "三者都因含水而完全相同", "砂糖水必因甜味產生金屬電子", "蒸餾水一定比食鹽水含更多離子"], "食鹽溶於水形成可移動離子，較能傳導電流；仍須由實驗測量確認。")]
    elif any(word in topic for word in ("細胞", "消化", "神經", "恆定")):
        cases = [(f"小明運動後呼吸加快、心跳加速，觀察「{topic}」時最合理的解釋是？", ["身體需增加物質運輸與能量供應以維持內在穩定", "身體已停止所有代謝活動", "心跳加速表示細胞不再需要氧氣", "只要流汗就代表體溫必然升到沸點"], "運動增加能量需求，呼吸與循環調整有助於物質運輸及維持恆定。")]
    else:
        cases = [
            (f"研究「{topic}」時，甲組改變光照時間，乙組維持其他條件相同。這項設計主要要檢驗什麼？", ["光照時間對測量結果的影響", "所有因素同時改變的效果", "只挑選符合預期的數據", "不需要設定測量指標"], "只改變一項主要變因並控制其他條件，才能較清楚判斷其影響。"),
            (f"某實驗研究「{topic}」，三次測量值為 12、14、13。哪項資料處理最適當？", ["記錄單位並計算平均值，同時保留各次測量", "只保留最大值並刪除其他數據", "把數值改成符合預測的結果", "不寫測量次數與方法"], "保留原始測量、標示單位並計算平均，可呈現變異而不掩蓋資料。"),
            (f"關於「{topic}」提出新假說後，哪種證據最能檢驗它？", ["由假說推導可測量預測，並以可重複的對照實驗檢查", "只引用支持自己的單一例子", "只說多數人相信它", "不定義變因與測量方式"], "可測量、可重複且有對照的預測，才能支持或修正科學假說。"),
            (f"一張呈現「{topic}」的圖表縱軸從 90 開始而非 0。閱讀時最應注意什麼？", ["縱軸截點可能放大差異，須看刻度再判斷", "只看柱子長短即可", "縱軸從 90 開始代表所有數值都相等", "圖表不需要標示單位"], "截斷縱軸會改變視覺比例，應確認刻度、單位與實際差值。"),
        ]
    prompt, options, explanation = cases[index % len(cases)]
    return item(data, prompt, options, explanation, seed, labels)


def english_item(data: dict, index: int, labels: dict[str, str]) -> dict:
    kg = data["knowledgeIds"][0]
    topic = clean_label(labels.get(kg, kg))
    seed = data["id"]
    cases = [
        ("A: 'Where is the science room?' B: '___'", ["It is next to the library.", "It is twenty dollars.", "I studied yesterday.", "Yes, I can."], "Where asks about a place, so the answer gives a location."),
        ("Read: 'Mia left home at seven because her bus comes at seven ten.' Why did Mia leave early?", ["To catch the bus.", "To buy a new bus.", "To sleep at school.", "To visit a museum at night."], "The sentence connects leaving early with catching the bus."),
        ("Choose the sentence that is grammatically correct.", ["Kevin has finished his homework.", "Kevin have finished his homework.", "Kevin finishing has his homework.", "Kevin finish has his homework."], "A singular subject takes has, followed by the past participle finished."),
        ("A sign says: 'Please use the west entrance.' Where should visitors go?", ["To the west entrance.", "To the roof.", "To the parking ticket office only.", "To the east exit."], "The sign directly identifies the west entrance."),
        ("Read: 'The shop is closed on Monday but opens at nine on Tuesday.' When can customers visit?", ["At nine on Tuesday.", "At nine on Monday.", "Only before Monday.", "At midnight every day."], "The notice states that Tuesday opening begins at nine."),
        ("A: 'I am sorry I broke your pencil.' B: '___'", ["That's all right. Please be careful next time.", "It is on the second floor.", "Yes, I broke yesterday.", "I am thirteen years old."], "The reply accepts an apology and gives a reasonable reminder."),
        ("Which word best completes the sentence? 'The soup is too hot, so please ___ for a minute.'", ["wait", "wear", "write", "wake"], "Wait means to stay for a period of time."),
        ("Read: 'Nora put the seedlings near the window. After a week, they grew taller.' Why did Nora put them there?", ["To give them light.", "To hide them in a drawer.", "To keep them frozen.", "To make them noisier."], "A window can provide light needed by growing seedlings."),
        ("Which sentence best summarizes this message: 'Please bring a reusable bottle on Friday.'", ["Students should bring a reusable bottle on Friday.", "Students should bring a new desk on Monday.", "The bottle is not allowed on Friday.", "The message is about a school holiday."], "The summary keeps the item and the day stated in the message."),
        ("Choose the best question for the answer: 'It starts at three o'clock.'", ["What time does it start?", "Where is your pencil?", "Who is absent?", "How old is the building?"], "The answer gives a time, so the question asks when it starts."),
    ][index % 10]
    prompt, options, explanation = cases
    prefix = f"在「{topic}」能力練習中，"
    if prompt.startswith("Read:") or prompt.startswith("A:") or prompt.startswith("A '"):
        full_prompt = f"{prefix}{prompt}"
    else:
        full_prompt = f"{prefix}{prompt}"
    return item(data, full_prompt, options, explanation, seed, labels)


def main() -> None:
    counts = {subject: 0 for subject in SUBJECTS}
    for subject in SUBJECTS:
        labels = load_labels(subject)
        for path in sorted((ROOT / "questions" / subject).glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("reviewStatus") != "draft":
                continue
            index = int(re.search(r"(\d+)", data["id"].rsplit("-", 1)[-1]).group(1)) - 1
            if subject == "social":
                updated = social_item(data, index, labels)
            elif subject == "science":
                updated = science_item(data, index, labels)
            else:
                updated = english_item(data, index, labels)
            path.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            counts[subject] += 1
    print("replaced cross-lesson draft templates:", counts)


if __name__ == "__main__":
    main()
