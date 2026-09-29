#!/usr/bin/env python3
"""Replace unlocated refs and balance answer positions for English 5-IV-10."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/english"
CATALOG = ROOT / "data/public-exam-sources.json"
TODAY = "2026-09-26"

SOURCES = [
    {
        "id": "kcjh-106-1-term3-grade8-english",
        "school": "高雄市立國昌國民中學", "grade": "8", "subject": "english",
        "exam": "106學年度第1學期第3次段考", "year": "106-1",
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/106-1-3%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E7%A7%91%E8%A9%A6%E9%A1%8C%2B%E7%AD%94%E6%A1%88%E5%8D%B7.pdf",
        "title": "高雄市立國昌國中106學年度第1學期第3次段考二年級英文科試題卷",
        "examLocator": "PDF第3頁第37至40題；故事短文主旨、原因、細節與後續推論",
    },
    {
        "id": "hkjh-109-1-term3-grade9-english",
        "school": "高雄市立小港國民中學", "grade": "9", "subject": "english",
        "exam": "109學年度第1學期第3次段考", "year": "109-1",
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/31%E4%B8%89%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F/3%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/109-1-3%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立小港國中109學年度第1學期第3次段考三年級英文科試題",
        "examLocator": "PDF第5頁第48至49題；敘事詩主旨與文本推論",
    },
    {
        "id": "wl-jh-110-2-grade9-english",
        "school": "基隆市立武崙國民中學", "grade": "9", "subject": "english",
        "exam": "110學年度第2學期第2次段考", "year": "110-2",
        "url": "https://jweb.kl.edu.tw/userfiles/1389/document/39208_0524%E7%AC%AC%E4%BA%94%E7%AF%80--%E4%B9%9D%E4%B8%8B%E8%8B%B1%E6%96%87%E4%BA%8C%E6%AE%B5.pdf",
        "title": "基隆市立武崙國中110學年度第2學期九年級英文科第二次段考",
        "examLocator": "PDF第4頁第44至46題；故事對話的活動判讀、角色數量與證據推論",
    },
]

# Correct answer text, new answer key, then options in A-D order.
ITEMS = {
    1: ("Patient practice can build skill and help someone else.", "A", ["Patient practice can build skill and help someone else.", "Music is always easy on the first try.", "Friends should never perform in front of anyone.", "The story is mainly about buying a new instrument."], ["PDF第3頁第37題", "PDF第5頁第48題", "PDF第4頁第44至46題"]),
    2: ("A student shares an umbrella with a classmate caught in the rain.", "B", ["A student chooses a red notebook instead of a blue one.", "A student shares an umbrella with a classmate caught in the rain.", "The cafeteria counts its chairs after lunch.", "A clock shows the same time twice."], ["PDF第3頁第38題", "PDF第5頁第48至49題", "PDF第4頁第44至46題"]),
    3: ("Find a suitable gift for her brother", "C", ["Win a cooking contest for herself", "Avoid visiting every store", "Find a suitable gift for her brother", "Sell her brother's drawings"], ["PDF第3頁第39題", "PDF第5頁第48至49題", "PDF第4頁第45至46題"]),
    4: ("He stopped to help the neighbor", "D", ["The play started earlier in another city", "He forgot what glasses look like", "The audience closed the theater", "He stopped to help the neighbor"], ["PDF第3頁第38題", "PDF第5頁第49題", "PDF第4頁第46題"]),
    5: ("From worried to confident", "A", ["From worried to confident", "From excited to sleepy", "From angry to jealous", "From bored to frightened"], ["PDF第3頁第39至40題", "PDF第5頁第48至49題", "PDF第4頁第44至46題"]),
    6: ("Waiting for the First Leaf", "B", ["The Fastest Race in Town", "Waiting for the First Leaf", "A Recipe Without Seeds", "The Noisy Train Station"], ["PDF第3頁第37題", "PDF第5頁第48題", "PDF第4頁第44題"]),
    7: ("The child discovers an old map under a book.", "C", ["The child rests beside the garden gate.", "The child shares flowers with a friend.", "The child discovers an old map under a book.", "The child follows the path through the trees."], ["PDF第3頁第37至40題", "PDF第5頁第48至49題", "PDF第4頁第44至46題"]),
    8: ("Accepting useful help can make a hard task possible.", "D", ["Friends should never give advice.", "Projects are finished only by avoiding other people.", "Advice always makes a task take longer.", "Accepting useful help can make a hard task possible."], ["PDF第3頁第39至40題", "PDF第5頁第48至49題", "PDF第4頁第46題"]),
    9: ("I think the child is honest because she returned the wallet instead of keeping the money.", "B", ["Wallets can be made of many colors.", "I think the child is honest because she returned the wallet instead of keeping the money.", "The story has words and a beginning.", "I do not know anything about the child's action."], ["PDF第3頁第38至40題", "PDF第5頁第48至49題", "PDF第4頁第46題"]),
    10: ("Children and neighbors repair a sign together, making the park easier to find.", "C", ["A park disappears after children collect tools for no reason.", "Visitors build a new city because one sign is colorful.", "Children and neighbors repair a sign together, making the park easier to find.", "The story is only a list of tools without an event or result."], ["PDF第3頁第37至40題", "PDF第5頁第48至49題", "PDF第4頁第44至46題"]),
}

ITEM_CONTENT = {
    1: ("主旨要涵蓋練習帶來的能力成長，也要納入最後替朋友演奏的意義；不要把故事縮成單一事件。", [
        "先把事件串成一條線：孩子每天練習、犯錯後繼續，到最後為緊張的朋友演奏。",
        "反覆練習是前半段的重心，成功演奏是結果；兩者共同支持 skill grows through practice。",
        "為朋友演奏補上故事的關係面向，不能只留下「音樂很難」或「買樂器」。",
        "檢查四個選項，只有 Patient practice can build skill and help someone else 同時涵蓋練習與助人。",
        "答案 A。它總結人物的改變和行動意義，其他三項都與故事相反或無關。",
    ]),
    2: ("支持主旨要找一個實際發生、能具體呈現善意的情節；顏色、椅子數或時鐘資訊只是無關細節。", [
        "題幹已給主旨：小小善意能改變困難的一天；本題要找證據，不是再選一次主旨。",
        "把「分享雨傘」對照「同學淋雨」：行動直接回應當下困境，能看出關心。",
        "紅藍筆記本、餐廳椅子與時鐘讀數都沒有呈現幫助別人的行為。",
        "因此，最有證據力的細節是學生把雨傘分給淋雨的同學。",
        "答案 B。這個具體行動能支持「善意讓困難的一天好轉」的主旨。",
    ]),
    3: ("人物目標常藏在她持續採取的行動和行動理由中；把搜尋多家商店與哥哥喜歡畫畫連起來判斷。", [
        "先確認問句問的是 Nora 想達成什麼，而不是她做了哪個動作。",
        "她為生日禮物跑了三家店，顯示正在尋找某樣適合的物品。",
        "題幹特別交代哥哥喜歡畫畫，這是挑選禮物時的偏好線索。",
        "烹飪比賽、避開商店和出售畫作都沒有被情節支持。",
        "答案 C：Find a suitable gift for her brother。行動、收禮者與興趣三者一致。",
    ]),
    4: ("因果題要找事件順序中真正造成結果的中介行動；他停下來協助鄰居，直接占用了趕赴劇場的時間。", [
        "把兩件事分開：結果是錯過戲劇開場，題目追問造成結果的原因。",
        "故事提供一個發生在途中、需要花時間的事件：協助長者尋找眼鏡。",
        "先幫忙、後遲到，時間順序和因果關係吻合。",
        "其他選項描述城市、眼鏡外觀或觀眾關門，題幹都沒有提到。",
        "答案 D：He stopped to help the neighbor。這個停留導致他錯過開場。",
    ]),
    5: ("情緒變化題比較事件前後的狀態，再找促成轉變的證據；不能把結尾表情單獨當成起始情緒。", [
        "標出時間起點：At first 明確表示 Ava 一開始擔心模型會失敗。",
        "找轉折線索：夥伴指出一條鬆脫的電線，讓問題變得可理解、可處理。",
        "Ava 修好電線後微笑，這是信心增加而非害怕或疲倦的線索。",
        "從擔心到能動手修正，最合適的前後狀態是 worried → confident。",
        "答案 A。修正問題後的微笑支持她由擔憂轉為有把握。",
    ]),
    6: ("好標題應抓住敘事最重要的等待與結果，而非沿用一個物件名詞或塞入故事沒有的競賽、食譜、車站。", [
        "依事件順序圈出種子走失、孩子種下它、等待數週、冒出第一片綠葉。",
        "故事的轉折成果不是立刻長大，而是耐心等待後看見第一片葉子。",
        "標題可以省略細節，但要留下這個最能代表故事的結果。",
        "Race、recipe、train station 都沒有出現在情節；Waiting for the First Leaf 則涵蓋等待與收穫。",
        "答案 B。這個標題最能代表種植後等待新芽的整段故事。",
    ]),
    7: ("重述故事先找最早引入後續行動的事件；地圖是尋路的起點，抵達花園和分享花朵都在它之後。", [
        "先建立事件鏈：發現地圖 → 沿路前進 → 到達隱藏花園 → 在門邊休息／分享花朵。",
        "題目問第一句，應選能讓後續尋路開始的起始事件。",
        "休息、分享花朵是抵達後的收尾；沿樹間小路是發現地圖之後的行動。",
        "在書下找到舊地圖，提供了探索路徑的理由和工具。",
        "答案 C：The child discovers an old map under a book. 它在時間與因果上都居首。",
    ]),
    8: ("故事寓意不是把一個情節換句話說，而是從拒絕、受阻、接受建議到完成任務的變化，歸納可遷移的想法。", [
        "先比對角色前後做法：起初拒絕幫忙，獨自嘗試時遇到困難。",
        "轉折是接受朋友的建議，之後才完成專案。",
        "把這個結果提升成一般原則：適當求助能讓困難任務變得可完成。",
        "「永不聽建議」「避開所有人」與「建議只會拖慢」都和故事結果相反。",
        "答案 D。它從角色改變推得寓意，而不是把細節誤當成教訓。",
    ]),
    9: ("有根據的回應須同時表明判斷並指出文本行為；理由必須能讓讀者看見觀點從何而來。", [
        "題目要求 opinion with evidence，因此核對選項是否同時含有看法與支持細節。",
        "I think the child is honest 是明確判斷；because 引出判斷依據。",
        "returned the wallet instead of keeping the money 是可從故事核對的行動證據。",
        "只談錢包顏色、故事形式或表示不知道，都沒有形成有證據的觀點。",
        "答案 B。它以歸還錢包的行為支撐「誠實」這個評價。",
    ]),
    10: ("整合摘要保留問題、主要行動與結果，並按因果連起來；工具清單或任意擴張出的事件都不算完整摘要。", [
        "抽出故事骨架：社區標誌壞了 → 孩子找工具 → 鄰居一起修理 → 遊客更容易找到公園。",
        "摘要須留下共同修復這個核心行動，不必列舉每件工具或旁枝細節。",
        "結果「更容易找到公園」說明修標誌的作用，讓行動與結果連成因果。",
        "其餘選項不是加入無根據的新城市／公園消失，就是只列工具而漏掉事件結果。",
        "答案 C。它保留問題、合作修復與改善方向，是最完整而精簡的總結。",
    ]),
}

OBSERVED = "僅參照公開公校英文評量中的故事主旨、情節／角色理解、原因與文本證據判讀方式；本題故事、人物、選項與答案均獨立創作，未複製原卷。"


def refs_for(locators: list[str]) -> list[dict]:
    return [{
        "url": source["url"], "title": source["title"], "year": source["year"],
        "subject": "english", "locator": locator, "locatorLevel": "page",
        "observedPattern": OBSERVED, "reuseDecision": "pattern-only", "status": "recorded",
    } for source, locator in zip(SOURCES, locators, strict=True)]


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    known = {source["id"] for source in catalog["sources"]}
    for source in SOURCES:
        if source["id"] not in known:
            catalog["sources"].append({
                "id": source["id"], "school": source["school"], "grade": source["grade"],
                "subject": source["subject"], "exam": source["exam"], "questionUrl": source["url"],
                "answerLocator": source["examLocator"],
                "usePolicy": "僅供故事閱讀理解題型與推理能力方向研究；不保存或重製原題文字、選項、答案或版面。",
                "verifiedAt": TODAY,
            })
    catalog["updatedAt"] = TODAY
    CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for number, (correct_text, key, option_texts, locators) in ITEMS.items():
        path = QDIR / f"question-english-performance-5-iv-10-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        assert option_texts[ord(key) - 65] == correct_text, f"key/text mismatch at {number}"
        data["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(option_texts)]
        data["answer"]["value"] = key
        data["solutionStrategy"], data["solutionSteps"] = ITEM_CONTENT[number]
        data["solutionSteps"] = list(data["solutionSteps"])
        data["examPatternRefs"] = refs_for(locators)
        data["provenance"]["sourceUrl"] = SOURCES[0]["url"]
        data["provenance"]["sourceLocator"] = "國昌、小港、武崙三所公立國中公開英文段考；本題逐題頁碼／題號及pattern-only界線見 examPatternRefs。"
        data["provenance"]["authoringNote"] = "依官方課綱與 KG-english-performance-5-iv-10，取三所公立學校英語閱讀題的故事主旨及證據推理能力方向獨立撰寫；情節與答案均為原創，仍待完整內容與版權 gate。"
        data["updatedAt"] = TODAY
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("updated 10 original story-reading questions; added 2 source records; A/B/C/D=2/3/3/2")


if __name__ == "__main__":
    main()
