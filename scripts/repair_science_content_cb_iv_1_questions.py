import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "science"
LESSON = "lesson-science-content-cb-iv-1"
KG = "kg-science-content-cb-iv-1"
SOURCES = [
    {"url": "https://www.nhjh.tp.edu.tw/uploads/1675416611615Uti9exJs.pdf", "title": "臺北市立內湖國中111學年度第一學期第三次段考八年級理化科", "year": "111"},
    {"url": "https://jdjh.kl.edu.tw/books/file/13/109%E4%B8%8A%E5%85%AB%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6%E7%A7%91%E8%A3%9C%E8%80%83%E9%A1%8C%E5%BA%AB.pdf", "title": "基隆市立建德國民中學109學年度第一學期八年級自然科補考題庫", "year": "109"},
    {"url": "https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E5%85%AB%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "title": "國立中科實驗高級中學第三冊補行評量題庫國中自然科學", "year": "115"},
]


def refs():
    return [{**s, "subject": "science", "locator": "原子、分子、元素、化合物、化學式係數／下標、粒子模型與原子守恆", "observedPattern": "公開學校理化資料常用 O、O2、H2O、CO2 與粒子圖判讀原子數、分子數、元素／化合物及反應前後守恆；本題只採能力方向與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-science-content-cb-iv-1-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公開學校理化科資料僅供原子／分子模型、元素化合物分類、化學式與原子守恆的能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開學校理化科資料的能力方向獨立改寫；題幹、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "下列何者是由同一種原子組成的分子？", {"A": "O₂", "B": "H₂O", "C": "CO₂", "D": "NaCl 化合物單位"}, "A", "O₂ 由兩個氧原子組成，雖是分子但只含一種元素；H₂O 和 CO₂ 含不同元素，選 A。", "先數一個粒子中出現的元素種類，再判斷元素或化合物。", ["讀取每個化學式中的元素符號。", "O₂ 只有 O 一種符號。", "下標 2 表示一個氧分子含兩個氧原子。", "只有一種元素仍可形成分子。", "所以選 A。"], "easy"),
    make(2, "化學式 3H₂O 表示什麼？", {"A": "3 個水分子，共含 6 個氫原子和 3 個氧原子", "B": "1 個水分子含 3 個氫原子和 2 個氧原子", "C": "3 個氫原子與 2 個氧原子混合", "D": "3 個氧分子和 2 個氫分子"}, "A", "前面的係數 3 表示三個 H₂O 分子；每個分子有 2 H 和 1 O，因此總數為 6 H、3 O，選 A。", "先處理係數代表幾個粒子，再乘上下標代表單一粒子的原子數。", ["辨認係數 3 作用於整個 H₂O。", "一個 H₂O 含 2 個氫原子和 1 個氧原子。", "三個分子共含 3×2 個氫。", "氧原子總數為 3×1。", "所以選 A。"], "medium"),
    make(3, "下列哪項最能區分原子與分子？", {"A": "原子可視為單一粒子單位，分子由兩個以上原子組成並保持物質特性", "B": "原子一定比分子重", "C": "分子一定只含一種元素", "D": "原子只能存在於金屬中"}, "A", "分子由原子以一定方式結合而成，可是同種原子如 O₂，也可是不同種原子如 H₂O；A 的區分最合理，選 A。", "用組成粒子數和元素種類，而不是重量或外觀判斷。", ["原子是元素的基本粒子單位。", "兩個以上原子結合可形成分子。", "分子可由同種或不同種原子組成。", "因此重量和金屬與否都不是定義。", "所以選 A。"], "easy"),
    make(4, "CO₂ 是化合物而 O₂ 是元素分子，主要差異是？", {"A": "CO₂ 含兩種元素固定結合，O₂ 只含一種元素", "B": "CO₂ 是混合物，O₂ 才是化合物", "C": "O₂ 含兩種元素而 CO₂ 只含一種", "D": "兩者都只由單一原子組成"}, "A", "CO₂ 含碳與氧兩種元素且以固定比例結合，是化合物；O₂ 只含氧元素，選 A。", "先數元素符號種類，再區分同種元素分子和不同元素固定組成。", ["讀取 CO₂ 中的 C 和 O。", "兩種元素以固定比例形成一種物質。", "讀取 O₂ 只有 O 一種元素。", "所以 O₂ 是元素形成的分子。", "因此選 A。"], "easy"),
    make(5, "化學式 2O₃ 中的數字 2 與右下角 3 分別表示什麼？", {"A": "2 表示兩個臭氧分子，3 表示每個分子有三個氧原子", "B": "2 表示每個分子有兩個原子，3 表示三個分子", "C": "兩個數字都表示分子數", "D": "兩個數字都表示元素種類"}, "A", "前係數表示粒子個數；下標表示一個粒子內該元素的原子個數，選 A。", "先區分式子前方和元素符號右下方兩種位置的功能。", ["找到化學式前的係數 2。", "它作用於整個 O₃，表示兩個分子。", "每個 O₃ 的 O 下標為 3。", "總氧原子數若需要計算為 2×3。", "所以選 A。"], "medium"),
    make(6, "若化學反應前有 2 個 H₂ 分子和 1 個 O₂ 分子，反應後原子重新排列，總共有多少個氫原子？", {"A": "4 個", "B": "2 個", "C": "1 個", "D": "8 個"}, "A", "每個 H₂ 有 2 個氫原子，2 個分子共有 2×2＝4 個；反應只重新排列原子，選 A。", "只追蹤題目指定元素，將係數乘上下標，不必先猜產物。", ["找出氫分子數為 2。", "每個 H₂ 含 2 個氫原子。", "氫原子總數為 2×2。", "化學反應不會憑空產生或消滅氫原子。", "所以選 A。"], "medium"),
    make(7, "下列哪個粒子表示法最容易造成『把係數當下標』的錯誤？", {"A": "2H₂：應分辨兩個分子與每分子兩個氫原子", "B": "He：只有一個元素符號", "C": "C：一個碳原子符號", "D": "O₂：兩個氧原子組成一個分子"}, "A", "2H₂ 同時有前係數和右下標，最需要分清粒子數與單一粒子的原子數，選 A。", "先找兩個數字分別位於哪裡，再說明各自作用範圍。", ["前方 2 代表兩個 H₂ 粒子。", "右下 2 代表每個粒子含兩個氫原子。", "總氫原子數需相乘為 4。", "不能把前方 2 當成一個分子內的下標。", "所以選 A。"], "hard"),
    make(8, "粒子模型中用不同顏色表示不同原子。若一個粒子含一黑兩白三個球，且每個粒子都相同，最合理的判斷是？", {"A": "它是由兩種元素固定比例組成的化合物分子", "B": "它一定是兩種物質隨意混合", "C": "它只代表一種元素的原子", "D": "顏色直接代表實際原子的外觀"}, "A", "不同顏色代表不同元素模型，而每個粒子都有固定的一黑兩白，表示不同元素以固定比例結合，選 A。", "先看單一粒子是否固定組合，再區分化合物和混合物。", ["顏色只當作模型符號，不當作真實外觀。", "粒子含兩種顏色，表示兩種元素。", "每個粒子的組成比例相同。", "固定結合的不同元素可表示化合物。", "所以選 A。"], "medium"),
    make(9, "化學反應式左右兩側的原子種類和數目應符合哪項原則？", {"A": "原子守恆：反應前後各元素原子數相同，只改變排列方式", "B": "反應後原子種類必定增加", "C": "係數可以任意改變原子總數", "D": "只有氧原子需要守恆"}, "A", "化學反應是原子重新排列，反應前後每種元素的原子數必須相同，選 A。", "逐元素計數並比較兩側，而不是只看分子數是否相等。", ["列出反應前各元素原子數。", "列出反應後各元素原子數。", "調整係數只能改變粒子數，不可改變元素種類。", "確認每一種元素左右總數相等。", "所以原則選 A。"], "easy"),
    make(10, "2H₂、H₂、2H 和 H₂O 四種表示中，哪項比較正確？", {"A": "2H₂ 是兩個氫分子；2H 是兩個氫原子；H₂O 是一個水分子", "B": "2H₂ 是兩個氫原子；2H 是兩個氫分子", "C": "H₂ 和 H₂O 都只含氫元素", "D": "2H 與 H₂ 都表示兩個氫分子"}, "A", "H₂ 是一個雙原子氫分子，前係數 2 表示兩個；2H 則是兩個獨立氫原子；H₂O 是一個水分子，選 A。", "先看是否有下標形成分子，再看前係數是幾個粒子。", ["H₂ 的下標 2 表示一個分子含兩個氫原子。", "前方 2 使粒子數變成兩個分子。", "2H 沒有下標，表示兩個氫原子。", "H₂O 含氫和氧，是一個水分子表示。", "所以選 A。"], "hard"),
]

for index, target in {2: "B", 4: "C", 6: "D", 8: "B", 10: "C"}.items():
    q = Q[index - 1]
    old = {o["id"]: o["text"] for o in q["options"]}
    old["A"], old[target] = old[target], old["A"]
    q["options"] = [{"id": k, "text": old[k]} for k in ("A", "B", "C", "D")]
    q["answer"]["value"] = target
    q["answer"]["explanation"] = q["answer"]["explanation"].replace("選 A", f"選 {target}")
    q["solutionStrategy"] = q["solutionStrategy"].replace("選 A", f"選 {target}")
    q["solutionSteps"] = [s.replace("選 A", f"選 {target}").replace("所以選 A", f"所以選 {target}") for s in q["solutionSteps"]]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")
