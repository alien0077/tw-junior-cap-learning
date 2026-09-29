#!/usr/bin/env python3
"""保守重算簡單一次方程與一次函數題。

只接受可由正規式唯一解析的線性式；括號、圖形、幾何與語境題全部 skipped。
"""

from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def norm(s: str) -> str:
    return (s.replace("－", "-").replace("−", "-").replace("＋", "+")
            .replace("＝", "=").replace("×", "*").replace(" ", ""))


def linear(expr: str) -> tuple[Fraction, Fraction] | None:
    expr = norm(expr)
    if not expr or "(" in expr or ")" in expr or "/" in expr or "*" in expr:
        return None
    expr = expr.replace("-", "+-")
    if expr.startswith("+"):
        expr = expr[1:]
    terms = [x for x in expr.split("+") if x]
    a = Fraction(0); b = Fraction(0)
    for term in terms:
        if "x" in term:
            if term.count("x") != 1 or not term.endswith("x"):
                return None
            coefficient = term[:-1]
            if coefficient in ("", "+"):
                coefficient = "1"
            elif coefficient == "-":
                coefficient = "-1"
            try: a += Fraction(coefficient)
            except ValueError: return None
        else:
            try: b += Fraction(term)
            except ValueError: return None
    return a, b


def value(text: str) -> Fraction | None:
    text = norm(text).replace("x", "")
    text = text.strip().rstrip("。．")
    text = re.sub(r"^(?:x|y)\s*", "", text)
    m = re.fullmatch(r"(-?\d+)(?:/(\d+))?", text)
    if not m: return None
    return Fraction(int(m.group(1)), int(m.group(2) or 1))


def option_value(text: str, variable: str = "x") -> Fraction | None:
    text = norm(text)
    m = re.search(rf"{variable}\s*=?\s*(-?\d+(?:/\d+)?)", text)
    return value(m.group(1)) if m else value(text)


def option_for(item: dict, expected: Fraction, variable: str = "x") -> str | None:
    for option in item.get("options", []):
        if option_value(option.get("text", ""), variable) == expected:
            return option.get("id")
    return None


def equation_expected(prompt: str) -> Fraction | None:
    p = norm(prompt)
    if "²" in p or "^2" in p or "根號" in p or "/" in p or "（" in p or "(" in p:
        return None
    if not ("解方程式" in p or "方程式" in p and "解" in p): return None
    m = re.search(r"([0-9.x+\-]+)=([0-9.x+\-]+)", p)
    if not m: return None
    left = linear(m.group(1)); right = linear(m.group(2))
    if left is None or right is None or left[0] == right[0]: return None
    return (right[1] - left[1]) / (left[0] - right[0])


def function_expected(prompt: str, kind: str) -> Fraction | None:
    p = norm(prompt)
    m = re.search(r"y=([+-]?\d*)x([+-]\d+)?", p)
    if not m: return None
    a = Fraction(m.group(1) or ("-1" if m.group(1) == "-" else "1"))
    b = Fraction(m.group(2) or 0)
    if kind == "slope": return a
    if kind == "intercept": return b
    return None


def main() -> int:
    checked = 0; skipped = 0; failures = []
    for path in sorted((ROOT / "questions" / "math").glob("*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        prompt = item.get("prompt", "")
        expected = equation_expected(prompt)
        kind = "equation"
        if expected is None and "斜率" in prompt and "直線" in prompt:
            expected = function_expected(prompt, "slope"); kind = "slope"
        if expected is None and "y截距" in norm(prompt):
            expected = function_expected(prompt, "intercept"); kind = "intercept"
        if expected is None:
            skipped += 1; continue
        answer = item.get("answer", {}).get("value")
        chosen = option_for(item, expected, "x" if kind == "equation" else "")
        checked += 1
        if chosen != answer:
            failures.append({"file": str(path.relative_to(ROOT)), "prompt": prompt, "kind": kind, "expected": str(expected), "answer": answer, "matchingOption": chosen})
    report = {"status": "pass" if not failures else "fail", "checked": checked, "skipped": skipped, "failureCount": len(failures), "failures": failures, "scope": "unambiguous linear equations and y=mx+b slope/intercept only"}
    out = ROOT / "implementation" / "reports" / "math-linear-numeric-audit.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "checked", "skipped", "failureCount")}, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
