"""以公立國中國文段考常見圖表判讀能力，替換 Bc-Ⅳ-3 泛用題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/content-bc-iv-3.json").read_text())["source"]["url"]
ITEMS = [
    ("校園用水圖表標示『每月用水量（公噸）』。閱讀數值前，最先應確認什麼？", ["縱軸與單位的意義", "圖表紙張的顏色", "作者的座號", "標題是否押韻"], "A", "先確認量的名稱、單位與刻度，才能正確解讀數值。", "easy", "圖表標題與單位"),
    ("甲班回收量由 20 公斤增為 30 公斤，乙班由 40 公斤增為 45 公斤。若比較增加量，哪項正確？", ["甲班增加 10 公斤，乙班增加 5 公斤", "甲乙兩班都增加 5 公斤", "甲班增加 20 公斤，乙班增加 40 公斤", "只看最後數值便可判斷增加量相同"], "A", "增加量要用後來數值減去原來數值；甲為 10，乙為 5。", "medium", "數值差異"),
    ("兩張圖分別以『人次』和『百分比』呈現午餐選擇。直接比較圖上的 60 與 60，最可能忽略什麼？", ["兩者的單位與分母不同", "兩張圖的標題一定相同", "百分比必定比人次大", "圖表不可能同時使用兩種單位"], "A", "人次是數量，百分比是比例，兩者的單位與分母不同，不能直接以數字大小比較。", "hard", "單位與分母"),
    ("流程圖由『訪問同學』指向『整理回答』，再指向『提出建議』。箭頭主要協助讀者看出什麼？", ["工作的先後與步驟關係", "每一步的字體大小", "資料必然百分之百正確", "作者的出生地"], "A", "箭頭在此表示活動由蒐集到整理再到提出建議的流程順序。", "easy", "流程圖"),
    ("長條圖縱軸從 90 起跳，兩柱高度看似差很多。讀者最應如何避免誤判？", ["查看刻度起點與實際差值，再判斷視覺差異", "只依柱子看起來的高度下結論", "把縱軸起點當成零", "忽略圖表上的數字"], "A", "截斷縱軸會放大視覺差異，應讀取刻度與數值差，而不能只看柱高。", "hard", "截斷縱軸"),
    ("表格記錄三次測量值為 12、18、15。若問題是『哪次最高』，答案應如何找？", ["比較同一欄的數值，找出 18 所在的那次", "把三個數值相加後當成次數", "只看表格最左邊的欄名", "因為第三次最後出現所以一定最高"], "A", "題目問最高值時，需比較同一指標的數值；三者中 18 最大。", "easy", "表格比較"),
    ("圖例以實線代表紙本、虛線代表電子資料。圖例最主要的功能是什麼？", ["說明圖中符號各自代表的類別", "增加圖表的裝飾", "表示虛線數值一定較小", "取代所有座標與單位"], "A", "圖例提供符號與資料類別的對照，讓讀者知道不同線條代表什麼。", "easy", "圖例"),
    ("總參加人數從 100 人增至 200 人，其中甲活動占比由 40% 降至 30%。哪項理解最合理？", ["甲活動人數可能由 40 人增至 60 人，但占總人數比例下降", "甲活動人數一定減少為 30 人", "總人數增加表示各活動占比都增加", "只看占比即可知道甲活動的實際人數"], "A", "甲活動人數為 100×40%=40、200×30%=60；實際人數增加，但占比下降。", "hard", "總量與比例"),
    ("把圖表貼入報告時，若裁掉縱軸標籤與單位，最可能造成什麼問題？", ["讀者無法確認數值代表什麼，解讀可能失真", "圖表會自動變成照片", "所有數值會因此變成零", "報告主旨必然更加清楚"], "A", "缺少縱軸名稱與單位，讀者無法判定數值意義，容易做出錯誤結論。", "medium", "圖片裁切"),
    ("文字說明寫『今年借閱人次增加』，圖表卻顯示只有暑假月份增加。整合兩者時，最恰當的做法是什麼？", ["限定結論的時間範圍，改寫成『暑假月份增加』", "把圖表中沒有的月份也說成增加", "只保留文字而刪除圖表", "把局部資料概括成全年必然增加"], "A", "圖表只支持暑假月份的變化，文字結論應配合資料範圍，避免過度推論。", "hard", "文字與圖表整合"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-content-bc-iv-3-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究圖表與資料整合判讀題型（{locator}）；課綱 Bc-Ⅳ-3：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
