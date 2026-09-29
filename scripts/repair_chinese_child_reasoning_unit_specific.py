#!/usr/bin/env python3
"""把 11 個中文 child lesson 題目的解題欄位改成單元專屬寫法。

只修改 solutionStrategy／solutionSteps；題幹、選項、answer.value、解析與來源不改。
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = sorted((ROOT / "questions" / "chinese").glob("question-chinese-content-*.json"))
UNIT_IDS = {
    "ab-iv-1", "ab-iv-2", "ab-iv-3", "ab-iv-4", "ab-iv-5", "ab-iv-6",
    "ab-iv-7", "ab-iv-8", "ac-iv-1", "ac-iv-2", "ad-iv-1",
}


def option_text(item: dict) -> str:
    answer = item["answer"]["value"]
    return next(o["text"] for o in item["options"] if o["id"] == answer)


def build(unit: str, item: dict) -> tuple[str, list[str]]:
    prompt = item["prompt"]
    answer = item["answer"]["value"]
    chosen = option_text(item)
    if unit == "ab-iv-1":
        strategy = "先把字音放回完整詞語，再同時核對聲音、詞義與公告或語境中的動作；不要只因部件相近就猜讀音。"
        steps = [f"圈出詞語與題目要求：{prompt}", "先以詞典式讀音判斷聲調與聲母，再暫不看選項位置。", f"把語詞放回原句，檢查它描述的動作或時間限制是否合理：{chosen}。", "逐項排除音近、形近或把詞義偷換成另一個動作的干擾。", f"最後朗讀原句並回查，確認選項 {answer} 的讀音與語境義同時成立。"]
    elif unit == "ab-iv-2":
        strategy = "把詞語當成句子中的功能零件，先看搭配對象與語氣，再判斷近義詞、關聯詞或形近字是否真的合用。"
        steps = [f"找出句中需要判斷的字詞功能：{prompt}", "查看它前後的主語、受詞與語氣，建立可接受的搭配條件。", f"用選項 {answer} 代回句子，檢查語意關係、語法位置與語氣是否完整：{chosen}。", "排除只在字面相近、但搭配對象或因果關係不成立的選項。", f"重讀整句，確認答案 {answer} 不是只符合單字意思，而是符合整個句子的使用情境。"]
    elif unit == "ab-iv-3":
        strategy = "造字題要分開看意符、聲符與構件關係：先描述構件提供的線索，再判斷它是表意、標示位置、組合意義或聲義分工。"
        steps = [f"鎖定題目要求的構件或造字線索：{prompt}", "逐一說明每個部件在字形中的位置與可能功能，不把讀音直接當成字義。", f"以選項 {answer} 的造字判準對照構件證據：{chosen}。", "排除只憑外形聯想、把聲符誤當意符，或缺少構件證據的說法。", f"回看整個字形，確認答案 {answer} 能解釋可見構件與字義／字音的關係。"]
    elif unit == "ab-iv-4":
        strategy = "成語與常用語不能只背單句翻譯；要用前後文、語氣與搭配對象確認它是在描述行動、態度、結果還是批評。"
        steps = [f"先讀完整語境並圈出成語的使用位置：{prompt}", "用自己的話說出句中需要的語氣或行動效果。", f"把選項 {answer} 放回原句，檢查主語、情境與褒貶是否一致：{chosen}。", "特別排除字面可通但語氣不合、搭配錯誤或把寓意縮窄的選項。", f"再讀一次前後句，確認答案 {answer} 能解釋整個語境而非只解釋其中一個字。"]
    elif unit == "ab-iv-5":
        strategy = "詞語使用要從語體與觀察角度切入：比較詞語的精確範圍、正式程度、情感色彩與可搭配的對象，再選最貼合的一項。"
        steps = [f"辨認題幹要表達的觀察、態度或語體需求：{prompt}", "列出必要條件，例如是否客觀、是否有意識地查看、是否需要書面語。", f"逐項代換並檢查選項 {answer} 的語意強度與搭配：{chosen}。", "刪去意思太寬、情感色彩不符或只在口語中自然的干擾。", f"把答案 {answer} 放回原句，確認讀者能從詞語精確理解題幹要求。"]
    elif unit == "ab-iv-6":
        strategy = "文言詞語結構要先找核心動作與修飾方向，再用古今語境判斷詞義；不可直接把現代常用義套回古文。"
        steps = [f"先切分詞組並確認題目要判斷的是結構或古義：{prompt}", "問自己『誰做什麼』『什麼修飾什麼』，標出詞內的主從或並列關係。", f"以選項 {answer} 解釋原句，再核對古今詞義是否吻合：{chosen}。", "排除只符合現代口語、但無法解釋古文句法位置的選項。", f"回譯整個詞組或句子，確認答案 {answer} 同時符合結構、古義與上下文。"]
    elif unit == "ab-iv-7":
        strategy = "虛詞判讀必須依句中位置與前後詞的關係；先辨它連接、代指、介引或語氣功能，再比較相同字在不同句子的作用。"
        steps = [f"抄出虛詞所在的完整短句，避免只看單一字：{prompt}", "觀察虛詞前後的詞性與句法位置，判斷它是在連接、代指、介引或表達語氣。", f"用選項 {answer} 的白話功能代回原句，檢查句意是否通順：{chosen}。", "與其他選項交換測試，排除只因字面翻譯相近、但句法角色不同的答案。", f"最後同時回看前後分句，確認答案 {answer} 解釋的是本句功能而非這個字的固定翻譯。"]
    elif unit == "ab-iv-8":
        strategy = "書法欣賞要把感覺轉成可觀察證據：看筆畫、結構、字距、行氣與留白，再用作品中的具體位置支持判斷。"
        steps = [f"先確認題目要求觀察的書體或形式特徵：{prompt}", "把抽象形容詞改寫成可指出的證據，例如筆畫方向、字間距或重心。", f"檢查選項 {answer} 是否能被作品中的多個位置核對：{chosen}。", "排除只有『好看』『有力量』等無法定位證據，或把不同書體特徵混用的說法。", f"回到作品整體，確認答案 {answer} 的描述可由他人依同一視覺線索重複判斷。"]
    elif unit == "ac-iv-1":
        strategy = "標點題先還原句子的語意層次與說話者關係，再判斷停頓、列舉、引用、轉折或問答功能；標點不是按句子長短亂放。"
        steps = [f"先讀未標或待修改的句子，指出需要分開的語意單位：{prompt}", "判斷句子是在列舉、引述、承接、轉折、提問還是說明條件。", f"把選項 {answer} 的標點放回原句，朗讀並檢查層次：{chosen}。", "排除只靠停頓感、卻改變引用範圍或句間邏輯的選項。", f"最後從頭讀到尾，確認答案 {answer} 讓讀者能正確還原語意與語氣。"]
    elif unit == "ac-iv-2":
        strategy = "句型判讀先找主語、動作、受事與存在位置，再看主動／被動、判斷、敘事或表態功能；句尾標點只是輔助線索。"
        steps = [f"抽出句子的核心成分並標記動作方向：{prompt}", "確認誰是動作者、誰是受事者，以及句子是在存在、敘述、判斷、要求或表態。", f"用選項 {answer} 的句型名稱對照成分關係：{chosen}。", "排除只看句尾、只看某個助詞或忽略主受事方向的判斷。", f"把句型改述成白話，確認答案 {answer} 保留原句的核心關係與語氣功能。"]
    elif unit == "ad-iv-1":
        strategy = "篇章題要把局部線索放進結構：先整理人物／事件或主張／證據的順序，再用轉折、結尾回扣與全文共同判斷主旨和推論。"
        steps = [f"先標記題幹提供的事件、觀點、證據與轉折線索：{prompt}", "用一句話整理段落如何開始、發展與收束，避免只抓最醒目的單句。", f"逐項比對選項 {answer} 是否涵蓋全文關係而非只重述一個細節：{chosen}。", "排除過度延伸、忽略轉折、只講人物表面行為或缺少證據的選項。", f"回到全文結構驗證答案 {answer}，確認它能同時說明開頭、發展與結尾的共同方向。"]
    else:
        raise ValueError(unit)
    return strategy, steps


def main() -> int:
    changed = 0
    for path in TARGETS:
        item = json.loads(path.read_text(encoding="utf-8"))
        unit = item.get("lessonId", "").split("content-")[-1]
        if unit not in UNIT_IDS:
            continue
        strategy, steps = build(unit, item)
        strategy = (
            f"{strategy} 本題焦點是「{item['prompt']}」；"
            f"作答時須以選項 {item['answer']['value']}「{option_text(item)}」的判準完成回查，"
            "不能把同單元的其他題目答案直接套用。"
        )
        item["solutionStrategy"] = strategy
        item["solutionSteps"] = steps
        item["reviewStatus"] = "draft"
        path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    report = {
        "changed": changed,
        "units": sorted(UNIT_IDS),
        "scope": "11 Chinese content-child units; prompt/options/answer/explanation/source unchanged",
        "reviewStatus": "draft",
    }
    out = ROOT / "implementation" / "reports" / "chinese-child-unit-specific-reasoning-repair.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
