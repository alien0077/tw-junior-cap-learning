#!/usr/bin/env python3
"""Independently rewrite Chinese public-argument questions for Ab-IV-3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-2-iv-3"
KG = "kg-chinese-performance-2-iv-3"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "議論文主張、證據與反方"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "公共議題、樣本與推論"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "論辯組織、修辭與方案"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以公共議題的有界主張、相關論據、反方回應、反例、樣本範圍、理由式辯論與評估方案要求完整論辯；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("有界主張", "辯論「午休是否開放操場」時，哪句最適合作為可討論的主張？", ["操場很重要，大家應該知道。", "我覺得這個方案很棒。", "所有人一定都會喜歡開放操場。", "學校應在晴天午休試辦開放兩週，再依安全和使用資料決定。"], "D", "明確主張交代行動、範圍、條件與判定方式，方便提出證據並接受反方檢驗。", "先圈出行動要求，再檢查是否有時間、對象、條件與評估方法。"),
    ("論據相關", "支持開放操場的發言提出「體育課借球次數增加」；判斷論據是否相關還應問什麼？", ["只要數字上升就證明所有效果。", "體育課和午休不同，所以資料完全無用。", "數字越大，論據就一定越相關。", "借球增加是否能支持午休開放的安全、需求或可行性？兩種情境有何差異？"], "D", "論據相關不只看有數字，也要看對象、情境、指標與主張是否連得上。", "把資料的測量對象與主張的判定標準並列，找出能直接支持和仍缺少的部分。"),
    ("論辯安排", "論辯先提出校園噪音問題，再列測量資料，接著回應增加規則會限制自由，最後提出試辦；這種安排有何優點？", ["先用結論壓過資料，避免反駁。", "把反方刪掉以維持簡短。", "證明所有人都會接受試辦。", "讓讀者依序理解問題、證據、反方疑問與可行方案。"], "D", "有條理的安排讓主張、證據、反方與回應可追蹤，不只堆疊立場。", "為每段標上問題、資料、反方與方案，再檢查前後是否互相回應。"),
    ("回應成本", "支持延長圖書館開放的人聽到清潔人員擔心加班；哪種回應最完整？", ["清潔人員不懂閱讀需求，不必回應。", "只重複圖書館很重要，避開加班。", "把反方寫成反對學習的人。", "承認清潔工時是成本，提出調整時段或增加支援方案，再用試辦資料檢查。"], "D", "有效回應處理反方真正的成本，提出條件和可驗證修正，不把不同利益轉成對人格的攻擊。", "先準確重述成本，再估算與提出支援，最後安排試辦指標檢查取捨。"),
    ("反例構成", "主張「只要張貼提醒，所有學生都會準時交作業」；哪項最能形成反例？", ["有人看到提醒後準時交作業。", "提醒使用紅色標題。", "老師下午張貼提醒。", "有學生看到提醒，仍因看不懂要求而遲交。"], "D", "反例保留看到提醒的前提，卻否定所有人準時的結論，指出理解要求也是必要條件。", "檢查例子是否符合主張前提，再看它是否讓全稱結論失效。"),
    ("樣本範圍", "辯論者引用一個班級一週問卷，便說全校學生都支持新制服；最精確的批評是？", ["問卷永遠不能作為論據。", "只要班級意見一致就代表全校。", "把全校改成大寫即可補足代表性。", "樣本與調查範圍不足以支持全校結論，應擴大資料或縮小主張。"], "D", "有證據不等於證據範圍足夠，概括程度要和樣本數、抽樣方法與調查範圍相稱。", "對照樣本和結論的族群大小，再決定是補資料還是收窄結論。"),
    ("理由式辯論", "下列哪句最符合有條理的論辯，而不是攻擊對手？", ["只有自私的人才支持你的方案。", "你連常識都沒有，不值得回答。", "大家都知道你錯了，所以不用看資料。", "我不同意全面禁止，因目前資料未比較替代方案成本；我們可先試辦並公布結果。"], "D", "有條理論辯批評主張、資料或推理，提出理由和可行替代，不把爭議轉成對人的羞辱。", "刪掉人格評語後，檢查句子是否仍有立場、理由、資料缺口與下一步。"),
    ("指標界線", "辯論資料顯示試辦後借閱人次增加，但沒有測量閱讀理解；哪個結論最負責任？", ["試辦已證明閱讀能力一定提升。", "借閱增加表示每位學生都更理解。", "沒有理解測量，所以借閱資料完全無效。", "試辦期間借閱增加，可能提高使用意願；理解成效仍需另行測量。"], "D", "證據可支持接近的結論，但不能跨越不同指標；保留資料價值與未知範圍才準確。", "把已測量的使用行為和未測量的學習成效分開，使用可能與仍需測量的語氣。"),
    ("傳統追問", "對方說「這是傳統，所以不能改」；哪個提問最能讓論辯具體化？", ["既然是傳統就一定比新方法好嗎？", "你是不是不尊重祖先？", "傳統不能改，不必說明理由。", "這做法過去解決過什麼問題？現在條件是否改變？若調整要保留哪項意義？"], "D", "好的交叉提問追問歷史功能、現在條件、保留價值與可調整範圍，不預設人格立場。", "把抽象的不能改拆成歷史用途、現況差異、核心價值與可變部分。"),
    ("完整辯論", "要完成一段有條理的公共議題論辯，哪種結構最完整？", ["先用口號取得支持，再刪除不利資料。", "只引用名人名言，不說明本地情境。", "把對手描述成壞人，讓結論看似自然。", "提出有範圍的主張，提供相關資料，說明推理，承認反方與限制，提出可試行方案和評估指標。"], "D", "完整論辯讓讀者檢查主張、證據、推理、反方、限制與後續行動，說服力來自可驗證組織而非聲量。", "依主張、資料、推理、反方、限制、方案與指標逐段檢查論辯骨架。"),
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
        f"讀題定位：圈出「{tag}」與主張、資料、樣本、反方、限制或評估指標。",
        f"拆解論辯：把立場、理由、證據與方案分開，再依「{explanation}」檢查結論範圍。",
        f"核對正解：選項 {target} 能提出可檢查的理由或有界結論，不以聲量、人身攻擊或口號取代論證。",
        "排除誘答：檢查是否把一次資料推成全體、把不同指標混為一談，或忽略反方成本與條件。",
        "回讀驗證：確認主張、證據、推理、反方、方案與指標彼此有明確連結。",
    ]
    item = {
        "id": f"question-chinese-performance-2-iv-3-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究有界主張、相關論據、反方、反例、樣本與公共議題方案。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文口語表達與公共議題論辯 Ab-Ⅳ-3 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-2-iv-3-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
