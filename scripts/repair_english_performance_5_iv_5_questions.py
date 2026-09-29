import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "english"
LESSON = "lesson-english-performance-5-iv-5"
KG = "kg-english-performance-5-iv-5"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "title": "高雄市立鹽埕國民中學公開英文評量", "year": "113-114"},
    {"url": "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "title": "新北市立北投國民中學公開定期評量試題頁", "year": "113-114"},
    {"url": "https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "title": "新北市立新埔國民中學公開段考試題頁", "year": "113-114"},
]

def refs():
    return [{**s, "subject": "english", "locator": "phonics, spelling, sound-letter patterns, and word-form selection", "observedPattern": "公開英文評量常以音形對應、拼字、字尾與語境辨識基本字彙；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-english-performance-5-iv-5-{i}", "subject": "english", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開英文評量僅供拼讀、音形對應與拼字規則能力方向研究；未複製原題、選項、文章或答案。", "authoringNote": "依官方課綱 KG 與三筆公開英文試題的拼讀與拼字能力方向獨立改寫；題幹、選項、解析與轉移任務均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "Which word has the same long-a spelling pattern as 'rain'?", {"A": "train", "B": "ran", "C": "ring", "D": "rent"}, "A", "Train uses the same ai vowel team as rain to represent the long-a sound.", "先找 rain 的核心 vowel team，再比較選項是否保留相同的字母與音值。", ["圈出 rain 中的 ai。", "辨認 ai 在 rain 中共同表示長母音音值。", "逐一查看選項，找出也含 ai 且音值相近的字。", "排除 ran、ring、rent，它們沒有相同的 ai 拼讀模式。", "選 A，將 rain 與 train 並讀確認音形對應。"], "easy"),
make(2, "Choose the correctly spelled word for a place where books are borrowed.", {"A": "libary", "B": "library", "C": "librery", "D": "liberry"}, "B", "Library is the standard spelling. The middle r is part of the word and the final syllable is spelled -ary.", "把語意線索與字母順序一起核對，不只依發音猜拼字。", ["先用 borrowed books 判斷目標字是 library。", "分段檢查 lib-rar-y 的字母順序。", "確認中間保留 r，字尾寫作 ary。", "比較四個選項，找出只有 B 完整符合標準拼法。", "選 B，逐字母回讀 library，確認沒有漏 r 或誤寫 e。"], "easy"),
make(3, "Which word shows the silent-e pattern that makes the vowel long?", {"A": "hope", "B": "hop", "C": "hot", "D": "help"}, "A", "The final e in hope is silent but changes the o to a long-o sound; the other words do not use this pattern.", "找出字尾 silent e，再比較有無 e 對母音音值的影響。", ["查看四個字的最後字母。", "找出 hope 的字尾 e 不另發音但改變前一母音。", "將 hope 與 hop 對照，確認 silent-e 造成長母音。", "排除 hot、help，因為它們沒有相同的 o-e 結構。", "選 A，朗讀 hope 並說明 e 的功能是改變 o 的音值。"], "medium"),
make(4, "The word 'washed' ends with -ed. Which sound does -ed have here?", {"A": "/t/", "B": "/d/", "C": "/ɪd/", "D": "It is not pronounced"}, "A", "The base verb wash ends with the voiceless /ʃ/ sound, so -ed is pronounced /t/ in washed.", "先看字根最後音，再依 -ed 的發音規則判斷，不只看字母 d。", ["圈出 washed 的字尾 -ed。", "去掉字尾，辨認 wash 最後是清音 /ʃ/。", "套用清音後 -ed 通常讀 /t/ 的規則。", "排除 /d/、/ɪd/ 與不發音，因為它們不符合 wash 的末音。", "選 A，將 washed 讀成包含 /t/ 的結尾並回查規則。"], "hard"),
make(5, "Which word correctly completes: 'The baby ____ when she is hungry.'?", {"A": "crys", "B": "cries", "C": "cryes", "D": "criez"}, "B", "Cry changes y to i before -es, so the third-person singular form is cries.", "辨認子音加 y 的字尾規則，再檢查第三人稱單數的拼字變化。", ["先看主詞 The baby，判斷動詞需要第三人稱單數。", "找出 cry 以子音 y 結尾。", "套用 y 改 i 再加 es 的規則。", "比較選項，只有 cries 正確完成兩個字母變化。", "選 B，回讀 baby cries 並確認語意是飢餓時哭。"], "medium"),
make(6, "Which spelling follows the rule for adding -ing to 'make'?", {"A": "makeing", "B": "making", "C": "makking", "D": "makaing"}, "B", "Make drops its final silent e before -ing, producing making.", "先判斷字根是否有 silent e，再依加 -ing 的刪 e 規則拼寫。", ["圈出 make 的最後 e，確認它是字根字尾。", "判斷加 -ing 時不保留 silent e。", "將 make 去掉 e，再加 ing 得到 making。", "排除 makeing、makking、makaing，這些都違反字尾規則。", "選 B，逐字母確認 m-a-k-i-n-g。"], "easy"),
make(7, "Which word begins with the /k/ sound spelled with 'c' before a, o, or u?", {"A": "cat", "B": "city", "C": "cent", "D": "cycle"}, "A", "In cat, c comes before a and represents /k/. Before e or i, c commonly represents /s/.", "同時檢查 c 後的母音與實際音值，避免只背 c 永遠讀 /k/。", ["找出四個字開頭的 c。", "查看 c 後面的母音：A 是 a，其餘多為 i 或 y。", "套用 c before a、o、u 常讀 /k/ 的規則。", "排除 city、cent、cycle，它們的 c 通常呈現 /s/。", "選 A，朗讀 cat 並確認開頭是 /k/。"], "medium"),
make(8, "Which word has the consonant blend /st/ at the beginning?", {"A": "stop", "B": "top", "C": "shop", "D": "soap"}, "A", "Stop begins with the two-consonant blend /st/; top lacks /s/, and the other choices begin differently.", "把開頭連續子音拆音，再找兩個音都保留的選項。", ["圈出每個選項的開頭字母。", "確認 stop 以 s 加 t 連續起首。", "將 /s/ 與 /t/ 連讀成 /st/。", "排除 top 少了 s，shop 與 soap 的開頭音不同。", "選 A，慢讀後合併 stop 的起始連音。"], "easy"),
make(9, "Which spelling correctly completes: 'The plural of 'box' is ____.'", {"A": "boxs", "B": "boxes", "C": "boxies", "D": "boxez"}, "B", "Words ending in x add -es for the plural, so box becomes boxes.", "先看字尾 x，再套用需要加 -es 的複數規則。", ["圈出 box 的最後字母 x。", "判斷 x 結尾的名詞不能只加 s，通常要加 es。", "將 box 加 es 得到 boxes。", "排除 boxs、boxies、boxez，逐一檢查字尾拼法。", "選 B，回讀 one box、two boxes 確認數量與拼字。"], "medium"),
make(10, "Which word has the same final /d/ sound as 'played'?", {"A": "cleaned", "B": "washed", "C": "laughed", "D": "missed"}, "A", "Played and cleaned end with a voiced sound before -ed, so -ed is pronounced /d/; the other choices end with /t/.", "比較字根最後音的清濁，再判斷 -ed 的結尾音，而非只看字尾字母。", ["圈出 played 與各選項的 -ed。", "辨認 play 最後音為有聲音，故 -ed 讀 /d/。", "逐項檢查 cleaned、washed、laughed、missed 的字根末音。", "確認 cleaned 也接在有聲音後，其他三個多接清音而讀 /t/。", "選 A，將 played 與 cleaned 的結尾音互相比較。"], "hard"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")
