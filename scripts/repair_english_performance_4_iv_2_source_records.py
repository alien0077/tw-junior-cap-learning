#!/usr/bin/env python3
"""Replace weak English 4-IV-2 references with inspected public-school exam loci."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions/english"
REPORT = ROOT / "implementation/reports/english-performance-4-iv-2-first-pass-review.json"

SOURCES = {
    "guochang_chart": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87-%E8%A9%A6%E9%A1%8C_1.pdf",
        "title": "高雄市立國昌國中109學年度第1學期第3次段考三年級英語科試題",
        "year": "109-1",
        "locator": "PDF第5頁第42–43題；第42題辨識圖表所呈現數量，第43題比對跨年度類別數據並判斷敘述",
        "observedPattern": "先辨識圖表類別與座標尺度，再把數值對應到類別／年份；比較題需逐項核對資料而非憑印象概述。",
    },
    "guochang_map": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87_1.pdf",
        "title": "高雄市立國昌國中107學年度第1學期第3次段考二年級英文科試題",
        "year": "107-1",
        "locator": "PDF第3頁第44–46題；依城市路線圖與火車時刻表整合地點、停靠站及時間選出符合條件的班次；第4頁第48題由路線文字辨識地圖",
        "observedPattern": "地圖、方向與時刻表題要求把文字條件逐一對應圖上位置／班次，不能只讀單一線索。",
    },
    "xiaogang_charts": {
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/22%E4%BA%8C%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/2%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/110-2-2%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
        "title": "高雄市立小港國中110學年度第2學期第2次段考二年級英文科試題",
        "year": "110-2",
        "locator": "PDF第3頁第44–47題；閱讀含Chart 1與Chart 2的資料題組，需連結圖表資訊與文章敘述作判斷",
        "observedPattern": "圖表與短文併讀時，先定位圖表所回答的面向，再核對文字限定條件；結論須受資料支持。",
    },
    "zhongshan_graphic": {
        "url": "https://csjh.kl.edu.tw/books/file/118/109-1%E9%AB%98%E4%B8%80%E6%84%9B%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E7%A7%91%E8%A9%A6%E9%A1%8C%E5%8D%B7.pdf",
        "title": "基隆市立中山高中109學年度第1學期第3次段考國中部英文科試題",
        "year": "109-1",
        "locator": "PDF第1頁閱讀測驗第1–3題；依COVID-19圖表讀取日期、確診數及圖表可支持的敘述",
        "observedPattern": "非連續圖文題需分辨時間標籤、數量與敘述範圍；答案不得超出圖表所示期間或數據。",
    },
    "dawan_chart": {
        "url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/114%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立大灣國中114學年度第1學期第1次段考三年級英文科試題",
        "year": "114-1",
        "locator": "閱讀測驗PDF第4頁第32–34題；由學生休閒活動長條圖判讀最大類別、數量及資料支持的結論",
        "observedPattern": "長條圖題以類別、數值和題目要求為線索，可考最大值、讀值及根據圖表作有限度推論。",
    },
    "minghu_schedule": {
        "url": "https://www.mtjh.tp.edu.tw/wp-content/uploads/doc/basicexam/95%E5%B9%B4%E7%AC%AC%E4%B8%80%E6%AC%A1%E5%9F%BA%E6%B8%AC%E8%8B%B1%E6%96%87%E8%A7%A3%E7%AD%94.pdf",
        "title": "臺北市立明湖國中網站公開之95年第一次國中基本學力測驗英文解答卷",
        "year": "95",
        "locator": "PDF第3頁第26–27題；整合West Town–South End地圖與火車時刻表，按人物位置、目的地及抵達時間判斷班次",
        "observedPattern": "雙表徵題須先分清地點與時間兩類線索，再逐站追蹤路線以排除不合條件的選項。",
    },
    "guochang_layout": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C-1%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87-%E9%A1%8C%E7%9B%AE%2B%E7%AD%94%E6%A1%88%E5%8D%B7-%E5%88%97%E5%8D%B0%E7%AC%A6%E5%90%88.pdf",
        "title": "高雄市立國昌國中108學年度第1學期第2次段考一年級英文科試題",
        "year": "108-1",
        "locator": "PDF第2頁第24題座位表；PDF第3頁第28–30題依房間圖片判讀物品與相對位置",
        "observedPattern": "位置圖題要求辨認物件、參照物及between／next to等相對關係，判斷選項是否忠實對應圖像。",
    },
}

ITEMS = {
    1: {
        "refs": ["guochang_chart", "dawan_chart", "xiaogang_charts"],
        "strategy": "把每個星期幾與其借閱數配成一組，再比較最大值；不要把「最高」誤讀成最後一天或相鄰兩天。",
        "explanation": "Tuesday 的18大於Wednesday的15和Monday的12，所以「Students borrowed the most books on Tuesday」符合資料。把Wednesday說成多於Tuesday會顛倒數值；說兩天相同或Monday借閱為零，也都和圖表不符。",
        "steps": ["先讀標題，確認數字代表每日借閱本數。", "逐組記下 Monday 12、Tuesday 18、Wednesday 15。", "比較三個數值，確認18是其中的最大值。", "回到類別軸確認18對應Tuesday，而非Wednesday。", "選出表示Tuesday借閱最多的句子，並確認星期與數值都吻合。"],
        "order": ["C", "D", "A", "B"],
    },
    2: {
        "refs": ["guochang_map", "zhongshan_graphic", "minghu_schedule"],
        "strategy": "先把圖示解碼，再鎖定圖示所屬日期；句子中的天氣與日期必須成對吻合。",
        "explanation": "雨天圖示位於Tuesday欄，因此「It was rainy on Tuesday」才符合資料。把晴天放在Wednesday或把多雲放在Monday都交換了日期；宣稱三天都下雨，則把單日資訊擴大到整週。",
        "steps": ["先依橫軸確認日期順序為Monday、Tuesday、Wednesday。", "只看Tuesday所在欄，辨認該欄是雨的圖示。", "將圖示轉成英文描述：It was rainy。", "檢查選項是否把日期移位，或把一天擴張成三天。", "選出It was rainy on Tuesday，核對日期和天氣均正確。"],
        "order": ["B", "A", "C", "D"],
    },
    3: {
        "refs": ["guochang_chart", "dawan_chart", "xiaogang_charts"],
        "strategy": "比較圓餅圖比例時，先讀百分比所屬類別，再比較題目指定的兩部分；不把比例當成實際人數。",
        "explanation": "Sports占40%，Art占25%，所以Sports比例高於Art。這只支持兩類比例的比較，不能推成所有人都參加Sports；Music也不是零，三類比例並不相同。",
        "steps": ["確認題目問的是Sports與Art的相對比例。", "從圖例／標籤讀出Sports 40%、Art 25%。", "比較40與25，差15個百分點，Sports比例較大。", "逐項排除把大小顛倒、說成零或宣稱相等的句子。", "選出表示Sports比例高於Art的句子，避免外推到所有學生。"],
        "order": ["D", "B", "C", "A"],
    },
    4: {
        "refs": ["guochang_map", "minghu_schedule", "guochang_layout"],
        "strategy": "讀方位句時固定參照物：先問「誰在誰的哪一側」，再核對主詞和介系詞有沒有倒轉。",
        "explanation": "已知café在library東側，因此「The café is east of the library」保留了物件、參照物與方向。其他說法不是把方位顛倒，就是換成題目未提供的park位置，或把east誤成inside。",
        "steps": ["先圈出參照物the library，再圈出要定位的the café。", "辨認方位詞east，並注意句型是X is east of Y。", "把已知關係回填：the café is east of the library。", "檢查其他選項有無反轉主客體或增加圖上不存在的關係。", "選出The café is east of the library，兩個位置角色均未顛倒。"],
        "order": ["A", "B", "C", "D"],
    },
    5: {
        "refs": ["xiaogang_charts", "guochang_map", "dawan_chart"],
        "strategy": "流程圖問「某步之後」時，沿箭頭只前進一格；先後順序不可用常識重排。",
        "explanation": "箭頭順序是wash the cup → add tea → pour hot water → wait three minutes。add tea之後緊接pour hot water；重新洗杯是前一步，先等待會打亂流程，而未加熱水就飲用則漏掉必要步驟。",
        "steps": ["在流程中定位題目指定的add tea這一步。", "沿箭頭方向看緊接的下一個方框，而不是回頭或跳格。", "下一個方框寫著pour hot water。", "逐項檢查是否顛倒順序、提前等待或省略必要步驟。", "找出寫著Pour hot water的選項；它是add tea後的下一步。"],
        "order": ["C", "A", "B", "D"],
    },
    6: {
        "refs": ["guochang_chart", "zhongshan_graphic", "dawan_chart"],
        "strategy": "描述趨勢要按時間順序比較相鄰點；下降須由每一段數值都變小支持，不能只看起點和終點。",
        "explanation": "April到May由80降到60，May到June再由60降到45，兩段都下降，因此「Water use decreased each month」符合整段趨勢。說用量逐月增加、維持80或六月高於四月，都與數值衝突。",
        "steps": ["先確認橫軸時間順序是April、May、June。", "讀出三點：80、60、45 liters。", "比較第一段：60小於80；再比較第二段：45小於60。", "因為兩段都下降，才可說decreased each month。", "選出描述逐月下降的句子，確認它涵蓋兩段變化而非只看首尾。"],
        "order": ["B", "A", "C", "D"],
    },
    7: {
        "refs": ["guochang_map", "minghu_schedule", "xiaogang_charts"],
        "strategy": "先確認表格單位都是分鐘；最大耗時對應最慢，最小耗時對應最快，不能把時間長短和速度快慢混為同向。",
        "explanation": "Walking需50分鐘，是三種方式中耗時最長，因此它最慢。把bicycle說成比walking慢，與20和50分鐘矛盾；bus也不是最快，因為bicycle只需20分鐘；walking更不可能比bicycle省時。",
        "steps": ["把三個方式及時間抄成配對：bus 35、bicycle 20、walking 50。", "確認數字單位相同，都是minutes，才可直接比較。", "找到最大耗時50分鐘，對應walking。", "題目問slowest，最長耗時才是最慢，不是最快。", "找出指出walking is the slowest的選項，這與耗時表一致。"],
        "order": ["D", "A", "C", "B"],
    },
    8: {
        "refs": ["guochang_layout", "guochang_map", "minghu_schedule"],
        "strategy": "位置題採一個物件、一個參照點逐句驗證；beside、between、inside不可互換，也不能補入未標示的位置。",
        "explanation": "平面圖把plant放在Desk 1旁邊，所以「The plant is beside Desk 1」符合資訊。垃圾桶的位置是Desk 3與door之間，不是Desk 1和Desk 2之間；圖上也未表示plant緊鄰垃圾桶。",
        "steps": ["先定位plant，再讀它旁邊的參照點Desk 1。", "把beside理解為緊鄰，而非between或inside。", "比對A是否保留同一物件、參照物和關係詞。", "其餘選項逐一對照垃圾桶位置或排除題目未提供的植物—垃圾桶關係。", "只有A精確對上平面圖資訊，故選A作答。"],
        "order": ["A", "C", "D", "B"],
    },
    9: {
        "refs": ["guochang_chart", "dawan_chart", "xiaogang_charts"],
        "strategy": "調查結論要由最大類別支持，並保留樣本界線；「最多受訪者」不等於「所有人」。",
        "explanation": "Bus有22人，高於walk的10人及bicycle的8人，因此可說在這次調查裡bus最常見。把結論擴大成everyone超出樣本；說bicycle比bus常見顛倒了數據；說沒有人步行也忽略了10位步行者。",
        "steps": ["確認三個數字都是本次受訪學生的人數。", "比較walk 10、bus 22、bicycle 8，最大值是22。", "將22對應回bus，形成限定於this survey的結論。", "檢查有沒有把調查樣本擴大成所有學生，或反轉／抹除資料。", "選出寫著The bus is the most common way in this survey的句子。"],
        "order": ["C", "A", "B", "D"],
    },
    10: {
        "refs": ["guochang_chart", "dawan_chart", "zhongshan_graphic"],
        "strategy": "比較前後柱狀值時分兩步：先用後值減前值求變化量，再用柱高判斷增加或減少。",
        "explanation": "修訂前是6分、修訂後是9分；後值減前值為9−6=3，且後一根柱較高，所以分數增加3分。說分數下降、沒有變化，或把前後兩個數值交換，都同時違反圖表呈現的數值順序與變化方向。",
        "steps": ["依時間標籤記下before revision為6、after revision為9。", "以後值減前值計算變化量：9−6=3分。", "比較柱高確認後值較高，所以變化方向是增加。", "核對句子須同時說對差值和方向，不能只說有變化。", "選出同時寫明increased及three points的句子。"],
        "order": ["B", "A", "C", "D"],
    },
}

def make_ref(key: str) -> dict:
    source = SOURCES[key]
    return {
        **source,
        "subject": "english",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }

def relabel_option_letters(text: str, order: list[str]) -> str:
    labels = {old: new for new, old in zip("ABCD", order)}
    return re.sub(r"\b([ABCD])\b", lambda match: labels[match.group(1)], text)

def main() -> int:
    failures = []
    for number, config in ITEMS.items():
        path = QUESTION_DIR / f"question-english-performance-4-iv-2-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("reviewStatus") != "draft":
            failures.append(f"{path.name}: refusing non-draft item")
            continue
        old = {option["id"]: option["text"] for option in data["options"]}
        if set(old) != {"A", "B", "C", "D"}:
            failures.append(f"{path.name}: unexpected source question shape")
            continue
        order = config["order"]
        correct = next(label for label, old_id in zip("ABCD", order) if old_id == "A")
        current_answer = data.get("answer", {}).get("value")
        if current_answer == "A":
            data["options"] = [{"id": label, "text": old[old_id]} for label, old_id in zip("ABCD", order)]
        elif current_answer != correct:
            failures.append(f"{path.name}: unexpected answer position {current_answer}")
            continue
        data["answer"] = {"value": correct, "explanation": relabel_option_letters(config["explanation"], order)}
        data["solutionStrategy"] = config["strategy"]
        data["solutionSteps"] = [relabel_option_letters(step, order) for step in config["steps"]]
        data["examPatternRefs"] = [make_ref(key) for key in config["refs"]]
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCES[config["refs"][0]]["url"],
            "sourceLocator": "；".join(SOURCES[key]["locator"] for key in config["refs"]),
            "authoringNote": "依可追溯公立學校英文試題之資料型態與推理能力方向重新設計；只借鑑作答技能，不複製原題、選項、圖表或答案。內容仍待完整內容與授權審查。",
        }
        data["updatedAt"] = date.today().isoformat()
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    paths = sorted(QUESTION_DIR.glob("question-english-performance-4-iv-2-*.json"))
    rows = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    if len(rows) != 10:
        failures.append(f"expected 10 items, got {len(rows)}")
    if any(len(item.get("solutionSteps", [])) != 5 for item in rows):
        failures.append("not every item has five worked steps")
    if len({item.get("solutionStrategy") for item in rows}) != 10:
        failures.append("strategies are not individually authored")
    if len({tuple(item.get("solutionSteps", [])) for item in rows}) != 10:
        failures.append("step sequences are not individually authored")
    if any(item.get("reviewStatus") != "draft" for item in rows):
        failures.append("review status escaped draft")
    report = {
        "unit": "4-Ⅳ-2：依圖示圖表寫句子",
        "checked": len(rows),
        "passed": len(rows) - len(failures),
        "failures": failures,
        "status": "pass" if len(rows) == 10 and not failures else "fail",
        "sourceInstitutions": ["高雄市立國昌國中", "高雄市立大灣國中", "高雄市立小港國中", "基隆市立中山高中國中部", "臺北市立明湖國中網站公開之國中基本學力測驗"],
        "sourcePolicy": "逐題保留公開卷頁碼／題號與圖表能力模式；未複製原題、選項、圖表或答案。",
        "notes": "10題各有唯一答案、逐題解釋、專屬策略與五步詳解；正解位置經調整分散。來源定位改善不等同完整內容／版權審查，題目仍為draft。",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
