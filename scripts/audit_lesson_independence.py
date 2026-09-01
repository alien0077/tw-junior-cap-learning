#!/usr/bin/env python3
"""Audit whether lesson teaching paragraphs are unit-specific rather than renamed templates."""
import argparse
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNIT_RE = re.compile(r"「[^」]+」|『[^』]+』")


def normalized(text):
    text = UNIT_RE.sub("〈UNIT〉", text or "")
    text = re.sub(r"\b(?:A|B|C|D|F|G|N|S|D|Fa|Jd|Me|INc|Ga|Bb|Ae|Ob|Cd|Be|Bc|Ca)-?Ⅳ?-?\d+(?:-\d+)?\b", "〈CODE〉", text)
    return re.sub(r"\s+", " ", text).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="fail any learning-content lesson with repeated teaching paragraphs")
    args = parser.parse_args()
    groups = collections.defaultdict(list)
    lessons = []
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("lessonScope") != "learning-content":
            continue
        body = data.get("teaching", {}).get("body", [])
        lessons.append((path, data))
        for index, paragraph in enumerate(body):
            signature = normalized(paragraph.get("body", ""))
            if signature:
                groups[(index, signature)].append(path)
    risks = []
    for (index, signature), paths in groups.items():
        if len(paths) >= 2:
            # Keep every affected lesson: strict mode is a full-course gate,
            # so truncating this list would silently undercount failures.
            risks.append({"index": index, "count": len(paths), "signature": signature, "paths": [str(p.relative_to(ROOT)) for p in paths]})
    risks.sort(key=lambda item: (-item["count"], item["index"]))
    strict_failures = []
    if args.strict:
        for path, data in lessons:
            # Every active learning-content lesson is subject to the same gate.
            if any(str(path.relative_to(ROOT)) in risk["paths"] for risk in risks):
                strict_failures.append(str(path.relative_to(ROOT)))
    report = [
        "# Lesson Independence Audit",
        "",
        "本報告檢查去除單元名稱後的教學段落是否跨課重複；任兩個 learning-content lesson 命中即為重寫阻擋，不代表內容已自動判定錯誤。",
        "",
        f"- learning-content lessons: {len(lessons)}",
        f"- repeated paragraph signatures (2 or more lessons): {len(risks)}",
        f"- affected lesson references: {sum(r['count'] for r in risks)}",
        "",
        "| 段落索引 | 課程數 | 正規化段落前 160 字 |",
        "|---:|---:|---|",
    ]
    for risk in risks[:100]:
        report.append(f"| {risk['index']} | {risk['count']} | {risk['signature'][:160].replace('|', '／')} |")
    (ROOT / "docs/LESSON_INDEPENDENCE_AUDIT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps({"lessonCount": len(lessons), "riskCount": len(risks), "affectedReferences": sum(r["count"] for r in risks), "strictFailures": len(strict_failures)}, ensure_ascii=False, indent=2))
    if args.strict and strict_failures:
        print("\n".join(strict_failures[:20]))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
