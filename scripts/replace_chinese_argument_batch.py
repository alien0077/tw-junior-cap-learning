"""替換國文 Bd-Ⅳ-2 的固定選項題；只借鑑公開會考的閱讀論證能力方向。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/01_114P_Chinese.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/806/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1(%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F%E2%94%80%E5%9C%8B%E8%AA%9E%E6%96%87).pdf"

ITEMS = [
    ("短文：「把閱讀地圖畫成一條路，讀者便能看見作者如何從問題走向結論。」這句主要運用哪種論證方式？", ["比喻論證", "數據論證", "因果論證", "引用論證"], "A", "以地圖與道路的相似關係說明文章結構，屬於比喻論證。", "easy", "比喻論證辨識"),
    ("某文比較紙本筆記與電子筆記，兩者都從「整理速度、查找便利、保存方式」三個面向說明。這樣安排的主要優點是什麼？", ["採用共同標準，讓比較較公平", "只挑一方有利的資料", "以情緒取代比較依據", "讓兩個對象無法區分"], "A", "兩個對象用相同面向呈現，讀者才能依共同標準判斷異同。", "easy", "比較論證的共同標準"),
    ("作者主張「校園應增加遮蔭」，並指出操場測得的地表溫度比樹蔭下高 8°C。這筆資料在論證中最接近什麼角色？", ["支持主張的證據", "與主張無關的背景", "反駁主張的結論", "單純的比喻對象"], "A", "溫度差資料直接支持增加遮蔭有助降溫的主張，因此是證據。", "medium", "證據與主張關係"),
    ("有人說：「小明一次考好，就像一顆流星，所以他以後每次都會第一名。」這個推論最主要的問題是什麼？", ["從單一事件過度推論長期結果", "比較時使用相同標準", "提供多筆可檢驗資料", "清楚指出比喻的相似點"], "A", "一次表現不能充分支持每次都第一名的長期結論，屬於證據不足的過度推論。", "medium", "論證漏洞判讀"),
    ("下列哪一項最能以比喻支持「練習需要持續累積」？", ["練習像存錢，每次投入一點，成果會逐步增加", "練習很重要，因為大家都這樣說", "練習的字數比休息多", "練習一定能讓所有人立刻成功"], "A", "存錢與練習都具有逐次累積的特徵，這個相似點能支持主張；其餘不是比喻或推論過度。", "medium", "比喻與主張的對應"),
    ("比較甲、乙兩種交通方式時，作者只列甲的票價，卻用乙最擁擠的一天作為代表。這樣的比較最可能有何問題？", ["取樣與比較標準不一致", "兩者都使用相同資料", "已完整呈現雙方優缺點", "結論必然沒有任何限制"], "A", "甲乙的資料條件不同，不能直接公平比較；應明確說明範圍並採相同標準。", "medium", "比較資料的公平性"),
    ("一段文章先提出「老建築值得保存」，接著列出建築年代、結構特色與居民訪談，最後回扣保存理由。這種安排主要形成什麼效果？", ["以多種證據逐步支持核心主張", "用無關故事取代論證", "只靠作者身分要求讀者相信", "刻意避免提出任何結論"], "A", "年代、結構與訪談從不同面向支持同一主張，讓論證較完整。", "easy", "多重證據支持主張"),
    ("「雨傘像一把可攜式屋頂，能在下雨時提供遮蔽。」若要檢查這個比喻是否恰當，最應先問什麼？", ["兩者是否在『提供遮蔽』上具有相關相似點", "兩者的重量是否完全相同", "雨傘是否一定比屋頂昂貴", "句子是否使用最多形容詞"], "A", "比喻是否成立，關鍵在本體與喻體是否有能支持主張的相關相似點。", "easy", "比喻恰當性檢核"),
    ("作者以兩個城市的公共自行車資料比較便利性，但甲市統計一整年、乙市只統計一週。讀者最合理的判斷是什麼？", ["資料期間不同，結論需要保留限制", "只要數字較大就一定較便利", "兩組資料可以直接視為同一範圍", "統計期間與結論完全無關"], "A", "統計期間不同會影響代表性，應先指出限制，不能直接把兩者當成同等條件。", "hard", "資料範圍與結論限制"),
    ("若文章主張「閱讀能拓展視野」，下列哪種寫法最能完成較可靠的論證？", ["先界定拓展視野，再提供閱讀前後的具體表現作比較", "只重複『閱讀很重要』而不提供理由", "用一個人的感想推論所有人都相同", "只寫華麗比喻而不說明相似點"], "A", "先界定概念，再以可比較的具體表現提供證據，主張與理由的關係較清楚。", "hard", "完整論證設計"),
]

def main() -> None:
    for i, (prompt, options, answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-content-bd-iv-2-{i}.json"
        data = json.loads(path.read_text())
        # 將正解輪替至不同位置，避免形成可由選項位置猜答案的模板。
        shift = i % 4
        options = options[shift:] + options[:shift]
        answer = chr(65 + ((4 - shift) % 4))
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(options)]
        data["difficulty"] = difficulty
        data["answer"] = {"value": answer, "explanation": explanation}
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": f"114年國中教育會考國文科；研究閱讀理解、論證、比較與寫作分析能力方向（{locator}）；官方答案表：{ANSWER}；另以官方語文領域課綱核對 Bd-Ⅳ-2（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
