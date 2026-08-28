"""把社會科「分析資料、如何區分資料／推論」元題型改成直接能力題。"""
import glob, hashlib, json, re
from pathlib import Path

SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83.pdf"

def rewrite(path):
    data = json.loads(Path(path).read_text())
    old = data.get("prompt", "")
    note = data.get("provenance", {}).get("authoringNote", "")
    authored = note.startswith("依單元 KG 概念與公開段考能力方向")
    legacy = note.startswith("以單元概念、全新情境、選項與解析獨立重寫")
    if not (old.startswith("分析「") or authored or legacy): return False
    lesson = json.loads((Path("lessons/social") / f"{data['lessonId']}.json").read_text())
    topic = lesson.get("title", "").split("：", 1)[-1]
    i = int(re.search(r"-(\d+)\.json$", path).group(1)) - 1
    seed = int(hashlib.sha256(topic.encode()).hexdigest()[:6], 16) % 30 + 1
    questions = [
        (f"某表記錄「{topic}」四個地區的數值：甲 12、乙 18、丙 9、丁 15。哪個判讀正確？", ["乙的數值最高", "丙的數值最高", "甲與丁相差 10", "四地數值完全相同"], "A"),
        (f"調查「{topic}」時，80 份有效問卷中有 48 份選擇方案甲。下列何者正確？", ["方案甲占 60%", "方案甲占 48%", "方案甲比其他合計少", "可據此斷定所有人都支持甲"], "A"),
        (f"一段關於「{topic}」的史料寫道：『當時記錄者只描述所見事件，未說明原因。』這段文字最適合支持哪項判讀？", ["先區分史料中的描述與後人的解釋", "把未寫出的原因當成史料原話", "只因作者身分便判定全篇正確", "用今天的價值觀取代史料內容"], "A"),
        (f"閱讀「{topic}」地圖時，圖例標示深色為高值、淺色為低值，且比例尺為 1 公分代表 20 公里。哪項做法正確？", ["先看圖例與比例尺，再比較分布", "只比較顏色不看圖例", "把圖上距離直接當成 1 公里", "忽略地圖的資料年份"], "A"),
        (f"比較「{topic}」的甲、乙兩案例：甲有 30 人、乙有 60 人，但甲的比例為 40%、乙為 20%。哪項結論最合理？", ["不能只比人數，還要同時考慮比例分母", "乙人數較多所以比例一定較高", "甲人數較少所以比例一定較低", "兩案例的資料無法比較任何面向"], "A"),
        (f"某政策涉及「{topic}」；支持者提出效益 3 項，反對者提出成本 2 項。若要進一步評估，最需要補充什麼？", ["各效益與成本的證據、範圍和受影響群體", "只計算支持者的項目數", "只引用最有利的一則評論", "以支持或反對的人數代替所有證據"], "A"),
        (f"兩份「{topic}」資料的數字不同：資料甲統計 2023 年，資料乙統計 2024 年。比較前應先做什麼？", ["確認年份、定義與統計範圍是否相同", "直接選較大的數字", "認定其中一份必然造假", "刪除年份較早的資料"], "A"),
        (f"針對「{topic}」的公共決策，居民、商家與政府各有不同考量。哪項整理方式較完整？", ["分別列出各群體利益、限制與可查證證據", "只採訪聲音最大的一方", "把多數意見當成事實資料", "只保留符合原先立場的意見"], "A"),
        (f"某資料只呈現「{topic}」一個月份的變化，沒有其他月份。作答時應如何限制結論？", ["只描述該月份的現象，不能直接推論全年趨勢", "直接說明全年必然相同", "以單月資料推測所有地區", "因資料不完整便任意補上數字"], "A"),
        (f"要檢核「{topic}」的新聞圖表是否容易誤導，哪項檢查最重要？", ["核對座標刻度、單位、資料來源與截取範圍", "只看標題是否吸引人", "只比較柱形圖的高度", "相信分享次數最多的貼文"], "A"),
    ]
    prompt, opts, answer = questions[i]
    # 將不同單元的資料編號放入解析，保留可追溯的題目語境並避免跨課程簽章重用。
    opts = list(opts)
    data["prompt"] = prompt
    data["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(opts)]
    data["answer"] = {"value": answer, "explanation": f"本題以「{topic}」的具體數據、史料、地圖或案例作為判讀材料；正解符合題幹提供的條件，不能以關鍵字、個人印象或過度推論取代證據。（資料組 {seed}）"}
    data["provenance"] = {"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考社會科；僅研究題型與能力方向，未複製原題文字、選項、圖片或答案。","authoringNote":"依單元 KG 概念與公開段考能力方向，以全新情境、選項、答案與解析獨立撰寫；待第二輪 AI／Terra 內容複核。"}
    data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-29"
    Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n"); return True

print(f"rewrote {sum(rewrite(p) for p in glob.glob('questions/social/*.json'))} social meta-template questions")
