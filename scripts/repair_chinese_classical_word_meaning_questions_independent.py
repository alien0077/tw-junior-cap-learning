#!/usr/bin/env python3
"""Independently rewrite Chinese classical word-meaning questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-classical-word-meaning"
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "古今詞義、語詞搭配與語境"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "文言詞義、詞性與閱讀理解"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "詞義轉換、句法與語境證據"),
]
def refs():
    return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量把古今詞義、詞性、固定搭配與文言語境放入句子判讀；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA = [
 ("去的古義", "「太丘捨去」中的「去」依故事情境最接近哪個意思？", ["離開", "前往", "除掉", "距離"], "A", "太丘捨去是太丘離開，不能套用現代語中前往或距離的其他義項。", "先看主語的移動方向與事件上下文，再從同字多義中選擇能放回句子的解釋。"),
 ("走的古義", "「雙兔傍地走」中的「走」在古文中最接近哪個意思？", ["奔跑", "散步", "離開某地", "行走去買東西"], "A", "此句描寫兔子快速奔跑，古義的走不等同現代語常說的慢步行走。", "遇到古今義變先列現代直覺，再用主語、動作速度與篇章畫面校正。"),
 ("妻子的古今義", "「率妻子邑人來此絕境」中的「妻子」應如何理解？", ["妻子和兒女", "現在法律上的配偶一人", "女性朋友", "鄰居家人"], "A", "桃花源語境中的妻子包含妻與子女，是古代複合詞，不能只套現代單一義。", "不要把現代固定詞義直接套回古文，要看詞語在句中的歷史語境與並列對象。"),
 ("交通的古今義", "「阡陌交通，雞犬相聞」的「交通」最接近哪個意思？", ["田間小路交錯相通", "現代的大眾運輸", "人與人交換意見", "道路因事故堵塞"], "A", "阡陌指田間小路，交通在此表示交錯相通；現代交通工具義不合句中景象。", "先看前後名詞與描寫對象，再判斷詞義是空間關係、人物往來或現代制度。"),
 ("詞性判斷", "「其一犬坐於前」中的「犬」在句中具有什麼用法？", ["名詞作狀語，像狗一樣", "名詞作主語，指一隻狗", "動詞，表示吠叫", "形容詞，表示忠誠"], "A", "犬本是名詞，放在坐前修飾動作，表示像狗一樣蹲坐，是名詞作狀語。", "把詞放回它修飾的動作前後，檢查它是在指物、做動作還是說明動作方式。"),
 ("一詞多義", "下列「顧」的意思，哪一項與「元方入門不顧」中的「顧」相同？", ["回頭看：顧野有麥場", "拜訪：三顧茅廬", "考慮：顧念家人", "但是：顧此失彼"], "A", "元方沒有回頭看，顧野有麥場也是回頭看田野；其他選項分別是拜訪、掛念或轉折。", "先替目標字找動作對象，再用選項句子逐一代換，不因字形相同而忽略語境。"),
 ("語詞結構", "「溫故而知新」中的「故」和「新」形成什麼關係？", ["已知的舊知與新得到的理解相對", "兩個地名並列", "一個人物與一件物品", "動作和地點的關係"], "A", "故是已學過的舊知，新是由舊知推得的新理解，兩詞在時間與知識狀態上形成對照。", "先辨認兩個詞的詞性與語意，再看它們是並列、對比、因果還是修飾。"),
 ("固定搭配", "「不蔓不枝」用來形容文章時，最接近哪種意思？", ["簡潔明快，不牽扯多餘內容", "枝葉茂密，景色漂亮", "文章沒有任何段落", "作者完全沒有感情"], "A", "蔓、枝引申為旁生枝節，形容文章簡潔，不牽扯多餘內容。", "成語要從字面意象連到慣用義，再放回文章評語的語境核對。"),
 ("古義證據", "若古文只寫「遂與外人間隔」，下列哪種作答最穩妥？", ["遂表示於是、接著；仍須依前後文確認事件先後", "遂永遠只能解作完成", "間隔一定是兩人吵架", "只看現代『間隔』就能推知全部故事"], "A", "遂常表示於是或就，間隔表示隔絕；但完整因果仍需前文支持，不能任意補造衝突。", "答案既要給出常見義，也要標示文本尚未提供的因果與人物資訊。"),
 ("完整查證", "遇到陌生古文詞語時，哪套流程最能避免古今義混淆？", ["看上下文與詞性，查注釋或字典，代回整句，再檢查前後事件是否連貫", "直接選現代最常見意思，不必讀全文", "只看成語字面，不管句法", "先猜作者心情，再讓詞義配合猜測"], "A", "完整判讀需要語境、詞性、工具查證與回句驗證，才能控制推論而非被現代直覺帶走。", "把詞義判讀做成可回溯流程，每一步都留下句法或語境證據。"),
]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與目標詞，確認題目要判斷古今義、詞性、搭配或查證流程。",f"建立語境證據：觀察主語、動作、前後詞與時代情境，再區分現代直覺與古文用法；本題核心是「{explanation}」",f"核對正解：選項 {target}「{answer}」能放回原句並保留事件與語意。", "排除誘答：檢查是否把現代義硬套、忽略詞性、只按字面猜，或補出文本沒有交代的心理與因果。", "結論回查：以注釋或可靠字典查證，再把義項代回完整句子，確認前後事件與詞語結構連貫。"]
 item={"id":f"question-chinese-classical-word-meaning-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-content-ab-iv-6"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究古今詞義、詞性、搭配與語境判讀能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫文言詞義題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-classical-word-meaning-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")
