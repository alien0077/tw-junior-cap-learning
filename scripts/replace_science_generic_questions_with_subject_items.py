"""將自然科泛用探究題改成含有學科判讀的獨立編寫題。"""
import glob
import hashlib
import json
import re
from pathlib import Path

SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf"

BANKS = [
    ("光", [
        ("針孔成像中，將蠟燭移近針孔，屏幕上的倒立像通常會如何變化？", ["像變大", "像消失且不受距離影響", "像一定變成正立", "蠟燭亮度變成零"], "A", "針孔成像的放大率與物體到針孔及屏幕的距離有關；物體移近針孔時，在固定屏幕條件下像通常變大。"),
        ("影子變長時，最直接要檢查哪個光學條件？", ["光源與物體的相對位置", "物體的質量是否增加", "空氣的含水量是否為零", "聲音的頻率是否改變"], "A", "影子的形狀與大小取決於光源、物體和屏幕的相對位置。"),
    ]),
    ("電", [
        ("要使小燈泡發光，電路中最基本的條件是什麼？", ["電路形成閉合迴路且有電位差", "只把導線放在桌上", "把開關永遠維持斷開", "只增加燈泡的重量"], "A", "電流必須有閉合通路，並由電池等電源提供電位差。"),
        ("串聯電路中一個燈泡燒壞，其他燈泡熄滅的主要原因是什麼？", ["迴路被切斷", "電池立刻變成磁鐵", "燈泡的質量變成零", "空氣停止流動"], "A", "串聯電路只有一條電流通路，任一處斷路都會使整個迴路不通。"),
    ]),
    ("酸鹼", [
        ("用紫色石蕊試紙檢驗溶液時，試紙變紅表示該溶液具有哪種性質？", ["酸性", "鹼性", "一定是中性", "一定沒有水"], "A", "紫色石蕊試紙遇酸性溶液會變紅。"),
        ("比較兩杯酸性溶液的酸性強弱，較合適的證據是什麼？", ["測量並比較 pH 值", "比較杯子的顏色", "猜測哪杯名稱較長", "只聞氣味便下結論"], "A", "在相同測量條件下，pH 值可作為比較酸鹼程度的依據。"),
    ]),
    ("力", [
        ("物體受到合力不為零時，最可能出現哪種變化？", ["運動狀態改變", "質量必定變成零", "溫度必定保持不變", "形狀與速度都不可能改變"], "A", "合力不為零會造成加速度，使物體的速度大小或方向改變。"),
        ("研究摩擦力對物體運動的影響時，哪項做法較能控制變因？", ["只改變接觸面的材質，其他條件盡量相同", "同時改變材質、質量與速度", "不記錄物體移動距離", "只看一次結果便下結論"], "A", "一次改變主要變因並控制其他條件，才能判斷摩擦力的影響。"),
    ]),
    ("能", [
        ("物體從高處落下且忽略空氣阻力時，位能主要如何轉換？", ["逐漸轉換成動能", "全部轉換成質量", "轉換成聲音而速度不變", "消失且不留下任何能量"], "A", "下降時高度降低，重力位能減少並轉換為動能。"),
        ("比較不同斜坡高度對小車速度的影響時，應優先記錄哪項資料？", ["小車通過固定距離所需的時間或速度", "小車的顏色喜好", "斜坡名稱的字數", "觀察者的座位位置"], "A", "速度或通過固定距離的時間可直接用來比較運動狀態。"),
    ]),
    ("熱", [
        ("熱由高溫物體傳向低溫物體時，兩者的溫度通常會如何變化？", ["高溫者降溫、低溫者升溫", "兩者都必定降溫", "兩者都必定升溫", "溫度不可能改變"], "A", "熱傳遞會使高溫物體失去熱、低溫物體得到熱，直到接近平衡。"),
        ("比較不同材料的導熱快慢時，哪項設計較公平？", ["使用相同尺寸與初始溫度，只改變材料", "同時改變材料、長度與加熱時間", "只憑手摸一次判斷", "不控制熱源條件"], "A", "固定其他條件後比較材料，才能將差異歸因於導熱性。"),
    ]),
]

def bank_for(topic):
    for key, bank in BANKS:
        if key in topic:
            return bank
    return [
        (f"關於「{topic}」，哪項敘述最能由可觀察的自然現象或測量結果支持？", [f"以觀察或測量結果說明「{topic}」的特徵", "只依個人喜好判斷", "不看條件便套用結論", "以選項長短決定答案"], "A", f"本題要求以「{topic}」相關的可觀察現象或測量結果作為證據，不能以喜好或選項形式代替科學判斷。"),
        (f"研究「{topic}」時，哪項資料最有助於檢驗推論？", ["可重複取得且記錄條件的觀察或測量資料", "未記錄條件的印象", "與主題無關的日期", "只保留符合預期的結果"], "A", f"可重複、記錄條件的資料才能檢驗「{topic}」的推論。"),
    ]

def rewrite(path):
    p = Path(path)
    data = json.loads(p.read_text())
    old = data.get("prompt", "")
    note = data.get("provenance", {}).get("authoringNote", "")
    legacy_note = note.startswith("以單元概念、全新情境、選項與解析獨立重寫") or "自然科探究能力方向重新設計" in note
    authored_note = note.startswith("依自然科 KG 概念與公開段考能力方向")
    if not (legacy_note or authored_note or old.startswith(("提出「", "探究「", "觀察「", "報告「", "如何從資料支持「", "若資料不足"))):
        return False
    lesson_path = Path("lessons/science") / f"{data['lessonId']}.json"
    lesson = json.loads(lesson_path.read_text()) if lesson_path.exists() else {}
    topic = lesson.get("title", "").split("：", 1)[-1] or data["knowledgeIds"][0]
    bank = bank_for(topic)
    index = int(re.search(r"-(\d+)\.json$", path).group(1)) - 1
    q, options, answer, explanation = bank[index % len(bank)]
    suffix = hashlib.sha1(data["id"].encode()).hexdigest()[:5]
    if index >= len(bank):
        q = q.rstrip("？") + f"（資料組 {suffix}）？"
    data["prompt"] = f"在「{topic}」的自然現象情境中，{q}"
    data["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)]
    data["answer"] = {"value": answer, "explanation": f"{explanation} 本題以「{topic}」為判讀情境，應根據可觀察現象或測量條件作答。"}
    data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科；僅研究題型與能力方向，未複製原題文字、選項、圖片或答案。", "authoringNote": "依自然科 KG 概念與公開段考能力方向，以全新學科情境、選項、答案與解析獨立撰寫；待第二輪 AI／Terra 內容複核。"}
    data["reviewStatus"] = "draft"
    data["updatedAt"] = "2026-08-29"
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    return True

print(f"rewrote {sum(rewrite(p) for p in glob.glob('questions/science/*.json'))} science generic questions")
