"""替換國文學習內容中的通用自我檢核題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/learning-content.json").read_text())["source"]["url"]
ITEMS = [
    ("閱讀公告『施工期間，東側入口暫停通行，請改由西側入口進入』，若要抓住關鍵資訊，最應先找什麼？", ["限制的時間或情況、受影響的地點與替代做法", "公告使用的紙張顏色", "發布者的座號", "最後一個標點符號"], "A", "公告的實用重點在於何時或何種情況、哪裡受影響及應採取什麼做法。", "easy", "公告資訊擷取"),
    ("句子『他把資料重新核對，因而找出了統計表中的錯誤』中，『因而』最接近哪種語意關係？", ["因果", "轉折", "選擇", "並列"], "A", "重新核對是原因，找出錯誤是結果，『因而』表示因果關係。", "easy", "關聯詞判讀"),
    ("下列哪一句的引號內詞語使用最恰當？", ["經過多次討論，團隊終於『達成』共識", "他把問題『消滅』後再向老師請教", "這篇報告的資料十分『荒涼』", "小明『聆聽』了一本厚重的字典"], "A", "『達成共識』是常見且語意搭配恰當的用法；其餘詞語與語境搭配不當。", "medium", "詞語搭配"),
    ("若要判斷一段說明文字的主旨，哪種做法最可靠？", ["綜合標題、段落重點與反覆出現的核心概念", "只抄下第一個形容詞", "只看全文最長的句子", "以自己熟悉的主題取代文章內容"], "A", "主旨需由整體線索歸納，不能只依單一詞語或讀者預設判定。", "medium", "主旨歸納"),
    ("圖表標示『每月借閱人次』，橫軸為月份、縱軸為人次。要比較哪個月最高，應如何做？", ["在同一縱軸尺度下比較各月份柱高與數值", "把月份名稱當成數值相加", "只看柱子的顏色深淺", "忽略縱軸單位直接猜測"], "A", "確認橫軸、縱軸與單位後，才能以同一尺度比較各月份數值。", "easy", "圖表閱讀"),
    ("一篇文章先提出主張，再引用調查結果，最後說明調查的樣本限制。這樣安排最能展現什麼？", ["提出主張時同時交代證據與結論適用範圍", "只用資料裝飾文章而不支持主張", "刻意把限制當成文章主旨", "表示所有調查結果都能推論全國"], "A", "證據與限制一起呈現，可讓讀者判斷主張有多少支持、結論能推到什麼範圍。", "hard", "論證與限制"),
    ("下列哪一組字的部件關係最適合用來推測字義，而不宜直接推測讀音？", ["明、林", "晴、清", "河、何", "銅、同"], "A", "『明、林』的部件組合可提示日月、雙木等意義線索；其他選項較明顯涉及形聲字的聲旁線索。", "hard", "字形結構"),
    ("讀到『他表面答應，心裡卻另有打算』時，『卻』在句中主要表示什麼？", ["轉折", "承接", "遞進", "因果"], "A", "前後分句的表面答應與內心另有打算不一致，因此『卻』表轉折。", "easy", "語句關係"),
    ("若文章只提供『受訪的三十位學生』資料，結論卻寫成『所有學生都如此』，最需要指出哪項問題？", ["樣本數與涵蓋範圍不足，不能直接推論所有學生", "文章一定沒有任何數據", "只要有數字就能代表所有人", "結論越肯定就越符合證據"], "A", "樣本數與母群範圍不一致，屬於超出證據的過度推論。", "hard", "資料推論"),
    ("修改一段文章時，若發現同一概念在相鄰兩句重複出現，最適合先做什麼？", ["確認重複是否有必要，再合併或改用更精確的銜接", "把兩句全部刪除，不看上下文", "加入更多無關形容詞", "只調整字體顏色"], "A", "先判斷重複的功能，再透過合併或銜接提升表達精確度，不能脫離上下文任意刪除。", "medium", "文章修改"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-learning-content-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究字音字形、語詞、圖表與文本判讀題型（{locator}）；課綱學習內容：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
