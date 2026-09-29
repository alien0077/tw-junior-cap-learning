#!/usr/bin/env python3
"""Detect obvious science-question archetype/unit mismatches.

This is a conservative triage audit. It reports only clear lexical domain
conflicts; a clean report is not a substitute for subject review.
"""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ARCHETYPES = {
    "mass": ("溶液質量為何", ("質量", "溶液", "水溶液", "物質", "組成", "混合", "分離", "化學", "原子", "元素")),
    "cell": ("細胞是否正在進行生命活動", ("細胞", "生物", "生態", "遺傳", "演化", "植物", "動物", "生命", "微生物", "人體", "生殖", "免疫", "神經", "恆定", "多樣性", "保育", "環境")),
    "rain": ("迎風坡年雨量", ("大氣", "氣候", "天氣", "地球", "海流", "風", "變遷", "季節", "水圈")),
    "speed": ("平均速率為何", ("運動", "速度", "力", "能量", "功率", "機械", "重力", "加速度")),
    "reflection": ("反射角為何", ("光", "聲音", "波", "介質", "反射")),
    "heat": ("最初的熱傳方向", ("熱", "溫度", "能量", "熱量")),
    "density": ("其密度為何", ("密度", "質量", "浮力", "壓力", "液體", "物質")),
    "genetics": ("基因型屬於哪一類", ("遺傳", "基因", "染色體", "血型", "生殖", "孟德爾")),
    "ph": ("pH＝", ("酸", "鹼", "鹽", "pH", "溶液", "化學")),
    "earthquake": ("淺層地震", ("板塊", "地震", "火山", "地質", "地球", "造山")),
}


def load_titles():
    result = {}
    for path in (ROOT / "lessons" / "science").glob("*.json"):
        try:
            data = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        result[data.get("id")] = data.get("title", "")
    return result


def main():
    titles = load_titles()
    mismatches = []
    archetype_counts = Counter()
    for path in sorted((ROOT / "questions" / "science").glob("*.json")):
        try:
            item = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        title = titles.get(item.get("lessonId"), "")
        prompt = item.get("prompt", "")
        for archetype, (needle, allowed) in ARCHETYPES.items():
            if needle in prompt:
                archetype_counts[archetype] += 1
                if not any(token in title for token in allowed):
                    mismatches.append({
                        "path": str(path.relative_to(ROOT)),
                        "lessonId": item.get("lessonId"),
                        "title": title,
                        "archetype": archetype,
                        "prompt": prompt,
                    })
                break
    out = {
        "status": "pass" if not mismatches else "mismatch-found",
        "scienceQuestionCount": sum(1 for _ in (ROOT / "questions" / "science").glob("*.json")),
        "archetypeCounts": dict(archetype_counts),
        "mismatchCount": len(mismatches),
        "mismatches": mismatches,
        "note": "Conservative lexical triage only; positive or clean results do not replace subject content review.",
    }
    report = ROOT / "implementation" / "reports" / "question-unit-fit.json"
    report.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: out[k] for k in ("status", "scienceQuestionCount", "archetypeCounts", "mismatchCount")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
