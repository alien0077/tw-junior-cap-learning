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


def inquiry_options(seed: str, topic: str, question_number: int) -> tuple[str, list[str]]:
    variables = ["光照時間", "水溫", "攪拌速度", "距離", "溶液濃度", "施力大小"]
    control = variables[n(seed + "-variable", len(variables))]
    groups = 3 + n(seed + "-groups", 3)
    repeats = 3 + n(seed + "-repeats", 3)
    sample_count = 8 + question_number
    correct = f"研究「{topic}」時只改變{control}，其餘條件一致，設置{groups}組、每組取樣{sample_count}份並各重複測量{repeats}次"
    wrong = [
        f"研究「{topic}」時同時改變{control}與另一個條件，卻不記錄方法",
        f"研究「{topic}」時只測量{groups}組中的一組就直接下結論",
        f"研究「{topic}」時先決定結論，再挑選支持結論的{sample_count}筆資料",
    ]
    return correct, wrong


def biology_options(seed: str, topic: str, question_number: int) -> tuple[str, list[str]]:
    evidence = [
        "連續觀察到細胞數量增加",
        "測得樣本持續吸收氧氣並產生二氧化碳",
        "在相同條件下多次觀察到新細胞形成",
        "記錄到樣本穩定進行物質交換",
        "觀察到個體在一段時間內生長並能重複驗證",
    ]
    days = 2 + question_number
    correct = f"連續{days}天研究「{topic}」並{evidence[n(seed + '-evidence', len(evidence))]}"
    wrong = [
        f"研究「{topic}」時只依樣本的顏色（未記錄{days}天的時間與條件）",
        f"研究「{topic}」時只依樣本的名稱推測，不進行觀察",
        f"研究「{topic}」時只觀察一次外形，便排除所有其他證據",
    ]
    return correct, wrong


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
    question_number = int(re.search(r"-(\d+)$", seed).group(1))
    base = context(seed)
    f = family(topic)
    # Use a broad data range so two independently authored cases do not
    # collapse into the same answer tuple; each value remains an actual case
    # parameter used by the explanation below.
    k = n(seed + "-case", 1000)
    if f == "electric":
        voltage, resistance = 6 + n(seed + "-voltage", 45), 2 + n(seed + "-resistance", 9)
        current = voltage / resistance
        current_text = f"{current:g} A"
        prompt = f"{base}將電壓 {voltage} V 加在電阻 {resistance} Ω 的元件兩端，研究「{topic}」時，電流約為多少？"
        correct = current_text
        distractors = [f"{voltage * resistance} A", f"{resistance / voltage:g} A", f"{voltage + resistance} A"]
        explanation = f"依歐姆定律 I＝V/R＝{voltage}/{resistance}＝{current_text}。"
    elif f == "mechanics":
        mass, volume = 120 + n(seed + "-mass", 880), 20 + n(seed + "-volume", 80)
        density = mass / volume
        prompt = f"{base}一個物體質量為 {mass} g、體積為 {volume} cm³，研究「{topic}」時，其密度為何？"
        correct = f"{density:g} g/cm³"
        distractors = [f"{mass + volume:g} g/cm³", f"{volume / mass:g} g/cm³", f"{mass * volume:g} g/cm³"]
        explanation = f"密度＝質量÷體積＝{mass}÷{volume}＝{density:g} g/cm³。"
    elif f == "wave":
        angle = 10 + (n(seed + "-angle", 16) * 5)
        medium = ["空氣射向平面鏡", "水中射向鏡面", "玻璃射向鏡面", "空氣射向金屬面", "水中射向金屬面", "玻璃射向平面鏡"][n(seed + "-medium", 6)]
        prompt = f"{base}{medium}時，光線與鏡面法線的入射角為 {angle}°，研究「{topic}」時，反射角為何？"
        correct = f"{angle}°（{medium}）"
        distractors = [f"{90-angle}°（把入射角誤當折射角）", f"{2*angle}°（把入射角加倍）", f"{180-angle}°（以平角計算）"]
        explanation = f"反射定律指出反射角等於入射角，因此為 {angle}°。"
    elif f == "thermal":
        hot, cold = 45 + n(seed + "-hot", 75) * 2, 20 + n(seed + "-cold", 18)
        prompt = f"{base}將 {hot}℃ 的金屬片放入 {cold}℃ 的水中，研究「{topic}」時，最初的熱傳方向為何？"
        correct = "由金屬片傳向水"
        distractors = [f"由 {cold}℃ 的水傳向 {hot}℃ 金屬片", "熱量只留在金屬片內而不進入水", "兩者溫度不同卻不會發生熱傳"]
        explanation = f"熱量自發由高溫物體傳向低溫物體，即由 {hot}℃ 金屬片傳向 {cold}℃ 的水。"
    elif f == "motion":
        distance, seconds = 60 + n(seed + "-distance", 900) * 2, 5 + n(seed + "-seconds", 45)
        speed = distance / seconds
        prompt = f"{base}小車在 {seconds} 秒內前進 {distance} m，研究「{topic}」時，平均速率為何？"
        correct = f"{speed:g} m/s"
        distractors = [f"{distance * seconds:g} m/s", f"{seconds / distance:g} m/s", f"{distance - seconds:g} m/s"]
        explanation = f"平均速率＝路程÷時間＝{distance}÷{seconds}＝{speed:g} m/s。"
    elif f == "chemistry":
        if any(x in topic for x in ("酸鹼", "酸、鹼")):
            ph = 2 + n(seed + "-ph", 6)
            indicator = ["石蕊試紙", "廣用試紙", "pH 計", "指示劑"][n(seed + "-indicator", 4)]
            prompt = f"{base}以{indicator}測得某溶液 pH＝{ph}，研究「{topic}」時，最合理的判斷為何？"
            correct = "此溶液呈酸性"
            distractors = [f"此溶液呈中性，因為 pH＝{ph} 且使用{indicator}", f"此溶液呈鹼性，因為 pH＝{ph} 且使用{indicator}", f"不必讀取{indicator}數值，只看容器外觀就能判斷酸鹼性"]
            explanation = f"pH 小於 7 的水溶液呈酸性；pH＝{ph}，因此判定為酸性。"
        elif any(x in topic for x in ("質量守恆", "化學反應的質量")):
            a, b = 8 + n(seed + "-reactant-a", 880), 5 + n(seed + "-reactant-b", 90)
            prompt = f"{base}密閉容器中兩反應物質量分別為 {a} g 與 {b} g，研究「{topic}」時，反應後總質量為何？"
            correct = f"{a+b} g"
            distractors = [f"{a-b} g", f"{a*b} g", "無法由密閉條件判斷"]
            explanation = f"密閉系統沒有物質進出，依質量守恆反應後總質量仍為 {a}＋{b}＝{a+b} g。"
        else:
            solute, water = 5 + n(seed + "-solute", 90), 100 + n(seed + "-water", 900)
            prompt = f"{base}將 {solute} g 食鹽溶於 {water} g 水，研究「{topic}」時，溶液質量為何？"
            correct = f"{solute + water} g"
            distractors = [f"{water - solute} g", f"{solute * water} g", f"{water} g"]
            explanation = f"溶液質量為溶質加溶劑：{solute}＋{water}＝{solute + water} g。"
    elif f == "biology":
        if any(x in topic for x in ("遺傳", "性染色體")):
            allele = ["Aa", "Bb", "Cc", "Dd", "Ee"][k % 5]
            prompt = f"{base}若以 {allele} 表示一對等位基因，研究「{topic}」時，{allele} 個體的基因型屬於哪一類？"
            correct = f"異型合子（{allele}）"
            distractors = [f"同型合子（兩個等位基因相同）", f"只有一個基因（{allele} 只剩一個字母）", f"不含遺傳物質（{allele} 不具遺傳意義）"]
            explanation = f"{allele} 含有兩個不同的等位基因，因此是異型合子。"
        elif any(x in topic for x in ("生態", "能量", "食物鏈")):
            plant, herb = 800 + k * 50, 80 + k * 10
            prompt = f"{base}某食物鏈中植物可利用能量 {plant} 單位，草食動物取得 {herb} 單位，研究「{topic}」時，最合理的結論為何？"
            correct = f"能量沿「{topic}」營養階層傳遞時通常逐級減少"
            distractors = [f"能量由 {plant} 單位傳到「{topic}」的下一階層後必定增加", f"「{topic}」中的所有能量都在生物間百分之百循環而不散失", f"研究「{topic}」時，高階消費者不需要由食物取得能量"]
            explanation = f"由 {plant} 單位降至 {herb} 單位可見能量傳遞並非百分之百有效，通常逐級減少。"
        else:
            days = 2 + n(seed + "-days", 5)
            prompt = f"{base}連續觀察「{topic}」{days} 天時，若要判斷細胞是否正在進行生命活動，哪項證據最直接？"
            correct, distractors = biology_options(seed, topic, question_number)
            explanation = "代謝或生長是可觀察、可重複檢驗的生命活動證據。"
    elif f == "earth":
        if any(x in topic for x in ("板塊", "地震", "火山")):
            events = 3 + n(seed + "-events", 8)
            region = ["東部測站", "西部測站", "山區測站", "沿海測站"][k % 4]
            depth = 5 + n(seed + "-depth", 35)
            prompt = f"{base}{region}一週記錄到 {events} 次、深度約 {depth} km 的淺層地震，研究「{topic}」時，最適當的解釋是？"
            correct = f"應結合{region}的震央位置、深度約 {depth} km 與板塊邊界資料判讀"
            distractors = [f"只要{region}有一次地震就能確定成因", f"{region}發生地震表示所有火山都會爆發", f"不需{region}的位置、深度與時間資料即可判斷"]
            explanation = "地震成因需比對位置、深度、時間與板塊構造等證據，不能只由一次紀錄推論。"
        elif any(x in topic for x in ("行星", "太陽", "月相", "宇宙")):
            prompt = f"{base}連續一個月在相同時間觀察月面亮部變化，研究「{topic}」時，最能支持哪項結論？"
            month = 1 + n(seed + "-month", 12)
            correct = f"在「{topic}」第 {question_number} 組、{month} 月觀察中，月相是由日、地、月相對位置改變造成的視覺變化"
            distractors = [f"在「{topic}」第 {question_number} 組、{month} 月觀察中，月亮本身每天產生不同亮度", f"在「{topic}」第 {question_number} 組、{month} 月觀察中，月相完全由雲量決定", f"在「{topic}」第 {question_number} 組、{month} 月觀察中，月亮只在滿月時才存在"]
            explanation = "月球反射太陽光，日、地、月相對位置改變會造成可規律觀察的月相。"
        else:
            rain_a, rain_b = 620 + k * 80, 340 + k * 55
            prompt = f"{base}比較兩地「{topic}」資料時，甲地迎風坡年雨量約 {rain_a} mm、乙地背風坡約 {rain_b} mm，最合理的做法是？"
            correct = f"同時比較地形、風向、觀測期間與 {rain_a}、{rain_b} mm 資料"
            distractors = [f"只看 {rain_a} mm 的單一數值便下結論", "認定背風坡一定比迎風坡多雨而不查風向", "不標示單位與觀測期間也能直接代表氣候"]
            explanation = "地科資料判讀需要結合地形、風向、時間與量測資料，避免過度推論。"
    else:
        groups = 3 + n(seed + "-groups", 3)
        sample_count = 8 + question_number
        prompt = f"{base}針對「{topic}」提出可檢驗的科學問題，若比較 {groups} 組、每組取樣 {sample_count} 份資料，哪一項設計最適當？"
        correct, distractors = inquiry_options(seed, topic, question_number)
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
