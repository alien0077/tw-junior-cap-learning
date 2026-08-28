"""替換國文 Bc-Ⅳ-2 說明方法模板題，採公開試題能力方向安全獨立改編。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/806/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1(%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F%E2%94%80%E5%9C%8B%E8%AA%9E%E6%96%87).pdf"

ITEMS = [
    ("短文：「校園樹木有三種主要用途：遮蔭、降低風速、提供鳥類棲息地。」這段主要採用哪種說明方式？", ["列舉", "因果", "比較", "定義"], "A", "逐項列出樹木的三種用途，屬於列舉。", "easy", "列舉辨識"),
    ("「連日高溫使池塘蒸發加快，水位因此下降。」這句呈現哪種關係？", ["因果", "分類", "比較", "定義"], "A", "高溫與蒸發是原因，水位下降是結果，形成因果關係。", "easy", "因果關係辨識"),
    ("文章將紙本地圖與電子地圖分別從更新速度、攜帶方式與定位功能說明，這是運用什麼方法？", ["比較", "列舉", "定義", "問題解決"], "A", "以相同面向說明兩個對象的異同，屬於比較。", "easy", "比較方法辨識"),
    ("作者把校園植物分為喬木、灌木與草本，並分別說明特徵。這種安排主要是什麼？", ["分類", "因果", "引用", "譬喻"], "A", "依共同標準把植物分組並說明特徵，屬於分類。", "easy", "分類方法辨識"),
    ("「所謂城市熱島，是指都市區域的氣溫通常高於周邊郊區的現象。」這句主要在做什麼？", ["定義概念", "列出例子", "比較優缺點", "提出解決方案"], "A", "句子直接界定術語的意義與範圍，是定義。", "easy", "定義方法辨識"),
    ("文章先指出校門口放學時壅塞，再提出分流接送與調整號誌兩項措施。這種寫法最接近哪種方式？", ["問題解決", "單純描寫", "時間順序", "人物對話"], "A", "先指出問題，再提出可行措施，符合問題解決的說明方式。", "medium", "問題解決結構"),
    ("為說明節水效果，作者列出安裝省水器具前後的每月用水量。這樣的資料最能發揮什麼作用？", ["提供具體數據支持比較", "把數據變成故事對話", "避免讀者檢查證據", "只增加文章篇幅"], "A", "前後用水量是具體數據，可支持節水效果的比較與判斷。", "medium", "數據與說明"),
    ("「蜜蜂負責授粉，蝴蝶也能傳播花粉；兩者都能幫助植物繁殖，但活動時間與偏好的花種不同。」這段重點是什麼？", ["比較共同點與差異", "只定義蜜蜂", "只列出時間順序", "提出交通問題的解法"], "A", "段落同時指出共同點與差異，重點是比較。", "medium", "比較的共同點與差異"),
    ("若文章主張『校園應設置雨水回收桶』，先說明缺水問題，再解釋回收桶如何收集雨水，最後估算可供澆灌的用量。這樣的組織有何優點？", ["由問題、方法到預期效果逐步說明", "只用情緒取代理由", "把不同主題任意拼接", "完全不涉及問題解決"], "A", "文章依序交代問題、處理方法與預期效果，說明脈絡完整。", "hard", "問題解決的完整脈絡"),
    ("說明一項新制度時，先交代術語定義，再分類介紹適用對象，最後列出實施步驟。這種安排最能幫助讀者什麼？", ["先建立概念，再掌握範圍與做法", "只記住零散例子", "避免理解關鍵詞", "把說明改成抒情詩"], "A", "先定義、再分類、後說明步驟，能建立由概念到應用的理解順序。", "hard", "多種說明方法組織"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-content-bc-iv-2-{i}.json"
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
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究說明方法與閱讀理解能力方向（{locator}）；另以官方語文領域課綱核對 Bc-Ⅳ-2（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
