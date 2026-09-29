#!/usr/bin/env python3
"""Independently rewrite Chinese calligraphy layout questions for Ab-IV-5."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-performance-4-iv-5"
KG = "kg-chinese-performance-4-iv-5"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "書法字形、章法與閱讀線索"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC一%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "語文表達、圖像判讀與證據說明"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "古典書寫、形式觀察與賞析語體"),
]


def refs():
    return [{
        "url": url,
        "title": f"{title}；僅研究公開題型與能力方向，未複製原題。",
        "year": "113-114", "subject": "chinese", "locator": locator,
        "observedPattern": "公立學校國文評量常要求從字距、行距、留白、行氣、墨色、章法與作品比較提出有證據的賞析；本題採全新語料。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]


DATA = [
    ("行款秩序", "一件直幅作品每行字數接近，但行距由上而下逐漸收緊；若要描述行款，哪項最精確？", ["只說字寫得很整齊", "只依最後一行推斷作者心情", "指出行距變化並說明它造成閱讀節奏由舒展轉緊密", "把行距誤當成單字筆畫粗細"], "C", "行款不只看每行字數，也要記錄行距如何改變；由疏到密可支持節奏收束的觀察，但不能直接等同作者心情。", "先分開字距、行距與筆畫，再描述變化方向，最後只提出資料能支持的效果。"),
    ("留白重心", "作品右側文字集中、左側留下大片空間，哪種賞析最不超出證據？", ["作者一定在表達孤獨", "留白改變視覺重心，可先描述觀看動線，不能僅憑空間斷言作者心情", "左側空白代表作品尚未完成", "只要留白多就一定是草書"], "B", "可直接觀察的是留白比例與視覺重心；作者情感或創作意圖還需要題跋、背景等額外證據。", "先列可見形式，再區分合理效果與未獲證明的作者意圖。"),
    ("行氣連續", "相鄰各行的字勢朝同一方向延伸，且收筆與下一行起筆互相呼應；此現象最適合用哪個概念說明？", ["行氣與章法的連續性", "單字部件的造字法", "紙張年代的確定證據", "作者籍貫的直接證據"], "A", "跨行方向與起收筆呼應屬於行氣和章法的觀察，能說明視線與節奏如何連接，不能直接證明年代或籍貫。", "把觀察單位從單字擴大到相鄰各行，再判斷線條如何形成整體節奏。"),
    ("墨色層次", "同一幅作品有濃、淡、枯、潤的墨色變化；要分析其效果，哪種做法最可靠？", ["把每種墨色都解釋成固定情緒", "只看最黑的一筆決定全作風格", "只用作者生平替代作品證據", "先標出墨色分布與筆勢，再說明它如何影響層次與速度感"], "D", "墨色分析須建立在分布、筆勢與視覺層次上；固定把濃淡對應單一情緒會超出作品可見證據。", "記錄濃淡位置，再連結筆速、輕重與視覺層次，避免先入為主地解讀情感。"),
    ("風格證據", "若要支持作品具有『沉著厚重』的風格，哪項證據最有力？", ["觀者覺得作品很有氣勢", "作品掛在古老建築裡", "多處主筆穩健、墨色厚實，且結體重心下沉並在不同字中反覆出現", "作者姓名聽起來很莊重"], "C", "風格判斷要有跨多個字反覆出現的形式證據；穩健主筆、厚實墨色與下沉重心能共同支持沉著厚重。", "先把抽象形容詞拆成可觀察特徵，再檢查特徵是否在作品中反覆出現。"),
    ("詩句與章法", "一段語氣低迴的詩句以疏朗章法、淡墨和較長停頓書寫；哪項說法最完整？", ["形式可與文字節奏互相呼應，但不能只因詩句內容就斷定書家心情", "淡墨必然表示作者悲傷", "疏朗章法代表作者不會安排字距", "文字內容與書寫形式永遠無關"], "A", "可由疏朗、淡墨與停頓觀察到節奏較緩，並與詩句的低迴語氣形成呼應；作者真實心情仍需其他資料。", "分別列出文字節奏與視覺形式，再說明兩者的呼應程度和推論界線。"),
    ("行末收束", "橫幅作品各行長短交錯，最後一行在右下方收束；閱讀章法時首先應做什麼？", ["把所有行改排成等長才好比較", "先標示每行起訖、行距與收束位置，再觀察視線是否形成整體動線", "只讀最後一行猜作者年代", "把右下角直接判定為錯字"], "B", "行長與收束位置是章法資料，先標示位置才能判斷閱讀動線；不應任意把不規則視為錯誤。", "先建立作品的空間草圖，再從行長、間距和收束處推論觀看順序。"),
    ("臨摹轉化", "臨寫一件行氣連貫的作品時，哪項練習最能避免只逐字模仿？", ["只背每個字的外形，不看相鄰字", "只挑最漂亮的單字重複寫", "先分析字距、行距、起收筆與跨行呼應，再分段臨寫並回看整體節奏", "把原作每個字放大後描黑，不做任何比較"], "C", "行氣是跨字、跨行的關係，先拆解空間與筆勢，再以分段練習回看整體，才能理解章法而非只複製單字。", "先觀察整體，再拆成可練習的關係，最後把分段結果放回原有行氣檢查。"),
    ("比較同書體", "比較兩件同一書體作品的風格時，哪組方法最能形成可檢驗的結論？", ["只比較作品大小與掛畫位置", "只看哪一件較符合個人喜好", "各挑一個最醒目的字作結論", "固定比較結體重心、筆畫粗細、字距行距與墨色，並以多處例證交叉核對"], "D", "同一書體仍可能在結體、筆勢、章法和墨色上不同；固定觀察面向並用多處例證，才能避免單一醒目字造成偏差。", "先建立共同比較表，再逐項記錄兩作證據，最後檢查結論是否由多處資料支持。"),
    ("完整賞析流程", "要完成一段碑帖行款布局賞析，哪套順序最完整？", ["先下風格結論，再挑符合結論的細節", "只抄作者生平，不描述作品", "先逐字翻譯，再忽略留白與行距", "先記錄可見形式，再分組比較行款與墨色，提出有界效果，最後用多處證據回查"], "D", "完整賞析應由觀察到分析、由證據到有界結論，並回查是否每項判斷都有作品細節支持。", "先蒐集形式資料，再比較關係與效果，最後以多處證據檢查結論範圍。"),
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
        f"觀察定位：圈出「{tag}」與題幹要求的字距、行距、留白、行氣、墨色或比較面向。",
        f"建立證據：先記錄可見形式，再依「{explanation}」區分直接觀察與推論。",
        f"核對正解：選項 {target} 能以多處作品線索支持，且沒有把作者意圖或年代當成未證明的事實。",
        "排除誘答：檢查是否只憑個人感覺、單一字、作品外部資訊或固定情緒對應，而忽略章法證據。",
        "回查結論：重新對照整幅作品，確認形式、視覺效果與賞析語句的推論範圍一致。",
    ]
    item = {
        "id": f"question-chinese-performance-4-iv-5-{i}", "subject": "chinese", "type": "single-choice",
        "prompt": prompt, "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(options)],
        "knowledgeIds": [KG], "difficulty": "medium",
        "answer": {"value": target, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
                       "sourceLocator": "三所公立學校公開國文資料；只研究書法章法、形式證據、賞析流程與比較判讀。",
                       "authoringNote": "依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫中文識字與寫字表現 Ab-Ⅳ-5 題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-13", "lessonId": LESSON,
        "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps,
    }
    (OUT / f"question-chinese-performance-4-iv-5-{i}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(DATA)} independent questions for {LESSON}")
