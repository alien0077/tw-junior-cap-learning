#!/usr/bin/env python3
"""Independently rewrite Chinese evidence-based presentation questions for Ab-IV-5."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-2-iv-5"
KG = "kg-chinese-performance-2-iv-5"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "口頭報告、資料與主旨"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "論證、受眾與反方"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "公共提案、證據與方案"),
]


def refs():
    return [{
        "url": url, "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量以口頭報告主旨、直接證據、敘述順序、事實／評價、因果反駁、方案涵蓋、受眾調整、資料比較與有證據說服要求完成公共表達；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("報告主旨", "班級要向校務會議報告午休噪音，已有七天測量值與三名同學訪談；哪句最適合作為開頭主旨？", ["午休真的太吵，大家一定同意。", "我們要談一件重要而且很長的事情。", "只播放測量機器畫面，觀眾自然會懂。", "本報告整理測量與訪談證據，說明高峰時段並提出可檢驗的改善建議。"], "D", "主旨交代對象、資料範圍、要回答的問題與輸出方向，不能只用情緒或空泛宣告。", "先圈出資料來源與報告目的，再選能讓聽眾預期內容與結論的句子。"),
    ("直接證據", "評論「校園應增設遮雨棚」時，哪組證據最能直接支持「雨天通行受阻」？", ["作者覺得遮雨棚漂亮。", "網路有人說所有學校都要有。", "演講者用很大聲音重複主張。", "連續四週同一時段的積水深度、通行人次與受阻紀錄。"], "D", "好的證據和理由在同一層次且可核對，直接記錄積水與通行受阻比美觀、他人意見或音量有關。", "把理由改成可觀察指標，再選有時間、地點與測量方法的資料。"),
    ("報告順序", "五分鐘口頭報告要說明社區樹木調查，哪種順序最能讓聽眾追蹤？", ["先念完所有數字再公布題目。", "先講個人結論省略方法。", "交錯排列不同地點觀察不說分類。", "先交代問題與方法，再呈現結果，接著說明限制，最後提出建議。"], "D", "聽眾需知道問題、方法、結果、限制與下一步如何相連，順序本身就是理解線索。", "把報告骨架排成問題—方法—結果—限制—建議，再檢查每段是否承接。"),
    ("事實與評價", "評論校服政策時，哪句最能清楚區分事實與評價？", ["校方一定故意忽略學生感受。", "這政策很糟，因為我不喜歡。", "大家都知道這種政策永遠不會成功。", "校方公告指出下學期試行一學期；我認為應公布舒適度調查才足以評估成效。"], "D", "句子先指出可查證公告，再標示自己的評價與所需證據，讓讀者分辨事實、推論和立場。", "找出可核對的發布內容，再用我認為或需要資料標示主觀判斷與證據需求。"),
    ("證據開場", "要向同學演說減少一次性餐具，哪種開場最能引發思考又不誇大？", ["不用餐具地球明天就完全恢復。", "不支持就是不愛地球。", "先播放無關煽情影片不交代主題。", "先呈現本校一週使用量數據，再問每人少用一件會改變多少總量。"], "D", "有效開場把本校具體證據轉成可思考問題，保留感染力但不以誇大因果或道德壓迫取代資料。", "先給聽眾可理解的數據，再設計能讓他們推算或比較的問題。"),
    ("因果反駁", "辯論對方說「延後到校必然讓成績變好」；最有力的第一步回應是？", ["直接說對方完全錯，不看資料。", "重複口號直到觀眾鼓掌。", "改談與到校時間無關的問題。", "指出必然是過強的因果主張，要求比較條件、成績指標與研究期間。"], "D", "先拆解主張範圍與關鍵詞，再要求可檢驗證據，才能針對同一命題往返。", "圈出必然與成績變好，分別追問比較組、指標、時間與替代原因。"),
    ("方案涵蓋", "正方主張全面取消紙本通知，反方哪個問題最能測試方案完整性？", ["你們是不是不喜歡紙張？", "紙本看起來老派，對吧？", "既然是新政策大家只能接受嗎？", "若家中無法穩定上網或需要紙本協助，如何取得同等資訊？"], "D", "好的反方問題尋找方案的適用條件與未涵蓋對象，而不是把價值判斷或情緒當反駁。", "找出政策預設的設備與能力，再追問例外者能否獲得等價資訊。"),
    ("受眾調整", "同一份校園安全調查要向校長與低年級學生說明，哪項調整最恰當？", ["對所有受眾使用相同術語與長度才公平。", "對校長只講情緒、對學生只念數字。", "為討喜而改變調查結果。", "保留相同證據與結論，分別調整術語、例子、說明速度與可追問細節。"], "D", "受眾調整改變呈現和理解支架，不改變資料本身；可信表達維持證據與結論一致。", "先判斷兩種受眾的先備知識與需要，再調整例子與節奏而不改寫結果。"),
    ("資料比較", "對方用十年前小樣本調查反駁你的校園問卷；最合宜的回應是？", ["年代久就完全無效。", "把自己的問卷稱唯一真理。", "轉而攻擊引用者個性與動機。", "承認它可能提供背景線索，再比較樣本、時間、測量方式與問題是否能回答本次主張。"], "D", "批判證據要檢查適切性而非只看支持或反對；承認限制能讓比較更精準。", "列出兩份資料的時間、樣本、方法與問題，再判斷哪些可互相補充或不能直接比較。"),
    ("有證據說服", "要提出校園增設飲水機的提案，哪套做法最符合有證據的說服？", ["只用感人個案要求全面施工。", "混合不同年份數據挑最有利數字。", "先決定結論再刪不支持意見。", "界定缺水問題，呈現分時段需求與成本，回應維護疑慮，提出試辦指標並邀請依證據檢討。"], "D", "完整說服同時處理主張、證據、反對意見、限制與可檢驗行動，讓觀眾能判斷而非被迫接受。", "依問題、需求、成本、反方、試辦與指標逐項建立可追蹤的提案鏈。"),
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
        f"讀題定位：圈出「{tag}」與受眾、資料、指標、限制、反方或評估條件。",
        f"整理表達：先分主旨、證據、評價與方案，再依「{explanation}」檢查結論強度。",
        f"核對正解：選項 {target} 能讓聽眾追蹤資料與推理，且沒有把有限證據誇大成必然。",
        "排除誘答：檢查是否用音量、口號、個案、情緒或挑選數據取代可核對證據。",
        "回讀驗證：確認主張、證據、受眾、反方、限制與行動指標彼此相連。",
    ]
    item = {
        "id": f"question-chinese-performance-2-iv-5-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究口頭報告、直接證據、受眾、反方、資料比較與公共提案。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文口語表達與證據說服 Ab-Ⅳ-5 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-2-iv-5-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
