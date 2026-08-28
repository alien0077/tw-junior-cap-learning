#!/usr/bin/env python3
"""Author social-studies draft items from their KG topic and source direction."""
from __future__ import annotations
import hashlib, json
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-08-29"

def n(seed: str, mod: int, offset: int = 0) -> int:
    return int(hashlib.sha256(seed.encode("utf-8")).hexdigest()[:12], 16) % mod + offset

def rotate(correct: str, wrong: list[str], seed: str):
    values = [correct] + wrong
    pos = n(seed + "-answer", 4)
    values.insert(pos, values.pop(0))
    return [{"id": chr(65+i), "text": x} for i, x in enumerate(values)], chr(65+pos)

def ctx(seed: str) -> str:
    places = ["地方文史館", "社區資料中心", "校園公民論壇", "地方政府公開資料", "區域地圖展"]
    d = date(2021, 1, 1) + timedelta(days=n(seed + "-date", 1500))
    return f"在{d.year}年{d.month}月{d.day}日{places[n(seed + '-place', len(places))]}的資料中，"

def kind(topic: str) -> str:
    if any(x in topic for x in ("地 ", "地理", "人口", "氣候", "地形", "產業", "區域", "地圖", "環境", "資源", "都市")):
        return "geo"
    if any(x in topic for x in ("歷 ", "歷史", "文化", "朝", "帝國", "戰爭", "政治", "殖民", "文明", "臺灣")):
        return "hist"
    if any(x in topic for x in ("公 ", "公民", "權利", "法律", "民主", "政府", "市場", "經濟", "社會")):
        return "civ"
    return "inquiry"

def rewrite(data: dict, topic: str) -> None:
    seed = data["id"]
    base, k = ctx(seed), n(seed + "-case", 5)
    f = kind(topic)
    if f == "geo":
        if any(x in topic for x in ("人口", "都市", "區域")):
            p1, a1, p2, a2 = 12 + k, 300 + k * 20, 10 + k, 150 + k * 10
            d1, d2 = p1 * 10000 / a1, p2 * 10000 / a2
            correct = ("乙區人口密度較高" if d2 > d1 else "甲區人口密度較高") + f"（依「{topic}」資料計算）"
            prompt = f"{base}甲區人口 {p1} 萬、面積 {a1} km²；乙區人口 {p2} 萬、面積 {a2} km²。研究「{topic}」時，哪項正確？"
            wrong = ["兩區人口密度相同", "只看人口總數即可判斷密度", "面積越大人口密度必然越高"]
            explanation = f"人口密度須以人口除以面積比較；甲約 {d1:.0f} 人/km²、乙約 {d2:.0f} 人/km²。"
        elif any(x in topic for x in ("地圖", "比例尺", "距離")):
            scale, cm = 10 + k * 5, 2 + k
            prompt = f"{base}地圖比例尺為 1 公分代表 {scale} 公里，甲乙兩地圖上相距 {cm} 公分。研究「{topic}」時，實際距離約為何？"
            correct = f"{scale * cm} 公里"
            wrong = [f"{scale + cm} 公里", f"{scale * (cm-1)} 公里", f"{cm} 公里"]
            explanation = f"實際距離＝圖上距離×每公分代表距離＝{cm}×{scale}＝{scale*cm} 公里。"
        else:
            rain1, rain2 = 900 + k * 120, 500 + k * 40
            prompt = f"{base}甲地年雨量約 {rain1} mm 且位於迎風坡，乙地約 {rain2} mm 且位於背風坡。研究「{topic}」時，哪項判讀較合理？"
            correct = f"在「{topic}」的資料中，地形與盛行風向可能共同造成兩地降雨差異"
            wrong = ["雨量差異必然只由緯度造成", "背風坡一定比迎風坡多雨", "單日雨量即可代表全年氣候"]
            explanation = "迎風坡抬升氣流可能增加降雨，背風坡可能較乾；仍須結合長期資料判斷。"
    elif f == "hist":
        if n(seed + "-mode", 2) == 0:
            y1, y2, y3 = 1700 + k * 20, 1750 + k * 20, 1800 + k * 20
            prompt = f"{base}研究「{topic}」時有三筆史料，年代分別為 {y2}、{y1}、{y3} 年。哪項最適合建立時間線？"
            correct = f"依 {y1}、{y2}、{y3} 的年代順序排列並標明史料來源，以判讀「{topic}」時序"
            wrong = ["依史料篇幅長短排列", "依人物知名度排列", "先決定結論再安排年代"]
            explanation = "時間線應依可核對的年代排序，並保留史料來源以便檢驗。"
        else:
            prompt = f"{base}比較「{topic}」的當時公告與後世回憶時，若兩者說法不同，第一步應如何處理？"
            correct = f"先確認作者、形成時間、資料目的，再比較「{topic}」的內容與限制"
            wrong = ["直接以年代較晚的回憶取代公告", "只看文字較長者判定真偽", "把所有後世解釋當成當時原文"]
            explanation = "史料解讀須辨識作者、時代、目的與資料性質，不能只依篇幅或年代早晚判斷。"
    elif f == "civ":
        if any(x in topic for x in ("權", "法律", "民主", "政府")):
            prompt = f"{base}針對「{topic}」的公共政策，若限制人民權利，哪項程序最符合權利保障？"
            correct = f"針對「{topic}」具法律依據、目的正當且符合必要與比例原則，並提供救濟途徑"
            wrong = ["只要多數人支持就可無限期限制", "政策名稱簡短即可不必說明依據", "只公布支持意見而不提供申訴方式"]
            explanation = "權利限制須有法律依據，並符合必要、比例及可救濟等法治要求。"
        else:
            budget = 80 + k * 20
            prompt = f"{base}社區有 {budget} 萬元預算處理「{topic}」，居民意見不同。哪項決策方式較適當？"
            correct = f"公開「{topic}」方案、成本與受影響對象，蒐集意見後依規則決定"
            wrong = ["只採納聲量最大者且不公開資料", "先決定結果再挑選支持數據", "排除少數受影響居民以加快決定"]
            explanation = "公共決策應資訊公開、納入受影響者並說明規則與取捨。"
    else:
        prompt = f"{base}小組探究「{topic}」時，甲資料與乙資料出現差異。哪項做法最能支持可靠結論？"
        correct = f"核對「{topic}」的來源、時間、範圍與概念定義，再說明證據限制"
        wrong = ["刪除與原結論不合的資料", "只引用一筆最方便的資料", "把個人感受直接寫成普遍結論"]
        explanation = "社會科資料判讀需確認來源、時空範圍與定義，並區分證據和推論。"
    options, answer = rotate(correct, wrong, seed)
    data.update({"prompt": prompt, "options": options, "answer": {"value": answer, "explanation": f"{explanation} 本題對應 KG「{topic}」。"}, "reviewStatus": "draft", "updatedAt": TODAY})

def main() -> None:
    labels = {x["id"]: x.get("label", x["id"]) for x in json.loads((ROOT / "knowledge/social/foundational-graph.json").read_text(encoding="utf-8"))["nodes"]}
    count = 0
    for path in sorted((ROOT / "questions/social").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("reviewStatus") != "draft":
            continue
        rewrite(data, labels.get(data["knowledgeIds"][0], data["knowledgeIds"][0]))
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        count += 1
    print(f"rewrote social draft questions by KG family: {count}")

if __name__ == "__main__":
    main()
