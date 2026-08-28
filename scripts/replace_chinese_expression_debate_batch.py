"""替換國文 2-Ⅳ-3 明確表達與有條理論辯模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-2-iv-3.json").read_text())["source"]["url"]

ITEMS = [
    ("班會討論是否延長午休時，哪種發言最明確？", ["我主張延長五分鐘，因為多數同學反映用餐時間不足；可先試行兩週再檢討", "午休當然越長越好，大家都知道", "我覺得這件事很複雜，以後再說", "反正別班都這樣，我們照做就好"], "A", "發言同時提出主張、理由、具體時間與檢討方式，資訊最完整。", "easy", "主張理由與做法"),
    ("小組想改善校園噪音，哪項提案最符合有條理表達？", ["先測量午休音量，再針對超標區域設計提醒與改善措施", "大家不要吵就好了，這沒有什麼好討論", "噪音很可怕，所以所有活動都應取消", "我以前也遇過類似事情，先講我的故事"], "A", "先蒐集資料、界定問題，再提出對應措施，推理步驟清楚。", "medium", "問題界定與提案"),
    ("評論一篇主張『制服應改為運動服』的文章時，哪項回應最適當？", ["文章指出活動便利性，但尚未討論正式場合需求；可補充這項反面資料", "作者一定不懂學生生活", "我喜歡運動服，所以文章全部正確", "這篇文章字很多，應該很有道理"], "A", "回應指出文章已有理由與尚未處理的面向，並提出可補充的資料。", "medium", "評論與反面資料"),
    ("辯論『校園是否應全面禁用一次性杯』時，哪種說法最能避免過度推論？", ["可先從校內活動試辦減量，蒐集垃圾量與使用者意見後再決定", "只要禁用，所有環境問題都會消失", "反對的人就是不關心地球", "別的地方有人成功，所以我們一定完全成功"], "A", "先試辦、蒐集資料再評估，保留了證據與政策範圍的限制。", "hard", "政策論辯與限制"),
    ("準備三分鐘口頭報告時，哪種大綱最有條理？", ["現況與問題 → 兩項證據 → 解決方案 → 結論", "結論 → 無關笑話 → 個人回憶 → 結論", "連續放十個例子，不說明彼此關係", "只列資料來源，不交代報告主題"], "A", "大綱由問題、證據、方案到結論組織，聽眾容易掌握論述。", "easy", "報告結構"),
    ("同學說『圖書館人太多』，若要使這個說法可討論，最適合先追問什麼？", ["你指的是哪個時段、哪個區域？有沒有座位使用數據？", "你是不是只是在抱怨？", "那就把圖書館關掉吧？", "別人也這樣說，所以一定是真的"], "A", "釐清時間、地點並要求數據，能把模糊描述轉成可檢驗問題。", "medium", "模糊語句具體化"),
    ("演說者想說服同學參加閱讀活動，哪個結尾最有力？", ["若每人每週閱讀二十分鐘並記錄心得，下月可用紀錄比較收穫", "閱讀真的很棒，大家應該都知道", "我講完了，至於參不參加隨便", "活動內容和前面一樣，先不說明"], "A", "提出明確、可執行且能檢核的行動，結尾比口號更具說服力。", "medium", "演說呼籲"),
    ("評論同學的辯論表現時，哪項回饋最能幫助修正？", ["你的第二個理由有資料支持，但沒有回應對方的成本疑慮，可補一項比較", "你講話很快，所以整場都不好", "我同意你，沒有其他建議", "我不同意你，因為我就是這樣想"], "A", "回饋指出具體優點、缺口與可採取的修正方式。", "medium", "辯論回饋"),
    ("若反方提出『延長開放時間會增加電費』，正方最適合如何回應？", ["承認可能增加電費，再提出先試辦並比較借閱人次與用電量", "那你一定不喜歡讀書", "電費不重要，完全不用計算", "因為我們的主張很好，所以反方錯了"], "A", "先承認反方合理疑慮，再提出可驗證的試辦比較，回應有邏輯。", "hard", "反駁與回應"),
    ("報告資料顯示『受訪 50 人中 32 人支持』，哪句結論最精確？", ["在這 50 位受訪者中，64% 表示支持，仍不能直接代表全校", "全校有 64% 的人一定支持", "所有人都會因而改變行為", "這項措施已證明永遠有效"], "A", "32÷50=64%，且結論限定在受訪樣本，不超出資料能支持的範圍。", "easy", "統計結論表達"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-performance-2-iv-3-{i}.json"
        data = json.loads(path.read_text())
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
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究明確表達與有條理論辯能力方向（{locator}）；另以官方語文領域課綱核對 2-Ⅳ-3（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
