#!/usr/bin/env python3
"""Conservative answer recalculation for additional numeric math families."""
from __future__ import annotations

import json
import math
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def options(item):
    return {str(o.get("id")): str(o.get("text", "")) for o in item.get("options", [])}

def chosen(item):
    opts = options(item)
    return opts.get(str(item.get("answer", {}).get("value")), "")

def number(text: str):
    text = text.replace(",", "")
    fraction = re.search(r"([-+]?\d+)\s*[／/]\s*([-+]?\d+)", text)
    if fraction:
        return Fraction(int(fraction.group(1)), int(fraction.group(2)))
    m = re.search(r"[-+]?\d+(?:\.\d+)?", text)
    return Fraction(m.group(0)) if m else None

def ratio(text: str):
    nums = re.findall(r"[-+]?\d+(?:\.\d+)?", text.replace("／", "/"))
    return tuple(Fraction(x) for x in nums[:2]) if len(nums) >= 2 else None

def normalized_ratio(value):
    if not value or value[0] == 0 or value[1] == 0:
        return None
    g = __import__("math").gcd(abs(value[0].numerator), abs(value[1].numerator))
    return value[0] / value[1]

def check(item):
    prompt = item.get("prompt", "")
    answer = chosen(item)
    # Similar figures: area ratio is the square of the corresponding side ratio.
    m = re.search(r"對應邊比為\s*(\d+(?:\.\d+)?)\s*[：:]\s*(\d+(?:\.\d+)?).*面積比", prompt)
    if m:
        a, b = Fraction(m.group(1)), Fraction(m.group(2))
        expected = a * a / (b * b)
        got = ratio(answer)
        if got:
            ok = normalized_ratio(got) == expected
            return "similar-area", ok, str(expected), answer
    # Circle circumference with an explicitly supplied decimal pi.
    m = re.search(r"圓周率取\s*(\d+(?:\.\d+)?).*半徑\s*(\d+(?:\.\d+)?)", prompt)
    if m and "圓周長" in prompt:
        expected = Fraction(m.group(1)) * 2 * Fraction(m.group(2))
        got = number(answer)
        if got is not None:
            return "circle-circumference", got == expected, str(expected), answer
    # Cylinder volume written as a coefficient of pi.
    m = re.search(r"圓柱半徑\s*(\d+(?:\.\d+)?)\s*公分、高\s*(\d+(?:\.\d+)?)\s*公分.*體積.*π", prompt)
    if m:
        expected = Fraction(1) * Fraction(m.group(1)) ** 2 * Fraction(m.group(2))
        got = number(answer)
        if got is not None and "π" in answer:
            return "cylinder-volume", got == expected, f"{expected}π", answer
    # Weighted mean from a frequency description.
    pairs = re.findall(r"數值\s*([-+]?\d+(?:\.\d+)?)\s*出現\s*(\d+)\s*次", prompt)
    if pairs and "平均數" in prompt:
        total = sum(Fraction(v) * int(n) for v, n in pairs)
        count = sum(int(n) for _, n in pairs)
        expected = total / count
        got = number(answer)
        if got is not None:
            return "weighted-mean", got == expected, str(expected), answer
    # Seven-day weekend probability.
    if "一週 7 天" in prompt and "週末" in prompt and "機率" in prompt:
        got = ratio(answer)
        if got:
            return "weekend-probability", normalized_ratio(got) == Fraction(2, 7), "2/7", answer
    # Geometric sequence with first, middle and third terms.
    m = re.search(r"三個正數\s*(\d+(?:\.\d+)?)、x、(\d+(?:\.\d+)?)\s*成等比", prompt)
    if m:
        product = Fraction(m.group(1)) * Fraction(m.group(2))
        got = number(answer)
        # Only compare exact integer/square-root-free cases handled by this conservative gate.
        if product.denominator == 1 and math.isqrt(product.numerator) ** 2 == product.numerator and got is not None:
            expected = Fraction(math.isqrt(product.numerator))
            return "geometric-sequence", got == expected, str(expected), answer
    # Square diagonal for a square with a numeric side.
    m = re.search(r"正方形邊長為\s*(\d+(?:\.\d+)?)\s*公分.*對角線長", prompt)
    if m:
        side = Fraction(m.group(1))
        got = answer.replace(" ", "")
        expected = f"{side}√2" if side.denominator == 1 else ""
        if expected and "√2" in got:
            return "square-diagonal", got.startswith(expected), expected, answer
    # Discounted price.
    m = re.search(r"標價\s*(\d+(?:\.\d+)?)\s*元.*打\s*(\d+(?:\.\d+)?)折.*售價", prompt)
    if m:
        expected = Fraction(m.group(1)) * Fraction(m.group(2)) / 10
        got = number(answer)
        if got is not None:
            return "discount-price", got == expected, str(expected), answer
    # Quadratic real-root count for monic x^2+bx+c forms.
    m = re.search(r"方程式\s*x²?\s*([+-])\s*(\d+)x\s*([+-])\s*(\d+)\s*=\s*0.*幾個實數解", prompt)
    if m:
        b = int(m.group(2)) * (1 if m.group(1) == "+" else -1)
        c = int(m.group(4)) * (1 if m.group(3) == "+" else -1)
        disc = b * b - 4 * c
        expected = 2 if disc > 0 else 1 if disc == 0 else 0
        got = number(answer)
        if got is not None:
            return "quadratic-root-count", got == expected, str(expected), answer
    # Triangle and parallelogram areas with explicit numeric base/height.
    m = re.search(r"(?:三角形).*?底\s*(\d+(?:\.\d+)?).*?高\s*(\d+(?:\.\d+)?)", prompt)
    if m and "面積" in prompt:
        expected = Fraction(m.group(1)) * Fraction(m.group(2)) / 2
        got = number(answer)
        if got is not None:
            return "triangle-area", got == expected, str(expected), answer
    m = re.search(r"平行四邊形.*?(?:底為|底)\s*(\d+(?:\.\d+)?).*?(?:高為|高)\s*(\d+(?:\.\d+)?)", prompt)
    if m and "面積" in prompt:
        expected = Fraction(m.group(1)) * Fraction(m.group(2))
        got = number(answer)
        if got is not None:
            return "parallelogram-area", got == expected, str(expected), answer
    # Trapezoid area with explicit parallel sides and height.
    m = re.search(r"梯形.*?(?:上底|上底長)\s*(\d+(?:\.\d+)?).*?(?:下底|下底長)\s*(\d+(?:\.\d+)?).*?(?:高|高度)\s*(\d+(?:\.\d+)?)", prompt)
    if m and "面積" in prompt:
        expected = (Fraction(m.group(1)) + Fraction(m.group(2))) * Fraction(m.group(3)) / 2
        got = number(answer)
        if got is not None:
            return "trapezoid-area", got == expected, str(expected), answer
    # Square side recovered from a perfect-square area.
    m = re.search(r"正方形面積(?:為|是)\s*(\d+(?:\.\d+)?).*?邊長", prompt)
    if m:
        area = Fraction(m.group(1))
        if area.denominator == 1 and math.isqrt(area.numerator) ** 2 == area.numerator:
            expected = Fraction(math.isqrt(area.numerator))
            got = number(answer)
            if got is not None:
                return "square-side-from-area", got == expected, str(expected), answer
    # Rectangle perimeter with explicit length and width.
    m = re.search(r"長方形.*?長\s*(\d+(?:\.\d+)?).*?寬\s*(\d+(?:\.\d+)?).*?周長", prompt)
    if m:
        expected = 2 * (Fraction(m.group(1)) + Fraction(m.group(2)))
        got = number(answer)
        if got is not None:
            return "rectangle-perimeter", got == expected, str(expected), answer
    # Rectangular numeric area and prism/cuboid volume.
    m = re.search(r"長方形長\s*(\d+(?:\.\d+)?)\s*(?:公分)?、寬\s*(\d+(?:\.\d+)?)\s*(?:公分)?.*面積", prompt)
    if m:
        expected = Fraction(m.group(1)) * Fraction(m.group(2))
        scale = re.search(r"放大為原來的\s*(\d+(?:\.\d+)?)\s*倍", prompt)
        if scale:
            factor = Fraction(scale.group(1))
            expected = expected * factor * factor
            if "幾倍" in prompt:
                expected = factor * factor
        got = number(answer)
        if got is not None:
            return "rectangle-area", got == expected, str(expected), answer
    m = re.search(r"底面積\s*(\d+(?:\.\d+)?).*?高\s*(\d+(?:\.\d+)?).*?體積", prompt)
    if m:
        expected = Fraction(m.group(1)) * Fraction(m.group(2))
        got = number(answer)
        if got is not None:
            return "prism-volume", got == expected, str(expected), answer
    m = re.search(r"長方體長\s*(\d+(?:\.\d+)?).*?寬\s*(\d+(?:\.\d+)?).*?高\s*(\d+(?:\.\d+)?).*?體積", prompt)
    if m:
        expected = Fraction(m.group(1)) * Fraction(m.group(2)) * Fraction(m.group(3))
        got = number(answer)
        if got is not None:
            return "cuboid-volume", got == expected, str(expected), answer
    # Number-line and coordinate distances, restricted to perfect-square cases.
    m = re.search(r"數線上.*?為\s*([-+]?\d+(?:/\d+)?).*?為\s*([-+]?\d+(?:/\d+)?).*?距離", prompt)
    if m:
        def f(v):
            return Fraction(v) if "/" not in v else Fraction(*map(int, v.split("/")))
        expected = abs(f(m.group(1)) - f(m.group(2)))
        got = number(answer)
        if got is not None:
            return "number-line-distance", got == expected, str(expected), answer
    m = re.search(r"A\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\).*?B\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\).*?距離", prompt)
    if m and "Q 到" not in prompt:
        dx = int(m.group(3)) - int(m.group(1)); dy = int(m.group(4)) - int(m.group(2))
        square = dx * dx + dy * dy
        root = math.isqrt(square)
        got = number(answer)
        if root * root == square and got is not None:
            return "coordinate-distance", got == root, str(root), answer
    # Simple one-variable linear equations whose answer is numeric.
    m = re.search(r"解方程式\s*([+-]?\d+)x\s*([+-])\s*(\d+)\s*=\s*([+-]?\d+).*?x\s*為何", prompt)
    if m:
        a = int(m.group(1)); b = int(m.group(3)) * (1 if m.group(2) == "+" else -1); c = int(m.group(4))
        expected = Fraction(c - b, a)
        got = number(answer)
        if got is not None:
            return "linear-equation", got == expected, str(expected), answer
    return None

def main():
    checked = 0
    skipped = 0
    failures = []
    families = {}
    for path in sorted((ROOT / "questions" / "math").glob("*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        result = check(item)
        if result is None:
            skipped += 1
            continue
        family, ok, expected, answer = result
        checked += 1
        families[family] = families.get(family, 0) + 1
        if not ok:
            failures.append({"path": str(path.relative_to(ROOT)), "family": family, "prompt": item.get("prompt"), "expected": expected, "answer": item.get("answer", {}).get("value"), "chosenOption": answer})
    out = {"status": "pass" if not failures else "mismatch-found", "checked": checked, "skipped": skipped, "families": families, "failureCount": len(failures), "failures": failures, "note": "Conservative numeric family audit; conceptual geometry, graph interpretation and subject correctness remain separate review gates."}
    (ROOT / "implementation/reports/math-numeric-family-audit.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: out[k] for k in ("status", "checked", "skipped", "families", "failureCount")}, ensure_ascii=False))

if __name__ == "__main__":
    main()
