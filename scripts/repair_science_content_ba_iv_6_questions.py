import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "science"
LESSON = "lesson-science-content-ba-iv-6"
KG = "kg-science-content-ba-iv-6"
SOURCES = [
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E昌--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國民中學111學年度第二學期三年級自然科第一次段考", "year": "111"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf", "title": "高雄市立鹽埕國民中學114學年度第二學期三年級自然科第一次段考", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193520/get-file/682ad6fe388a7353717ca362", "title": "臺中市立安和國民中學113學年度第二學期三年級自然領域第二次學習評量", "year": "113"},
]


def refs():
    return [{**s, "subject": "science", "locator": "功率定義、功與時間、瓦特與焦耳、輸入／輸出功率、平均功率與資料判讀", "observedPattern": "公開自然科評量常以電器規格、馬達作功、暖器電量、同功不同時間與平均功率資料判斷每秒作功量；本題只取能力方向、資料型態與推理層次。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-science-content-ba-iv-6-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校公開自然科資料僅供功率、功與時間及電器規格推理方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開自然科資料的功率能力方向獨立改寫；題幹、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "機器在 10 s 內完成 300 J 的功，平均功率是多少？", {"A": "3 W", "B": "30 W", "C": "300 W", "D": "3000 W"}, "B", "平均功率 P＝W/t＝300 J÷10 s＝30 W，選 B。", "先辨認題目要功率，再用功除以時間並核對 W 的單位。", ["找出完成的功 W＝300 J。", "找出時間 t＝10 s。", "套用 P＝W/t。", "計算 300÷10＝30。", "功率單位是 W，所以選 B。"], "easy"),
    make(2, "某馬達的功率為 50 W，連續運轉 8 s，理想情況下完成的功約為多少？", {"A": "6.25 J", "B": "42 J", "C": "400 J", "D": "800 J"}, "C", "由 P＝W/t 得 W＝Pt＝50×8＝400 J，選 C。", "功率已知、時間已知時，把 P＝W/t 變形為 W＝Pt。", ["確認 P＝50 W。", "確認 t＝8 s。", "寫出 W＝Pt。", "計算 50×8＝400 J。", "所以選 C。"], "easy"),
    make(3, "裝置以 20 W 的功率完成 200 J 的功，需要多少時間？", {"A": "0.1 s", "B": "4 s", "C": "10 s", "D": "4000 s"}, "C", "t＝W/P＝200 J÷20 W＝10 s，選 C。", "先寫基本式，再依未知量整理，避免把功率與時間相乘。", ["列出 P＝W/t。", "移項得到 t＝W/P。", "代入 W＝200 J、P＝20 W。", "計算 200÷20＝10 s。", "所以選 C。"], "easy"),
    make(4, "1 W 的物理意義是什麼？", {"A": "每秒完成 1 J 的功", "B": "每分鐘完成 1 J 的功", "C": "每秒移動 1 m 的距離", "D": "每庫侖帶有 1 J 的電量"}, "A", "功率是單位時間完成的功，因此 1 W＝1 J/s，選 A。", "把單位 W 展開成 J/s，再用一句話解釋其物理意義。", ["回想功率定義 P＝W/t。", "令 P＝1 W。", "得到每 1 s 完成 1 J 的功。", "注意這不是速度或電量的定義。", "所以選 A。"], "easy"),
    make(5, "甲、乙都完成 600 J 的功；甲用 6 s，乙用 12 s。哪項比較正確？", {"A": "甲的平均功率是乙的 2 倍", "B": "乙的平均功率是甲的 2 倍", "C": "兩人的平均功率相同", "D": "無法比較，因為沒有給質量"}, "A", "P甲＝600÷6＝100 W，P乙＝600÷12＝50 W，所以甲是乙的 2 倍，選 A。", "同功比較功率時，時間較短者功率較大；必要時再計算確認。", ["確認兩人的功相同。", "甲功率＝600÷6＝100 W。", "乙功率＝600÷12＝50 W。", "比較 100÷50＝2。", "所以選 A。"], "medium"),
    make(6, "兩人質量相同，都從地面爬到相同高度；甲用 10 s、乙用 20 s。忽略損失，何者正確？", {"A": "兩人對自身增加的重力位能相同，但甲的平均功率較大", "B": "甲增加的重力位能是乙的 2 倍", "C": "乙的平均功率是甲的 2 倍", "D": "兩人都沒有作功，因為最後都靜止"}, "A", "增加的重力位能 mgh 相同，所作功相同；甲用時較短，所以 P甲＝W/10 大於 P乙＝W/20，選 A。", "先比較總功，再比較完成相同功所需的時間。", ["兩人質量 m 相同。", "上升高度 h 相同，故 mgh 相同。", "忽略損失時兩人所作的功相同。", "甲時間較短，單位時間完成的功較多。", "所以甲功率較大，選 A。"], "medium"),
    make(7, "馬達輸入功率 500 W，輸出有用機械功率 350 W，效率是多少？", {"A": "30%", "B": "50%", "C": "70%", "D": "850%"}, "C", "效率＝輸出有用功率／輸入功率×100%＝350÷500×100%＝70%，選 C。", "效率分子放有用輸出、分母放總輸入，最後乘 100%。", ["找出輸入功率 500 W。", "找出有用輸出功率 350 W。", "套用 η＝P輸出/P輸入×100%。", "計算 350÷500＝0.7。", "換成百分比為 70%，選 C。"], "medium"),
    make(8, "一臺電器標示功率 2 kW，換算成瓦特是多少？", {"A": "2 W", "B": "20 W", "C": "200 W", "D": "2000 W"}, "D", "1 kW＝1000 W，所以 2 kW＝2000 W，選 D。", "先處理單位前綴，再進行數值換算。", ["寫出 1 kW＝1000 W。", "把 2 kW 乘以 1000。", "得到 2000 W。", "確認不是把 k 當成 100。", "所以選 D。"], "easy"),
    make(9, "兩臺機器同時運轉相同時間，甲的功率比乙大。在其他條件不變下，哪個結果合理？", {"A": "甲完成的功較多，也消耗較多能量", "B": "乙完成的功較多，因為功率較小", "C": "兩臺完成的功一定相同", "D": "功率只影響速度，不影響完成的功"}, "A", "相同時間 t 下，W＝Pt；功率較大的甲完成的功較多，能量轉移量也較大，選 A。", "看到相同時間，直接用 W＝Pt 比較功與能量。", ["確認兩臺運轉時間相同。", "寫出 W＝Pt。", "時間相同時，完成的功與功率成正比。", "甲功率較大，所以甲完成的功較多。", "因此選 A。"], "medium"),
    make(10, "裝置先用 10 s 以 600 J 的功率完成工作，再用 20 s 以 400 J 的功完成另一段工作。整段過程的平均功率是多少？", {"A": "20 W", "B": "33.3 W", "C": "50 W", "D": "100 W"}, "B", "平均功率要用總功除以總時間：P平均＝(600＋400) J÷(10＋20) s＝1000÷30≈33.3 W，選 B。", "不可直接平均兩段功率；先求每段總功，再以總功／總時間計算。", ["第一段功為 600 J，第二段功為 400 J。", "總功＝600＋400＝1000 J。", "總時間＝10＋20＝30 s。", "P平均＝1000÷30≈33.3 W。", "所以選 B。"], "hard"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")
