#!/usr/bin/env python3
"""Recalculate conservative numeric science question families."""
import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def option_text(item):
    aid = item.get("answer", {}).get("value")
    return next((o.get("text", "") for o in item.get("options", []) if o.get("id") == aid), "")


def number(text):
    m = re.search(r"[-+]?\d+(?:\.\d+)?", text.replace(",", ""))
    return Fraction(m.group(0)) if m else None


def main():
    checked = 0
    failures = []
    for path in sorted((ROOT / "questions" / "science").glob("*.json")):
        item = json.loads(path.read_text())
        prompt = item.get("prompt", "")
        expected = None
        kind = None
        m = re.search(r"將\s*(\d+(?:\.\d+)?)\s*g\s*食鹽溶於\s*(\d+(?:\.\d+)?)\s*g\s*水.*溶液質量", prompt)
        if m:
            expected, kind = Fraction(m.group(1)) + Fraction(m.group(2)), "mass"
        m = re.search(r"物體質量為\s*(\d+(?:\.\d+)?)\s*g、體積為\s*(\d+(?:\.\d+)?)\s*cm³.*密度", prompt)
        if m:
            expected, kind = Fraction(m.group(1)) / Fraction(m.group(2)), "density"
        m = re.search(r"小車在\s*(\d+(?:\.\d+)?)\s*秒內前進\s*(\d+(?:\.\d+)?)\s*m.*平均速率", prompt)
        if m:
            expected, kind = Fraction(m.group(2)) / Fraction(m.group(1)), "speed"
        m = re.search(r"入射角為\s*(\d+(?:\.\d+)?)°.*反射角", prompt)
        if m:
            expected, kind = Fraction(m.group(1)), "reflection"
        if expected is None:
            continue
        checked += 1
        chosen = option_text(item)
        got = number(chosen)
        # Density and speed options may be rounded; compare exact when possible,
        # otherwise accept a stated decimal within 0.01 of the exact value.
        ok = got == expected
        if not ok and got is not None:
            ok = abs(float(got - expected)) <= 0.01
        if not ok:
            failures.append({"path": str(path.relative_to(ROOT)), "kind": kind, "prompt": prompt, "expected": str(expected), "answer": item.get("answer", {}).get("value"), "chosenOption": chosen})
    out = {"status": "pass" if not failures else "mismatch-found", "checked": checked, "failureCount": len(failures), "failures": failures, "note": "Only direct numeric families are evaluated; conceptual and unit-specific science correctness remains a separate gate."}
    (ROOT / "implementation" / "reports" / "direct-science-answer-audit.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: out[k] for k in ("status", "checked", "failureCount")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
