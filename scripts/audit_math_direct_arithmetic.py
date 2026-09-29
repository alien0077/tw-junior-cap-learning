#!/usr/bin/env python3
"""保守重算沒有變數或圖形語意的數學直接算式題。

只接受題幹以「計算」開頭、且算式僅含數字、括號、四則運算與小數；
任何含變數、根號、圓周率、單位轉換或不完整語境的題目都列為 skipped，
不把 skipped 當成通過。
"""

from __future__ import annotations

import ast
import glob
import json
import operator
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_GLOB = str(ROOT / "questions" / "math" / "*.json")
ALLOWED_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def normalize(text: str) -> str:
    return (
        text.replace("－", "-")
        .replace("−", "-")
        .replace("＋", "+")
        .replace("×", "*")
        .replace("÷", "/")
        .replace("（", "(")
        .replace("）", ")")
        .replace("．", ".")
        .replace("。", ".")
        .replace(" ", "")
    )


def safe_eval(expression: str) -> float | None:
    if not re.fullmatch(r"[0-9.+\-*/()]+", expression):
        return None
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError:
        return None

    def visit(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = visit(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_BINOPS:
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Div) and right == 0:
                raise ZeroDivisionError
            return float(ALLOWED_BINOPS[type(node.op)](left, right))
        raise ValueError("unsupported expression")

    try:
        return visit(tree)
    except (ValueError, ZeroDivisionError, OverflowError):
        return None


def numeric_option(text: str) -> float | None:
    value = normalize(text)
    value = value.replace(",", "")
    fraction = re.fullmatch(r"(-?\d+)/(\d+)", value)
    if fraction and int(fraction.group(2)) != 0:
        return int(fraction.group(1)) / int(fraction.group(2))
    match = re.fullmatch(r"(-?(?:\d+(?:\.\d+)?|\.\d+))(?:公分|公尺|元|人|本|公斤|毫米|度|°|%)?", value)
    return float(match.group(1)) if match else None


def extract_expression(prompt: str) -> str | None:
    normalized = normalize(prompt)
    if not normalized.startswith("計算"):
        return None
    match = re.match(r"計算(.+?)(?:的值為何|結果為何|是多少|為何)[？?]?$", normalized)
    if not match:
        return None
    expression = match.group(1)
    return expression if re.fullmatch(r"[0-9.+\-*/()]+", expression) else None


def main() -> int:
    checked = []
    skipped = []
    failures = []
    for path_text in glob.glob(QUESTION_GLOB):
        path = Path(path_text)
        data = json.loads(path.read_text(encoding="utf-8"))
        expression = extract_expression(data.get("prompt", ""))
        if expression is None:
            skipped.append(path.name)
            continue
        expected = safe_eval(expression)
        option_values = {item["id"]: numeric_option(item["text"]) for item in data.get("options", [])}
        answer = data.get("answer", {}).get("value")
        actual = option_values.get(answer)
        item = {"file": str(path.relative_to(ROOT)), "expression": expression, "expected": expected, "answer": answer, "optionValue": actual}
        checked.append(item)
        if expected is None or actual is None or abs(expected - actual) > 1e-9:
            failures.append(item)
    report = {
        "status": "pass" if not failures else "fail",
        "checked": len(checked),
        "skipped": len(skipped),
        "failureCount": len(failures),
        "failures": failures,
        "scope": "pure numeric four-operation prompts only; skipped questions require separate subject review",
    }
    output = ROOT / "implementation" / "reports" / "math-direct-arithmetic-audit.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("status", "checked", "skipped", "failureCount")}, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
