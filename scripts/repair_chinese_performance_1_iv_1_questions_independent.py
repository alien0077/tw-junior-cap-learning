#!/usr/bin/env python3
"""Independently rewrite Chinese listening and communication questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-1-iv-1"
KG = "kg-chinese-performance-1-iv-1"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "聆聽、摘要與溝通回應"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "口語溝通、同理與觀點整理"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "聆聽策略、澄清與資訊界線"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以聆聽目的、事實與感受、澄清追問、重述摘要、非語言線索、保密界線與多方會議紀錄要求精確回應；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("意願與限制", "同學說「我想參加，但放學要照顧弟弟，常來不及準備」；聆聽紀錄最完整的是？", ["他完全不想參加。", "他已答應下次一定參加。", "他想參加，但受到照顧責任與準備時間限制。", "他只是找藉口逃避。"], "C", "說話者同時表達參與意願與現實限制；完整紀錄不能把限制改寫成拒絕或加入未說出的承諾。", "先圈出意願，再圈出限制與原因，避免只摘錄其中一半。"),
    ("事實與感受", "組員說「昨天你沒有回訊息，我覺得自己被排除」；哪項記錄最精確？", ["事實：昨天未收到回訊息；感受／解讀：他覺得被排除。", "事實：你故意排除他；感受：他很生氣。", "事實：他太敏感；感受：你沒有責任。", "事實和感受完全相同，不必分開。"], "A", "未收到回訊息可由紀錄核對，被排除是說話者的感受或解讀，不能擅自加入故意與生氣。", "把可驗證事件和說話者感受分欄，並刪除自己推測的動機。"),
    ("具體澄清", "同學說「老師都不聽我們的意見」；哪個回應最能同理又澄清？", ["老師很忙，你不要抱怨。", "所以老師從來沒聽過任何人嗎？", "我也覺得老師很糟，先一起指責。", "你覺得哪些意見沒有被回應？可以說一個具體場合嗎？"], "D", "回應先承認對方的困擾，再把籠統的都轉成可說明的事件，避免否定、誇大或跟著指責。", "用開放而具體的問題追問時間、事件與未被回應的內容，不急著判斷誰對。"),
    ("確認重述", "對方說完社團場地問題後，哪句重述最適合確認理解？", ["你就是不喜歡活動，所以才提出很多問題。", "我確認一下：你最在意晚上照明不足和器材搬運時間，不是反對整個活動，對嗎？", "場地問題全部由你負責。", "內容太複雜，我先替你決定。"], "B", "重述保留具體需求，也區分場地條件和是否反對整體活動，最後用疑問讓對方修正誤解。", "摘要具體名詞與需求，再加上『對嗎』讓說話者確認，而非把解讀當定論。"),
    ("多方摘要", "會議中有人擔心安全、有人在意費用、有人希望保留樹蔭、有人要求先試辦；最好的摘要是？", ["大家都反對改建。", "大家都同意先試辦，其他意見不重要。", "大家提出安全、費用、環境與試辦等考量，尚未形成單一方案。", "會議很混亂，所以沒有可記錄內容。"], "C", "摘要保留共同討論主題與彼此差異，不把多元意見壓成單一贊成或反對。", "先列出每位的關切，再找可共同命名的議題，最後明確寫出尚未決定之處。"),
    ("同理回應", "對方只說「我覺得很累」；哪種回應最合宜？", ["大家都很累，你應該習慣。", "你一定是不會安排時間。", "我直接替你取消所有事情。", "聽起來你最近承受不少壓力；你想先說是時間、工作量，還是其他事情讓你累嗎？"], "D", "回應先反映感受，再提供可選方向讓對方說明，不武斷診斷，也不未經同意代為決定。", "先接住情緒，再用選擇式追問降低回答負擔，讓對方保有說或不說的權利。"),
    ("共同目標與分歧", "兩位同學都想改善午餐，一人主張延長時間、一人主張增加座位；應如何歸納？", ["兩人已同意延長時間。", "兩人的意見矛盾，所以沒有共同目標。", "只記錄較早提出的方案。", "共同目標是改善午餐經驗，但方法仍有延長時間與增加座位的差異。"], "D", "好的歸納先找共同目的，再保留方案分歧，才能讓後續討論針對方法而非假裝已有共識。", "先問兩個方案要解決的共同問題，再並列各自方法與尚待決定的差異。"),
    ("非語言線索", "對方說「沒關係」，卻停頓很久、聲音變小；聆聽者最適合怎麼做？", ["直接判定他一定在說謊。", "只記錄沒關係，忽略其他線索。", "溫和確認：你說沒關係，但我感覺你似乎還有顧慮，想談談嗎？", "當眾要求他立刻說出全部原因。"], "C", "非語言線索提供追問方向，不等於證明內心；應以尊重且可拒絕的方式確認。", "描述自己的感受而非替對方下診斷，並留下選擇談或暫時不談的空間。"),
    ("保密界線", "同學分享家庭困難，並說「只想讓你知道，不想被轉傳」；紀錄應如何處理？", ["把內容完整貼到群組，讓大家關心。", "只記下完成必要協助所需的資訊，尊重保密意願，若需轉告先說明並取得同意。", "因為是朋友分享，所以可自由轉述。", "完全不記任何內容，避免承擔責任。"], "B", "聆聽也包含資訊界線；紀錄應限於協助所需的最小範圍，不把信任內容當公共材料。", "先確認用途與必要性，再取得同意並刪除不必要的私密細節。"),
    ("完整會議紀錄", "要把一場公聽會整理成小組可用的紀錄，哪套做法最完整？", ["只記最後發言者的結論。", "把所有感受改寫成客觀事實。", "用自己的立場刪除不認同的意見。", "分欄記錄說話者、事件、感受／需求、方案與待確認問題，再整理共同目標和歧異。"], "D", "完整紀錄保留來源、事實、感受、需求、方案與未知，再做有範圍的歸納，不替群體消除差異。", "先逐項記錄原始資訊，再區分事實與感受，最後摘要共識、分歧與下一步。"),
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
        f"讀題定位：圈出「{tag}」及說話者的事件、感受、需求、限制或保密要求。",
        f"分層整理：把可核對事實、對方感受與聆聽者推測分開，再依「{explanation}」設計回應。",
        f"核對正解：選項 {target} 能保留原意、提出適切澄清，並讓說話者有修正或拒答空間。",
        "排除誘答：檢查是否替對方診斷、誇大、代做決定、刪除分歧或洩漏私密資訊。",
        "回讀驗證：確認紀錄或回應既精確又尊重，且下一步能由對方確認而不是由聆聽者猜定。",
    ]
    item = {
        "id": f"question-chinese-performance-1-iv-1-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究聆聽目的、事實／感受、澄清、摘要、保密與溝通回應。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文聆聽與溝通表現 Ab-Ⅳ-1 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-1-iv-1-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
