import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "science"
LESSON = "lesson-science-content-eb-iv-1"
KG = "kg-science-content-eb-iv-1"
SOURCES = [
    {"url": "https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "title": "國立中科實驗高級中學國中自然科補行評量題庫", "year": "2026", "locator": "合力、力矩、槓桿平衡與運動狀態題型"},
    {"url": "https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "title": "臺北市立內湖國中111學年度第一學期第二次段考九年級理化科試題", "year": "111", "locator": "槓桿力臂、合力矩與合力題組"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%835-OK.pdf", "title": "高雄市立國昌國中109學年度上學期三年級第三次段考自然科試題", "year": "109", "locator": "槓桿、簡單機械與力矩題型"},
]


def refs():
    return [{**s, "subject": "science", "observedPattern": "公立學校公開理化題常以推車、開門、槓桿、力臂與合力矩要求比較平移和轉動效果；本題只改寫能力與推理層次。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-science-content-eb-iv-1-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校公開自然／理化資料僅作合力、力矩、力臂與槓桿平衡的能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與公立學校公開試題能力方向獨立改寫，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-12", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
make(1, "小車受到向東 6 N 與向西 2 N 的水平力，合力為何？", {"A": "向東 4 N", "B": "向西 4 N", "C": "向東 8 N", "D": "0 N"}, "A", "反方向的力相減，6−2＝4 N，較大的向東力決定合力方向。", "先選方向，再把同一直線反向力相減，不只比較數字。", ["列出向東 6 N 與向西 2 N。", "確認方向相反所以相減。", "計算 6−2＝4 N。", "方向跟隨較大的向東力。", "因此選 A。"], "easy"),
make(2, "推門時，手放在遠離鉸鏈處通常較容易轉動，主要因為？", {"A": "同樣的力具有較大的垂直力臂，產生較大力矩", "B": "門把會讓手的力自動變大", "C": "鉸鏈附近沒有任何力", "D": "力矩只由門的質量決定"}, "A", "力矩＝力×垂直力臂；施力大小相同時，遠離鉸鏈使力臂變大，轉動效果較大。", "找出轉軸，再判斷作用線到轉軸的垂直距離。", ["確定門的鉸鏈是轉軸。", "比較兩個施力位置到作用線的垂直距離。", "確認遠處位置力臂較長。", "由力矩公式判斷轉動效果較大。", "所以答案是 A。"], "easy"),
make(3, "對轉軸施加一個作用線通過轉軸的力，力矩為何？", {"A": "最大", "B": "等於力的數值", "C": "0", "D": "一定使物體加速平移"}, "C", "力矩使用垂直力臂；作用線通過轉軸時力臂為零，因此力矩為零，即使力本身不為零。", "不要把施力大小直接當成力矩，先找垂直力臂。", ["找出力的作用線。", "確認作用線通過轉軸。", "判定垂直距離為零。", "代入力矩＝力×力臂。", "所以選 C。"], "medium"),
make(4, "一把扳手受到 20 N 的垂直力，力臂為 0.30 m，力矩大小是多少？", {"A": "6 N·m", "B": "20.3 N·m", "C": "60 N·m", "D": "0.015 N·m"}, "A", "力矩＝力×力臂＝20 N×0.30 m＝6 N·m。", "先確認力與力臂互相垂直，再代入公式和單位。", ["寫出 τ＝F×r。", "代入 F＝20 N、r＝0.30 m。", "計算 20×0.30＝6。", "保留 N·m 單位。", "故選 A。"], "medium"),
make(5, "翹翹板左側 300 N 的力作用於 2 m 處，右側要在 3 m 處平衡，需要多大的力？", {"A": "100 N", "B": "200 N", "C": "450 N", "D": "900 N"}, "B", "平衡時兩側力矩相等：300×2＝F×3，所以 F＝200 N。", "以支點為中心列出順、逆時針力矩相等的方程式。", ["寫左側力矩 300×2＝600 N·m。", "設右側力為 F，右側力矩為 3F。", "令 3F＝600。", "解得 F＝200 N。", "因此選 B。"], "medium"),
make(6, "物體受到合力為零，但兩個力矩方向不相等，可能發生什麼？", {"A": "一定完全不動", "B": "可能平移加速但不轉動", "C": "可能合力矩不為零而轉動", "D": "質量必然變成零"}, "C", "合力為零只表示平移方向的推拉抵消；若合力矩不為零，仍可能產生角加速度而轉動。", "把平移平衡和轉動平衡分成兩個獨立檢查項目。", ["先檢查所有力的向量和。", "確認合力為零只處理平移。", "再計算順、逆時針力矩總和。", "若不相等，判斷有轉動趨勢。", "所以答案是 C。"], "hard"),
make(7, "書本放在水平桌面上靜止，不能因此說書本『沒有受到力』，因為？", {"A": "重力與桌面支持力大小相等、方向相反，合力為零", "B": "靜止物體不可能受重力", "C": "桌面把重力消除了", "D": "書本沒有質量"}, "A", "書本仍受向下重力與向上支持力；兩力平衡使合力為零，不代表力不存在。", "列出物體受力圖，再判斷合力是否為零。", ["找出書本的重力。", "找出桌面提供的支持力。", "比較兩力大小與方向。", "確認合力為零造成靜止。", "因此選 A。"], "easy"),
make(8, "若把同樣大小的力改成斜向施在門上，判斷轉動效果時最重要的量是？", {"A": "力到轉軸的垂直力臂與力的方向", "B": "只看力的數值，不看方向", "C": "只看門的顏色", "D": "只看施力點到轉軸的斜線距離"}, "A", "斜向施力的力矩由力與作用線到轉軸的垂直距離決定，不能以任意斜線距離代替力臂。", "畫出作用線，再量轉軸到作用線的垂直距離。", ["畫出斜向力的作用線。", "找出門的轉軸。", "作轉軸到作用線的垂線。", "用力和垂直力臂判斷力矩。", "所以選 A。"], "hard"),
make(9, "兩人以相反方向推同一箱子，東向 50 N、西向 50 N，箱子原本靜止。合理結論是？", {"A": "合力為零，若無其他不平衡效果，平移加速度為零", "B": "箱子一定向東加速 100 N", "C": "箱子一定向西加速 50 N", "D": "相反力會互相消失成沒有任何力"}, "A", "兩力大小相等方向相反，合力為零；仍然存在兩個力，只是平移效果互相抵消。", "分清『合力為零』和『沒有力』，再判斷運動狀態。", ["列出東西兩個力。", "計算向量和 50−50＝0。", "確認沒有平移加速度的合力來源。", "保留兩個力仍實際存在的描述。", "因此答案是 A。"], "medium"),
make(10, "要讓槓桿靜力平衡，最完整的條件是？", {"A": "只要順時針力矩等於逆時針力矩", "B": "合力為零且合力矩為零", "C": "只要物體看起來不動，不必計算", "D": "只要兩端力大小相等，不必看位置"}, "B", "完整靜力平衡要同時滿足平移的合力為零和轉動的合力矩為零；只看力大小或外觀都不足。", "把平移與轉動兩個自由度分別列出平衡條件。", ["先檢查所有外力的向量和。", "再以同一支點計算順、逆時針力矩。", "確認兩個總和都為零。", "排除只看力大小或只看外觀。", "所以選 B。"], "hard"),
]

for index, target in {2: "B", 4: "C", 6: "D", 8: "B", 10: "C"}.items():
    q = Q[index - 1]
    m = {o["id"]: o["text"] for o in q["options"]}
    m["A"], m[target] = m[target], m["A"]
    q["options"] = [{"id": k, "text": m[k]} for k in ("A", "B", "C", "D")]
    q["answer"]["value"] = target
    q["solutionSteps"] = [s.replace("選 A", f"選 {target}").replace("為 A", f"為 {target}") for s in q["solutionSteps"]]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")
