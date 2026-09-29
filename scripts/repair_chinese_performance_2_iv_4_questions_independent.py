#!/usr/bin/env python3
"""Independently rewrite Chinese technology-supported presentation questions for Ab-IV-4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-2-iv-4"
KG = "kg-chinese-performance-2-iv-4"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "科技媒介、圖表與說明"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "數位資料、無障礙與來源"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "影像、隱私與負責任表達"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以圖表選擇、指標界線、數位來源、簡報結構、影像證詞、無障礙、訪談同意、問卷限制與隱私要求科技媒介服務表達目的；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("時間圖表", "要向校長說明校園午餐剩食一個月的每日變化，哪種科技媒介最適合？", ["只播放節奏快的背景音樂", "使用沒有刻度的裝飾圖", "把所有數據塞進看不清的投影片", "有標題、單位、日期與來源的折線圖，並用文字解釋趨勢"], "D", "每日變化需要可比較的時間圖表，且標題、單位、日期、來源與文字說明讓讀者能正確解讀。", "先確認資料是時間序列，再檢查圖表是否有分母、單位、來源與必要文字。"),
    ("指標界線", "圖表顯示借閱量上升，但作者想說明閱讀理解提升；最需要補什麼？", ["把上升線畫粗就能證明", "刪掉圖表只留結論", "只要有顏色資料就完整", "說明借閱量和理解測量不是同一指標，補理解評量或降低結論強度"], "D", "科技呈現能清楚展示借閱變化，卻不能替不同指標建立不存在的因果；需補證據或修正主張。", "把圖表實際測量的指標和想宣稱的結果並列，找出缺少的測量或改寫結論。"),
    ("來源標示", "簡報引用網路統計圖，負責任的做法是什麼？", ["只寫網路資料避免投影片太擠", "刪除來源讓觀眾專注畫面", "換顏色後當成自己的", "標示資料機構、網址、發布／查閱日期與圖表重製或改寫方式"], "D", "來源讓觀眾追溯資料，也要說明是否重製或改寫；視覺修改不會消除證據與著作責任。", "為每張圖建立來源註記，寫清楚原作者、日期、網址、改動與授權或使用界線。"),
    ("簡報負荷", "一張投影片放八段文字、三張照片和四個結論；最適合的修正是？", ["字體縮到最小全部保留", "增加動畫讓內容看起來豐富", "刪除所有文字只留照片", "每張投影片聚焦一個訊息，將證據分頁並用標題和口頭說明連結"], "D", "簡報需安排認知負荷與閱讀路徑，層次設計應突出主旨與證據，不是塞滿或只剩裝飾。", "先為每頁寫一句核心訊息，再分配必要證據與口頭補充，避免同頁競爭注意力。"),
    ("影像證詞", "短片呈現居民說「晚上很吵」，要支持改善噪音提案還需補什麼？", ["把一句話剪成代表所有人的結論", "只加煽情音樂讓問題更嚴重", "刪除受訪者身分和拍攝日期", "記錄時間、地點、測量方式與不同使用者聲音，並說明影像是個案證詞"], "D", "影像有現場感但有範圍，時間、地點、測量與來源能把個案證詞和普遍主張分開。", "先標明影像誰在何時何地說話，再補客觀測量與其他使用者資料。"),
    ("無障礙設計", "要讓視力或聽力不同的同學都能理解線上簡報，哪項做法最完整？", ["只使用鮮豔動畫", "把所有資訊放圖片裡不需文字", "只提供聲音", "提供圖片替代文字、清楚對比、字幕、文字稿與可鍵盤操作的檔案"], "D", "公平科技表達要涵蓋不同感官與操作方式，無障礙是讓資訊可取得的基本設計。", "逐項檢查圖片、聲音、色彩、文字與操作是否都有替代或可使用路徑。"),
    ("字幕與同意", "把訪談逐字稿轉成短片字幕時，哪項最需注意？", ["為吸引觀眾改寫成受訪者沒說過的句子", "只留下最衝突片段，不需脈絡", "移除身分與時間避免查證", "保留原意與語氣，標示刪節或改寫，並確認公開同意"], "D", "媒介轉換不能偽造他人聲音；剪輯、字幕與公開範圍要尊重來源、語意與同意。", "對照原始逐字稿，標示刪節與編修，確認受訪者知道用途和公開範圍。"),
    ("問卷分母", "線上問卷結果要放進簡報，哪項資訊能避免誤讀？", ["只放最高比例不放問題文字", "把未填答者當反對者", "用動畫把少數比例放大", "交代填答人數、題目、選項、調查時間與樣本限制"], "D", "數據要說明分母、題目與樣本，視覺效果不能替代方法透明度。", "先檢查比例的分母與未回答者，再補題目、選項、時間、抽樣方式與限制。"),
    ("定位隱私", "製作社區人物故事的照片地圖，哪種做法最負責任？", ["公開照片就能任意標精確住址", "為故事效果公開姓名與家庭資訊", "刪除說明讓觀眾自己猜", "說明拍攝和定位用途、取得同意，必要時模糊住址並提供移除方式"], "D", "照片與定位會連結人物和地點，需納入目的、同意、最小揭露與撤下機制。", "先評估是否真的需要精確位置，再取得同意、模糊敏感資訊並提供撤下管道。"),
    ("科技專題流程", "要完成有資料、有科技媒介且能負責任說服讀者的專題，哪套流程最完整？", ["先做最炫動畫再找資料", "資料很多就不必考量媒介與受眾", "直接貼網路圖表省略來源與限制", "先定受眾與主張，查證資料與來源，選適合媒介，設計文字／圖像層次，加入無障礙與隱私措施，最後測試讀者理解"], "D", "科技資訊表達要同時處理內容、媒介、來源、可及性、倫理與讀者理解，工具不能取代判斷。", "依受眾、主張、資料、媒介、可及性、隱私與使用者測試逐步檢查專題。"),
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
        f"讀題定位：圈出「{tag}」與圖表、指標、來源、受訪者、無障礙或隱私線索。",
        f"拆解媒介：先確認表達目的與讀者，再依「{explanation}」檢查資料與設計是否匹配。",
        f"核對正解：選項 {target} 能讓資訊可理解、可追溯、可取得且沒有超出證據或同意範圍。",
        "排除誘答：檢查是否把視覺效果代替來源、把單一指標代替成效，或忽略字幕、分母、同意與敏感位置。",
        "回讀驗證：確認主張、資料、媒介、讀者需求、倫理措施與測試方式彼此一致。",
    ]
    item = {
        "id": f"question-chinese-performance-2-iv-4-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究圖表、數位來源、簡報、無障礙、影像同意、問卷與定位隱私。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文口語表達與科技媒介 Ab-Ⅳ-4 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-2-iv-4-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
