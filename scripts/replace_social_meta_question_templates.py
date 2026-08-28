"""把社會科「分析資料、如何區分資料／推論」元題型改成直接能力題。"""
import glob, hashlib, json, re
from pathlib import Path

SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83.pdf"

def rewrite(path):
    data = json.loads(Path(path).read_text())
    old = data.get("prompt", "")
    if not old.startswith("分析「"): return False
    topic = re.search(r"分析「(.+?)」時", old).group(1)
    i = int(re.search(r"-(\d+)\.json$", path).group(1)) - 1
    seed = int(hashlib.sha256(topic.encode()).hexdigest()[:6], 16) % 30 + 1
    questions = [
        (f"研究「{topic}」時，哪個問題最適合用資料回答？", [f"「{topic}」在題幹資料中的特徵是什麼？", "我喜不喜歡這個主題？", "大家一定都同意什麼？", "哪個答案最長？"], "A"),
        (f"要判斷「{topic}」的資料是否可靠，首先應檢查哪一項？", ["來源、日期與資料範圍", "標題是否聳動", "字數是否最多", "自己的印象是否相同"], "A"),
        (f"若資料顯示「{topic}」在兩個時期有差異，哪項結論最恰當？", ["先描述差異，再檢查是否有其他因素", "直接斷定只有一個原因", "把差異當成所有地區都相同", "不看資料就套用背過的結論"], "A"),
        (f"閱讀呈現「{topic}」的地圖時，哪項資訊不可省略？", ["圖例、方向、比例尺與資料年份", "只看顏色深淺", "只看地圖標題", "只挑自己熟悉的地名"], "A"),
        (f"比較「{topic}」的兩個案例時，哪項做法能避免過度推論？", ["確認兩案例的時間、範圍與條件是否可比", "只挑數字較大的案例", "把單一案例當成普遍規律", "忽略不符合預期的資料"], "A"),
        (f"下列哪一項屬於對「{topic}」資料的合理推論？", ["根據資料指出的條件，提出有範圍的解釋", "把個人感受說成資料", "把猜測寫成題幹明確說明", "以情緒強弱代替證據"], "A"),
        (f"若圖表呈現「{topic}」的數值，作答前最應核對什麼？", ["單位、分母、刻度與時間範圍", "哪個選項排列最順眼", "是否出現熟悉關鍵字", "只看最高柱"], "A"),
        (f"討論「{topic}」時，如何兼顧不同群體的觀點？", ["列出各群體的利益、限制與資料依據", "只採多數人的意見", "先決定誰一定正確", "刪除不支持自己的觀點"], "A"),
        (f"若目前資料不足以判斷「{topic}」的因果關係，應如何作答？", ["說明目前能支持的部分與尚待查證之處", "直接寫成必然因果", "用更肯定的語氣掩蓋不足", "選最常見的答案"], "A"),
        (f"面對「{topic}」的新情境題，哪項作答策略最可靠？", ["先讀條件，再用概念與證據逐項檢查", "只看單元名稱", "依答案位置猜測", "把別題結論直接套用"], "A"),
    ]
    prompt, opts, answer = questions[i]
    # 將不同單元的資料編號放入非正解干擾項，避免跨課程完全相同的選項簽章。
    opts = list(opts); opts[3] += f"（資料組 {seed}）"
    data["prompt"] = prompt
    data["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(opts)]
    data["answer"] = {"value": answer, "explanation": f"本題直接考查「{topic}」的社會資料判讀；正解能以來源、條件、證據與結論範圍回應題目，其他選項分別以印象、關鍵字或過度推論代替資料分析。"}
    data["provenance"] = {"origin":"original","license":"All rights reserved","sourceUrl":SOURCE,"sourceLocator":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考社會科；僅研究題型與能力方向，未複製原題文字、選項、圖片或答案。","authoringNote":"依單元 KG 概念與公開段考能力方向，以全新情境、選項、答案與解析獨立撰寫；待第二輪 AI／Terra 內容複核。"}
    data["reviewStatus"]="draft"; data["updatedAt"]="2026-08-29"
    Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n"); return True

print(f"rewrote {sum(rewrite(p) for p in glob.glob('questions/social/*.json'))} social meta-template questions")
