#!/usr/bin/env python3
"""保守重算題幹可直接解析的二次方程與判別式題。

只納入含 x²、整數係數、等號兩側可正規化的題目；含括號、分數、圖形
或無法唯一抽出根的選項全部 skipped，不把 skipped 當成通過。
"""

from __future__ import annotations

import json
import re
from fractions import Fraction
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def norm(text: str) -> str:
    return (text.replace("－", "-").replace("−", "-").replace("＋", "+")
            .replace("＝", "=").replace("×", "*").replace(" ", ""))


def polynomial(expr: str) -> tuple[Fraction, Fraction, Fraction] | None:
    expr = norm(expr).replace("^2", "²")
    if not expr or any(x in expr for x in ("(", ")", "/", "*")):
        return None
    expr = expr.replace("-", "+-")
    if expr.startswith("+"):
        expr = expr[1:]
    a = Fraction(0); b = Fraction(0); c = Fraction(0)
    for term in (part for part in expr.split("+") if part):
        if "²" in term:
            if term.count("²") != 1 or not term.endswith("²"):
                return None
            if not term.endswith("x²"):
                return None
            coefficient = term[:-2] or "1"
            if coefficient == "-": coefficient = "-1"
            try: a += Fraction(coefficient)
            except ValueError: return None
        elif "x" in term:
            if term.count("x") != 1 or not term.endswith("x"):
                return None
            coefficient = term[:-1] or "1"
            if coefficient == "-": coefficient = "-1"
            try: b += Fraction(coefficient)
            except ValueError: return None
        else:
            try: c += Fraction(term)
            except ValueError: return None
    return a, b, c


def equation_coefficients(prompt: str) -> tuple[Fraction, Fraction, Fraction] | None:
    p = norm(prompt).replace("^2", "²")
    if "方程式" not in p or "²" not in p or "=" not in p or any(x in p for x in ("(", ")", "/", "根號")):
        return None
    match = re.search(r"([0-9x²+\-]+)=([0-9x²+\-]+)", p)
    if not match:
        return None
    left = polynomial(match.group(1)); right = polynomial(match.group(2))
    if left is None or right is None:
        return None
    result = tuple(left[i] - right[i] for i in range(3))
    if result[0] == 0:
        return None
    return result


def rational_roots(coefficients: tuple[Fraction, Fraction, Fraction]) -> set[Fraction] | None:
    a, b, c = coefficients
    if any(value.denominator != 1 for value in coefficients):
        return None
    ai, bi, ci = int(a), int(b), int(c)
    discriminant = bi * bi - 4 * ai * ci
    if discriminant < 0:
        return set()
    root = isqrt(discriminant)
    if root * root != discriminant:
        return None
    denominator = 2 * ai
    return {Fraction(-bi + root, denominator), Fraction(-bi - root, denominator)}


def count_expected(coefficients: tuple[Fraction, Fraction, Fraction]) -> int | None:
    a, b, c = coefficients
    if any(value.denominator != 1 for value in coefficients):
        return None
    discriminant = int(b) * int(b) - 4 * int(a) * int(c)
    return 0 if discriminant < 0 else 1 if discriminant == 0 else 2


def option_count(text: str) -> int | None:
    p = norm(text)
    if "無限" in p: return None
    match = re.search(r"(\d+)個", p)
    if match: return int(match.group(1))
    if "沒有實數解" in p or "無實數解" in p: return 0
    if "一個實數解" in p: return 1
    if "兩個相異實數解" in p or "兩個實數解" in p: return 2
    return None


def option_roots(text: str) -> set[Fraction] | None:
    p = norm(text)
    if "√" in p or "根號" in p:
        return None
    marker = re.search(r"x=", p)
    candidate = p[marker.end():] if marker else p
    candidate = re.split(r"[（(]", candidate, maxsplit=1)[0]
    values = re.findall(r"-?\d+(?:/\d+)?", candidate)
    if not values:
        return None
    return {Fraction(value) for value in values}


def option_value(text: str) -> Fraction | None:
    p = norm(text)
    if not re.fullmatch(r"-?\d+(?:/\d+)?", p):
        return None
    return Fraction(p)


def main() -> int:
    checked = 0; skipped = 0; failures = []
    for path in sorted((ROOT / "questions" / "math").glob("*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        prompt = item.get("prompt", "")
        coefficients = equation_coefficients(prompt)
        if coefficients is None:
            skipped += 1; continue
        roots = rational_roots(coefficients)
        normalized_prompt = norm(prompt)
        if "判別式" in normalized_prompt or "相差" in normalized_prompt:
            skipped += 1; continue
        if "正數解" in normalized_prompt and roots is not None:
            roots = {root for root in roots if root > 0}
        is_count_question = "幾個實數解" in norm(prompt)
        answer = item.get("answer", {}).get("value")
        matching = None
        if is_count_question:
            expected_count = count_expected(coefficients)
            if expected_count is None:
                skipped += 1; continue
            for option in item.get("options", []):
                if option_count(option.get("text", "")) == expected_count:
                    matching = option.get("id")
                    break
            checked += 1
            if matching != answer:
                failures.append({"file": str(path.relative_to(ROOT)), "prompt": prompt,
                                 "expectedCount": expected_count, "answer": answer,
                                 "matchingOption": matching})
        elif roots is not None and roots:
            for option in item.get("options", []):
                parsed = option_roots(option.get("text", ""))
                if parsed == roots or ("哪一個數" in normalized_prompt and parsed is not None
                                       and len(parsed) == 1 and parsed.issubset(roots)):
                    matching = option.get("id")
                    break
            checked += 1
            if matching != answer:
                failures.append({"file": str(path.relative_to(ROOT)), "prompt": prompt,
                                 "expectedRoots": sorted(str(x) for x in roots),
                                 "answer": answer, "matchingOption": matching})
        else:
            skipped += 1
    report = {"status": "pass" if not failures else "fail", "checked": checked,
              "skipped": skipped, "failureCount": len(failures), "failures": failures,
              "scope": "integer-coefficient quadratic equations with directly countable or rational roots"}
    out = ROOT / "implementation" / "reports" / "math-quadratic-numeric-audit.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "checked", "skipped", "failureCount")}, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
