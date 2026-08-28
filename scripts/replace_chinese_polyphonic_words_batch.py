"""替換國文 4-Ⅳ-3 一字多音多義模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/01_114P_Chinese.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-4-iv-3.json").read_text())["source"]["url"]

ITEMS = [
    ("下列「行」字的讀音，何者標示正確？", ["行走：ㄒㄧㄥˊ；銀行：ㄏㄤˊ", "行走：ㄏㄤˊ；銀行：ㄒㄧㄥˊ", "兩詞都讀ㄒㄧㄥˊ", "兩詞都讀ㄏㄤˊ"], "A", "『行走』讀ㄒㄧㄥˊ，『銀行』讀ㄏㄤˊ；讀音須依詞義與詞語判定。", "easy", "行的一字多音"),
    ("下列「長」字的讀音，何者標示正確？", ["長大：ㄓㄤˇ；長短：ㄔㄤˊ", "長大：ㄔㄤˊ；長短：ㄓㄤˇ", "兩詞都讀ㄓㄤˇ", "兩詞都讀ㄔㄤˊ"], "A", "『長大』指成長，讀ㄓㄤˇ；『長短』指長度，讀ㄔㄤˊ。", "easy", "長的一字多音"),
    ("下列「樂」字的讀音，何者標示正確？", ["樂趣：ㄌㄜˋ；音樂：ㄩㄝˋ", "樂趣：ㄩㄝˋ；音樂：ㄌㄜˋ", "兩詞都讀ㄌㄜˋ", "兩詞都讀ㄩㄝˋ"], "A", "『樂趣』讀ㄌㄜˋ，『音樂』讀ㄩㄝˋ；詞義不同會造成讀音不同。", "easy", "樂的一字多音"),
    ("下列「降」字的讀音，何者標示正確？", ["降落：ㄐㄧㄤˋ；投降：ㄒㄧㄤˊ", "降落：ㄒㄧㄤˊ；投降：ㄐㄧㄤˋ", "兩詞都讀ㄐㄧㄤˋ", "兩詞都讀ㄒㄧㄤˊ"], "A", "『降落』是落下，讀ㄐㄧㄤˋ；『投降』是屈服，讀ㄒㄧㄤˊ。", "medium", "降的一字多音"),
    ("下列「參」字的讀音，何者標示正確？", ["參加：ㄘㄢ；人參：ㄖㄣˊㄕㄣ", "參加：ㄕㄣ；人參：ㄖㄣˊㄘㄢ", "兩詞中的參都讀ㄘㄢ", "兩詞中的參都讀ㄕㄣ"], "A", "『參加』讀ㄘㄢ，『人參』的參讀ㄕㄣ；應以完整詞語查證。", "medium", "參的一字多音"),
    ("下列「處」字的讀音，何者標示正確？", ["處理：ㄔㄨˇ；處所：ㄔㄨˋ", "處理：ㄔㄨˋ；處所：ㄔㄨˇ", "兩詞都讀ㄔㄨˇ", "兩詞都讀ㄔㄨˋ"], "A", "『處理』是動作，讀ㄔㄨˇ；『處所』指地方，讀ㄔㄨˋ。", "medium", "處的一字多音"),
    ("下列「數」字的讀音，何者標示正確？", ["數學：ㄕㄨˋ；數落：ㄕㄨˇ", "數學：ㄕㄨˇ；數落：ㄕㄨˋ", "兩詞都讀ㄕㄨˋ", "兩詞都讀ㄕㄨˇ"], "A", "『數學』讀ㄕㄨˋ；『數落』指責備，讀ㄕㄨˇ。", "medium", "數的一字多音"),
    ("下列「傳」字的讀音，何者標示正確？", ["傳送：ㄔㄨㄢˊ；傳記：ㄓㄨㄢˋ", "傳送：ㄓㄨㄢˋ；傳記：ㄔㄨㄢˊ", "兩詞都讀ㄔㄨㄢˊ", "兩詞都讀ㄓㄨㄢˋ"], "A", "『傳送』讀ㄔㄨㄢˊ；『傳記』是記載人物生平的文體，讀ㄓㄨㄢˋ。", "medium", "傳的一字多音"),
    ("下列「薄」字的讀音，何者標示正確？", ["薄荷：ㄅㄛˋ；薄弱：ㄅㄛˊ", "薄荷：ㄅㄛˊ；薄弱：ㄅㄛˋ", "兩詞都讀ㄅㄛˋ", "兩詞都讀ㄅㄛˊ"], "A", "『薄荷』讀ㄅㄛˋ；『薄弱』讀ㄅㄛˊ，不能只依部件或字形猜讀音。", "hard", "薄的一字多音"),
    ("遇到「重」出現在『重複』與『重量』時，最適合的查證步驟是什麼？", ["先辨認詞義，再查字典確認各詞的讀音與解釋", "看到同一個字就直接套用同一讀音", "只看字的筆畫數決定讀音", "只讀句子第一個字便下結論"], "A", "一字多音多義要先依詞語與上下文判斷，再用字典核對，不能機械套用。", "easy", "字典查證策略"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-performance-4-iv-3-{i}.json"
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
            "sourceLocator": f"114年國中教育會考國文科試題本；研究一字多音、多義、詞語判讀與字典查證能力方向（{locator}）；官方答案表：{ANSWER}；另以官方語文領域課綱核對 4-Ⅳ-3（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
