#!/usr/bin/env python3
"""Author lesson-level interactions for legacy standalone lessons without specs."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def make(goal, scenario, steps):
    return {
        "type": "guided-choice",
        "goal": goal,
        "scenario": scenario,
        "steps": [
            {"id": f"step-{i}", "prompt": prompt, "options": [correct, wrong], "answer": "A", "feedback": feedback}
            for i, (prompt, correct, wrong, feedback) in enumerate(steps, 1)
        ],
    }


INTERACTIONS = {
    "lesson-chinese-argument-evidence-basics": make(
        "辨認主張、事實性論據與推論連結",
        "把一段校園是否延長午休的短文拆成主張、資料與推理箭頭，再檢查結論是否超出證據。",
        [("先找哪一層？", "圈出作者希望讀者接受的主張", "先選最有氣勢的句子當答案", "主張是要被支持的結論，不等於語氣最強的句子。"), ("什麼能當論據？", "定位可查證的數據或事件並說明與主張的關係", "只引用作者的感受", "論據需要可核對，還要說明它如何支持主張。"), ("如何檢查推論？", "指出資料到結論中間的連接理由與限制", "把資料重抄一次就算證明", "推論要交代連結，並承認資料不能支持的範圍。")]),
    "lesson-chinese-calligraphy-appreciation": make(
        "以筆畫、結體、章法與背景證據描述書法風格",
        "在虛構校展中比較兩幅碑帖局部，從可定位的筆畫與行列證據寫出鑑賞判斷。",
        [("觀看作品先做什麼？", "記錄筆畫運行、結體與行列等可見特徵", "直接用漂亮或有氣勢下結論", "鑑賞需要先有可定位的觀察，再形成風格解釋。"), ("如何說明風格？", "把特徵與書寫材料、用途或流傳背景連起來", "只背名家姓名", "背景能補充解釋，但不能取代作品本身的證據。"), ("如何避免過度推論？", "明確寫出作品支持的判斷與仍缺少的資料", "把個人喜好當成作者意圖", "好的鑑賞同時呈現理由與界線。")]),
    "lesson-chinese-classical-function-words": make(
        "依句法與篇章判斷文言虛字功能並轉寫語氣",
        "把同一個文言虛字放入三個自編句子，觀察它和前後成分的關係，再比較白話轉寫是否保留邏輯。",
        [("遇到虛字先看什麼？", "看它和前後詞語及分句的句法關係", "直接套用最常見的現代翻譯", "同字可能有不同功能，位置與上下文是必要證據。"), ("如何選義？", "比較代指、連接、介引或語氣等候選並回讀原句", "只依字典第一個義項", "字典提供候選，原句才能決定功能。"), ("白話翻譯要保留什麼？", "保留指向、邏輯關係與語氣強弱", "只逐字替換而不管句意", "轉寫的目標是保留句子作用，不是字面排列。")]),
    "lesson-chinese-classical-word-meaning": make(
        "用詞性、句法、上下文與回讀驗證文言詞義",
        "面對一個古今同形詞，先列出可能詞義，再用原句、對偶和篇章語氣逐一排除。",
        [("詞義推論第一步？", "先觀察詞性與它在句中的位置", "脫離句子背唯一翻譯", "詞性與句法能先排除不合的候選。"), ("哪種證據較有力？", "用上下文、對偶與語氣比較候選解釋", "只看現代常用意思", "古今同形不代表意義相同，篇章證據要優先。"), ("如何驗證翻譯？", "把完整白話放回原句檢查關係與語氣是否通順", "只確認每個字都有對應字", "回讀能發現省略、指向或因果被漏掉。")]),
    "lesson-chinese-common-character-form-sound-meaning": make(
        "以部件、讀音、搭配與語境辨識常用字",
        "校對一張社團海報中的形近字與同音字，留下選字證據後再用朗讀和回述確認。",
        [("看到形近字先做什麼？", "提出部件提供的形音線索並回到詞語", "只挑看起來最像的字", "部件只是線索，詞語與句子才能驗證。"), ("如何排除同音字？", "用搭配、詞義和句中角色比較候選字", "只依讀音相同就互換", "同音不等於同義，搭配能提供可檢查的差異。"), ("怎麼確認真的理解？", "朗讀、解釋詞義並在新句中正確使用", "抄寫字形一次就算學會", "形音義要能在語境中互相支持。")]),
    "lesson-chinese-common-phrases-advanced": make(
        "依事件條件、語氣、搭配與文體選用語詞",
        "為校刊同一段訊息準備正式版與口語版，比較近義詞的感情色彩和搭配是否合適。",
        [("選詞前先問什麼？", "確認事件條件、說話者態度與溝通目的", "只挑字面最華麗的詞", "語詞是否合適取決於情境，不是華麗程度。"), ("近義詞怎麼比較？", "對照搭配對象、感情色彩與語體", "把近義詞視為完全可互換", "近義詞的細微差異會改變語氣與責任。"), ("跨語體改寫要注意？", "保留核心意思並調整正式程度與讀者預期", "只把四字詞全部換成口語", "改寫既要保留內容，也要符合新的溝通場景。")]),
    "lesson-chinese-common-phrases-usage": make(
        "依詞義、詞性、搭配、語體與感情色彩正確用詞",
        "替校園公告挑選三個近義詞，先判斷對象與目的，再檢查句子是否自然。",
        [("詞語能不能放進句子？", "先確認詞性與搭配對象", "只看字面意思相近就填入", "詞性和搭配會限制詞語能否成立。"), ("語境判斷要看什麼？", "比較說話對象、正式程度與情感方向", "忽略公告與聊天的語體差異", "相同意思在不同語體可能需要不同詞語。"), ("完成後如何回查？", "朗讀整句並說明詞語帶來的態度", "只檢查字有沒有寫對", "用語是否負責任還要看語氣與對象。")]),
    "lesson-chinese-common-words-recognition": make(
        "在完整詞語與語境中核對字音、字形與詞義",
        "校對校園廣播與社團公告中的多音、形近和音近詞，完成朗讀、回述與改寫。",
        [("辨認陌生詞先保留什麼？", "把字音、字形與完整詞語一起記錄", "只把每個字分開朗讀", "詞語整體才能提供語義與讀音線索。"), ("如何查證理解？", "用上下文、查證來源和詞語搭配互相核對", "看到熟悉字就自行猜完", "熟字組合也可能改變意思，需要證據。"), ("怎麼確認訊息傳達？", "用自己的話回述，再在新句中改寫", "只抄寫原句", "回述與改寫能測到真正理解，而非表面認讀。")]),
    "lesson-chinese-main-idea-structure": make(
        "由段落功能、轉折、反覆線索與結尾推回主旨",
        "閱讀一篇自編校園觀察短文，將各段標記為事件、轉折或反思，再比較主旨與自行添加的寓意。",
        [("找主旨先看什麼？", "追蹤材料安排與反覆出現的線索", "把每段第一句拼在一起", "主旨關乎材料如何共同指向關係，不是段落摘要相加。"), ("結構如何提供證據？", "說明轉折、照應與結尾如何改變讀者理解", "只挑最感人的句子", "結構證據能解釋作者如何安排讀法。"), ("寓意判斷要有界線嗎？", "區分文本支持的寓意與讀者額外聯想", "把所有感想都當成作者意圖", "解讀必須標明哪些能由文本支持。")]),
    "lesson-chinese-punctuation-effects-advanced": make(
        "依語意關係、聲音與引述功能安排標點",
        "在校園廣播字幕剪輯中，為同一段話安排不同標點並比較句意、停頓與引述層次。",
        [("切句前先確認什麼？", "先辨認分句的語意關係與主次", "只依說話時的呼吸停頓", "標點要呈現語意骨架，不能只靠感覺停頓。"), ("引述文字要注意？", "用引號與冒號等標示說話者和被引用內容", "把所有聲音混成一段", "標點會影響責任歸屬與讀者判斷。"), ("改完如何檢查？", "朗讀並比較不同標點造成的語氣與關係", "只看符號數量是否足夠", "要驗證標點改變了什麼意義，而不是追求越多越好。")]),
    "lesson-chinese-punctuation-effects": make(
        "觀察標點如何改變停頓、層次、語氣與句間關係",
        "替失物招領、採訪逐字稿和提醒訊息校訂標點，先說明讀者可能如何理解，再選擇寫法。",
        [("逗號與句號的差別？", "比較分句是否仍屬同一信息與語氣是否收束", "把所有停頓都換成逗號", "標點同時管理關係與停頓，不能只按口語節奏。"), ("冒號、引號何時重要？", "需要引出說明或標示原話時清楚分層", "用符號裝飾句子", "讀者要能看出後文和前文的關係或說話者。"), ("完成後怎麼驗證？", "朗讀、回述可能意思並檢查是否產生歧義", "只確認每句都有標點", "有效標點要讓讀者較穩定地理解。")]),
    "lesson-chinese-sentence-patterns": make(
        "用句型區分敘事、存在、判斷與表態的資訊責任",
        "在班級公約提案辯論中，把同一事件改寫成記錄、事實聲明、價值評語與待討論主張。",
        [("先判斷句子在做什麼？", "看它是在敘述事件、指出存在、判斷或表達立場", "只看句子長短", "句型分配資訊與責任，不由長短決定。"), ("改寫時要保留什麼？", "保留事件內容並明確改變說話者的立場位置", "只替換幾個形容詞", "不同句型會改變哪些內容被當成事實或主張。"), ("如何檢查責任？", "指出哪一句需要證據、哪一句是待辯論的價值判斷", "把意見包裝成客觀事實", "表達清楚才能讓讀者知道如何查證或回應。")]),
    "lesson-chinese-six-forms-character-making": make(
        "比較象形、指事、會意與形聲的構形線索與限制",
        "進行字源偵探：從古文字圖像、部件位置與讀音線索比較四種構形方式，再區分古今字形。",
        [("分析字形先看什麼？", "觀察它是描摹事物、提示抽象位置、合併意義或提供聲音線索", "把每個部件都當成現代意思", "構形類型提供不同線索，不能用單一規則套全部漢字。"), ("形聲字如何驗證？", "分開檢查意義部件與聲音部件能否支持判斷", "因讀音相近就說一定是形聲", "聲符是線索而非絕對同音，還要對照字源與現代讀音。"), ("古今比較要保留界線嗎？", "區分古代構形、現代字形與今天的讀音", "把現代部件解釋直接當成古人造字原因", "不同時代的資料不能互相冒充證明。")]),
    "lesson-chinese-source-reliability": make(
        "辨認作者、目的、論據與來源範圍並縮小結論",
        "檢查三則校園社群貼文：追查原始發布者、時間與引用資料，判斷哪些結論仍需保留。",
        [("收到訊息先查什麼？", "記下作者、發布時間、目的與原始連結", "先看轉發數量決定真假", "流量不是來源可靠性的證據。"), ("如何檢查論據？", "把可查證事實和推論分開並比較獨立來源", "把作者語氣當成證據", "語氣只能表達態度，不能替代資料。"), ("結論要縮到哪裡？", "只說證據真正支持的範圍並標記未知部分", "把單一案例推成普遍規則", "可靠閱讀包括知道不能推出什麼。")]),
    "lesson-english-context-clues": make(
        "Use nearby words, sentence structure, and contrast clues to infer an unfamiliar word",
        "Read a short school announcement with one unfamiliar word; underline clues, propose meanings, and check the sentence again.",
        [("What should you do first?", "Look for nearby examples, definitions, or contrasts", "Choose a meaning from the first translation you remember", "Context clues must come from the sentence and paragraph."), ("How do you test a guess?", "Replace the word and check grammar and meaning", "Keep the guess because the spelling looks familiar", "A good guess must fit both structure and message."), ("What if evidence is weak?", "Keep more than one possible meaning and find another clue", "Pretend the first guess is certain", "Good readers show uncertainty until context resolves it.")]),
    "lesson-english-fact-opinion": make(
        "Distinguish checkable facts, opinions, and claims with insufficient evidence",
        "Read an English school-lunch proposal and label each sentence by its evidence, wording, and level of certainty.",
        [("How can you spot a fact?", "Ask whether the statement can be checked with a source or measurement", "Treat a confident sentence as a fact", "Confidence is not evidence."), ("How can you spot an opinion?", "Look for evaluation words, preferences, or recommendations", "Assume every number proves the writer's conclusion", "Numbers need context and may still be used to support an opinion."), ("How should you write a conclusion?", "Separate what the text shows from what still needs evidence", "Repeat the strongest claim without checking", "A careful conclusion matches its certainty to the evidence.")]),
    "lesson-social-media-literacy": make(
        "檢查網路訊息的主張、來源、證據與結論範圍",
        "比較一則短影音說明與它引用的原始資料，建立主張—證據—限制三欄表。",
        [("看到主張先做什麼？", "把可查證的句子拆出來並找原始來源", "先依按讚數決定可信度", "傳播量與證據品質不是同一件事。"), ("如何判斷證據？", "檢查日期、作者、資料方法與是否真的支持主張", "只要附一張圖就算證明", "圖片也需要來源、時間與脈絡。"), ("如何分享比較負責任？", "標示已知、推論與仍待查證的部分", "把推測改寫成確定消息", "分享時保留限制能降低誤導。")]),
    "lesson-social-opportunity-cost": make(
        "辨認選擇後放棄的最佳替代方案並正確理解機會成本",
        "用週末時間在讀書、打工與休息之間作選擇，列出可行方案、限制與真正放棄的最佳替代方案。",
        [("做選擇前先列什麼？", "列出在限制下真正可行的替代方案", "把所有想過的事情都算成成本", "機會成本只從可行替代方案中比較。"), ("成本是哪一項？", "找出放棄方案中價值最高的最佳替代方案", "把第二、第三名全部相加", "機會成本不是所有放棄項目的總和。"), ("如何說明結果？", "指出選擇、最佳替代方案與判斷價值的標準", "只說最後選了什麼", "完整說明需要同時交代被放棄的最佳選項。")]),
}


def main() -> None:
    changed = []
    missing = []
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        lesson_id = data.get("id")
        if lesson_id not in INTERACTIONS:
            continue
        if data.get("interactive"):
            continue
        data["interactive"] = INTERACTIONS[lesson_id]
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append({"lessonId": lesson_id, "file": str(path.relative_to(ROOT))})
    for lesson_id in INTERACTIONS:
        if lesson_id not in {item["lessonId"] for item in changed}:
            path = next((p for p in (ROOT / "lessons").glob("*/*.json") if json.loads(p.read_text(encoding="utf-8")).get("id") == lesson_id), None)
            if path is None:
                missing.append(lesson_id)
    report = {"updatedAt": "2026-09-07", "changedLessons": len(changed), "missingLessons": missing, "changed": changed, "authoringRule": "standalone lessons individually authored with unit-specific prompts and evidence"}
    out = ROOT / "implementation/reports/orphan-lesson-interaction-authoring.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
