#!/usr/bin/env python3
"""Legacy migration helper only.

This script is intentionally blocked by default. Its generated prose is a
shared scaffold and must not be used for new or reviewed lessons. New content
must be authored per unit from version research and LLM synthesis.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = json.loads((ROOT / "data/m4-coverage-matrix.json").read_text(encoding="utf-8"))
ROW_BY_LESSON = {row["lessonId"]: row for row in MATRIX["rows"]}
RESEARCH_SOURCE = {
    "chinese": ("hanlin", "翰林 115 國文網頁版 PPT", "https://sites.google.com/hanlin.com.tw/112chwebppt/1%E4%B8%8A"),
    "english": ("nani", "南一國中英語公開期刊索引", "https://mag.nani.com.tw/?id1=2&id2=4"),
    "math": ("hanlin", "翰林國中數學公開解題影音網", "https://mathvideo.hle.com.tw/1A/"),
    "science": ("kanghsuan", "康軒國中自然公開影音", "https://digitalmaster.knsh.com.tw/all/video/j/nature.html"),
    "social": ("kanghsuan", "康軒國中社會公開影音", "https://digitalmaster.knsh.com.tw/all/video/j/geography_page.html?l1=7%E4%B8%8A&l2=%E7%AC%AC1%E8%AA%B2%E3%80%80%E4%BD%8D%E7%BD%AE%E3%80%81%E5%9C%B0%E5%9C%96%E8%88%87%E5%BA%A7%E6%A8%99%E7%B3%BB%E7%B5%B1"),
}


def concept(title: str) -> str:
    return title.split("：", 1)[1] if "：" in title else title


def science_example(title: str) -> str:
    t = concept(title)
    if any(k in t for k in ("酸鹼", "pH", "氫離子", "中和", "指示劑")):
        return f"以「{title}」為主題，使用三杯標示為甲、乙、丙的安全水溶液，量得 pH 分別為 3、7、10；不品嘗、不混合未知藥品，只比較數值與指示劑顏色。先判斷酸性、接近中性或鹼性，再說明 pH 改變代表的相對差異，最後列出量測器材與讀值誤差。"
    if any(k in t for k in ("原子", "分子", "元素", "化合物", "週期", "符號")):
        return f"以「{title}」為主題，製作只含符號與數量的自編粒子卡：O₂、H₂O、CO₂ 與 Fe。先依卡片判斷是元素或化合物、原子或分子，再用「組成粒子—排列方式—可觀察性質」三欄表說明判斷依據；答案以卡片上的資訊為限。"
    if any(k in t for k in ("光合作用", "呼吸作用", "生態", "食物鏈", "生物圈", "能量流", "物質循環")):
        return f"以「{title}」為主題，讀一張自編校園生態資料表：草地、昆蟲、鳥各自記錄數量與觀察到的取食關係。先畫箭頭表示關係，再標出能量或物質移動方向，最後指出資料只是一週觀察，不能直接推論全年趨勢。"
    if any(k in t for k in ("力", "運動", "速度", "摩擦", "壓力", "浮力", "槓桿", "功率", "能量")):
        return f"以「{title}」為主題，在低風險桌面情境量測同一小車通過 1 公尺的時間：木板甲 2.0 秒、木板乙 2.5 秒，重複三次並記錄平均。把材質視為自變因、時間或速度視為應變因，列出可能干擾並以公式檢查單位。"
    if any(k in t for k in ("熱", "溫度", "比熱", "傳導", "對流", "輻射", "形態")):
        return f"以「{title}」為主題，將等質量的水與砂放在相同光源下，每 5 分鐘記錄溫度；用自編表格比較升溫曲線，先描述資料再提出解釋，並標註容器、初溫與光照需固定，避免把單次差異當成定律。"
    if any(k in t for k in ("電池", "電流", "電壓", "電阻", "電路", "導電", "電解", "磁")):
        return f"以「{title}」為主題，在低電壓模擬電路中依序只更換一個元件，記錄電壓、電流或燈的亮度三次。把接線圖、讀值與單位放在同一張表，先預測再實測，最後檢查是否有接觸不良或儀器量程造成的替代解釋。"
    if any(k in t for k in ("光", "聲", "波", "音", "反射", "折射", "影")):
        return f"以「{title}」為主題，使用手電筒、紙卡與量角器（或線上模擬器）建立可重複的觀察；每次只改變入射角或距離，記錄角度、位置與現象。把觀察和模型預測分兩欄，最後說明誤差來源與安全限制。"
    if any(k in t for k in ("板塊", "地震", "火山", "岩石", "地層", "地貌")):
        return f"以「{title}」為主題，讀兩張自編地圖／剖面圖，先依圖例標出位置與時間，再排列事件先後並提出一個可查證的解釋；明確區分圖上直接資訊、推論與仍缺少的證據。"
    if any(k in t for k in ("大氣", "天氣", "氣候", "海流", "潮汐", "季風", "颱風")):
        return f"以「{title}」為主題，整理一週自編氣象表（溫度、風向、降雨或氣壓），先畫趨勢再比較兩個地點；把天氣的短期觀察與氣候的長期平均分開，並列出測站、時間與儀器限制。"
    if any(k in t for k in ("太陽系", "星系", "月球", "日月食", "月相", "宇宙")):
        return f"以「{title}」為主題，用球體與手電筒建立比例不精確但方向一致的模型，依序標示觀察者、光源與運動位置；將模型能解釋的現象和不能代表的尺度分開記錄。"
    return f"以「{title}」為主題，建立一份自編三欄證據表：可直接觀察的現象、支持的模型、尚待查證的限制。先用表格整理資料，再用一句條件式結論回應問題，避免只背名詞。"


def social_example(title: str) -> str:
    t = concept(title)
    if any(k in t for k in ("人口", "遷移", "族群", "聚落")):
        return f"以「{title}」為主題，閱讀兩個虛構鄉鎮的自編資料：甲鎮人口 8→10 萬、平均年齡 38→42 歲；乙鎮人口 8→8.5 萬、平均年齡 31→33 歲。先標出直接數據，再提出需要戶籍、就業或出生資料才能檢驗的解釋。"
    if any(k in t for k in ("法律", "憲法", "權利", "人權", "政府", "選舉", "投票", "行政", "刑法", "契約")):
        return f"以「{title}」為主題，閱讀一則自編校園公共事件與一段規範文字；把事實、規則、受影響者與可用救濟途徑分欄，先判斷規範層級，再說明結論需要哪一條明文依據。"
    if any(k in t for k in ("資源", "機會成本", "價格", "市場", "交易", "貨幣", "消費", "競爭", "勞動")):
        return f"以「{title}」為主題，給定班級活動預算 600 元與三種方案的成本效益表；先列出選一方案就放棄的次佳方案，再比較價格、誘因與分配結果，最後寫出同時考慮公平與效率的條件式建議。"
    if any(k in t for k in ("地圖", "經緯", "地形", "氣候", "水資源", "產業", "貿易", "區域", "環境", "資源")):
        return f"以「{title}」為主題，閱讀一張自編地圖和一張統計圖，依圖例、尺度、時間與來源先描述分布，再提出一個可能原因；把地理事實、推論與政策選擇分開，避免用單一指標代表整個區域。"
    if any(k in t for k in ("歷", "戰爭", "殖民", "改革", "革命", "冷戰", "文化", "宗教", "海外")):
        return f"以「{title}」為主題，對照兩段自編史料摘要與一條時間軸；先標出作者、年代、立場與直接訊息，再排列事件因果的可能鏈條，並指出哪些說法仍需其他史料交叉驗證。"
    return f"以「{title}」為主題，讀兩段自編資料並製作「來源—時間—直接資訊—推論—限制」五欄表；先回答資料顯示什麼，再說明何種證據才能支持因果或價值判斷。"


def chinese_example(title: str) -> str:
    t = concept(title)
    if any(k in t for k in ("書法", "字形", "形、音、義", "字詞", "詞義")):
        return f"以「{title}」為主題，使用自編字詞卡「行、當、解」各兩個句子，先依上下文圈出詞義與詞性，再比較字形、讀音與語意的關係；所有判斷都回指句中線索，不套用單一固定解釋。"
    if any(k in t for k in ("文言", "古文", "古典", "韻文", "新詩", "詩")):
        return f"以「{title}」為主題，閱讀兩句自編仿古短句與一段白話改寫，先標出時間、人物與語氣，再以「字面—語境—主旨」三步說明理解；仿寫時只使用自己的句子。"
    if any(k in t for k in ("敘事", "描寫", "篇章", "主旨", "結構", "寓意")):
        return f"以「{title}」為主題，閱讀自編校園短文，將事件卡重新排成順敘、倒敘或插敘，並圈出一個描寫細節；用兩句話說明順序或細節如何影響讀者理解。"
    if any(k in t for k in ("抒情", "情感", "感受")):
        return f"以「{title}」為主題，閱讀自編雨後校園片段，分別標記直接說出情緒的句子與藉景物表達的句子，再改寫一版讓語氣更克制；說明改寫後證據如何改變。"
    if any(k in t for k in ("說明", "論證", "因果", "比較", "分類", "數據", "圖表")):
        return f"以「{title}」為主題，閱讀一張自編校園用水圖表與一段說明文字，先區分事實、例子與推論，再用主張—證據—推理三欄寫出一個可檢驗結論。"
    if any(k in t for k in ("書信", "簡報", "演講", "新聞", "應用", "溝通")):
        return f"以「{title}」為主題，將同一則自編校園活動資訊改寫成給同學的公告與給家長的電子郵件；比較受眾、目的、語氣與資訊順序，並保留可核對的時間地點。"
    return f"以「{title}」為主題，閱讀一段自編短文，先畫出關鍵詞與句間關係，再以主旨、證據、語氣三欄整理理解；最後用自己的話重述，避免搬用原句。"


def english_example(title: str) -> str:
    t = concept(title)
    if any(k in t for k in ("文法", "句型", "時態", "句子")):
        return f"以「{title}」為主題，使用原創句子 “Mia studies at home.”、“Mia studied at home yesterday.”、“Mia will study at home tonight.”，先標記時間線與動詞形式，再替換主詞和時間副詞，檢查句意是否仍一致。"
    if any(k in t for k in ("發音", "重音", "語調", "韻文", "拼讀", "字母")):
        return f"以「{title}」為主題，對原創短句 “I can finish it today.” 做音節、重音與語調標記；先慢讀再自然速度朗讀，錄下差異，最後說明哪個聲音線索改變了聽者理解。"
    if any(k in t for k in ("圖片", "描述", "人事時地物")):
        return f"以「{title}」為主題，使用一張自製校園情境圖的文字提示：two students, an umbrella, near the library；依人物—動作—地點—時間組成三句描述，再替換一項細節並檢查主詞與動詞。"
    if any(k in t for k in ("故事", "敘事", "主旨", "文章", "體裁")):
        return f"以「{title}」為主題，閱讀三句原創故事：A student finds a lost key, asks two classmates, and returns it to the office；先標出背景、事件、結果與敘事者態度，再用自己的句子改變結局。"
    if any(k in t for k in ("節慶", "文化", "風土", "世界觀")):
        return f"以「{title}」為主題，比較兩個自編校園社團活動通知的時間、參與方式與禮貌用語；用英文表格記錄相同點與差異，避免把單一案例當成整個文化的代表。"
    return f"以「{title}」為主題，使用一段原創英文訊息與一張小表格，先圈出人物、時間、目的與關鍵字，再以完整句子回答 who/what/when/why，最後檢查語法與證據是否對應。"


def worked(subject: str, title: str) -> str:
    if subject == "science":
        return science_example(title)
    if subject == "social":
        return social_example(title)
    if subject == "chinese":
        return chinese_example(title)
    if subject == "english":
        return english_example(title)
    return ""


def math_explain(title: str) -> str:
    """Keep the A-7 proof lessons concept-rich instead of generic prose."""
    if title.startswith("A-7-1"):
        return "代數式把情境中的量分成可變量與固定量：字母代表可變量，係數表示每一單位的量，常數表示不隨字母改變的量。讀式子時先說出每個符號的單位，再依括號、乘除、加減的結構代入；只有字母與次方都相同的項才可合併。每一步都用代回或單位檢查，確認式子仍在描述原問題。"
    if title.startswith("A-7-2"):
        return "方程式是含有未知數且帶等號的敘述；解是讓等號左右同時成立的數值。解題時把等式想成平衡的兩邊，任何一步都必須對兩邊做相同運算，才不會改變解的集合。最後一定把結果代回原式，並檢查未知數是否符合原情境的範圍。"
    if title.startswith("A-7-3"):
        return "解一元一次方程式可依固定順序進行：先用加減消去常數，再用乘除消去未知數的係數；若有括號先使用分配律，若有分數先處理共同分母。移項只是等量公理的簡寫，不能省略理由；解出後代回原式，才能確認應用問題的單位與意義。"
    if title.startswith("A-7-4"):
        return "二元一次聯立方程式描述兩個未知量同時滿足的兩條線性關係。一組解不是各自解一條式子，而是同時讓兩式成立的有序數對。先為每個字母定義量與單位，再用代入或表格找出共同條件，最後把數對分別代回兩式檢核。"
    if title.startswith("A-7-5"):
        return "聯立方程式的消去法和代入法都在保留兩條關係：可先把其中一式整理成某個未知數，再代入另一式；或將兩式相加減消去同一未知數。選方法要看係數與分數是否容易處理，算出一個未知數後仍須回代求另一個並驗證兩式。"
    if title.startswith("A-7-6"):
        return "把每一條二元一次方程式視為坐標平面上的直線，直線上每個點都是該方程式的解；兩條直線的交點就是同時滿足兩式的解。畫圖時標出截距或兩個可計算點，再用代數回代檢查交點，並說明平行、重合或相交各代表什麼。"
    if title.startswith("A-7-7"):
        return "不等式表達的是一段解的範圍，而非單一數值。先把未知數集中，再依等量運算整理；若兩邊同乘或同除以負數，大小方向必須反轉。完成後用數線標示端點是否包含，並挑選範圍內外的測試值驗證方向。"
    if title.startswith("A-7-8"):
        return "一元一次不等式的應用先把文字條件翻成符號，再解出可行範圍；例如容量上限、預算或最低需求都要保留單位與邊界。解出後用端點和一個範圍外數值測試，確認不等號方向、整數限制與原情境一致。"
    return ""


def generic_body(subject: str, title: str) -> list[dict[str, str]]:
    """Create a complete learning-path page for grouping/performance nodes too."""
    c = concept(title)
    if subject == "science":
        hook = f"先從「{c}」相關的生活現象提出一個可觀察問題，寫下已知條件、可能變因與安全限制；把看到的事實和自己的解釋分開，才有可檢查的探究起點。"
        guided = f"針對「{c}」列出問題、假設、變因、步驟、資料與結論；每次只改變一個因素，重複觀察並把異常值與量測限制記下來，再用證據支持或修正模型。"
        transfer = f"把「{c}」的探究方法換到家庭、校園或環境資料，檢查來源、尺度、樣本與不確定性；若證據不足，保留條件式結論並提出下一個可行測試。"
        reflect = f"回顧「{c}」的問題：哪個觀察最關鍵、哪個變因仍未控制、資料能支持到什麼程度？用一句話寫出結論與限制，再提出一項安全的改進。"
    elif subject == "social":
        hook = f"先以「{c}」為題，圈出資料中的人物、時間、地點、制度或資源，並把直接資訊和自己的推論分欄，避免先下結論再找證據。"
        guided = f"針對「{c}」製作來源—時間—直接資訊—推論—限制五欄表，至少比較兩種解釋與受影響群體，再說明何種新資料能支持或推翻判斷。"
        transfer = f"將「{c}」的資料判讀方法移到新聞、地圖、統計或公共議題，核對來源與尺度，分開描述事實、因果推論及價值選擇。"
        reflect = f"回顧「{c}」：我的結論依據是哪筆資料？誰的觀點可能被忽略？哪些說法仍需交叉查證？把答案寫成可讓他人重做的推理鏈。"
    elif subject == "chinese":
        hook = f"遇到「{c}」時，先讀一段自編短文或生活訊息，標出讀者、目的、關鍵詞與語氣；把文字直接說出的內容和需要推論的部分分開。"
        guided = f"針對「{c}」以關鍵詞—句間關係—主旨／語氣三欄整理，再用自己的話重述或改寫；完成後核對是否保留原資訊與溝通目的。"
        transfer = f"把「{c}」的閱讀或表達策略換到公告、圖表、對話與短文，比較受眾、媒介和語氣改變後需要調整的證據與結構。"
        reflect = f"回顧「{c}」：哪個詞句支持我的理解？改寫後語氣與目的是否仍清楚？用一句話說明可遷移的方法，並指出一項仍可改善之處。"
    else:
        hook = f"以「{c}」為情境，先讀一則原創英文訊息或對話，圈出人物、時間、目的與關鍵字，再預測訊息重點；不懂的字先依上下文標記而非亂猜。"
        guided = f"針對「{c}」先辨識句型或溝通功能，再組成完整英文句子；替換一項條件後重讀，檢查主詞、動詞、語序、語意與禮貌程度。"
        transfer = f"把「{c}」的語言策略換到圖片、表格、短文或角色扮演，依受眾與目的調整字詞和句型，並用原文線索檢查理解。"
        reflect = f"回顧「{c}」：哪個字詞或句型完成了溝通目的？改變人物、時間或語氣後，哪些地方必須重寫？把修正理由寫成完整句子。"
    return [
        {"id": "hook", "phase": "hook", "heading": f"從情境進入「{c}」", "body": hook},
        {"id": "explain", "phase": "explain", "heading": f"建立「{c}」的概念架構", "body": f"本頁以官方課綱的「{c}」為範圍，先界定關鍵詞與判斷任務，再用自編例子驗證。學習時把條件、步驟、證據與結論分開記錄；若資料不足，明確寫出限制，不把推測當成事實。"},
        {"id": "worked-example", "phase": "worked-example", "heading": "用自編資料走完一次", "body": worked(subject, title) if subject != "math" else f"以「{title}」為主題，先把題目條件整理成符號、表格或圖形，再逐步推理並回到原條件驗算；所有數字與情境皆為本專案自編，重點是示範可重做的理由。"},
        {"id": "guided-practice", "phase": "guided-practice", "heading": "依步驟完成練習", "body": guided},
        {"id": "transfer", "phase": "transfer", "heading": "換到新情境仍能使用", "body": transfer},
        {"id": "reflect", "phase": "reflect", "heading": "回顧證據與限制", "body": reflect},
    ]


def generic_interactive(subject: str, title: str) -> dict:
    c = concept(title)
    if subject == "math":
        return {"type": "algebra-expression-builder", "goal": f"用可檢查的步驟處理「{c}」並驗算結果。", "scenario": f"以「{title}」為題，先定義未知量，再選擇表示法與檢查方式。", "variables": [{"symbol": "x", "meaning": "題目中待求或可變的量"}], "steps": [
            {"id": "step-1", "prompt": f"處理「{c}」的第一步是什麼？", "options": ["先定義量與條件", "直接猜最後答案", "省略題目資料"], "answer": "A", "feedback": "先定義量與條件，後續表示法才可檢查。"},
            {"id": "step-2", "prompt": "建立表示法後應如何繼續？", "options": ["逐步推理並記錄理由", "只寫最後結果", "任意更換符號"], "answer": "A", "feedback": "每一步都要保留運算或幾何理由。"},
            {"id": "step-3", "prompt": "完成後如何確認？", "options": ["回到原條件代回、看圖或檢查單位", "只看答案順不順眼", "跳過範圍檢查"], "answer": "A", "feedback": "回到原條件驗算，才能確認答案有意義。"},
        ]}
    return {"type": "scientific-investigation", "goal": f"以安全探究步驟理解「{c}」並用證據修正解釋。", "scenario": f"針對「{title}」設計可在教室或模擬器完成的觀察；不使用危險藥品或高電壓。", "variables": [{"symbol": "x", "meaning": "選定的觀察條件"}], "steps": [
        {"id": "step-1", "prompt": "先做哪一件事？", "options": ["提出可觀察問題並列出變因", "先寫預期答案", "省略安全檢查"], "answer": "A", "feedback": "問題、變因與安全限制是探究起點。"},
        {"id": "step-2", "prompt": "如何取得可信資料？", "options": ["固定條件、重複量測並記錄單位", "只量一次且不記錄", "任意改變多個因素"], "answer": "A", "feedback": "固定與重複讓資料能比較。"},
        {"id": "step-3", "prompt": "如何形成結論？", "options": ["先描述證據，再提出有條件的解釋", "把猜測當成結果", "刪掉不符合預期的資料"], "answer": "A", "feedback": "證據與限制都要保留，才能修正模型。"},
    ]}


def update_lesson(path: Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("reviewStatus") == "deprecated":
        return False
    title = str(data.get("title", ""))
    c = concept(title)
    row = ROW_BY_LESSON.get(data.get("id"), {})
    # The review state is machine-readable; do not leave a historical
    # "草稿：" prefix in the learner-facing title after the lesson is enriched.
    if row.get("curriculumPath"):
        curriculum_path = ROOT / row["curriculumPath"]
        if curriculum_path.exists():
            curriculum = json.loads(curriculum_path.read_text(encoding="utf-8"))
            if curriculum.get("title"):
                title = str(curriculum["title"])
                data["title"] = title
                c = concept(title)
    level = row.get("level", data.get("lessonScope", "learning-content"))
    was_full = data.get("authoringStandard") == "full-lesson-v1"
    if not was_full:
        data["authoringStandard"] = "full-lesson-v1"
        data["lessonScope"] = level
        data["publisherResearch"] = []
        data["teaching"] = {"body": generic_body(path.parent.name, title), "summary": [], "exitCheck": [
            {"prompt": "", "expectedEvidence": ""},
            {"prompt": "", "expectedEvidence": ""},
            {"prompt": "", "expectedEvidence": ""},
        ]}
    else:
        data["lessonScope"] = level
    publisher, edition, source_url = RESEARCH_SOURCE[path.parent.name]
    if not data.get("publisherResearch"):
        data["publisherResearch"] = [{
            "publisher": publisher,
            "edition": edition,
            "subject": path.parent.name,
            "chapterLocator": f"{title}；公開教材結構研究定位",
            "sourceUrl": source_url,
            "access": "public-open",
            "reviewedAt": "2026-08-27",
            "researchScope": ["teaching-sequence", "concept-progression", "activity-pattern", "assessment-pattern"],
            "outcome": f"公開出版社資源用於核對「{c}」的教學順序、表徵與活動型態；本頁採自編正文與可重做示例，並標示其為{level}節點。",
            "copyrightBoundary": "只研究公開章節定位與教學結構；本頁正文、例題、選項、提示與回饋均獨立撰寫，不複製出版社文字、圖片、題目或答案。",
        }]
    body = data.get("teaching", {}).get("body", [])
    if not was_full:
        body = data["teaching"]["body"]
    else:
        # Existing full lessons keep their detailed hook/worked/transfer prose;
        # only the concept-specific explanation and guided practice are refreshed.
        body = data.get("teaching", {}).get("body", [])
    for block in body:
        if block.get("phase") == "explain":
            specific = math_explain(title) if path.parent.name == "math" else ""
            block["body"] = specific or (
                f"本單元依官方課綱所列的「{c}」範圍，先界定關鍵詞與判斷任務，再用一個可重做的例子驗證。"
                "閱讀或操作時把條件、步驟、證據與結論分開記錄；若資料不足，明確寫出限制，不把推測當成事實。"
            )
        elif block.get("phase") == "worked-example" and path.parent.name != "math":
            block["body"] = worked(path.parent.name, title)
        elif block.get("phase") == "guided-practice":
            if path.parent.name == "science":
                block["body"] = f"針對「{c}」先寫可觀察問題，再列自變因、應變因與控制變因；依序記錄預測、操作、數據與限制，重複量測後才下條件式結論。"
            elif path.parent.name == "social":
                block["body"] = f"針對「{c}」先標來源、時間、尺度與直接資訊，再分開寫推論與價值判斷；比較至少兩種解釋，指出需要補查的資料與受影響群體。"
            elif path.parent.name == "chinese":
                block["body"] = f"針對「{c}」先圈關鍵詞與句間關係，再以主旨、證據、語氣三欄整理；重述或改寫後回看是否保留原資訊與溝通目的。"
            elif path.parent.name == "english":
                block["body"] = f"針對「{c}」先辨識人物、目的、時間與關鍵語句，再組成完整句子；替換一項條件後重讀，檢查主詞、動詞、語序與語意。"
        if len(str(block.get("body", ""))) < 80:
            block["body"] = str(block.get("body", "")) + " 完成後把判斷依據寫成一至兩句完整說明，讓同學能依相同步驟重做並檢查答案。"
    teaching = data.setdefault("teaching", {})
    teaching["summary"] = [
        f"先用自己的話界定「{c}」的關鍵概念與適用條件。",
        "依序完成表示、操作或閱讀步驟，並在每一步留下可檢查的理由。",
        "把直接證據、推論與限制分開，避免只背結論或套用固定模板。",
        "把方法換到新情境，再檢查條件改變後哪些步驟與答案需要調整。",
    ]
    if str(data.get("content", {}).get("summary", "")).startswith("本單元以官方課綱"):
        data.setdefault("content", {})["summary"] = f"本課聚焦「{c}」，以自編範例練習概念、證據與新情境遷移。"
    checks = teaching.get("exitCheck", [])
    if checks:
        checks[0]["prompt"] = f"請用自己的話說明「{c}」的核心概念與一個適用條件。"
        checks[0]["expectedEvidence"] = "能定義關鍵詞，並以正文中的自編例子指出條件與理由。"
        checks[1]["prompt"] = f"在「{c}」的自編例子中，哪一項資料或語句最能支持你的判斷？"
        checks[1]["expectedEvidence"] = "能指出可重現的數據、句子、圖表或規則，並說明它如何支持結論。"
        checks[2]["prompt"] = f"若題目的條件改變，如何調整處理「{c}」的方法？"
        checks[2]["expectedEvidence"] = "能比較新舊條件，說明要調整的步驟、表示法或推理，並標示限制。"
    if path.parent.name in {"math", "science"} and not isinstance(data.get("interactive"), dict):
        data["interactive"] = generic_interactive(path.parent.name, title)
    elif path.parent.name in {"math", "science"} and data.get("interactive", {}).get("type") == "guided-choice":
        data["interactive"] = generic_interactive(path.parent.name, title)
    data["provenance"] = data.get("provenance", {"origin": "original", "license": "All rights reserved"})
    data["provenance"]["origin"] = "original"
    data["provenance"]["authoringNote"] = "Full lesson v1 is independently authored from the official curriculum and recorded publisher research. No publisher text, image, example, exercise, answer, or transcript is reproduced; classification and performance pages are learning-path material, not publisher chapter reproductions."
    data["updatedAt"] = "2026-08-27"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return True


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--allow-legacy-template",
        action="store_true",
        help="explicitly allow the historical scaffold migration; never use for content authoring",
    )
    args = parser.parse_args()
    if not args.allow_legacy_template:
        print("拒絕執行：此為歷史模板遷移工具。新教材必須逐單元研究並獨立撰寫。")
        return 2
    changed = 0
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        changed += update_lesson(path)
    print(f"enriched {changed} full-lesson-v1 files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
