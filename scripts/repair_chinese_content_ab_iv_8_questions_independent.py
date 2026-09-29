#!/usr/bin/env python3
"""Independently rewrite Chinese Ab-IV-8 calligraphy appreciation questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-content-ab-iv-8"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "書法觀察與作品證據"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "書體、筆畫與章法判讀"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "藝術作品描述與證據"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以書體特徵、筆畫、結體、章法與圖像證據要求學生描述作品並保留判讀界線；本題採全新作品情境。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("篆書線索", "某作品左右對稱、線條圓轉，仍可看出古文字的象形意味；較合理的書體判斷是？", ["楷書", "行書", "篆書", "草書"], "C", "圓轉、對稱與象形意味是篆書的觀察線索，但仍應以實際字形與作品資料交叉確認。", "先記錄可見的線條與結體，再把證據和書體典型特徵對照，不只靠作品名稱猜測。"),
    ("隸書線索", "某碑刻橫畫常見波磔，結體由長圓轉為較扁平；這些證據最支持哪種書體？", ["篆書", "隸書", "行書", "草書"], "B", "波磔與由長圓轉為扁平的結體，是隸書常見的視覺線索；碑刻名稱仍需核對。", "把線條特徵和結體變化分開列出，再用兩項以上證據交叉判斷書體。"),
    ("楷書證據", "下列哪項描述最適合作為楷書的觀察證據？", ["字與字大量連綴，難以分辨單字。", "線條全部圓轉，保留象形圖畫。", "橫畫帶明顯波磔，結體向左右開張。", "筆畫起收較清楚，結體穩定，單字輪廓容易辨認。"], "D", "楷書通常具有筆畫起收清楚、結體穩定與單字容易辨識等可觀察特徵。", "優先選能直接從圖像檢查的筆畫與結體描述，排除作者推測或其他書體線索。"),
    ("行書判讀", "作品字間偶有連帶，筆勢比楷書流動，但大多仍可辨認；較合理的判斷是？", ["行書", "篆書", "隸書", "甲骨文"], "A", "行書介於楷書與草書之間，筆勢較流動而辨識度通常仍高，符合題述證據。", "同時比較連帶程度與可辨識度，避免看到一處連筆就直接判為草書。"),
    ("草書觀察流程", "作品筆畫高度連綿、省略與變形較多，需要依上下文辨識字形；欣賞時最應先做什麼？", ["先猜作者，再把模糊處套入其風格。", "先記錄筆畫和結體證據，再用上下文核對字形。", "只挑喜歡的局部評分。", "直接把所有連筆改寫成楷書。"], "B", "連綿與變形需要圖像證據和上下文交互核對，不能先猜作者或任意規整化。", "先觀察並記錄，再以字形上下文與作品資料核對，最後才提出風格描述。"),
    ("碑帖比較目的", "學習碑帖時比較原作拓本的筆畫、結體與章法，主要目的為何？", ["只為背出名家姓名。", "把所有作品改寫成同一字體。", "從可觀察證據理解作品風格與書寫選擇。", "判斷哪件作品價格最高。"], "C", "比較筆畫、結體與章法能把欣賞建立在作品證據上，理解線條、空間與節奏的選擇。", "確認題目要的是藝術觀察還是外部價值，再選能連結圖像證據與風格效果的答案。"),
    ("章法與空間", "比較兩件同為楷書的作品，單字結構相近但行距、字距與布局不同；應優先觀察哪個面向？", ["作者出生地。", "單一字的筆畫數。", "紙張價格。", "章法與空間安排。"], "D", "行距、字距與整體布局屬章法，能說明相同書體中不同作品的空間與節奏。", "把單字層次和整體布局分開，題目涉及行列、疏密與節奏時優先看章法。"),
    ("證據式評論", "下列哪句評論最符合「以證據描述書法」的要求？", ["這幅字很有氣質，看起來就是名家作品。", "我覺得它比另一幅高級很多。", "作品以連續牽絲連接相鄰字，行距收緊，形成快速的行氣。", "作者一定在心情不好時寫下這件作品。"], "C", "C 指出牽絲、字距與行氣等可觀察證據，再提出風格效果；其餘多為價值判斷或心理推測。", "評論先寫看得到的線條、結體與空間，再說明造成的節奏或風格效果，不跳到作者心理。"),
    ("衝突證據", "若書法家姓名與作品局部線索似乎不一致，最妥當的作法是？", ["只相信姓名。", "只相信第一眼喜好。", "標記衝突，分別核對書體、作品來源與圖像證據。", "把局部改畫成符合姓名的樣子。"], "C", "姓名與圖像線索衝突時應保留不確定性，回查作品來源、書體特徵與圖像，而不能任意選一項。", "把不同證據分欄記錄，先標記矛盾，再找可追溯資料解決，不用權威名稱取代圖像。"),
    ("資料不足界線", "題目只提供「某名家某帖」的名稱，沒有圖像、筆畫描述或可靠作品資料；此時可以下哪個結論？", ["一定能判定書體和風格。", "只能說名稱已出現，不能據此完成書體或風格判定。", "名家姓名等於作品證據。", "可依作品名稱猜出所有章法特徵。"], "B", "只有名稱不足以觀察筆畫、結體與章法，不能據此斷定書體或風格，應要求圖像或可靠資料。", "先列出判定所需的觀察證據，再檢查題目是否提供；缺資料時清楚說明不能推出的範圍。"),
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
        f"讀題定位：圈出「{tag}」及題目提供的筆畫、結體、連帶、空間或作品資料。",
        f"整理證據：把可觀察描述與主觀推測分開，再依「{explanation}」判定書體或欣賞方法。",
        f"核對正解：選項 {target} 能由題目中的具體視覺證據支持，且沒有超出資料範圍。",
        "排除誘答：檢查是否只憑作者姓名、喜好、作品價格或心理猜測，或把單一線索誇大成結論。",
        "回讀驗證：重新比對筆畫、結體與章法，確認評論同時保留證據、效果與不確定性界線。",
    ]
    item = {
        "id": f"question-chinese-content-ab-iv-8-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": ["kg-chinese-content-ab-iv-8"], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究書體、筆畫、結體、章法與證據式藝術評論。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫 Ab-Ⅳ-8 書法欣賞與證據判讀題；未複製原文、選項、作品或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-content-ab-iv-8-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
