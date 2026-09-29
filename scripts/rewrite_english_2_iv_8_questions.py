#!/usr/bin/env python3
"""Re-author 2-IV-8 sound, prosody, and intelligibility items with exact sources."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DASHE = "https://www.dam.kh.edu.tw/upload/68/101_28414/108-1-1%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%95%E9%87%8F%E8%A9%A6%E9%A1%8C%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf"
DAGANG = "https://web.dgjh.tyc.edu.tw/asp/exam/upload/100%E5%AD%B8%E5%B9%B4%E5%BA%A6%E5%85%AB%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%9C%88%E8%80%83%E5%AD%B8%E7%94%9F%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf"
DAWAN = "https://www.dwm.kh.edu.tw/upload/344/104_64184/113%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf"
SOURCES = {
    DASHE: ("高雄市立大社國中", "108學年度第一學期七年級第一次段考英語科試題", "只參考原卷第1題聽辨/t/與/d/、第2題聽辨/k/與/g/及聽句辨圖題型；題幹、音檔、選項與答案均重新創作。"),
    DAGANG: ("桃園市立大崗國中", "100學年度上學期八年級第二次月考英文科考題", "只參考原卷第1、3題聽音選字詞及第6至10題聽辨合宜回應的任務形式；未複製字詞、對話、選項或答案。"),
    DAWAN: ("高雄市立大灣國中", "113學年度第一學期八年級英語科第一次段考", "只參考原卷第5、6題聽力問答與對話理解任務形式；未複製原卷對話、選項或答案。"),
}

ITEMS = [
    {
        "answer": "C", "source": (DASHE, 1, "PDF page 8 (printed page 1), pronunciation listening question 1"),
        "prompt": "The audio coach says the first sound in ‘tide’ is the voiceless /t/, not /d/. Which listening note records the sound accurately?",
        "options": [("A", "/d/: voice on, tongue at the ridge behind the teeth"), ("B", "/θ/: air passes between the teeth"), ("C", "/t/: voice off, tongue briefly blocks air at the ridge"), ("D", "/n/: voice on, air leaves through the nose")],
        "explanation": "/t/ 與 /d/ 都是舌尖在齒齦處短暫阻氣的塞音，主要差別是 /t/ 不振動聲帶、/d/ 振動聲帶。C 同時指出發音位置與清濁對比。",
        "strategy": "遇到近似子音，分開檢查發音部位、阻氣方式與聲帶是否振動；不要只看拼字或把清濁對立混成不同舌位。",
        "steps": ["先定位要聽的不是整個 tide，而是字首子音；題目已明示目標音為 /t/。", "用手指輕觸喉部發 /t/，聲帶不應持續振動；再發 /d/ 比較即可感到差異。", "兩音都在齒齦附近形成短暫阻塞，所以區分重點是清音 /t/ 與濁音 /d/。", "C 描述無聲帶振動及舌尖阻氣；A 寫的是 /d/，B、D 則改變了發音方式或氣流出口。", "因此選 C；練習時先慢速分辨起音，再放回 tide 等完整單字確認聽辨沒有被拼字干擾。"],
    },
    {
        "answer": "B", "source": (DASHE, 2, "PDF page 8 (printed page 1), pronunciation listening question 2"),
        "prompt": "A headset plays the first sound in ‘gate.’ Which description distinguishes /k/ from its voiced partner /g/?",
        "options": [("A", "/k/ is voiced and made with the lips"), ("B", "/k/ is voiceless and made at the back of the mouth"), ("C", "/k/ is a nasal sound made with the tongue tip"), ("D", "/k/ is the same sound as /s/ but longer")],
        "explanation": "/k/ 與 /g/ 都是舌根在軟顎附近形成的塞音；/k/ 是清音，/g/ 是濁音。B 正確保留發音位置及清濁差異。",
        "strategy": "把成對子音放在同一發音位置比較，只改變聲帶振動這一項；這樣能避免把 /k/、/g/ 誤認成唇音或鼻音。",
        "steps": ["從 gate 的字首抽出 /g/，題目要找的是它的清音對應音 /k/。", "發 /k/ 時舌根靠近軟顎、氣流短暫受阻後釋出，嘴唇不是主要阻塞位置。", "/k/ 不振動聲帶；/g/ 在相同位置發音但聲帶振動，形成清濁配對。", "B 同時說明清音與口腔後部位置；A 把部位和清濁都弄錯，C、D 也不符合塞音特徵。", "所以選 B；可用 cap/gap 等自編最小對立詞交替朗讀，聽出只改一個聲音時字義如何變化。"],
    },
    {
        "answer": "C", "source": (DAGANG, 1, "PDF page 1, listening word-choice question 1"),
        "prompt": "A recording from the science fair gives one word: /ˌfoʊtəˈɡræfɪk/. Which printed form matches the sound and stress you hear?",
        "options": [("A", "photography"), ("B", "photographer"), ("C", "photographic"), ("D", "photograph")],
        "explanation": "音標呈現四音節並在 /ɡræf/ 位置帶主要重音，對應 photographic；photography、photographer 與 photograph 的重音位置不同。",
        "strategy": "先聽字首與音節數，再找主要重音落點；最後逐音節比對母音，不要只用相似的字尾猜答案。",
        "steps": ["先依節奏切出 pho-to-graph-ic 四個音節，不要把熟悉字根直接當成答案。", "主要重音落在 graph 這一拍；其餘音節較輕，符合音標中的 ˈ 標記。", "photograph 的主要重音在第一音節；photography 與 photographer 通常在第二音節，photographic 則在第三音節。", "只有 photographic 對上 /ˌfoʊtəˈɡræfɪk/ 的四音節和第三音節主要重音。", "選 C；同字根詞可能因構詞變化而移動重音，聽音時要同時核對音節和強弱。"],
    },
    {
        "answer": "B", "source": (DAGANG, 3, "PDF page 1, listening word-choice question 3"),
        "prompt": "A recording names one item from the costume box. Which option ends with the voiced /z/ sound?",
        "options": [("A", "caps"), ("B", "gloves"), ("C", "cliffs"), ("D", "walks")],
        "explanation": "gloves 的複數字尾在濁音 /v/ 後讀成 /z/；caps、cliffs 與 walks 的字尾則以清音 /s/ 收尾。辨音需聽最後一個音。",
        "strategy": "判斷複數字尾時先看字根最後一個音是否為濁音；濁音後常接 /z/，清音後則維持 /s/。用喉部振動驗證比背拼字可靠。",
        "steps": ["題目指定聽 /z/，所以逐字檢查真正的末尾聲音，不依選項中 s 的拼法猜測。", "gloves 的詞根以濁音 /v/ 結尾，複數詞尾接上後仍帶聲帶振動，形成 /vz/。", "caps、cliffs、walks 的詞根末音是清音，因此詞尾 /s/ 不會變成濁音 /z/。", "B 是唯一以 /z/ 收尾的選項；其餘三字的最後氣流較清、沒有尾端嗡鳴。", "答案選 B；喉部輕觸比較 gloves 與 caps，可用聲帶振動確認，而非被字母 s 誤導。"],
    },
    {
        "answer": "D", "source": (DAWAN, 6, "PDF page 1, listening basic-response question 6"),
        "prompt": "The dispatcher needs to confirm whether the parcel will arrive before noon. Which contour best signals a genuine yes-or-no check?",
        "options": [("A", "A low, flat ending that sounds like a final report"), ("B", "A falling ending that closes the topic"), ("C", "A pause before ‘okay’ with no pitch movement"), ("D", "A modest rise on the final stressed part of ‘okay?’")],
        "explanation": "在沒有特殊情緒、確實等待是非回答的語境中，句尾適度上揚是常見的確認語調。D 保留問句功能；降調仍可能出現在特定語境，但不符合題目設定的真誠確認。",
        "strategy": "先辨認說話目的，再選語調；同一句話可因確認、驚訝或不耐而改變音高，不能把標點符號當成唯一判準。",
        "steps": ["語境要確認包裹能否在中午前送達，因此說話者需要對方給 yes／no 回答。", "一般是非問句常以句尾上揚提示聽者回應，但升幅應自然，不必把整句唱高。", "D 把上揚放在問句最後的重讀部分，保留確認功能，也沒有額外加入不耐或驚嚇。", "A、B 會讓句子更像報告或話題收束；C 只有停頓，未提供確認所需的語調線索。", "因此選 D；朗讀時聽者應能感覺說話者正在等待確認，而不是單純宣告送達時間。"],
    },
    {
        "answer": "C", "source": (DAWAN, 5, "PDF page 1, listening basic-response question 5"),
        "prompt": "A volunteer asks which room stores the spare microphones. Which ending best fits a neutral information-seeking wh-question?",
        "options": [("A", "A rising ending that sounds like a yes-or-no check"), ("B", "A sharp rise that signals disbelief"), ("C", "A natural falling ending after the key place word"), ("D", "A level tone that leaves the sentence unfinished")],
        "explanation": "中性的 wh- 問句要索取具體地點，常以自然下降的句尾完成訊息；上揚可能改成確認或表示驚訝，平調則容易聽成尚未說完。",
        "strategy": "先看疑問詞要求開放答案還是是非回答；中性 wh- 問句通常下降，若要表達驚訝或確認，才依情境調整語調。",
        "steps": ["Which room 要求回答具體房間，是開放式資訊問題，不是只等待 yes 或 no 的確認問句。", "聽者需要知道備用麥克風存放在哪裡，因此 room 是這句話的資訊焦點。", "中性詢問時讓 room 一帶承載重音，句尾自然下降，表示問題完整並把回答權交給對方。", "A 的上揚較像要求確認；B 額外加入懷疑；D 平直不收束，容易讓人以為句子還沒講完。", "所以選 C；若情境改成驚訝追問，語調可能不同，判斷時須連同說話目的一起考量。"],
    },
    {
        "answer": "B", "source": (DAGANG, 7, "PDF page 1, listening-response question 7"),
        "prompt": "You asked for the brass key, but your partner hands you the wooden one. To repair the misunderstanding, which delivery emphasizes the requested material?",
        "options": [("A", "I asked for the key."), ("B", "I asked for the BRASS key, not the wooden one."), ("C", "The key is beside the bowl."), ("D", "Could you bring it tomorrow?")],
        "explanation": "誤會在於鑰匙材質，brass 與 wooden 才是對比資訊。把主要重音放在 BRASS，能立即指出應拿黃銅鑰匙，而不是木製鑰匙。",
        "strategy": "對比重音放在被更正、且能區分兩個候選物的資訊；朗讀前先指出對比軸是材質，而不是物件或時間。",
        "steps": ["眼前的誤會不是拿錯物件，而是同一種鑰匙有 brass 與 wooden 兩種材質。", "句子後半 not the wooden one 已建立對照，因此 brass 是最能修正誤解的新資訊。", "把主要重音落在 BRASS，並在 wooden 上保留次要對比，聽者會立刻知道要替換材質。", "A 只重複 key，沒有提供區別；C 談位置；D 改問時間，都無法修正拿錯材質。", "所以選 B；若改重讀 key，聽者可能只聽成物件種類，而不知道錯在材質。"],
    },
    {
        "answer": "A", "source": (DASHE, 6, "PDF page 8 (printed page 1), sentence-picture listening question 6"),
        "prompt": "A speaker says ‘Leave it in the open folder’ at natural speed. Which rehearsal note helps the phrase flow without losing the word boundaries?",
        "options": [("A", "Link the final /v/ in ‘leave’ into the vowel beginning ‘it,’ while keeping both words identifiable."), ("B", "Insert a full stop after every word."), ("C", "Delete the /v/ and /t/ so only vowels remain."), ("D", "Move the first sound of ‘open’ to the end of ‘it.’")],
        "explanation": "leave it 的 /v/ 接到下一字母音時可自然銜接，但 /v/ 仍要聽得到，it 也要保持可辨識。A 兼顧連讀流暢度與詞語邊界。",
        "strategy": "連音是相鄰語音的銜接，不是吞掉字音；先慢讀保留每個音，再逐漸縮短詞間停頓，確認聽者仍能辨認詞界。",
        "steps": ["注意 leave it 的交界：leave 以 /v/ 收尾，it 以母音起首，兩者可在連續語流中接得更緊。", "銜接不是漏掉字音；/v/ 仍是 leave 的尾音，it 的起始母音也必須保留。", "自然朗讀時縮短兩字之間的空隙，不另加停頓，但不把詞界完全抹除。", "A 描述了子音接母音的連讀且保留可辨識度；B 切碎語流，C 刪除必要音，D 任意搬動音素。", "故選 A；先慢讀 leave／it，再逐漸加速，回聽確認聽者仍能分辨兩個詞。"],
    },
    {
        "answer": "C", "source": (DAWAN, 10, "PDF page 1, basic-response question 10"),
        "prompt": "A student calls the school office and needs a transfer to the archive desk. Which spoken request sounds courteous and keeps the destination easy to hear?",
        "options": [("A", "Archive desk. Do it."), ("B", "You must send my call there."), ("C", "Could you connect me to the archive desk, please?"), ("D", "I called, so move me now.")],
        "explanation": "Could you…please? 以疑問句形式提出請求，please 補足禮貌；自然重讀 connect 與 archive desk，接線人就能聽清動作和目的地。",
        "strategy": "口語禮貌不只看句尾 please，也要用完整請求句並讓關鍵人物或需求容易聽見；音量自然、重音清楚即可，不需刻意放大每個字。",
        "steps": ["這通電話的目的在請櫃台轉接，不是要求對方立刻執行或責怪接線人。", "Could you connect me to…? 是完整的禮貌請求，please 再清楚標示友善語氣。", "朗讀時可以輕輕突出 connect 與 archive desk，讓關鍵動作和目的地比功能詞更清楚。", "A、B、D 都帶命令或強迫語氣，且沒有同時具備自然句構與禮貌緩和。", "答案是 C；語調平穩上揚即可，不必把 please 拉得很長或把整句變成誇張問腔。"],
    },
    {
        "answer": "D", "source": (DAGANG, 10, "PDF page 1, listening-response question 10"),
        "prompt": "Read this instruction aloud: ‘Before the second bell rings, place the model beside the window.’ Which phrasing best helps listeners track the long sentence?",
        "options": [("A", "Pause between every syllable, including inside ‘window.’"), ("B", "Run the entire sentence together with no boundary."), ("C", "Pause after ‘the’ and stress the comma."), ("D", "Group ‘Before the second bell rings’ together, pause briefly, then say the main instruction as one unit.")],
        "explanation": "句首時間子句提供背景，先連成一個意義單位，在 rings 後稍停，再把 place the model beside the window 作為主要指令讀完，層次最清楚。",
        "strategy": "長句先依語意而非字數切分：背景子句可形成前置語塊，主句要保持動詞與受詞相連，停頓不應拆散固定詞組。",
        "steps": ["句子前半 Before the second bell rings 說明時間條件，後半才是要執行的主要動作。", "先把前置子句讀成完整語塊，在 rings 後稍停，讓聽者準備接收主句。", "主句 place the model beside the window 要保持動詞、受詞與位置補語的關係。", "A 把停頓切進音節，B 不分層，C 拆開冠詞並把標點本身當成重音對象。", "D 的分組符合語意邊界，所以選 D；錄音回聽時檢查停頓是否幫助理解，而非只是聽起來較慢。"],
    },
]


def make_ref(url: str, number: int, locator: str) -> dict:
    school, exam, boundary = SOURCES[url]
    year = {DASHE: "108-1", DAGANG: "100-1", DAWAN: "113-1"}[url]
    return {
        "url": url,
        "title": f"{school}{exam}",
        "year": year,
        "subject": "english",
        "locator": locator,
        "observedPattern": f"只參考第{number}題的聽辨／口語任務型態與語音資訊處理方式；{boundary}",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


def main() -> None:
    if len(ITEMS) != 10:
        raise ValueError("2-IV-8 must contain ten stable items")
    paths = [ROOT / f"questions/english/question-english-performance-2-iv-8-{n}.json" for n in range(1, 11)]
    if any(not p.is_file() for p in paths):
        raise FileNotFoundError("Existing stable IDs are incomplete; no writes performed")
    for path, item in zip(paths, ITEMS, strict=True):
        data = json.loads(path.read_text(encoding="utf-8"))
        url, source_n, locator = item["source"]
        data["prompt"] = item["prompt"]
        data["options"] = [{"id": k, "text": t} for k, t in item["options"]]
        data["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
        data["examPatternRefs"] = [make_ref(url, source_n, locator)]
        data["solutionStrategy"] = item["strategy"]
        data["solutionSteps"] = item["steps"]
        data["provenance"] = {
            "origin": "original", "license": "All rights reserved", "sourceUrl": url,
            "sourceLocator": f"{SOURCES[url][0]}公開原卷 {locator}；只取聽辨／口語任務模式，不重製原卷內容。",
            "authoringNote": "依官方英語課綱、Knowledge Graph 與公立學校公開英語試題的精確 item-level pattern-only 證據獨立創作；未複製原題、選項、音檔、圖像或答案。題目維持 draft，尚待版本研究與完整內容發布審查。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-09-24"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    catalog_path = ROOT / "implementation/reports/public-exam-source-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    for url, (institution, exam, boundary) in SOURCES.items():
        entry = {"institution": institution, "url": url, "subjects": ["english"], "availableMaterial": exam,
                 "researchUse": "英語 2-Ⅳ-8 之子音聽辨、單字辨識、語調、對比重音、連音與意群停頓；逐題 pattern-only，不複製考題。",
                 "licenseBoundary": boundary}
        row = next((r for r in catalog["sources"] if r.get("url") == url), None)
        if row:
            row.update(entry)
        else:
            catalog["sources"].append(entry)
    catalog["questionSourceUrls"] = sorted({r["url"] for r in catalog["sources"] if r.get("url")})
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rewritten": len(ITEMS), "allRemainDraft": True, "sourceSchools": len(SOURCES)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
