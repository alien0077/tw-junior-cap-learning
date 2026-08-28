"""替換國文 4-Ⅳ-4 書體與碑帖欣賞模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-4-iv-4.json").read_text())["source"]["url"]

ITEMS = [
    ("欣賞一幅書法作品時，若要判斷整體章法，最應觀察什麼？", ["字與字、行與行的間距及整體布局", "作品裝框所用的價格", "作者當天的座位", "展場播放的音樂"], "A", "章法涉及字與字、行與行的安排及整體布局，不能只看外在裝裱。", "easy", "章法觀察"),
    ("下列哪項描述最符合楷書的基本特徵？", ["筆畫與結構較端正清楚，便於辨認", "筆畫大量省略到難以辨認", "字形必須連成一條曲線", "只能使用在印章上"], "A", "楷書字形端正、筆畫清楚，是辨識與臨寫的重要基礎。", "easy", "楷書特徵"),
    ("行書通常被描述為介於哪兩種書體之間？", ["楷書與草書", "隸書與篆書", "甲骨文與金文", "黑體與明體"], "A", "行書在楷書的可辨識性與草書的流動性之間，具有較連貫的書寫特色。", "easy", "行書定位"),
    ("若作品筆畫連帶、省略較多，仍可辨認字形，但比楷書更流動，最可能屬於哪種書體？", ["行書", "甲骨文", "楷書", "隸書"], "A", "筆畫較連帶且仍保有辨識度，是行書常見的視覺特徵。", "medium", "書體判讀"),
    ("觀察隸書作品時，哪項筆畫特色最值得留意？", ["橫畫常見波磔，字形具有較寬展的感覺", "所有筆畫都必須完全相同粗細", "字形一定上下顛倒", "作品不能有任何橫畫"], "A", "隸書常可觀察到波磔等筆意與較寬展的結體；仍應以作品整體特徵判斷。", "medium", "隸書特色"),
    ("碑帖中的『帖』通常是指什麼類型的書法資料？", ["名家法書的摹本、拓本或臨習範本等傳本", "只指展覽門票", "只指書法家的印章尺寸", "只指紙張的製造年份"], "A", "『帖』多指流傳供學習、觀摩的法書傳本，不能把名稱當成單一紙張規格。", "medium", "碑帖概念"),
    ("比較同一字在兩幅碑帖中的寫法時，哪種做法最有助於學習？", ["同時比較筆畫方向、結構比例、重心與章法", "只看哪幅作品價格較高", "只數兩字是否有相同筆畫數", "只依作者名氣判定優劣"], "A", "從筆畫、結構、重心與章法比較，才能形成有根據的書體觀察。", "medium", "碑帖比較"),
    ("若一幅作品單字很漂亮，但字距忽大忽小、行距凌亂，評論時最精確的說法是什麼？", ["單字結構有優點，但整體章法仍可改善", "只要單字漂亮，章法必定完美", "字距凌亂代表一定不是書法", "只看落款即可判斷全部"], "A", "可分別評論單字與整體章法，避免以單一面向取代完整觀察。", "medium", "局部與整體"),
    ("臨寫碑帖後要檢查自己是否掌握字形，哪項證據最直接？", ["對照原帖檢查筆畫、比例、重心與筆勢", "只確認自己寫得比別人快", "只看墨水顏色是否相同", "只記住作品的展覽地點"], "A", "對照筆畫、比例、重心與筆勢，能具體檢驗臨寫是否接近原帖特徵。", "easy", "臨寫檢核"),
    ("欣賞碑帖時，哪種結論最符合有根據的評析？", ["指出作品的結構或筆勢特色，並以可觀察的字例說明", "只說名家作品一定最好，不需提出觀察", "只依裝裱華麗程度評價", "只用『很有氣質』而不說明原因"], "A", "具體指出可觀察特色並舉例，評析才有證據而不是只靠名氣或感覺。", "easy", "書法評析證據"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-performance-4-iv-4-{i}.json"
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
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究書體、碑帖與書法欣賞能力方向（{locator}）；另以官方語文領域課綱核對 4-Ⅳ-4（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
