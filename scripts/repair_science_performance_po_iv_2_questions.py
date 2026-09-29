import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/science"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "探究問題、變因辨識與實驗設計能力方向"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "觀察紀錄、可行問題與證據推理能力方向"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "資料判讀、問題形成與結論界線能力方向"),
]

DATA = [
    ("question type", "下列哪一項最適合改寫成可由校園資料回答的科學問題？", ["午休時操場與圖書館外的分貝是否不同？", "校園噪音是不是很糟？", "哪種聲音最有意義？", "學校應不應該禁止所有聲音？"], "A", "A 指定時間、地點、可測量結果與比較對象；B 含有未定義的價值判斷，C 是偏好，D 是政策與價值問題，不能直接以一次科學測量決定。"),
    ("scope", "把『植物需要多少水』縮小為哪個問題最能在一週內安全觀察？", ["相同光照下，同品種幼苗每天澆 10 mL 或 30 mL，七天後葉片數是否不同？", "水對世界上所有植物的全部影響是什麼？", "哪種植物最值得人類喜歡？", "植物為什麼存在？"], "A", "A 指定植物、光照、水量、時間與葉片數，能形成可行比較；其餘問題過大、屬偏好或缺少可操作邊界。"),
    ("moon", "若想保留『月亮每天看起來不同』的好奇，哪個改寫最適合先做觀察？", ["連續兩週每天晚上八點記錄月亮亮面比例與位置", "用一次照片解釋月亮形成的全部原因", "投票決定哪個月相最美", "直接宣布月亮變化一定是雲造成的"], "A", "A 固定時間並記錄可觀察現象，能產生連續資料；B 範圍過大，C 是偏好，D 是未經檢驗的結論。"),
    ("variables", "研究不同澆水量對盆栽葉片數的影響時，哪組條件最適合固定？", ["植物品種、盆土量、光照位置與觀察時間", "澆水量與葉片數", "研究者預期的答案", "只固定最後一天的照片角度"], "A", "A 固定可能影響結果的條件，讓澆水量成為主要比較因素；澆水量是自變因，葉片數是應變因，預期答案不能當控制條件。"),
    ("feasibility", "班上沒有分貝計，仍想研究校園噪音，哪個方案最負責任？", ["改用可取得的公開測站資料或設計一致的相對聲音觀察，並說明限制", "把猜測的分貝數填入表格", "借用危險器材自行拆裝", "因為沒有器材就宣稱問題沒有答案"], "A", "A 保留問題並誠實交代測量限制；B 捏造資料，C 忽略安全，D 把目前不可直接測量誤當成永遠不能研究。"),
    ("value", "下列對『哪個月相最美？』的判斷最恰當的是？", ["可調查不同人的偏好，但不能只靠自然科實驗決定唯一答案", "只要測量亮面比例就能決定所有人的美感", "因為是主觀題，所以不能蒐集任何資料", "直接選亮面最大的月相作為科學答案"], "A", "A 區分偏好與事實；偏好可以透過問卷描述分布，但亮面比例不會單獨決定美感，也不能因主觀就拒絕研究觀點。"),
    ("question review", "同儕審查一個探究問題時，哪項檢核最完整？", ["確認對象、結果、範圍、比較條件、資料來源與安全風險", "只看題目聽起來是否有趣", "只確認答案是否符合老師預期", "先做實驗再補寫問題"], "A", "A 同時檢查可觀察性、可行性、方法對齊與安全；有趣或符合預期不能代替問題品質，問題也不應在資料後才倒填。"),
    ("data method", "若問題是『兩個地點哪裡較吵』，哪個方法與問題最對齊？", ["在相同時段於兩地重複記錄聲音測量值並保留天氣與活動紀錄", "只在最吵的一地測一次", "詢問一位同學的印象後下結論", "先選好地點再刪除不符合的紀錄"], "A", "A 讓比較地點成為主要差異，並用重複資料和背景紀錄檢查結果；其餘做法不是單一樣本、印象判斷，就是選擇性刪資料。"),
    ("ethical boundary", "問題涉及夜間觀察校園昆蟲時，哪項修正最合適？", ["改成白天或獲得同意後在安全範圍觀察，不捕捉或傷害生物並記錄限制", "為了樣本數私自進入封閉區域", "把昆蟲帶回家直到得到想要的結果", "刪除安全要求以免影響實驗"], "A", "A 把安全、同意和生物倫理納入問題設計；其他選項可能造成危險、未經授權或傷害生物，不能以探究為理由忽略。"),
    ("transfer", "哪一項最能把『教室通風好不好』改成可檢查的問題？", ["開窗與關窗條件下，在相同時間記錄教室溫度與二氧化碳濃度是否不同？", "通風好的教室是不是比較幸福？", "為什麼所有教室都不能永遠開窗？", "我覺得有風就代表通風一定好。"], "A", "A 將通風概念轉為可記錄指標並指定比較條件；B、C 混入價值或過大原因問題，D 是個人感受和過度推論。"),
]

def make(index, row):
    topic, prompt, choices, answer, explanation = row
    refs = [{
        "url": url, "title": f"{title}；僅取能力方向，未複製原題、選項、圖表或答案。",
        "year": "113-114", "subject": "science", "locator": locator,
        "observedPattern": "公開自然科評量常以現象、變因、資料、方法與證據界線要求學生形成或判讀探究問題；本題以原創情境改寫。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"
    } for url, title, locator in SOURCES]
    steps = [
        f"讀題定位：圈出本題要求的問題類型或設計條件，核心是「{topic}」。",
        "把情境拆成研究對象、可觀察結果、時間範圍、比較條件、資源與安全限制。",
        f"逐項比對是否能取得可核對資料；本題正確答案是 {answer}。",
        f"核對理由：{explanation}",
        "最後回查結論是否只超出樣本、時間或方法所能支持的範圍；若不可行，先縮小問題或改用觀察、模型與公開資料。",
    ]
    return {
        "id": f"question-science-performance-po-iv-2-{index}", "subject": "science", "type": "single-choice", "prompt": prompt,
        "options": [{"id": chr(65+i), "text": text} for i, text in enumerate(choices)],
        "knowledgeIds": ["kg-science-performance-po-iv-2"], "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation + f" 正確答案：{answer}。"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
            "sourceLocator": "三個公立國中公開自然科評量；僅研究問題形成、探究設計與證據判讀能力方向，不重製原題、選項、圖表或答案。",
            "authoringNote": "依官方課綱 KG 與三個公立學校公開自然科評量來源的能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},
        "reviewStatus": "draft", "updatedAt": "2026-09-21", "lessonId": "lesson-science-performance-po-iv-2",
        "examPatternRefs": refs,
        "solutionStrategy": "先分辨問題是事實、價值、偏好或倫理，再檢查對象、結果、範圍、比較條件、資源、方法與安全，最後限制結論界線。",
        "solutionSteps": steps,
    }

for index, row in enumerate(DATA, 1):
    (OUT / f"question-science-performance-po-iv-2-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
