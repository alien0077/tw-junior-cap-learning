"""替換國文 5-Ⅳ-1 的通用標點／朗讀題為獨立改編題。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-5-iv-1.json").read_text())["source"]["url"]
LESSON = "lesson-chinese-performance-5-iv-1"
KNOWLEDGE = "kg-chinese-performance-5-iv-1"

ITEMS = [
    ("班級公告寫著『請攜帶下列物品：水壺、雨具。』冒號的作用是什麼？", ["引出後面的列舉內容", "表示前句正在提問", "表示說話者突然驚訝", "連接兩個對比句"], "A", "冒號可引出後文的具體列舉。", "冒號與列舉"),
    ("朗讀『明天校外教學延期。』時，句末句號最主要提示哪項訊息？", ["語意告一段落，語氣通常收束", "必須把聲音提高成疑問", "後面一定還有三項列舉", "表示說話者正在驚嘆"], "A", "句號通常表示陳述句結束，朗讀時語氣較收束。", "句號與停頓"),
    ("『你已經把實驗器材收好了嗎？』最適合用哪種朗讀語氣？", ["疑問語氣，句末略上揚以等待回答", "命令語氣，句末完全下降", "列舉語氣，每字都停頓", "驚嘆語氣，大聲喊叫"], "A", "問號表示疑問，朗讀須呈現詢問並等待回應。", "問號與語氣"),
    ("導覽員朗讀『太好了！我們終於找到出口。』時，驚嘆號主要表現什麼？", ["強烈的情緒反應", "兩個分句的因果關係", "未完成的疑問", "後文的項目清單"], "A", "驚嘆號可加強喜悅、驚訝等情緒。", "驚嘆號"),
    ("將『先檢查電源再按下開關』改成『先檢查電源，再按下開關。』，逗號帶來的主要效果是什麼？", ["分開先後步驟，讓朗讀與理解更清楚", "把陳述句改成疑問句", "表示兩個步驟互相矛盾", "表示後文一定是引用"], "A", "逗號分開連續動作，使步驟關係較清楚。", "逗號與步驟"),
    ("朗讀對話時，甲說明規則、乙提出疑問。最適合的處理方式為何？", ["依角色與語意調整重音、速度和語調", "所有句子使用完全相同的語氣", "只提高音量，不理會標點", "把疑問句讀成平淡標題"], "A", "有感朗讀要依角色、語意與標點調整聲情。", "對話朗讀"),
    ("句子『雨停了；操場仍然積水。』使用分號，最能顯示什麼？", ["兩個相關但相對獨立的分句", "後句是前句的物品清單", "前句是在詢問答案", "說話者突然發出驚呼"], "A", "分號可連接語意相關、結構相近的獨立分句。", "分號"),
    ("朗讀前把『一定』『終於』圈起來，主要是在規劃哪一項？", ["需要加強的重音與語氣", "每個字的部首", "文章的作者資料", "紙張的裝訂方向"], "A", "圈出關鍵詞有助於朗讀時安排重音與情感。", "重音標記"),
    ("『老師說如果完成修正就可以重新提交』容易誤解時，最適合先做什麼？", ["依條件與結果的關係補上適當停頓或標點", "刪除『如果』讓句意更模糊", "把所有標點改成驚嘆號", "只提高最後一字的音量"], "A", "先辨認條件與結果，再用停頓或標點呈現語意層次。", "停頓與語意"),
    ("流暢有感朗讀一段說明文時，除了正確讀字，還應兼顧什麼？", ["依內容層次調整停頓、重音、速度與語調", "不論內容一律快速讀完", "只注意聲音越大越好", "完全忽略句末標點"], "A", "流暢有感朗讀需同時掌握正確性、流暢度與語意聲情。", "有感朗讀"),
]


def main() -> None:
    for i, (prompt, options, answer, explanation, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-5-iv-1-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        rotated = options[shift:] + options[:shift]
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + j), "text": text} for j, text in enumerate(rotated)]
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["difficulty"] = "medium"
        data["knowledgeIds"] = [KNOWLEDGE]
        data["lessonId"] = LESSON
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中公開國文段考；研究 5-Ⅳ-1 標點與朗讀能力題型（{locator}）；課綱：{CURRICULUM}",
            "authoringNote": "獨立改編，未重製原題文字、選項、文章、圖像或答案；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(ITEMS)} questions")


if __name__ == "__main__":
    main()
