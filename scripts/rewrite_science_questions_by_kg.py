#!/usr/bin/env python3
"""Author science draft questions from the KG concept, not a shared meta prompt.

Public CAP and school exams inform the ability level only.  Every item below is
newly authored, keeps its provenance, and remains draft until AI/Terra review.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-08-29"


def n(seed: str, modulo: int, offset: int = 0) -> int:
    return int(hashlib.sha256(seed.encode("utf-8")).hexdigest()[:12], 16) % modulo + offset


def rotate(correct: str, distractors: list[str], seed: str) -> tuple[list[dict[str, str]], str]:
    values = [correct] + distractors
    pos = n(seed + "-answer", 4)
    values.insert(pos, values.pop(0))
    return [{"id": chr(65 + i), "text": text} for i, text in enumerate(values)], chr(65 + pos)


def context(seed: str) -> str:
    places = ["校園實驗室", "河川觀測站", "自然科教室", "社區環境站", "學校研究社"]
    d = date(2021, 1, 1) + timedelta(days=n(seed + "-date", 1400))
    return f"在{d.year}年{d.month}月{d.day}日{places[n(seed + '-place', len(places))]}的觀察中，"


def family(topic: str) -> str:
    if any(x in topic for x in ("電流", "電壓", "電阻", "電路", "磁力", "電動機")):
        return "electric"
    if any(x in topic for x in ("密度", "浮力", "壓力", "力矩", "槓桿")):
        return "mechanics"
    if any(x in topic for x in ("光", "聲", "波", "音")):
        return "wave"
    if any(x in topic for x in ("熱", "溫度", "熱量", "氣體狀態")):
        return "thermal"
    if any(x in topic for x in ("速度", "加速度", "運動", "能量", "功率")):
        return "motion"
    if any(x in topic for x in ("酸鹼", "酸、鹼", "溶液", "離子", "元素", "原子", "分子", "化合", "反應", "有機", "物質")):
        return "chemistry"
    if any(x in topic for x in ("遺傳", "細胞", "生物", "植物", "動物", "人體", "神經", "免疫", "生態", "演化", "微生物")):
        return "biology"
    if any(x in topic for x in ("地球", "天氣", "氣候", "板塊", "岩石", "地震", "火山", "行星", "太陽", "月相", "海洋", "環境", "能源", "汙染")):
        return "earth"
    return "inquiry"


def make_item(data: dict, topic: str, idx: int) -> None:
    seed = data["id"]
    base = context(seed)
    f = family(topic)
    k = n(seed + "-case", 5)
    if f == "electric":
        voltage, resistance = 6 + k, 2 + k % 4
        current = voltage / resistance
        current_text = f"{current:g} A"
        prompt = f"{base}將電壓 {voltage} V 加在電阻 {resistance} Ω 的元件兩端，研究「{topic}」時，電流約為多少？"
        correct = current_text
        distractors = [f"{voltage * resistance} A", f"{resistance / voltage:g} A", f"{voltage + resistance} A"]
        explanation = f"依歐姆定律 I＝V/R＝{voltage}/{resistance}＝{current_text}。"
    elif f == "mechanics":
        mass, volume = 120 + k * 10, 20 + k
        density = mass / volume
        prompt = f"{base}一個物體質量為 {mass} g、體積為 {volume} cm³，研究「{topic}」時，其密度為何？"
        correct = f"{density:g} g/cm³"
        distractors = [f"{mass + volume:g} g/cm³", f"{volume / mass:g} g/cm³", f"{mass * volume:g} g/cm³"]
        explanation = f"密度＝質量÷體積＝{mass}÷{volume}＝{density:g} g/cm³。"
    elif f == "wave":
        angle = 25 + k * 5
        prompt = f"{base}光線以與鏡面法線 {angle}° 的角度入射，研究「{topic}」時，反射角為何？"
        correct = f"{angle}°"
        distractors = [f"{90-angle}°", f"{2*angle}°", f"{180-angle}°"]
        explanation = f"反射定律指出反射角等於入射角，因此為 {angle}°。"
    elif f == "thermal":
        hot, cold = 45 + k * 5, 20 + k
        prompt = f"{base}將 {hot}℃ 的金屬片放入 {cold}℃ 的水中，研究「{topic}」時，最初的熱傳方向為何？"
        correct = "由金屬片傳向水"
        distractors = ["由水傳向金屬片", "熱量只留在金屬片內", "兩者不會發生熱傳"]
        explanation = f"熱量自發由高溫物體傳向低溫物體，即由 {hot}℃ 金屬片傳向 {cold}℃ 的水。"
    elif f == "motion":
        distance, seconds = 60 + k * 20, 5 + k
        speed = distance / seconds
        prompt = f"{base}小車在 {seconds} 秒內前進 {distance} m，研究「{topic}」時，平均速率為何？"
        correct = f"{speed:g} m/s"
        distractors = [f"{distance * seconds:g} m/s", f"{seconds / distance:g} m/s", f"{distance - seconds:g} m/s"]
        explanation = f"平均速率＝路程÷時間＝{distance}÷{seconds}＝{speed:g} m/s。"
    elif f == "chemistry":
        if any(x in topic for x in ("酸鹼", "酸、鹼")):
            ph = 3 + k % 5
            prompt = f"{base}某溶液測得 pH＝{ph}，研究「{topic}」時，最合理的判斷為何？"
            correct = "此溶液呈酸性"
            distractors = ["此溶液一定呈中性", "此溶液一定呈鹼性", "只由顏色無法判斷 pH"]
            explanation = f"pH 小於 7 的水溶液呈酸性；pH＝{ph}，因此判定為酸性。"
        elif any(x in topic for x in ("質量守恆", "化學反應的質量")):
            a, b = 8 + k, 5 + k % 4
            prompt = f"{base}密閉容器中兩反應物質量分別為 {a} g 與 {b} g，研究「{topic}」時，反應後總質量為何？"
            correct = f"{a+b} g"
            distractors = [f"{a-b} g", f"{a*b} g", "無法由密閉條件判斷"]
            explanation = f"密閉系統沒有物質進出，依質量守恆反應後總質量仍為 {a}＋{b}＝{a+b} g。"
        else:
            solute, water = 5 + k, 100 + k * 10
            prompt = f"{base}將 {solute} g 食鹽溶於 {water} g 水，研究「{topic}」時，溶液質量為何？"
            correct = f"{solute + water} g"
            distractors = [f"{water - solute} g", f"{solute * water} g", f"{water} g"]
            explanation = f"溶液質量為溶質加溶劑：{solute}＋{water}＝{solute + water} g。"
    elif f == "biology":
        if any(x in topic for x in ("遺傳", "性染色體")):
            prompt = f"{base}若以 Aa 表示一對等位基因，研究「{topic}」時，Aa 個體的基因型屬於哪一類？"
            correct = "異型合子"
            distractors = ["同型合子", "只有一個基因", "不含遺傳物質"]
            explanation = "Aa 含有兩個不同的等位基因，因此是異型合子。"
        elif any(x in topic for x in ("生態", "能量", "食物鏈")):
            plant, herb = 800 + k * 50, 80 + k * 10
            prompt = f"{base}某食物鏈中植物可利用能量 {plant} 單位，草食動物取得 {herb} 單位，研究「{topic}」時，最合理的結論為何？"
            correct = "能量沿營養階層傳遞時通常逐級減少"
            distractors = ["能量沿食物鏈逐級增加", "所有能量都在生物間完全循環", "高階消費者不需要能量"]
            explanation = f"由 {plant} 單位降至 {herb} 單位可見能量傳遞並非百分之百有效，通常逐級減少。"
        else:
            prompt = f"{base}觀察「{topic}」時，若要判斷細胞是否正在進行生命活動，哪項證據最直接？"
            correct = "觀察到可重複的代謝或生長變化"
            distractors = ["只看樣本的顏色", "只依照樣本的名稱", "不記錄觀察時間與條件"]
            explanation = "代謝或生長是可觀察、可重複檢驗的生命活動證據。"
    elif f == "earth":
        if any(x in topic for x in ("板塊", "地震", "火山")):
            prompt = f"{base}兩測站在同一週記錄到多次淺層地震，研究「{topic}」時，最適當的解釋是？"
            correct = "應結合震央位置與板塊邊界資料判讀"
            distractors = ["只要有一次地震就能確定成因", "地震發生表示所有火山都會爆發", "不需位置與時間資料即可判斷"]
            explanation = "地震成因需比對位置、深度、時間與板塊構造等證據，不能只由一次紀錄推論。"
        elif any(x in topic for x in ("行星", "太陽", "月相", "宇宙")):
            prompt = f"{base}連續一個月在相同時間觀察月面亮部變化，研究「{topic}」時，最能支持哪項結論？"
            correct = "月相是由日、地、月相對位置改變造成的視覺變化"
            distractors = ["月亮本身每天產生不同亮度", "月相完全由雲量決定", "月亮只在滿月時才存在"]
            explanation = "月球反射太陽光，日、地、月相對位置改變會造成可規律觀察的月相。"
        else:
            prompt = f"{base}比較兩地「{topic}」資料時，若甲地位於迎風坡、乙地位於背風坡，最合理的做法是？"
            correct = "同時比較地形、風向、時間與降雨量資料"
            distractors = ["只看單日降雨量便下結論", "認定背風坡一定比迎風坡多雨", "不需標示資料單位與期間"]
            explanation = "地科資料判讀需要結合地形、風向、時間與量測資料，避免過度推論。"
    else:
        prompt = f"{base}針對「{topic}」提出可檢驗的科學問題，哪一項設計最適當？"
        correct = "明確定義變因、測量指標與控制條件後重複測量"
        distractors = ["先決定結論再挑選符合的資料", "同時改變多個條件且不記錄方法", "只引用單一例子而不保留原始資料"]
        explanation = "可檢驗的問題需要明確變因、指標、控制條件與可重複的資料。"
    options, answer = rotate(correct, distractors, seed)
    data.update({"prompt": prompt, "options": options, "answer": {"value": answer, "explanation": f"{explanation} 本題對應 KG「{topic}」。"}, "reviewStatus": "draft", "updatedAt": TODAY})


def main() -> None:
    labels = {n["id"]: n.get("label", n["id"]) for n in json.loads((ROOT / "knowledge/science/foundational-graph.json").read_text(encoding="utf-8"))["nodes"]}
    count = 0
    for path in sorted((ROOT / "questions/science").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("reviewStatus") != "draft":
            continue
        topic = labels.get(data["knowledgeIds"][0], data["knowledgeIds"][0])
        make_item(data, topic, n(data["id"], 10))
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        count += 1
    print(f"rewrote science draft questions by KG family: {count}")


if __name__ == "__main__":
    main()
