#!/usr/bin/env python3
"""Repair provenance, answer positions, and a grammar ambiguity in English 5-IV-1."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions/english"
CATALOG_PATH = ROOT / "data/public-exam-sources.json"
TODAY = "2026-09-26"

SOURCES = {
    "kcjh": {
        "id": "kcjh-109-2-grade7-english",
        "school": "高雄市立國昌國民中學",
        "grade": "7",
        "subject": "english",
        "exam": "109學年度第2學期第2次定期評量",
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立國昌國中109學年度第2學期第2次定期評量一年級英文科試題",
        "year": "109-2",
        "policyLocator": "PDF第1頁（試卷頁碼1）單題選擇第1至11題；依情境判斷基本字彙、搭配與詞性",
    },
    "dawwan": {
        "id": "dwm-113-2-grade8-english",
        "school": "高雄市立大灣國民中學",
        "grade": "8",
        "subject": "english",
        "exam": "113學年度第2學期第2次定期評量",
        "url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/113%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%BA%8C%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立大灣國中113學年度第2學期第2次段考二年級英文科題目卷",
        "year": "113-2",
        "policyLocator": "PDF第2頁第17至24題；短句語境中的基本字彙選擇",
    },
    "wulun": {
        "id": "wl-jh-110-2-grade9-english",
        "school": "基隆市立武崙國民中學",
        "grade": "9",
        "subject": "english",
        "exam": "110學年度第2學期第2次段考",
        "url": "https://jweb.kl.edu.tw/userfiles/1389/document/39208_0524%E7%AC%AC%E4%BA%94%E7%AF%80--%E4%B9%9D%E4%B8%8B%E8%8B%B1%E6%96%87%E4%BA%8C%E6%AE%B5.pdf",
        "title": "基隆市立武崙國中110學年度第2學期九年級英文科第二次段考",
        "year": "110-2",
        "policyLocator": "PDF第2頁（試卷頁碼2）單題第13至27題；情境中的詞義與詞性判斷",
    },
}

ITEMS = {
    1: ("report", ["repair", "report", "borrow", "invite"], "B", "PDF第1頁第3題；PDF第2頁第18至20題；PDF第2頁第19題"),
    2: ("light", ["ticket", "corner", "light", "schedule"], "C", "PDF第1頁第5題；PDF第2頁第18題；PDF第2頁第18題"),
    3: ("plant", ["print", "pack", "promise", "plant"], "D", "PDF第1頁第3題；PDF第2頁第24題；PDF第2頁第15至16題"),
    4: ("match", ["match", "climb", "collect", "translate"], "A", "PDF第1頁第9題；PDF第2頁第20至21題；PDF第2頁第15題"),
    5: ("notice", ["freeze", "notice", "deliver", "measure"], "B", "PDF第1頁第1題；PDF第2頁第17至19題；PDF第2頁第19題"),
    6: ("field", ["pocket", "recipe", "field", "ceiling"], "C", "PDF第1頁第5題；PDF第2頁第20至24題；PDF第2頁第20題"),
    7: ("walk", ["whisper", "water", "fold", "walk"], "D", "PDF第1頁第3題；PDF第2頁第21至24題；PDF第2頁第22題"),
    8: ("patient", ["patient", "wooden", "weekly", "empty"], "A", "PDF第1頁第5題；PDF第2頁第17至20題；PDF第2頁第23題"),
    9: ("raise", ["hide", "lose", "raise", "shake"], "C", "PDF第1頁第3題；PDF第2頁第21至24題；PDF第2頁第21題"),
    10: ("record", ["melt", "record", "stretch", "decorate"], "B", "PDF第1頁第1題；PDF第2頁第17至24題；PDF第2頁第24題"),
}

ITEM_CONTENT = {
    1: {
        "prompt": "The school bus was delayed, so Mina called the school office to ____ that it would arrive about twenty minutes late.",
        "explanation": "Report that + 子句表示正式傳達一項消息；校車延誤時，Mina 是向校方通報抵達時間。",
        "strategy": "先把空格後的 that 子句當成要傳達的消息，再挑選能帶出「通報內容」的動詞；不要只憑 arrive 一字猜答案。",
        "steps": [
            "先讀到 that it would arrive...：空格後是一整項消息，不是人或物的受詞。",
            "校車延誤，Mina 打電話給學校辦公室，語境是正式通知交通狀況。",
            "report 可接 that 子句，表示把所知情況報告給相關單位。",
            "repair 是修理、borrow 是借用、invite 是邀請，都不能引出這項延誤消息。",
            "答案是 B report；句型為 report that + 子句，語意與通報目的相符。",
        ],
    },
    2: {
        "explanation": "走廊太暗而看不清階梯，turn on the light 表示開啟照明；其餘選項都不是能照亮走廊的物品。",
        "strategy": "用後半句的可見度結果回推前半句需要的物件，並檢查 turn on 與該名詞是否自然搭配。",
        "steps": [
            "the ____ 在句中是 turn on 的受詞，因此空格應填可開啟的名詞。",
            "too dark to see the steps 指向缺少照明，而非缺少車票或行程表。",
            "light 可指燈具或光源，開啟它能改善走廊能見度。",
            "ticket、corner、schedule 分別是票、角落、時間安排，不能提供照明。",
            "答案是 C light；turn on the light 與黑暗走廊的因果線索一致。",
        ],
    },
    3: {
        "explanation": "Plant 作及物動詞表示把植物種進土裡；種下樹苗後，樹長大才能提供更多遮蔭，所以正解是 D。",
        "strategy": "從 will 後的動詞位置、a tree 這個受詞，以及 make more shade 的長期目的三處一起確認動詞。",
        "steps": [
            "will 後接原形動詞；a tree 是動作直接作用的對象。",
            "社團在圖書館旁做的是改造環境，不是印刷、打包或許諾。",
            "樹木長成後能增加遮蔭，這個目的說明要先把樹種下。",
            "plant 可作及物動詞帶入 a tree；print、pack、promise 均不符合種植行動。",
            "答案是 D plant；plant a tree 與增加遮蔭的因果順序成立。",
        ],
    },
    4: {
        "explanation": "Match 在此表示兩個物件相合、相配；鑰匙不適用於這把鎖，因此 match 是唯一符合句意的動詞。",
        "strategy": "把鑰匙與鎖視為一組配對物件，判斷空格描述的是相容性，而不是人或物的其他動作。",
        "steps": [
            "does not 後接原形動詞，且空格後的 old lock 是動作所關聯的物件。",
            "blue key 與 lock 的關係是能否搭配使用，不是攀爬或翻譯。",
            "match + 物件可表相符；does not match the lock 即鑰匙不適用這把鎖。",
            "climb、collect、translate 都無法描述鑰匙與鎖的相容性。",
            "答案是 A match；鑰匙不相配，所以需要另找一把。",
        ],
    },
    5: {
        "explanation": "Did you notice the sign? 是詢問是否曾看見並留意入口標示；標示中的閉館時間正是需要注意的資訊。",
        "strategy": "先由 Did 判斷動詞形式，再分辨問題是在問「有沒有注意到資訊」，而非是否執行其他動作。",
        "steps": [
            "Did 已承擔過去式，空格要用原形動詞。",
            "受詞 the sign 是入口的告示牌，下一句補充牌上寫了什麼。",
            "notice 不只表示視線掃過，也包含察覺到告示所傳達的內容。",
            "freeze、deliver、measure 分別是結冰、遞送、測量，不適用於閱讀標示。",
            "答案是 B notice；問句確認對方是否注意到閉館時間。",
        ],
    },
    6: {
        "explanation": "足球隊通常在 field（運動場）練習；體育館正被會議使用，因而提供改到戶外場地的理由。",
        "strategy": "把空格當作練習地點分類題，先用 soccer 限定場地，再用 gym 被占用的轉折核對答案。",
        "steps": [
            "practiced on the school ____ 要求填一個可供練習的地點。",
            "soccer team 限定活動類型，field 是球隊可在校內使用的戶外場地。",
            "because 子句說明室內 gym 被會議占用，解釋地點改變。",
            "pocket 是口袋、recipe 是食譜、ceiling 是天花板，均非練球場地。",
            "答案是 C field；戶外球場與室內體育館的對比完整解釋了句子。",
        ],
    },
    7: {
        "explanation": "Too tired to walk home 表示累到無法步行回家；父親開車載他，正好替代這段移動。",
        "strategy": "同時使用 too...to... 句型與父親開車的補救行動，判斷 Leo 原本做不到的是哪種移動方式。",
        "steps": [
            "too tired to 後面要接原形動詞，表示疲累造成的限制。",
            "home 是移動目的地；父親 drove him 說明 Leo 需要交通協助。",
            "賽跑後太累，步行回家是合理但做不到的行動。",
            "whisper、water、fold 都不能與 home 組成此處需要的移動方式。",
            "答案是 D walk；開車載他補足了無法步行回家的情況。",
        ],
    },
    8: {
        "prompt": "The nurse asked the ____ to sit quietly while she called his parents.",
        "explanation": "Patient 作名詞時可指接受醫療照護的人；護士要求病人坐著並聯絡家長，句法和醫療語境都吻合。",
        "strategy": "從 ask + 人 + to V 的句型判斷空格必須是「人」，再用 nurse 與聯絡家長的情境選擇 patient 的名詞義。",
        "steps": [
            "句型是 ask + 受詞 + to V，空格填被要求坐下的人。",
            "nurse 與 called his parents 暗示這個人正在接受照護。",
            "patient 作名詞可指病人；本句不是形容詞修飾後面的名詞。",
            "wooden、weekly、empty 都不能作為被要求坐下的人。",
            "答案是 A patient；名詞位置與護士照護病人的語境相合。",
        ],
    },
    9: {
        "explanation": "Raise money 是固定搭配，意思是為某個目的籌募資金；學生販售手作書籤正是籌款方式。",
        "strategy": "把 money 當作搭配線索，並用學生採取的募款行動驗證動詞，而不是只翻譯單字本身。",
        "steps": [
            "句首 To... 表目的，空格需要一個能帶出 money 的原形動詞。",
            "animal shelter 是款項的用途，指出這不是賺取個人零用錢的情境。",
            "賣手作書籤是募款活動；英文常用 raise money 表達籌款。",
            "hide、lose、shake money 都與為收容所募集資金的目的相反或不通。",
            "答案是 C raise；raise money for + 目的地／用途完整表達籌款。",
        ],
    },
    10: {
        "explanation": "Record their names 表示把姓名寫下或登錄，才能在借用平板前留下借用紀錄。",
        "strategy": "由 names、before borrowing tablets 推出這是設備借用登記流程，再檢查動詞是否表示保存資料。",
        "steps": [
            "asked students to 後需接原形動詞；their names 是要處理的資料。",
            "借出平板前先留下姓名，目的是建立可追查的借用紀錄。",
            "record 可表示記錄或登錄資訊，與圖書館管理流程吻合。",
            "melt、stretch、decorate 分別是融化、伸展、裝飾，不能完成登記。",
            "答案是 B record；登錄姓名後才借出設備，程序與詞義一致。",
        ],
    },
}

PATTERN = "只借用公立學校英文評量以語境判斷字義、搭配與詞性的題型方向；本題情境、詞彙組合、選項與解答均獨立撰寫，未複製來源題文。"


def question_refs(locators: str) -> list[dict]:
    parts = locators.split("；")
    refs = []
    for (source, locator) in zip(SOURCES.values(), parts, strict=True):
        refs.append({
            "url": source["url"],
            "title": source["title"],
            "year": source["year"],
            "subject": "english",
            "locator": locator,
            "observedPattern": PATTERN,
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "locatorLevel": "page",
        })
    return refs


def main() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    entries = catalog["sources"]
    known = {item["id"] for item in entries}
    for source in SOURCES.values():
        if source["id"] not in known:
            entries.append({
                "id": source["id"],
                "school": source["school"],
                "grade": source["grade"],
                "subject": source["subject"],
                "exam": source["exam"],
                "questionUrl": source["url"],
                "answerLocator": source["policyLocator"],
                "usePolicy": "僅供語境詞彙題型能力方向研究；不保存或重製原題文字、選項、答案或版面。",
                "verifiedAt": TODAY,
            })
    catalog["updatedAt"] = TODAY
    CATALOG_PATH.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for number, (target, ordered, key, locators) in ITEMS.items():
        path = QUESTION_DIR / f"question-english-performance-5-iv-1-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["options"] = [{"id": chr(65 + index), "text": text} for index, text in enumerate(ordered)]
        if ordered[ord(key) - 65] != target:
            raise ValueError(f"answer-position mismatch for item {number}")
        data["answer"]["value"] = key
        data["solutionSteps"][-1] = f"選 {key}，確認 {target} 的詞義與句中動作／對象完全相合。"
        data["examPatternRefs"] = question_refs(locators)
        data["provenance"]["sourceUrl"] = SOURCES["kcjh"]["url"]
        data["provenance"]["sourceLocator"] = "三所公立國中英語段考的語境詞彙單題（逐題列於 examPatternRefs）；僅取題型能力方向，不複製原卷內容。"
        data["provenance"]["authoringNote"] = "依官方課綱與 KG-english-performance-5-iv-1，參照三所公立學校公開英文段考的語境字彙能力方向獨立撰寫；題幹、選項、解析、策略與五步解題皆為原創，仍待內容與版權 gate。"
        data["updatedAt"] = TODAY
        if number == 8:
            data["prompt"] = "The nurse asked the ____ to sit quietly while she called his parents."
            data["answer"]["explanation"] = "Patient 作名詞時可指接受醫療照護的人；護士讓 patient 安靜坐著並聯絡家長，語意和句法都吻合。"
            data["solutionStrategy"] = "先看空格在句中的位置，再用 nurse 與聯絡家長的線索判斷 patient 是名詞「病人」，不是形容詞「有耐心的」。"
            data["solutionSteps"] = [
                "讀出主幹：The nurse asked the ____ to sit quietly；asked 後面需要被要求做事的人。",
                "用 to sit quietly 找出空格是 ask 的受詞，而不是修飾後方名詞的形容詞。",
                "護士聯絡對方家長，提供醫療照護情境；patient 作名詞可表示病人。",
                "wooden、weekly、empty 都不能指稱一個被要求坐下的人。",
                "選 A patient；此處是名詞「病人」，句法與語意均成立。",
            ]
        content = ITEM_CONTENT[number]
        data["prompt"] = content.get("prompt", data["prompt"])
        data["answer"]["explanation"] = content["explanation"]
        data["solutionStrategy"] = content["strategy"]
        data["solutionSteps"] = content["steps"]
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("updated 10 questions; added 3 public-school exam sources; answer distribution A/B/C/D=2/3/3/2")


if __name__ == "__main__":
    main()
