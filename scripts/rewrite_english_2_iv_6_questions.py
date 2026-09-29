#!/usr/bin/env python3
"""Create original English 2-IV-6 questions from public-school exam patterns."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAWAN = "https://www.dwm.kh.edu.tw/upload/344/104_64184/113%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf"
NEIHU_113 = "https://www.nhjh.tp.edu.tw/uploads/1738658361761hrnHCuVf.pdf"
NEIHU_110 = "https://www.nhjh.tp.edu.tw/30/2133/news/19/2022-1/42022-1-27-13-49-5-nf1.pdf"
QIANZHEN = "https://www.qzjh.kh.edu.tw/qzjh/Fileupload/File/Logo_990.pdf"

SOURCES = {
    DAWAN: ("高雄市立大灣國中", "113學年度第一學期八年級英語科第一次段考", "只參考原卷人事時地資訊擷取、問答與閱讀資料定位方式；不複製題幹、選項、答案或素材。"),
    NEIHU_110: ("臺北市立內湖國中", "110學年度第一學期八年級英語科第三次段考（翰林版）", "只參考原卷路線對話與依序擷取方向資訊的能力；不複製題幹、選項、答案、圖表或音檔。"),
    QIANZHEN: ("高雄市立前鎮國中", "112學年度第一學期七年級英語科段考", "只參考原卷聽力位置描述、地圖方位題的資訊辨識方式；不複製題幹、選項、答案、圖表或音檔。"),
}

ITEMS = [
    {
        "answer": "B", "source": (DAWAN, 1, "PDF page 1, listening basic-response question 6"),
        "prompt": "A: Who told you the story about the lost kite?\nB: ______",
        "options": [("A", "At the playground after lunch."), ("B", "Mina told it to me on the bus."), ("C", "It was about a blue kite."), ("D", "I read it last Saturday.")],
        "explanation": "問句中的 who 要求指出說故事的人。Mina 是人名，且句子明確說她把故事告訴 B；其他選項分別回答地點、故事內容或時間。",
        "strategy": "先把 who 對應到「人」，再從回應中找出執行 told 的人；別被句中其他時間、地點或故事內容帶走。",
        "steps": ["圈出疑問詞 who，確認要找的是人物，而不是故事題材或發生時間。", "回讀答句的主詞：Mina 是告訴故事的人，代名詞 it 指前面的 story。", "核對動詞關係：Mina told it to me，符合「Mina 把故事告訴我」。", "A 回答何時何地，C 說故事內容，D 說閱讀時間，都沒有指出說話者。", "因此選 B；定位人物時要追蹤動作的主詞，不要只挑含有人名的句子。"],
    },
    {
        "answer": "D", "source": (DAWAN, 1, "PDF page 1, grammar-choice question 1"),
        "prompt": "A message says, “Leo returned the borrowed camera to the media-room desk before lunch.” What did Leo do?",
        "options": [("A", "He borrowed a desk from the media room."), ("B", "He took photographs during lunch."), ("C", "He bought a new camera before school."), ("D", "He brought the borrowed camera back to the desk.")],
        "explanation": "訊息的核心動作是 returned，受詞是 borrowed camera，目的地是 media-room desk。D 保留了「歸還相機」這個動作；before lunch 是時間線索，不是動作本身。",
        "strategy": "把句子拆成「主詞—動作—受詞—去向」，再選同義改述；小心不要把時間片語誤當成 what 問句的答案。",
        "steps": ["先找主詞 Leo，接著找句子的主要動詞 returned。", "returned 在這裡表示把借來的物品送回原處，不是購買或拍照。", "確認受詞是 borrowed camera，去向是 media-room desk。", "A 把 desk 誤當借來的物品，B、C 則加入句中沒有發生的拍照與購買。", "D 同時保留歸還、相機與桌子三項關係，所以是完整的 what 回答。"],
    },
    {
        "answer": "C", "source": (DAWAN, 3, "PDF page 3, reading schedule question 3"),
        "prompt": "The robotics team practices every Tuesday at 4:25 p.m. When does the team practice?",
        "options": [("A", "On Thursday mornings."), ("B", "Every Tuesday before school."), ("C", "Every Tuesday at 4:25 p.m."), ("D", "At 4:25 p.m. on Saturdays.")],
        "explanation": "時間資訊有兩部分：固定星期 Tuesday 和鐘點 4:25 p.m.。只有 C 同時保留這兩個條件；B 把時間改成上學前，D 改成星期六。",
        "strategy": "讀 when 時把日期與鐘點都抄成核對清單；只答星期或只答時間，都可能漏掉題目提供的關鍵資訊。",
        "steps": ["標記 when，確認題目詢問練習時間，而非練習地點或活動內容。", "從原句圈出 every Tuesday，代表每週二固定舉行。", "另圈出 at 4:25 p.m.，辨明這是下午四點二十五分。", "逐一比較選項：B 漏掉鐘點且改成上學前；D 的日期不是 Tuesday。", "C 完整符合星期與時間，故選 C；讀行程表時也應同時保留列與欄的標籤。"],
    },
    {
        "answer": "A", "source": (DAWAN, 2, "PDF page 2, grammar-choice question 4"),
        "prompt": "The notice says, “Please leave found items in the first-floor office beside the nurse’s room.” Where should a student take a lost water bottle?",
        "options": [("A", "To the first-floor office next to the nurse’s room."), ("B", "To the second-floor gym beside the stage."), ("C", "To the nurse’s room on the third floor."), ("D", "To the front gate across from the library.")],
        "explanation": "通知同時提供樓層與相鄰地點：first-floor office、beside the nurse’s room。A 保留兩項位置資訊；其他選項更換樓層、地點或相對方位。",
        "strategy": "回答 where 時先找地點名詞，再把樓層及方位詞一起核對，避免只找到同一棟建築卻走錯位置。",
        "steps": ["辨認問句的 where，目標是找出交物品的地點。", "在通知中找主要地點名詞 office，接著確認它在 first floor。", "再讀 beside the nurse’s room，確認辦公室緊鄰護理室。", "B、C、D 各自改動樓層、房間或相對位置，與通知不一致。", "A 完整保留 office、first floor 和 nurse’s room 三項線索，故選 A。"],
    },
    {
        "answer": "B", "source": (QIANZHEN, 1, "PDF page 1, listening picture-description question 1 (item set 1–5)"),
        "prompt": "A student describes an object: “It is a small silver key. A red tag on it says ‘Studio 4.’” Which item matches the description?",
        "options": [("A", "A large silver key with a blue tag marked ‘Studio 4.’"), ("B", "A small silver key with a red tag marked ‘Studio 4.’"), ("C", "A small red key with a silver tag marked ‘Studio 4.’"), ("D", "A small silver key with a red tag marked ‘Studio 2.’")],
        "explanation": "描述包含物品種類、大小、主體顏色、標籤顏色與標籤文字。只有 B 五項都符合；其餘選項各改動了其中一個屬性。",
        "strategy": "把名詞與修飾資訊分欄核對：物品、尺寸、顏色、標籤色、標籤文字；不要因大部分相同就忽略一個錯誤細節。",
        "steps": ["先確認物品種類是 key，排除不是鑰匙的圖像或物品。", "第二個條件是 small；A 的鑰匙較大，因此不符。", "主體是 silver，標籤則是 red；C 把這兩種顏色對調。", "最後逐字核對標籤內容 Studio 4，D 把數字改成 2。", "只有 B 同時符合五項視覺線索；細節題要逐欄比對，不能只看整體相似度。"],
    },
    {
        "answer": "D", "source": (DAWAN, 2, "PDF page 2, grammar-choice question 7"),
        "prompt": "Mira moved the picnic from the hill to the community room. Why did she change the plan?\n“Because the weather alert predicts strong winds.”",
        "options": [("A", "Because the picnic had ended the day before."), ("B", "Because the community room was farther away."), ("C", "Because her friends wanted to climb the hill."), ("D", "Because strong winds were expected outside.")],
        "explanation": "why 問原因，回應中的 because 子句直接說明改地點的理由：戶外預報有強風。D 是同義改述；其他選項不在對話中。",
        "strategy": "用 why 找 because 或可推得因果的句子，再檢查該原因是否能解釋前述決定；不要把場景中的其他地點當成原因。",
        "steps": ["先找出被問的決定：Mira 把野餐從山丘移到活動室。", "why 要求原因，第二句以 Because 開頭，是最直接的因果線索。", "strong winds 是強風，weather alert predicts 表示預報將出現，並非已經結束的活動。", "A、B、C 都沒有出現在原因句中，也不能解釋為何改到室內。", "D 保留「預期強風」這個原因，因此是正確回答。"],
    },
    {
        "answer": "C", "source": (NEIHU_110, 36, "printed page 3, reading-directions question 36 (set 36–40)"),
        "prompt": "To reach the planetarium from the gym, walk past the bakery. Turn right at the first corner. The planetarium is across from the post office. What should you do at the first corner?",
        "options": [("A", "Turn left before reaching the bakery."), ("B", "Cross the street at the post office and go back."), ("C", "Turn right after walking past the bakery."), ("D", "Stop at the gym and wait for the bus.")],
        "explanation": "路線有先後順序：先從 gym 出發並走過 bakery，接著在第一個街角右轉；post office 只用來描述終點對面的位置。",
        "strategy": "把路線連接詞按順序標記，分清楚「要做的方向」和「終點相對位置」；終點地標不能取代途中指令。",
        "steps": ["起點是 gym，第一個動作是沿路前進並走過 bakery。", "題目問 at the first corner，因此要找轉彎指令而不是終點在哪裡。", "原文指定 turn right，且是在走過 bakery 之後才發生。", "across from the post office 描述 planetarium 的終點位置，不是要在郵局回頭。", "C 完整保留先經過 bakery、再右轉的次序，故選 C。"],
    },
    {
        "answer": "A", "source": (QIANZHEN, 13, "PDF page 1, listening basic-response question 13"),
        "prompt": "A visitor asks, “Where are the two students going?” The conversation gives directions past a church and says the bakery is across from a bicycle shop. Which reply answers the question?",
        "options": [("A", "They are going to the bakery."), ("B", "They are going to the church."), ("C", "They are going to the bicycle shop."), ("D", "They are going to the bus stop.")],
        "explanation": "問題要目的地。教堂是沿途地標，自行車店是用來定位麵包店的對面地點；真正要去的是 bakery。",
        "strategy": "先把方向對話中的「經過地標」與「目的地」分開，再回答 where；被提到的場所不一定就是終點。",
        "steps": ["抓住問句中的 where，並確認主詞是兩位學生，題目要找他們的目的地。", "回讀對話結構：church 是用來判斷轉彎位置的參照物。", "bicycle shop 出現在 bakery 的相對位置描述中，功能是協助定位。", "若把最近提到的地點直接當答案，就會誤選 church 或 bicycle shop。", "目的地是 bakery，所以 A 正確；路線資訊需區分起點、地標與終點。"],
    },
    {
        "answer": "B", "source": (QIANZHEN, 30, "PDF page 2, map-reading question 30"),
        "prompt": "On the campus map, the blue backpack is under the bench, not on it. Which sentence reports the map correctly?",
        "options": [("A", "The backpack is behind the bench, and the bench is beside the gym."), ("B", "The blue backpack is below the bench."), ("C", "The backpack is on top of a red desk."), ("D", "The bench is inside the blue backpack.")],
        "explanation": "under 表示在下方，與題目明確排除的 on（在上面）不同。只有 B 保留藍色背包位於長椅下方的空間關係。",
        "strategy": "讀地圖或位置描述時，分開核對物件、顏色與方位介系詞；under、on、behind 不能互換。",
        "steps": ["先找主體 blue backpack，避免把長椅本身當成要定位的物件。", "關鍵位置詞是 under，表示背包在長椅下方。", "題幹特別補充 not on it，排除「放在長椅上」的解讀。", "A 偷換成 behind，C 改了物件與顏色，D 把兩物件內外關係倒置。", "B 用 below 表達下方位置，與原訊息一致，所以選 B。"],
    },
    {
        "answer": "D", "source": (DAWAN, 7, "PDF page 3, reading-calendar question 7"),
        "prompt": "A school notice reads: “At 3:20 on Friday, Ava, Ben, and Rui planted native flowers beside the east gate because the garden club needed volunteers.” Which summary keeps all the key details?",
        "options": [("A", "On Friday morning, the garden club planted trees behind the library."), ("B", "Ava and Rui watered flowers at the east gate after school on Thursday."), ("C", "Ben asked for volunteers to plant flowers at 3:20 beside the west gate."), ("D", "At 3:20 on Friday, Ava, Ben, and Rui planted native flowers by the east gate to help the garden club.")],
        "explanation": "完整摘要要保留時間、人物、動作、地點與目的。D 五項都與通知相符；其餘選項改了星期、人物、動作、方位或事件角色。",
        "strategy": "摘要前列出 who、when、what、where、why 五格，逐一回到原文核對；不能只憑主題相同就接受細節有誤的選項。",
        "steps": ["把通知拆成五個欄位：人物 Ava、Ben、Rui；時間 Friday 3:20。", "動作是 planted native flowers，作物是本土花卉，不是樹木或澆水。", "地點是 east gate 旁；east 不能和 west 或 behind the library 混淆。", "目的在 because 子句：garden club 需要志工，所以三人前往協助。", "D 保留全部五項資訊；A、B、C 各至少改動一項，因此選 D。"],
    },
]


def make_ref(url: str, item_number: int, locator: str) -> dict:
    school, exam, boundary = SOURCES[url]
    year = {DAWAN: "113", NEIHU_110: "110", QIANZHEN: "112"}[url]
    return {
        "url": url,
        "title": f"{school}{exam}",
        "year": year,
        "subject": "english",
        "locator": locator,
        "observedPattern": f"只參考第{item_number}題的閱讀／問答能力與資訊擷取方式；{boundary}",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


def main() -> None:
    if len(ITEMS) != 10:
        raise ValueError(f"預期 10 題，實際為 {len(ITEMS)} 題；停止避免題目 ID 越界")
    paths = [ROOT / f"questions/english/question-english-performance-2-iv-6-{n}.json" for n in range(1, 11)]
    if any(not path.is_file() for path in paths):
        raise FileNotFoundError("既有穩定題目 ID 不完整；停止避免部分寫入")
    for path, item in zip(paths, ITEMS, strict=True):
        old = json.loads(path.read_text(encoding="utf-8"))
        url, item_number, locator = item["source"]
        old["prompt"] = item["prompt"]
        old["options"] = [{"id": key, "text": text} for key, text in item["options"]]
        old["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
        old["examPatternRefs"] = [make_ref(url, item_number, locator)]
        old["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": url,
            "sourceLocator": f"{SOURCES[url][0]}公開原卷 {locator}；只採用命題能力／資料閱讀模式，不複製原卷內容。",
            "authoringNote": "依官方課綱、Knowledge Graph 與公立學校公開英語試題的 item-level pattern-only 證據獨立改寫；未複製原題、選項、圖表或音檔。題目維持 draft，尚待單元版本研究、內容與發布審查。",
        }
        old["solutionStrategy"] = item["strategy"]
        old["solutionSteps"] = item["steps"]
        old["reviewStatus"] = "draft"
        old["updatedAt"] = "2026-09-24"
        path.write_text(json.dumps(old, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    catalog_path = ROOT / "implementation/reports/public-exam-source-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    for url, (school, exam, boundary) in SOURCES.items():
        rows = catalog.setdefault("sources", [])
        existing = next((row for row in rows if row.get("url") == url), None)
        entry = {
            "institution": school,
            "url": url,
            "subjects": ["english"],
            "availableMaterial": exam,
            "researchUse": "2-Ⅳ-6 之人、時、地、物描述／問答；題庫改寫採精確題號的 pattern-only 參照。",
            "licenseBoundary": boundary,
        }
        if existing:
            existing.update(entry)
        else:
            rows.append(entry)
    catalog["questionSourceUrls"] = sorted({row.get("url") for row in catalog.get("sources", []) if row.get("url")})
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rewritten": len(ITEMS), "allRemainDraft": True, "sources": len(SOURCES)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
