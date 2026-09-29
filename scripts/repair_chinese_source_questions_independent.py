#!/usr/bin/env python3
"""Independently rewrite Chinese source-reliability questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-source-reliability"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "資訊來源、證據與查核"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "資料判讀、來源衝突與限制"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "事實、推論與媒體識讀"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量要求查找原始來源、比較衝突資料、區分觀察與推論、檢查樣本限制、保留不確定性並避免錯誤轉傳；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("可追溯來源", "社群貼文宣稱某飲品能改善失眠；哪項最能提高這則資訊的可查核性？", ["附作者、發布日期、原始研究連結與適用限制", "只寫很多人都說有效", "用醒目圖片取代資料來源", "把轉發次數當療效證據"], "A", "作者、日期、原始研究與限制讓讀者能追溯主張並檢查適用範圍，人氣與圖片不等於證據。", "先找來源、時間、原文與限制四項欄位，再判斷讀者能否重做查核。"),
    ("衝突數字", "兩篇報導對同一場活動的參加人數不同，第一步最適合做什麼？", ["直接選自己喜歡的數字", "比較發布時間、資料來源、統計口徑與原始紀錄", "把兩個數字相加", "認定其中一篇一定造假"], "B", "差異可能來自時間、估算方式或統計口徑，先比較定義與原始紀錄才能判斷是否真正矛盾。", "把兩個數字的時間點、計算單位、資料來源與涵蓋範圍並列比較。"),
    ("觀察與推論", "觀察紀錄寫「下午三點測得教室溫度 29°C」；哪句屬推論而非直接觀察？", ["下午三點溫度計顯示 29°C", "測量地點在教室窗邊", "溫度計讀值為 29°C", "教室太熱，所以所有人都無法專心"], "D", "所有人都無法專心是由溫度推導出的廣泛結論，紀錄沒有直接提供每個人的專注狀態。", "把句子分成儀器讀值與由讀值推導的效果，檢查推論是否多加了未測量的變項。"),
    ("官方核對", "查核「明天全市停課」的截圖時，哪項做法最可靠？", ["只看截圖轉發次數", "依朋友說法通知全班", "看到排版像公告就當成真的", "到政府或學校官方管道核對日期、全文與發布單位"], "D", "官方管道、日期、全文與發布單位能檢查公告真實性與適用範圍，截圖外觀與轉發量不足。", "先找發布機關，再核對公告日期、適用地區與完整內容，不把截圖當原始來源。"),
    ("第一手資料", "研究社區河川水質時，下列哪項最接近第一手資料？", ["網路文章的河川摘要", "朋友轉述去年看過的報告", "研究團隊在採樣現場記錄的水溫與檢測數值", "未附來源的評論影片"], "C", "研究團隊直接在現場測量並記錄，是針對研究問題取得的原始資料；其餘多為轉述或評論。", "確認資料是否由研究者直接取得，以及它是否記錄測量時間、地點與方法。"),
    ("樣本限制", "一份滿意度調查只訪問同一社團的 12 人，卻宣稱全校學生都支持；最應指出什麼？", ["問卷一定沒有任何價值", "結果符合直覺就能推廣", "樣本來源與數量不足以直接代表全校", "受訪者越少越客觀"], "C", "同一社團的小樣本可能有選樣偏差，不能直接推論全校；資料仍可描述受訪者的回應。", "分別評估資料本身能說明什麼，以及結論是否超過樣本的族群與數量範圍。"),
    ("失效引用", "文章引用一篇研究但連結失效，也沒有作者、年份與期刊資訊；最妥當的處理是？", ["先把研究結論當事實", "用另一篇無關文章補上原文", "依引用句長短判斷可信度", "標記來源尚待查證，不把它當唯一證據"], "D", "無法追溯原文與基本書目時，應標記查證缺口並尋找可核對來源，不能把不可查證引用當定論。", "記下缺少的作者、日期、出版資訊與原文，再決定結論能否暫時保留。"),
    ("限定語", "「目前資料顯示可能與睡眠時間有關」中的「可能」提醒讀者什麼？", ["句子沒有任何主張", "因果關係已被完全證明", "這是保留不確定性的推論，仍需更多證據", "作者完全不相信資料"], "C", "可能表示證據尚未達到確定程度，讀者應保留判斷並查看研究設計與其他資料。", "圈出可能、初步、或許等限定語，再確認結論強度沒有被誇大或誤讀成否定。"),
    ("交叉驗證", "要判斷一項地方交通政策的效果，哪組證據最完整？", ["單一網紅的感想", "一張沒有日期的照片", "留言區最多按讚的評論", "政策前後的客觀數據、受影響者訪談與官方方法說明"], "D", "數據呈現變化、訪談補充經驗、方法說明讓資料可檢查，多種來源能互相補強。", "至少交叉比較結果數據、使用者經驗與資料取得方法，不用人氣取代政策效果證據。"),
    ("錯誤轉傳", "看到聳動標題、沒有日期且要求立即轉傳的訊息，最合理的行動是？", ["先停下來，查找原始來源與日期，再決定是否分享", "刪掉所有不同意見的留言", "因為標題聳動所以一定是真的", "改寫標題後立即轉傳"], "A", "先停下、查原始來源與日期能降低過時、斷章取義或失真的資訊繼續傳播風險。", "辨認緊迫性與情緒性語言，再做來源、日期、全文與其他可靠管道的查核。"),
]
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]

for i, (tag, prompt, options, answer, explanation, strategy) in enumerate(DATA, 1):
    target = TARGETS[i - 1]
    correct_index = ord(answer) - 65
    target_index = ord(target) - 65
    correct = options[correct_index]
    rest = [value for index, value in enumerate(options) if index != correct_index]
    options = rest[:target_index] + [correct] + rest[target_index:]
    steps = [
        f"讀題定位：圈出「{tag}」與來源、日期、樣本、測量、限定語或轉傳要求。",
        f"分層查核：區分直接資料、推論與結論強度，再依「{explanation}」評估證據範圍。",
        f"核對正解：選項 {target} 能提出可重做的查核步驟，且沒有把有限資料誇大成確定事實。",
        "排除誘答：檢查是否只看轉發量、排版、人氣或直覺，或把無法追溯的引用當成可靠來源。",
        "回讀驗證：重新確認來源、時間、方法與樣本是否足以支持句子的主張與語氣。",
    ]
    item = {
        "id": f"question-chinese-source-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": ["kg-chinese-content-bd-iv-1"], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究來源追溯、資料衝突、事實／推論、樣本限制與媒體查核。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫資訊來源可靠性題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-source-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
