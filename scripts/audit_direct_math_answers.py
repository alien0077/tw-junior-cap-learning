#!/usr/bin/env python3
"""Conservative re-calculation audit for direct arithmetic math questions."""
import ast
import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def eval_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return Fraction(str(node.value))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        value = eval_node(node.operand)
        return -value if isinstance(node.op, ast.USub) else value
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)):
        left, right = eval_node(node.left), eval_node(node.right)
        if isinstance(node.op, ast.Add): return left + right
        if isinstance(node.op, ast.Sub): return left - right
        if isinstance(node.op, ast.Mult): return left * right
        if isinstance(node.op, ast.Div): return left / right
        if right.denominator != 1 or abs(right.numerator) > 12:
            raise ValueError("unsupported exponent")
        return left ** right.numerator
    raise ValueError("unsupported expression")


def normalize_expr(text):
    text = text.translate(str.maketrans({"＋": "+", "－": "-", "−": "-", "×": "*", "÷": "/", "﹣": "-"}))
    text = re.sub(r"\(([-+]?\d+)\)\s*\^?([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", lambda m: f"({m.group(1)})**{m.group(2).translate(str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹','0123456789'))}", text)
    text = re.sub(r"(?<![A-Za-z])(-?\d+)[⁰¹²³⁴⁵⁶⁷⁸⁹]+", lambda m: m.group(0), text)
    text = text.replace("^", "**")
    return text


def parse_value(text):
    text = text.strip().replace("－", "-").replace("−", "-").replace("＋", "+")
    text = re.sub(r"\s*(公分|平方公分|公尺|公升|克|秒|公里|公尺)$", "", text)
    text = text.replace("／", "/")
    if re.fullmatch(r"[-+]?\d+(?:\.\d+)?", text):
        return Fraction(text)
    if re.fullmatch(r"[-+]?\d+\s*/\s*[-+]?\d+", text):
        a, b = re.split(r"\s*/\s*", text); return Fraction(int(a), int(b))
    return None


def main():
    checked, failures, skipped = 0, [], 0
    for path in sorted((ROOT / "questions" / "math").glob("*.json")):
        item = json.loads(path.read_text())
        prompt = item.get("prompt", "")
        match = re.search(r"(?:計算\s+)(.+?)(?:的值為何|的結果為何|，結果為何|的值。)", prompt)
        if not match or re.search(r"[A-Za-z√]|\d+\s*公尺|\d+\s*公分", match.group(1)):
            skipped += 1
            continue
        expr = normalize_expr(match.group(1).strip())
        try:
            value = eval_node(ast.parse(expr, mode="eval").body)
        except Exception:
            skipped += 1
            continue
        checked += 1
        answer_id = item.get("answer", {}).get("value")
        chosen = next((o.get("text", "") for o in item.get("options", []) if o.get("id") == answer_id), "")
        parsed = parse_value(chosen)
        if parsed != value:
            failures.append({"path": str(path.relative_to(ROOT)), "prompt": prompt, "expected": str(value), "answer": answer_id, "chosenOption": chosen})
    out = {"status": "pass" if not failures else "mismatch-found", "checked": checked, "skipped": skipped, "failureCount": len(failures), "failures": failures, "note": "Only direct arithmetic strings are evaluated; formula, geometry, units and subject correctness remain separate reviews."}
    (ROOT / "implementation" / "reports" / "direct-math-answer-audit.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: out[k] for k in ("status", "checked", "skipped", "failureCount")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
