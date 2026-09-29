"""Correct A-8-2 lesson claims and align its teaching/interactive model to the official scope."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "lessons/math/lesson-math-content-a-8-2.json"
data = json.loads(path.read_text(encoding="utf-8"))

data["authoringStandard"] = "full-lesson-v1"
data["content"] = {
    "summary": "讀懂一元多項式的結構：先辨認項與項數，再讀係數、常數項、一次項、二次項和最高次項，最後用升冪或降冪整理表示順序。",
    "sections": [
        {"heading": "先辨識式子的邊界", "body": "多項式不是看到 x 就任意湊成的式子。以一元 x 為例，各項的 x 指數必須是非負整數；因此 4x³−2x+5 是多項式，而 3/x 與 √x 不符合這個定義。係數可以是負數，也可以是 1；寫成 −x 時，係數是 −1。"},
        {"heading": "項數和次數是兩種資訊", "body": "式中的加減號幫你分辨各項，但負號屬於後面的項。4x⁵−3x²+2x−8 有四項，最高次數卻是五；項數回答『有幾項』，多項式次數回答『最高的項次是多少』。中間缺少 x⁴、x³ 項並不會把最高次改成四或三。"},
        {"heading": "係數與項的名稱", "body": "在 4x⁵−3x²+2x−8 中，4 是五次項的係數，−3 是二次項的係數，2 是一次項的係數，−8 是常數項。係數要連同正負號讀；一次項、二次項依 x 的指數命名；最高次項則是指數最大的非零項。常數項不含 x，其次數視為零。"},
        {"heading": "把同一個式子排整齊", "body": "排列不會改變多項式，只改變閱讀順序。將 4x⁵−3x²+2x−8 寫成升冪，可由常數項開始：−8+2x−3x²+4x⁵；降冪則由最高次項開始：4x⁵−3x²+2x−8。逐項核對符號和指數，可避免排序時漏項或把負係數改成正係數。"},
        {"heading": "引導練習：讀一張項目清單", "body": "請讀 7x⁴−5x²+x−6。先用加減號分成四項：7x⁴、−5x²、x、−6；再標出項數為四、最高次項為 7x⁴、最高次數為四、一次項為 x、二次項為 −5x²、常數項為 −6。x 前沒有寫數字，仍有係數 1。這題只要求辨認名稱與排列，不進行多項式四則運算。"},
        {"heading": "離開前做雙重核對", "body": "遇到新的多項式，依序問：每一項的符號是否保留？項數是否逐項計數？係數是否包含正負號？一次、二次與最高次項是否依指數判定？升降冪是否由低到高或由高到低？以 −2x³+5x−1 為例，三項、三次、最高次項 −2x³、一次項 5x、常數項 −1；它缺少二次項仍不影響以上判斷。"}
    ],
    "studyEntry": "把多項式想成一份有符號的項目清單：先保留每項的正負，再標記指數和係數；不要把『項目有幾列』誤當成『最高到幾次』。",
}
data["teaching"] = {
    "body": [
        {"id": "hook", "phase": "hook", "heading": "一串符號，先不要急著計算", "body": "校園闖關記分器以 x 代表每完成一關所累積的點數，顯示 −2x³+5x−1。畫面上有三種不同線索：加減號把式子分成幾項、x 上的指數標出項的次數、前面的有號數字是係數。先不計分、不化簡，只要替每一項貼上標籤，就能讀出這個式子描述的結構。今天的任務是學會這種閱讀，而不是提前做下一單元的多項式運算。"},
        {"id": "explain", "phase": "explain", "heading": "先切項，再讀每個標籤", "body": "讀式時從左到右切分，第一項的符號也要保留。以 4x⁵−3x²+2x−8 為例，四項依序是 4x⁵、−3x²、+2x、−8，所以項數是四。每項的係數分別為 4、−3、2、−8；最後一項雖然沒有 x，仍是常數項。含 x 的指數告訴你項的次數：4x⁵ 是五次項、−3x² 是二次項、2x 是一次項。整個多項式的次數取最高次項的次數，因此是五，不是四。"},
        {"id": "worked", "phase": "worked-example", "heading": "完整示範：用表格讀 4x⁵−3x²+2x−8", "body": "第一步，把式子保留符號地拆成四項；第二步逐項填表：4x⁵ 的係數 4、次數 5；−3x² 的係數 −3、次數 2；+2x 的係數 2、次數 1；−8 的係數 −8、常數項、次數 0。第三步從最大指數找出最高次項 4x⁵，故整式為五次。第四步排序：升冪是 −8+2x−3x²+4x⁵，降冪是 4x⁵−3x²+2x−8。注意式中缺少 x⁴、x³ 項，仍不改變最高次數。"},
        {"id": "guided", "phase": "guided-practice", "heading": "分類挑戰：找出每個欄位的證據", "body": "請讀 7x⁴−5x²+x−6，先自行完成四格：項數、最高次項、一次項、常數項。逐項核對後，答案是四項、7x⁴、x、−6；若題目問係數，則一次項 x 的係數為 1，不是沒有係數。再把原式改寫為升冪 −6+x−5x²+7x⁴。若你得出三項，回到每個加減號兩側檢查有沒有把 +x 漏掉；若把次數答成四項，請分清數項目與比較指數是兩種工作。"},
        {"id": "transfer", "phase": "transfer", "heading": "把讀式方法搬到新的式子", "body": "某電子看板以 n 表示輪次，記錄 3n⁶−4n³−n+9。請像校對清單一樣標記：共四項；最高次項是 3n⁶；−4n³ 是三次項；−n 是一次項且係數為 −1；9 是常數項。降冪已完成，升冪則為 9−n−4n³+3n⁶。這個轉換不需要計算 n 的值，也不需要把項相加；只要保持每一項的符號和指數完整，兩種排列就呈現同一個多項式。"},
        {"id": "reflect", "phase": "reflect", "heading": "最後檢查定義、名稱與順序", "body": "離開前用三個反問檢查自己的判讀。第一，若式子有四項，能否直接說它是四次？不能，必須查看最高的非零指數。第二，−x 的係數是什麼？是 −1，隱含的 1 不能漏掉，負號也不能丟。第三，升冪和降冪會改變式子的值嗎？不會，它們只改變項的書寫先後。現在試讀 −2x³+5x−1：三項、三次、最高次項 −2x³、一次項 5x、常數項 −1；沒有二次項並不妨礙辨認。"}
    ],
    "summary": [
        "項數是逐項計數；多項式次數是最高次項的指數，兩者不可混為一談。",
        "每項的係數包含符號；不含變數的常數項，其次數視為零。",
        "升冪與降冪只改變書寫順序，不改變多項式本身。"
    ],
    "exitCheck": [
        {"prompt": "在 6x⁴−2x²+x−5 中，項數、最高次項與整式次數各為何？", "expectedEvidence": "指出四項、最高次項 6x⁴、整式次數 4，並說明項數不等於次數。"},
        {"prompt": "−x³+4x−9 的一次項係數和常數項各為何？", "expectedEvidence": "一次項為 4x、係數 4；常數項 −9；負號留在 −x³ 這一項。"},
        {"prompt": "把 2x⁴−3x+1 改寫為升冪，並說明是否改變多項式。", "expectedEvidence": "寫成 1−3x+2x⁴，並指出只是排列改變、式子不變。"}
    ]
}

plan_outcomes = {
    "hanlin": "公開校方課程計畫可核實其採用翰林版、A-8-2列出的課程名詞及週次安排；這不是翰林課本正文或出版社教學法證據。出版社教材內容、例型與迷思研究尚待合法可讀章節。",
    "kanghsuan": "公開校方課程計畫可核實其採用康軒版及A-8-2課程名詞範圍；這不是康軒課本正文或出版社教學法證據。出版社教材內容、例型與迷思研究尚待合法可讀章節。",
    "nani": "北投國中公開課程計畫明示南一版及多項式相關課程目標；該文件為108學年度計畫，僅作歷史課程定位線索，不代表現行教材正文或出版社教學法。出版社教材內容仍待合法可讀章節。"
}
for item in data["publisherResearch"]:
    item["researchScope"] = ["teaching-sequence", "assessment-pattern"]
    item["outcome"] = plan_outcomes[item["publisher"]]
    item["copyrightBoundary"] = "僅引用公立學校公開課程計畫可直接核實的版本採用、課綱範圍、週次或評量線索；未取得出版社正文，不推論其例題、迷思或完整教學順序，也不複製教材內容。"
data.pop("versionResearch", None)
data.pop("fusionRecord", None)
data["studyHighlights"] = [
    "A-8-2 官方課綱只列一元多項式定義及相關名詞；四則運算屬 A-8-3，面積公式展開屬 A-8-1。",
    "項數、項的次數和整式次數分別回答不同問題；最高次數看最高的非零指數。",
    "係數要包含符號；常數項不含變數；升冪與降冪只是同一多項式的兩種排列。"
]
data["studyReferences"] = [
    "https://www.naer.edu.tw/upload/1/16/doc/815/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E6%95%B8%E5%AD%B8%E9%A0%98%E5%9F%9F.pdf",
    "https://www.yfms.tyc.edu.tw/uploads/1691566195851cFHgZ0kS.pdf",
    "https://www.msjh.tp.edu.tw/uploads/1722920307663FExPXxBD.pdf",
    "https://www.ptjh.tp.edu.tw/wp-content/uploads/doc/b001/4-%E4%BF%AE%E6%AD%A3%E4%B8%8A%E5%82%B3%E9%A1%9E_423501_%E5%8C%97%E6%8A%95%E5%9C%8B%E4%B8%AD_%E5%85%AB%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf",
    "https://www.junyiacademy.org/topics/n-m8a-c01-2",
    "https://www.junyiacademy.org/topics/k-m8a-c01-2",
    "https://www.junyiacademy.org/topics/h-m8a-c01-2"
]
data["provenance"]["authoringNote"] = "本課依官方課綱與 A-8-2 穩定知識節點獨立撰寫；公校課程計畫僅用於核對課程定位，均一頁面僅為第三方補充教學參考。南一、康軒、翰林出版社教材正文研究尚未完成，因此不宣稱三版本融合，lesson 與題目維持 draft。全篇例子、說明、互動提示均為原創，未重製教材或公開試題。"
data["interactive"].update({
    "goal": "操作項目標籤辨認多項式的項數、係數、常數項、各項次數與升降冪，不進行 A-8-3 四則運算。",
    "scenario": "你是闖關記分器的資料校對員。把每個有號項放進欄位，讀出項目數、係數、常數項與最高次，再切換升冪／降冪排列；標籤只反映結構，不替你合併或運算。",
    "variables": [{"symbol": "x", "meaning": "多項式中唯一的文字符號；指數決定項次，數值輸入不是本活動判斷項身分的依據。"}],
    "steps": [
        {"id": "step-1", "prompt": "把 4x⁵−3x²+2x−8 依符號切成完整的項，項數是多少？", "options": ["四項：4x⁵、−3x²、+2x、−8", "五項：4、x⁵、3x²、2x、8", "三項，因為只有三個 x"], "answer": "A", "feedback": "保留每項的正負；加減號切開項，但係數和變數不能拆散。"},
        {"id": "step-2", "prompt": "在 −x³+4x−9 中，−x³ 的係數、一次項係數和常數項依序是什麼？", "options": ["−1、4、−9", "1、4、9", "3、1、−9"], "answer": "A", "feedback": "−x³ 隱含係數 −1；一次項是 4x；常數項保留為 −9。"},
        {"id": "step-3", "prompt": "在 7x⁴−5x²+x−6 中，最高次項與整式次數為何？", "options": ["7x⁴，次數 4", "−5x²，次數 4", "四項，所以次數 4"], "answer": "A", "feedback": "最高次項由最大指數辨認；項數雖也為四，不能拿項數當作判斷理由。"},
        {"id": "step-4", "prompt": "把 2x⁴−3x+1 改寫成升冪排列，哪個正確？", "options": ["1−3x+2x⁴", "2x⁴−3x+1", "1+3x−2x⁴"], "answer": "A", "feedback": "升冪從常數、一次到四次排列；每一項的符號與係數都要原樣保留。"}
    ]
})
data["simulation"].update({"engine": "concept-explorer", "goal": data["interactive"]["goal"], "mission": data["interactive"]["scenario"]})
data["simulation"]["learningDesign"] = {
    "type": "representation-match",
    "objective": "以項卡、標籤表與排列切換，準確讀出一元多項式定義相關名詞；不提前進行 A-8-3 運算。",
    "predictionPrompt": "看到 4x⁵−3x²+2x−8，先預測有幾項、最高次是多少；項數與最高次是否必須相同？",
    "evidencePrompt": "提交每項的有號係數、次數、常數標記，再展示升冪和降冪排列；以式中具體項目說明判斷。",
    "steps": [
        {"id": "step-1", "action": "逐個標出加減號分隔的完整代數項。", "equation": "4x⁵｜−3x²｜+2x｜−8", "reason": "係數、變數和指數構成一項，符號不可遺失。", "feedback": "數出分隔後的四項；不要把係數或 x 拆成獨立項。"},
        {"id": "step-2", "action": "讀係數並定位常數項。", "equation": "係數：4、−3、2、−8；常數項：−8", "reason": "係數包含正負號；不含 x 的項是常數項。", "feedback": "若把 −3 讀成 3，回到原式確認負號屬於該項。"},
        {"id": "step-3", "action": "比較指數並命名一次項、二次項與最高次項。", "equation": "最高次項 4x⁵；二次項 −3x²；一次項 2x", "reason": "項次由 x 的指數決定，整式次數是最高項次，不是項數。", "feedback": "式子雖有四項，最高指數為五，所以是五次多項式。"},
        {"id": "step-4", "action": "在不改變項與符號下切換升冪和降冪。", "equation": "升冪：−8+2x−3x²+4x⁵；降冪：4x⁵−3x²+2x−8", "reason": "重新排列只改變項目的書寫位置；只要每一項及其符號保持不變，呈現的仍是同一個多項式。", "feedback": "逐項對照兩列，確認同樣四項都出現、符號和指數沒有改變；排列方向則分別是由低到高與由高到低。"}
    ]
}
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {path.relative_to(ROOT)}; reviewStatus={data['reviewStatus']}; authoringStandard={data['authoringStandard']}")
