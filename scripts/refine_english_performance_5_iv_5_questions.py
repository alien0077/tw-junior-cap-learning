#!/usr/bin/env python3
"""Refine English 5-IV-5 original questions, answers, explanations, and exam-pattern evidence."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
LESSON = "lesson-english-performance-5-iv-5"
TODAY = "2026-09-26"
SOURCES = [
    {"url": "https://www.nhjh.tp.edu.tw/30/2133/news/19/2021-7/2021-7-30-9-57-24-nf1.pdf", "title": "臺北市立內湖國中109學年度第2學期七年級第1次段考英語科試卷", "year": "109-2", "locator": "PDF第4頁第（三）大題文意字彙第1至10題；依語境及殘留字母補完整字詞", "locatorLevel": "page", "observedPattern": "以句意及字首、字尾等殘留字母提供線索，要求考生重建完整英文拼字；本題另行設計規則辨識情境與詞項。"},
    {"url": "https://www.nhjh.tp.edu.tw/uploads/1675415417084qr49L1rs.pdf", "title": "臺北市立內湖國中111學年度第1學期七年級第1次段考英語科答案卷", "year": "111-1", "locator": "PDF第4頁第A區第41至44題大小寫互換、第B區第45至49題名詞單複數拼寫", "locatorLevel": "page", "observedPattern": "校方公開答案卷明列大小寫轉換及名詞複數拼寫任務；本題只參照拼寫規則與作答型態，不使用其字詞或答案。"},
    {"url": "https://www.dam.kh.edu.tw/upload/68/101_28414/106-1%E4%B8%80%E5%B9%B4%E7%B4%9A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C%28%E5%90%AB%E8%A7%A3%E7%AD%94%29.pdf", "title": "高雄市立大社國中106學年度第1學期七年級第1次段考英語科試題（含解答）", "year": "106-1", "locator": "試卷第一大題英語大小寫、第二大題文意字彙", "locatorLevel": "paper", "observedPattern": "公校段考把字母大小寫與語境字彙拼寫列為分項能力；本題另行設計音形規則，不複製題目或答案。"},
]
KEYS = {1: "D", 2: "B", 3: "C", 4: "A", 5: "D", 6: "B", 7: "C", 8: "A", 9: "D", 10: "B"}
CORRECT = {1: "train", 2: "library", 3: "hope", 4: "/t/", 5: "cries", 6: "making", 7: "cat", 8: "stop", 9: "boxes", 10: "cleaned"}
SOLUTIONS = {
1: ("從 rain 的母音拼寫開始做字形比對，不要只憑首尾字母猜韻腳。", ["把 rain 拆看為 r-a-i-n，題目問的是長 a 的拼寫模式。", "指出 ai 是連在一起的母音字母組，在 rain 中對應長 a 音。", "檢查選項是否同時保留 ai，且該字母組也讀出相同音值。", "train 符合；ran 少 i，ring 與 rent 的母音組合和音值都不同。", "答案 D：rain／train 共用 ai → 長 a 的對應。"]),
2: ("先由借書地點的語意鎖定目標詞，再以分段拼字檢查常見漏字。", ["borrowed books 指向可以借閱書籍的場所，目標詞是 library。", "按音節檢查 li-bra-ry，留意中間的 r 不能省略。", "再核對尾段字母是 -ary，而不是把中間母音誤換成 e。", "libary 漏 r；librery、liberry 都把目標詞中的 a 寫錯。", "答案 B：library，逐段回讀拼字與句意。"]),
3: ("把候選字和去掉字尾 e 的近似字配對，觀察唯一改變的是哪個母音音值。", ["題目要找讓前面母音讀長音的 silent-e 型態。", "hope 以 o-e 跨越一個子音形成常見 magic-e 拼法。", "對照 hop 和 hope：字尾 e 不發音，卻使 o 從短音轉為長音。", "hot 沒有字尾 e；help 的母音及拼寫結構也不是此模式。", "答案 C：hope 展示 o-e 的長母音模式。"]),
4: ("判斷 -ed 時先移除字尾、聽字根末音的清濁，再套用三分規則。", ["把 washed 還原為 wash，先不依拼寫字母 d 作答。", "wash 的最後一個音是清音 /ʃ/，不是有聲子音，也不是 /t/ 或 /d/。", "規則動詞在清音後的 -ed 通常讀 /t/。", "/d/ 用於多數有聲音之後；/ɪd/ 只接字根末音 /t/ 或 /d/。", "答案 A：washed 的 -ed 讀 /t/。"]),
5: ("分開處理主詞一致與字尾變化：先決定動詞形式，再拼寫該形式。", ["The baby 是單數第三人稱，現在簡單式動詞需加 -s。", "字根 cry 的 y 前面是子音 r，因此不能直接寫 crys。", "子音加 y 的字尾先把 y 改成 i，再加 -es。", "變化後是 cries；cryes 保留 y，crys 少了規則要求的 e，criez 拼法錯誤。", "答案 D：The baby cries，主詞一致且 y→i＋es。"]),
6: ("辨識字根是 silent-e 型態後，套用加 -ing 時刪除不發音 e 的規則。", ["make 的末尾 e 是不發音字母，字根可看成 mak＋e。", "加 -ing 時通常刪除這個字尾 e，避免把 e 留在字中。", "把 make 去 e，再接 ing，得到 m-a-k-i-n-g。", "makeing 留下不該保留的 e；makking 多加 k；makaing 插入 a。", "答案 B：make＋ing → making。"]),
7: ("看 c 後面的字母並核對實際起始音；不要把規則誤記成每個 c 都讀 /k/。", ["題目限定字首 c 要讀 /k/，因此先比較 c 後接的母音字母。", "cat 的 c 後接 a，符合 c 在 a、o、u 前常讀 /k/ 的模式。", "city、cent 的 c 接 i 或 e，常讀 /s/；cycle 的起始 c 也讀 /s/。", "逐字朗讀可確認只有 cat 以 /k/ 開始，其餘不是目標音。", "答案 C：cat 的字首 c 表示 /k/。"]),
8: ("連音群每個子音都聽得到；拆開頭兩音再合併，而不是只看字母數。", ["把題目指定的 /st/ 拆成連續的 /s/ 與 /t/。", "stop 開頭字母 st 對應兩個可聽見的子音音素。", "快速合讀 /s/＋/t/，後面再接短母音和 p，形成 stop。", "top 缺少 /s/；shop 起音是 /ʃ/；soap 的第二個音是母音而非 /t/。", "答案 A：stop 保留 /s/、/t/ 兩音的 consonant blend。"]),
9: ("先辨認名詞的末尾字母群，再選擇複數字尾，不要把所有名詞都直接加 s。", ["box 的最後字母是 x，讀音結尾含 /ks/。", "以 s、x、sh、ch 等音結尾的許多名詞，複數需加 -es 方便發音。", "box＋es 形成 boxes，字根 box 保持不變。", "boxs 漏掉 e；boxies 套錯子音＋y 規則；boxez 使用錯誤字母。", "答案 D：one box，two boxes。"]),
10: ("比較 -ed 前一個音而非前一個字母；/t/、/d/ 由字根末音清濁決定。", ["played 的字根是 play，最後音 /eɪ/ 為有聲音，因此 -ed 讀 /d/。", "逐一去掉各選項的 -ed，聽字根最後音再判斷後綴讀音。", "clean 的末音 /n/ 有聲，故 cleaned 的 -ed 同樣讀 /d/。", "wash、laugh、miss 分別以清音結尾，後綴 -ed 都讀 /t/。", "答案 B：played 與 cleaned 同為有聲末音＋/d/。"]),
}

def main() -> None:
    for number, key in KEYS.items():
        path = OUT / f"question-english-performance-5-iv-5-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["lessonId"] == LESSON
        old_key = data["answer"]["value"]
        options = {item["id"]: item["text"] for item in data["options"]}
        correct = options[old_key]
        assert correct == CORRECT[number], (number, correct, CORRECT[number])
        remaining = [item["text"] for item in data["options"] if item["id"] != old_key]
        remaining.insert(ord(key) - ord("A"), correct)
        data["options"] = [{"id": chr(65 + index), "text": value} for index, value in enumerate(remaining)]
        strategy, steps = SOLUTIONS[number]
        data["answer"] = {**data["answer"], "value": key, "explanation": steps[-1]}
        data["solutionStrategy"], data["solutionSteps"] = strategy, steps
        data["reviewStatus"], data["updatedAt"] = "draft", TODAY
        data["provenance"]["sourceUrl"] = SOURCES[0]["url"]
        data["provenance"]["sourceLocator"] = "內湖國中109-2七年級第1次段考PDF第4頁（三）文意字彙1–10題；內湖111-1七年級第1次段考答案卷PDF第4頁大小寫及單複數拼寫；大社國中106-1七年級第1次段考第一、二大題。只參照公開評量的拼字任務形式與能力層次，不複製原卷字詞、題幹或答案。"
        data["provenance"]["authoringNote"] = "依官方課綱與KG-english-performance-5-iv-5，參照三所公立學校公開英語評量的語境補字、大小寫及單複數拼寫任務，獨立撰寫音形規則題；情境、選項、正解解析及策略均為原創。出版社融合與完整內容審查未完成，維持draft。"
        data["examPatternRefs"] = [{
            "url": source["url"], "title": source["title"], "year": source["year"], "subject": "english",
            "locator": source["locator"], "locatorLevel": source["locatorLevel"],
            "observedPattern": source["observedPattern"], "reuseDecision": "pattern-only", "status": "recorded",
        } for source in SOURCES]
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("refined ten English 5-IV-5 questions with varied keys, item-specific solutions, and located public-school patterns")

if __name__ == "__main__":
    main()
