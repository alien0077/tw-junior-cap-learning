import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-9-9"
KG = "kg-math-content-s-9-9"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "內角平分線、內心三邊等距、內切圓、面積與半周長及角平分線定理", "observedPattern": "公立學校公開數學試題常以角平分線交點、到三邊等距、內切圓半徑與面積關係，以及角平分線分邊比例考查內心推理；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-9-9-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供三角形內心能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的內心能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "三角形的內心是哪些線的交點？", {"A": "三邊垂直平分線", "B": "三個內角的角平分線", "C": "三條中線", "D": "三條高"}, "B", "三角形內心是三個內角角平分線的交點，選 B。", "先辨認內心的定義，再與外心、重心和垂心的線型區分。", ["回想內心的幾何定義。", "每個內角都有一條角平分線。", "三條內角平分線會共點。", "該交點就是內心。", "選 B。"], "easy"),
    make(2, "若 I 是三角形 ABC 的內心，則 I 到三邊 AB、BC、CA 的距離有何關係？", {"A": "三者相等", "B": "依邊長成比例", "C": "只有到 AB、AC 相等", "D": "無法比較"}, "A", "內心在三個內角的角平分線上，到每一對鄰邊距離相等，因此到三邊的距離全相等，選 A。", "把角平分線的等距性質套用到三個內角，逐步連結到三邊。", ["確認 I 在 A 角平分線上。", "得到 I 到 AB、AC 距離相等。", "同理使用 B、C 角平分線。", "三個距離都等於內切圓半徑。", "選 A。"], "easy"),
    make(3, "三角形內切圓半徑為 4 公分，半周長為 15 公分，三角形面積是多少？", {"A": "19 平方公分", "B": "30 平方公分", "C": "60 平方公分", "D": "120 平方公分"}, "C", "三角形面積＝內切圓半徑×半周長＝4×15＝60 平方公分，所以選 C。", "看到內切圓半徑與半周長時，使用面積 K＝rs，而不是圓面積公式。", ["記下內切圓半徑 r＝4。", "記下半周長 s＝15。", "寫出三角形面積 K＝rs。", "計算 K＝4×15＝60 平方公分。", "選 C。"], "medium"),
    make(4, "正三角形的內心與外心有何關係？", {"A": "兩者是同一點", "B": "內心在外心外部", "C": "外心必在某個頂點", "D": "兩者距離等於邊長"}, "A", "正三角形的對稱性使角平分線與垂直平分線交於同一點，因此內心與外心重合，選 A。", "利用正三角形的對稱線同時具有多種幾何意義。", ["確認三角形三邊等長。", "正三角形的中線同時是角平分線。", "同一條線也通過邊的中點並垂直邊。", "內心與外心都落在相同交點。", "選 A。"], "easy"),
    make(5, "直角三角形兩股長 6、8 公分，斜邊長 10 公分，其內切圓半徑為多少？", {"A": "1 公分", "B": "2 公分", "C": "3 公分", "D": "4 公分"}, "B", "直角三角形內切圓半徑 r＝(兩股和－斜邊)/2＝(6＋8－10)/2＝2 公分，選 B。", "先辨認直角三角形，再用兩股、斜邊的快速半徑公式並檢查正值。", ["列出兩股和 6＋8＝14。", "扣除斜邊 10 得 4。", "將結果除以 2。", "得到內切圓半徑 2 公分。", "選 B。"], "medium"),
    make(6, "在 △ABC 中，A 角的角平分線交 BC 於 D。若 AB＝6、AC＝9，則 BD：DC 為何？", {"A": "2：3", "B": "3：2", "C": "1：3", "D": "6：15"}, "A", "角平分線定理給 BD：DC＝AB：AC＝6：9＝2：3，選 A。", "先確認角平分線從 A 出發，再把鄰近兩邊的比例對應到 BC 的兩段。", ["確認 AD 平分 ∠A。", "套用 BD：DC＝AB：AC。", "代入得到 6：9。", "約分為 2：3。", "選 A。"], "medium"),
    make(7, "若一點 I 到三角形三邊的距離都相等，且 I 位於三角形內部，I 最可能是哪個中心？", {"A": "外心", "B": "重心", "C": "內心", "D": "垂心"}, "C", "到三邊距離相等且位於三角形內部的點是內心，選 C。", "用『到三邊等距』這個辨識線索，不要以位置單獨猜中心名稱。", ["讀出 I 到三邊等距。", "把等距條件連結到角平分線。", "三個角平分線的交點是內心。", "內心位於三角形內部。", "選 C。"], "easy"),
    make(8, "相對於外心的位置，三角形內心有哪個必然性？", {"A": "內心必在三角形內部", "B": "內心必在三角形外部", "C": "內心必在最長邊上", "D": "內心必與外心重合"}, "A", "三角形三個內角的角平分線在三角形內部相交，因此內心必在三角形內部，選 A。", "區分外心可在內、外或邊界，但內心的角平分線交點固定在內部。", ["確認內心由三條內角平分線構成。", "每條內角平分線都位於相應角的內部。", "三線交點仍在三角形內部。", "此性質不要求三角形是哪種角型。", "選 A。"], "medium"),
    make(9, "內切圓與三角形的邊 AB 相切於 T。下列哪項必成立？", {"A": "IT 垂直 AB", "B": "IT 平行 AB", "C": "AT＝AB", "D": "T 是三角形頂點"}, "A", "I 是內心也是內切圓圓心，半徑 IT 會垂直切線 AB，選 A。", "把內心視為內切圓圓心，套用圓心到切點半徑垂直切線。", ["確認 I 是內切圓圓心。", "T 是圓與 AB 的接觸點。", "連接圓心 I 與接觸點 T。", "半徑 IT 垂直切線 AB。", "選 A。"], "medium"),
    make(10, "三角形三邊長為 5、5、6 公分，內切圓半徑為 2 公分。若半周長為 8 公分，三角形面積為多少？", {"A": "8 平方公分", "B": "12 平方公分", "C": "16 平方公分", "D": "20 平方公分"}, "C", "三角形面積 K＝rs＝2×8＝16 平方公分，選 C；邊長資料也符合半周長 8。", "先抓內切圓的 r、半周長 s，再以 K＝rs 求面積並核對資料。", ["確認內切圓半徑 r＝2。", "確認半周長 s＝8。", "套用 K＝rs。", "計算 K＝2×8＝16 平方公分。", "選 C。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")
