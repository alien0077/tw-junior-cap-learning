"""替換國文 4-Ⅳ-1 詞語理解與使用模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.grow22.com/download/114/114_cp/01_114P_Chinese.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-4-iv-1.json").read_text())["source"]["url"]

ITEMS = [
    ("下列句子中的「佇立」使用最恰當的是：", ["夕陽西下，他佇立在港邊，久久凝望遠方", "妹妹佇立早餐，把牛奶喝完", "我們佇立三張桌子完成分組", "雨水佇立在屋簷，立刻流下"], "A", "『佇立』指長時間站立，放在港邊凝望的語境最恰當。", "easy", "詞義與語境"),
    ("下列句子中的「不約而同」使用最恰當的是：", ["聽見鐘聲後，同學們不約而同地走向集合場", "大家事先約好時間，因此不約而同地參加會議", "他每天不約而同地按照鬧鐘起床", "我不約而同地單獨完成了整份作業"], "A", "『不約而同』指沒有事先約定，卻做出相同反應；第一句符合。", "easy", "成語條件判讀"),
    ("下列句子中的「絡繹不絕」使用最恰當的是：", ["展覽開幕後，參觀人潮絡繹不絕地進入會場", "他絡繹不絕地只寫了一個字", "這棵樹絡繹不絕地長出一片葉子", "我絡繹不絕地一次關上門"], "A", "『絡繹不絕』形容人、車或事物接連不斷，第一句使用正確。", "easy", "成語使用"),
    ("下列句子中的「相形見絀」使用最恰當的是：", ["和經驗豐富的選手相比，他的表現相形見絀", "兩座山相形見絀地同樣高", "她相形見絀地準時抵達教室", "這張白紙相形見絀地沒有任何字"], "A", "『相形見絀』指相比之下顯得不足，第一句有明確比較對象。", "medium", "比較語境"),
    ("下列句子中的「首當其衝」使用最恰當的是：", ["暴雨來襲時，位於低窪處的村落首當其衝受到淹水影響", "他首當其衝地獲得全班最高分而感到開心", "妹妹首當其衝地把蛋糕切成四份", "這本書首當其衝地放在書架第二層"], "A", "『首當其衝』指最先受到衝擊或災害，第一句符合。", "medium", "成語語義與事件"),
    ("下列句子中的「莫衷一是」使用最恰當的是：", ["委員對開放時間各有看法，討論很久仍莫衷一是", "全班已有一致決定，因此莫衷一是地照表操課", "他莫衷一是地獨自跑完比賽", "花朵莫衷一是地在春天盛開"], "A", "『莫衷一是』指意見分歧、不能得到一致結論，第一句正確。", "medium", "意見與結論"),
    ("下列句子中的「按部就班」使用最恰當的是：", ["他按部就班地完成實驗：先記錄，再操作，最後整理結果", "他按部就班地突然衝出教室，完全沒有計畫", "雲朵按部就班地被風吹散，毫無步驟可言", "她按部就班地忘記帶雨傘"], "A", "『按部就班』指依照一定步驟與次序進行，第一句有清楚流程。", "easy", "流程語境"),
    ("下列句子中的「差強人意」使用最恰當的是：", ["這次簡報雖不完美，但整體表現尚可，還算差強人意", "他考了滿分，成績差強人意到令人驚嘆", "暴雨造成嚴重災情，景色差強人意地壯觀", "她完全沒有準備，卻差強人意地一定成功"], "A", "『差強人意』指大致尚可、還能使人滿意，第一句語意正確。", "hard", "成語語氣"),
    ("下列句子中的「鞠躬盡瘁」使用最恰當的是：", ["那位護理師多年投入偏鄉服務，為照顧居民鞠躬盡瘁", "他鞠躬盡瘁地把雨傘借給自己", "小鳥鞠躬盡瘁地停在電線上休息", "這支鉛筆鞠躬盡瘁地放進筆袋"], "A", "『鞠躬盡瘁』形容竭盡心力、奉獻至最後，第一句符合人物投入。", "medium", "人物品格語境"),
    ("下列句子中的「斟酌」使用最恰當的是：", ["他反覆斟酌用字，才完成這封重要的邀請函", "弟弟斟酌地把球踢到操場另一端", "樹葉斟酌地在秋風吹拂下落下", "我們斟酌地把三盒彩筆搬進教室"], "A", "『斟酌』指反覆考慮、推敲，第一句用於用字選擇最恰當。", "easy", "詞語搭配"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-performance-4-iv-1-{i}.json"
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
            "sourceLocator": f"114年國中教育會考國文科試題本；研究詞語理解與語境使用能力方向（{locator}）；官方答案表：{ANSWER}；另以官方語文領域課綱核對 4-Ⅳ-1（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
