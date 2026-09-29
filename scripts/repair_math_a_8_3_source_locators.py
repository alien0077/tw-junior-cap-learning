import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW_DADAO113 = {
    "url": "https://school.tc.edu.tw/open-message/064519/get-file/65c1df1090ff2c381053ac91",
    "title": "臺中市立大道國中數學科八年級補行評量題庫（原卷未載學年度）",
    "year": "unknown",
}
DAJIA = {
    "url": "https://school.tc.edu.tw/open-message/064510/get-file/5e49ebb9a2bac601505f73d8",
    "title": "大甲國中二年級數學補考題庫（原卷未載學年度）",
    "year": "unknown",
}

# 每題依原卷逐題定位；不以一筆來源涵蓋多道考題，也不把考點寫成整卷泛稱。
locators = {
    1: ["PDF 第2頁計算題1(甲)：括號分配後整理多項式", "選擇題第9題：兩多項式相加並依係數條件求值", "選擇題第28題：兩多項式相加並合併同類項", "選擇題第12題：兩多項式相加後整理各次項"],
    2: ["PDF 第2頁計算題1(甲)：括號分配後整理多項式", "選擇題第10題：外層減號作用於巢狀多項式括號", "選擇題第18題：含正負係數的多項式連續加減整理", "選擇題第11題：巢狀括號展開並整理同類項"],
    3: ["PDF 第2頁計算題1(甲)：係數分配至括號內各項", "選擇題第7題：以乘法公式化簡兩個一次式的乘積", "選擇題第4題：展開兩個一次式的乘積", "選擇題第11題：括號內負號分配與多項式整理"],
    4: ["PDF 第2頁計算題1(甲)：係數分配至括號內各項", "選擇題第7題：以乘法公式化簡兩個一次式的乘積", "選擇題第4題：展開兩個一次式的乘積", "選擇題第11題：括號內負號分配與多項式整理"],
    5: ["PDF 第2頁計算題1(甲)：分配律展開並整理多項式", "選擇題第7題：一次式乘積展開後利用差平方關係", "選擇題第4題：直接展開兩個一次式乘積", "選擇題第16題：以長方形尺寸相乘建立二次式面積模型"],
    6: ["選擇題第12題：多項式除以另一多項式並給定商、餘式", "選擇題第29題：多項式除以單項式並判斷餘式", "選擇題第15題：由除法等式與商、餘式反求多項式"],
    7: ["PDF 第2頁計算題1(甲)：多項式分配、加減及同類項整理", "選擇題第9題：兩多項式相加後依係數條件求值", "選擇題第28題：兩多項式相加並合併同類項", "選擇題第12題：兩多項式相加後整理各次項"],
    8: ["PDF 第2頁計算題1(甲)：多層括號分配及多項式加減", "選擇題第10題：外層減號作用於巢狀多項式括號", "選擇題第28題：合併同類項整理多項式加法", "選擇題第11題：巢狀括號展開並整理同類項"],
    9: ["PDF 第2頁計算題1(甲)：括號分配與多項式整理", "選擇題第9題：兩多項式相加並依係數條件求值", "選擇題第28題：兩多項式相加並合併同類項", "選擇題第16題：長方形尺寸代數化後以乘法式表示面積"],
    10: ["選擇題第7題：代入指定 x 值求兩一次式乘積", "選擇題第10題：多項式化為 ax²+bx+c 後求 a+b+c（等同代入 x=1）", "選擇題第23題：利用已知 x²+3x 關係代入化簡多項式值"],
}

for number, item_locators in locators.items():
    path = ROOT / "questions" / "math" / f"question-math-content-a-8-3-{number}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    refs = data["examPatternRefs"]
    if number in (3, 4, 5):
        refs[1].update(NEW_DADAO113)
        refs[1]["subject"] = "math"
        refs[1]["reuseDecision"] = "pattern-only"
        refs[1]["status"] = "recorded"
        refs[1]["locatorLevel"] = "item"
    if number == 10:
        refs[0].update(NEW_DADAO113)
        refs[0]["subject"] = "math"
        refs[0]["reuseDecision"] = "pattern-only"
        refs[0]["status"] = "recorded"
        refs[0]["locatorLevel"] = "item"
        refs = [ref for ref in refs if "大道國民中學 114" not in ref.get("title", "")]
        data["examPatternRefs"] = refs
    if number == 2:
        refs[2].update(DAJIA)
        refs[2]["subject"] = "math"
        refs[2]["reuseDecision"] = "pattern-only"
        refs[2]["status"] = "recorded"
        refs[2]["locatorLevel"] = "item"
    if number == 6:
        refs = [ref for ref in refs if "至善國民中學 112" not in ref.get("title", "")]
        data["examPatternRefs"] = refs
    for ref, locator in zip(refs, item_locators):
        ref["locator"] = locator
        ref["locatorLevel"] = "item"
        skill = locator.split("：", 1)[-1]
        ref["observedPattern"] = f"pattern-only：僅參考原卷單題的「{skill}」能力；未沿用來源算式、數值、情境或選項。"
    if len(refs) < 3:
        raise ValueError(f"{path.name}: fewer than three public-exam references")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print("Replaced broad A-8-3 locators with item-level references for questions 1-10.")
