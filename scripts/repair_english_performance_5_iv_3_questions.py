#!/usr/bin/env python3
"""Repair answer placement and write item-specific solutions for English 5-IV-3."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/english"
TODAY = "2026-09-26"
SOURCE_URLS = [
    ("基隆市立中山高中國中部110學年度第1學期七年級英語科段考試題", "110-1", "https://oldcsjh.kl.edu.tw/books/file/263/110-1%E5%9C%8B%E4%B8%80%E8%8B%B1%E6%96%87%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf", "PDF第1頁第5至8題，聽力基本問答回應選擇"),
    ("花蓮縣立宜昌國中112學年度第2學期七年級第2次段考英語聽力試題", "112-2", "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=417&cfsn=2790&name=112-2-%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E8%81%BD%E5%8A%9B%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile", "PDF第1頁第7至8題及第2頁第9至13題，聽力基本問答回應選擇"),
    ("高雄市立大灣國中113學年度第2學期七年級第1次段考英語科試題", "113-2", "https://www.dwm.kh.edu.tw/upload/344/104_64184/113%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%BA%8C%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "PDF第1頁第5至8題，聽力基本問答回應選擇"),
]
ITEMS = {
 1: ("D", "先鎖定問句中的時間需求，再排除談電影類型、過去觀影或戲院設施的句子。", ["What time 問的是鐘點，不是電影內容或類型。", "因此回答要提供明確的開演時刻。", "At 7:30 this evening 給出今晚七點半這個具體時間。", "動作片的描述、上個月看過及戲院有幾個影廳，都沒有回答何時開始。", "正解是 D：今晚七點半直接回答電影何時開始。"]),
 2: ("B", "Why 要找原因；把攜帶雨傘的行動與可能下雨的理由連成因果。", ["Why are you carrying an umbrella 是詢問帶傘的原因。", "回答應解釋為何帶傘，而非只提供地點或時間。", "Because it may rain later 指出稍後可能下雨，能解釋帶傘的決定。", "門邊位置、借書經驗和公車站都不是帶傘的理由。", "正解是 B：預期稍後可能下雨，是帶傘的原因。"]),
 3: ("C", "How often 問頻率；辨認週期表達，別把地點、受益者或難度當頻率。", ["How often do you practice the piano 詢問練琴的頻率。", "先找能表示重複週期的時間用語。", "Twice a week 清楚說明每週練習兩次。", "音樂教室是地點，for my sister 表示對象，difficult 描述難度，都不是頻率。", "正解是 C：每週兩次是明確的練琴頻率。"]),
 4: ("A", "飲品邀請的回應要表明接受或拒絕；附加條件應落在飲用方式上。", ["Would you like some tea 是提供茶飲的邀請。", "回覆應先表達接受或拒絕，再補充飲用偏好。", "Yes, please 接受邀請，No sugar 說明不加糖，兩者語意相容。", "樓層、昨天做桌子和商店打烊時間都沒有回應這項邀請。", "正解是 A：接受茶並說明不要加糖，兩部分都回應邀請。"]),
 5: ("D", "現在完成式詢問成果是否完成；Not yet 與今晚補做標題構成一致的未完成計畫。", ["Have you finished 是詢問海報現在是否已經完成。", "注意回覆必須說明已完成、尚未完成，或交代進度。", "Not yet 表示還沒完成；今晚加上標題是具體的後續計畫。", "只說顏色沒有交代完成狀態；午餐改變話題；yesterday 也不符合此處的進行中工作。", "正解是 D：海報尚未完成，今晚會補上標題。"]),
 6: ("C", "借物請求需要允許／拒絕及必要時交付；比較回覆是否完成這個互動動作。", ["Could you lend me a pencil 是借用物品的請求。", "合宜回覆要表示准許或拒絕；若准許，也可以把物品交給對方。", "Sure 表示答應，Here you are 則完成遞交動作。", "昨天削鉛筆、考試難度和筆袋顏色都沒有回應借筆請求。", "正解是 C：答應借筆並把筆交給對方。"]),
 7: ("B", "交通建議要連結目的地與可搭乘路線；只說景點特徵並不能解決移動問題。", ["Which bus 是詢問前往博物館該選哪一班公車。", "回答應指出會在目的地或附近停靠的路線。", "The number 12 bus stops near it 提供可實際採用的公車選擇。", "博物館大小、曾經造訪和司機友善，都沒有指出該搭哪一班。", "正解是 B：搭12號公車可在博物館附近下車。"]),
 8: ("A", "Do you mind 是詢問是否介意；Not at all 表示不介意，因此允許開窗。", ["Do you mind if I open the window 是在確認開窗會不會造成困擾。", "要依 mind 的語意判讀回覆，不能把 yes／no 機械地當成准許或拒絕。", "Not at all 表示完全不介意；室內很暖也支持開窗。", "筆記本的回應換了動作；花園景色和看不見黑板都沒有表達是否介意。", "正解是 A：對方不介意開窗，並補充室內很暖。"]),
 9: ("C", "How was 問已發生經驗的評價；答案需給結果或感受，時態與內容都要對上。", ["How was your group project 是詢問已完成小組專題的評價。", "找過去式的結果或感受，不要選截止日、物品位置或未來會議。", "It went well 評價結果順利；everyone shared the work 補上與合作相關的理由。", "下週五、背包裡的位置及明天的會議都屬於不同時間或資訊。", "正解是 C：專題進行順利，組員也共同分工。"]),
 10: ("B", "失物情境先辨認當下需要，再選能共同採取且可能找回物品的下一步。", ["Cannot find my bus card 說明交通卡不見了，現在需要尋找。", "合用的回覆應提出能協助定位或找回卡片的行動。", "一起查看失物招領處是可執行的搜尋步驟，也提供陪伴協助。", "卡片材質、每天搭公車和昨天找到鑰匙，都無法幫忙找這張卡。", "正解是 B：一起去失物招領處查找，直接處理卡片遺失問題。"]),
}

def main() -> None:
    for number, (key, strategy, steps) in ITEMS.items():
        path = QDIR / f"question-english-performance-5-iv-3-{number}.json"
        item = json.loads(path.read_text(encoding="utf-8"))
        old = {option["id"]: option["text"] for option in item["options"]}
        correct = old[item["answer"]["value"]]
        wrong = [option["text"] for option in item["options"] if option["text"] != correct]
        wrong.insert(ord(key) - 65, correct)
        item["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(wrong)]
        item["answer"]["value"] = key
        item["answer"]["explanation"] = steps[-1]
        item["solutionStrategy"] = strategy
        item["solutionSteps"] = steps
        note = [
            "公開基本問答呈現時間詢問與具體時刻回應；僅參照題型能力，不沿用試卷內容。",
            "公開基本問答呈現原因問句與因果回應；僅參照溝通功能，不沿用試卷內容。",
            "公開基本問答要求辨認頻率詢問與週期表達；僅參照能力方向。",
            "公開基本問答呈現邀請／提供與接受或拒絕的語用配對；僅參照能力方向。",
            "公開基本問答要求理解完成狀態並選擇相符回應；僅參照能力方向。",
            "公開基本問答包含請求及允許回應功能；僅參照溝通模式，不複製原句。",
            "公開基本問答要求依交通目的辨認路線資訊；僅參照能力方向。",
            "公開基本問答測量禮貌詢問與許可回應的語用理解；僅參照能力方向。",
            "公開基本問答要求依過去活動問題選擇評價性回應；僅參照能力方向。",
            "公開基本問答呈現生活問題與可行協助回應；僅參照能力方向。",
        ][number - 1]
        item["examPatternRefs"] = [{"url": url, "title": title, "year": year, "subject": "english", "locator": locator, "locatorLevel": "page", "observedPattern": note + " 不含原卷題幹、選項、音檔或答案。", "reuseDecision": "pattern-only", "status": "recorded"} for title, year, url, locator in SOURCE_URLS]
        item["provenance"]["sourceUrl"] = SOURCE_URLS[0][2]
        item["provenance"]["sourceLocator"] = "基隆中山高中國中部110-1、花蓮宜昌112-2、高雄大灣113-2七年級公開英文段考基本問答；各校PDF頁次及題號列於 examPatternRefs。"
        item["provenance"]["authoringNote"] = "依官方課綱與 KG-english-performance-5-iv-3 的常見問答能力，參照三所公立學校段考基本問答題型的溝通功能方向獨立撰寫；情境、對話與選項皆原創，未複製試卷文字或音檔；完整內容與版權 gate 尚待完成。"
        item["updatedAt"] = TODAY
        path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("repaired ten English 5-IV-3 answer mappings, strategies, steps, and source references")

if __name__ == "__main__":
    main()
