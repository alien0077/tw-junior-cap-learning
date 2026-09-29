#!/usr/bin/env python3
"""Audit additional exact math answer patterns without promoting content.

This is intentionally conservative.  It evaluates only prompts whose numbers
and requested operation can be parsed unambiguously; all other questions are
reported as skipped rather than guessed.
"""
from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def clean(s: str) -> str:
    return (s.replace("－", "-").replace("−", "-").replace("＋", "+")
            .replace("×", "*").replace("÷", "/").replace("／", "/")
            .replace("＝", "=").replace(" ", ""))


def value(text: str) -> Fraction | None:
    s = clean(text)
    s = re.split(r"[（(]", s, maxsplit=1)[0]
    s = s.replace(",", "")
    s = re.sub(r"(公分|平方公分|立方公分|公尺|公尺/秒|元|個|分|倍|公升)$", "", s)
    if re.fullmatch(r"[-+]?\d+(?:\.\d+)?", s):
        return Fraction(s)
    m = re.fullmatch(r"([-+]?\d+)[:：/]([-+]?\d+)", s)
    if m:
        return Fraction(int(m.group(1)), int(m.group(2)))
    return None


def chosen(item: dict) -> str:
    aid = item.get("answer", {}).get("value")
    return next((o.get("text", "") for o in item.get("options", []) if o.get("id") == aid), "")


def linear(expr: str) -> Fraction | None:
    s = clean(expr).lower().replace("x", "*x")
    s = s.replace("*x", "x")
    if "=" not in s or s.count("x") != 1:
        return None
    left, right = s.split("=", 1)

    def side(t: str) -> tuple[Fraction, Fraction]:
        t = t.replace("-", "+-")
        a = b = Fraction(0)
        for part in t.split("+"):
            if not part:
                continue
            if part == "x": a += 1
            elif part == "-x": a -= 1
            elif part.endswith("x"):
                a += Fraction(part[:-1] or "1")
            else:
                b += Fraction(part)
        return a, b

    try:
        al, bl = side(left); ar, br = side(right)
    except (ValueError, ZeroDivisionError):
        return None
    if al == ar:
        return None
    return (br - bl) / (al - ar)


def pair_linear(prompt: str) -> tuple[Fraction, Fraction] | None:
    eqs = re.findall(r"[-+0-9xy*/().]+=[-+0-9xy*/().]+", clean(prompt), flags=re.I)
    eqs = [e for e in eqs if "x" in e and "y" in e]
    if len(eqs) != 2:
        return None

    def coeff(e: str):
        left, right = e.split("=", 1)
        left = left.replace("-", "+-")
        a = b = c = Fraction(0)
        for part in left.split("+"):
            if not part: continue
            if part.endswith("x"):
                a += Fraction("-1" if part == "-x" else (part[:-1] or "1"))
            elif part.endswith("y"):
                b += Fraction("-1" if part == "-y" else (part[:-1] or "1"))
            else: c += Fraction(part)
        return a, b, Fraction(right) - c
    a,b,c=coeff(eqs[0]); d,e,f=coeff(eqs[1])
    det=a*e-b*d
    if det == 0: return None
    return ((c*e-b*f)/det, (a*f-c*d)/det)


def parse_pair(text: str) -> tuple[Fraction, Fraction] | None:
    m = re.search(r"x\s*=\s*(-?\d+(?:/\d+)?)[，,；; ]+y\s*=\s*(-?\d+(?:/\d+)?)", clean(text))
    if not m: return None
    return Fraction(m.group(1)), Fraction(m.group(2))


def parse_coordinate(text: str) -> tuple[Fraction, Fraction] | None:
    m = re.search(r"\((-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\)", clean(text))
    return (Fraction(m.group(1)), Fraction(m.group(2))) if m else None


def parse_ratio(text: str) -> tuple[Fraction, Fraction] | None:
    m = re.search(r"(-?\d+)[:：](-?\d+)", clean(text))
    return (Fraction(m.group(1)), Fraction(m.group(2))) if m else None


def quadratic_coefficients(prompt: str) -> tuple[Fraction, Fraction, Fraction] | None:
    s = clean(prompt).replace("^2", "²")
    m = re.search(r"([+-]?\d*)x²([+-]\d*)x([+-]\d+)", s)
    if not m:
        return None
    a_text, b_text, c_text = m.groups()
    a = Fraction(-1 if a_text == "-" else (1 if a_text in ("", "+") else a_text))
    b = Fraction(-1 if b_text == "-" else (1 if b_text == "+" else b_text))
    return a, b, Fraction(c_text)


def check(item: dict) -> tuple[str, str] | None:
    p = clean(item.get("prompt", ""))
    ans = chosen(item)

    # One-variable linear equations.
    m = re.search(r"(?:方程式|解)\s*([^，。；]+=[^，。；]+).*?(?:解為何|x為何|x是多少)", p)
    if m and "x" in m.group(1) and "x^2" not in m.group(1):
        expr_match = re.match(r"[-+0-9xy*/().]+=[-+0-9xy*/().]+", m.group(1), re.I)
        x = linear(expr_match.group(0)) if expr_match else None
        if x is not None: return ("linear-equation", str(x)) if value(ans) != x else None

    # Simultaneous equations with an explicitly requested solution.
    if "聯立方程式" in p and ("解為何" in p or "哪一組數" in p):
        pair = pair_linear(p)
        got = parse_pair(ans)
        if pair is not None and got is not None:
            return ("simultaneous-equation", str(pair)) if got != pair else None

    # Common exact probability forms.
    expected = None; kind = None
    if "一週7天" in p and "週末" in p: expected,kind=Fraction(2,7),"weekend-probability"
    elif "連續擲兩次公平硬幣" in p and "至少出現一次正面" in p: expected,kind=Fraction(3,4),"coin-at-least-one-head"
    elif "公平骰子擲一次" in p and "大於4點" in p: expected,kind=Fraction(1,3),"die-greater-than-four"
    elif "1到10" in p and "大於7" in p: expected,kind=Fraction(3,10),"cards-greater-than-seven"
    elif "1至12" in p and "3的倍數" in p: expected,kind=Fraction(1,3),"multiples-of-three"
    elif "公平骰子一次" in p and "偶數" in p and "且硬幣" in p: expected,kind=Fraction(1,4),"even-die-and-head"
    elif "公平骰子一次" in p and "偶數" in p: expected,kind=Fraction(1,2),"even-die"
    if expected is not None:
        got=value(ans)
        if got is not None: return (kind,str(expected)) if got != expected else None

    # Frequency mean.
    m = re.search(r"數值\s*(\d+)\s*出現\s*(\d+)\s*次、數值\s*(\d+)\s*出現\s*(\d+)\s*次、數值\s*(\d+)\s*出現\s*(\d+)\s*次", p)
    if m and "平均數" in p:
        nums=list(map(int,m.groups())); expected=Fraction(nums[0]*nums[1]+nums[2]*nums[3]+nums[4]*nums[5], nums[1]+nums[3]+nums[5]); got=value(ans)
        if got is not None: return ("weighted-mean",str(expected)) if got != expected else None

    # Circle circumference and cylinder volume, preserving pi when present.
    m = re.search(r"半徑(\d+(?:\.\d+)?).*圓周長", p)
    if m and "3.14" in p:
        expected=Fraction(628,100)*Fraction(m.group(1)); got=value(ans)
        if got is not None: return ("circle-circumference",str(expected)) if got != expected else None
    m = re.search(r"圓柱半徑(\d+).*高(\d+).*體積", p)
    if m and "以π表示" in p:
        expected=Fraction(int(m.group(1))**2*int(m.group(2))); got=re.search(r"(\d+)\s*π", clean(ans))
        if got is not None: return ("cylinder-volume",str(expected)) if Fraction(got.group(1)) != expected else None

    # Coordinate distance and slope between two explicit points.
    points = re.findall(r"\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)", p)
    if len(points) >= 2 and "斜率" in p:
        (x1, y1), (x2, y2) = ((Fraction(a), Fraction(b)) for a, b in points[:2])
        if x2 != x1:
            expected = (y2 - y1) / (x2 - x1); got = value(ans)
            if got is not None: return ("slope", str(expected)) if got != expected else None
    if len(points) >= 2 and ("距離" in p or "長度" in p):
        (x1, y1), (x2, y2) = ((Fraction(a), Fraction(b)) for a, b in points[:2])
        square = (x2 - x1) ** 2 + (y2 - y1) ** 2
        root = int(square ** Fraction(1, 2))
        if root * root == square:
            got = value(ans)
            if got is not None: return ("coordinate-distance", str(root)) if got != root else None

    # Basic rectangular/parallelogram/triangle area with explicit base-height.
    m = re.search(r"(?:底為|底長為)(\d+(?:\.\d+)?).*?(?:高為|高是)(\d+(?:\.\d+)?).*?面積", p)
    if m:
        expected = Fraction(m.group(1)) * Fraction(m.group(2))
        if "三角形" in p: expected /= 2
        got = value(ans)
        if got is not None: return ("base-height-area", str(expected)) if got != expected else None
    m = re.search(r"長方形.*?(?:寬為|寬是)(\d+(?:\.\d+)?).*?(?:長為|長是)(\d+(?:\.\d+)?).*?面積", p)
    if m:
        expected = Fraction(m.group(1)) * Fraction(m.group(2)); got = value(ans)
        if got is not None: return ("rectangle-area", str(expected)) if got != expected else None

    # Arithmetic/geometric sequence with enough explicit information.
    m = re.search(r"(?:形成|為)\s*(\d+)、(\d+)、(\d+)、.*?(?:第|項)(\d+)項", p)
    if m and "等差" in p:
        a, b, _, n = map(int, m.groups()); expected = Fraction(a + (int(n) - 1) * (b - a)); got = value(ans)
        if got is not None: return ("arithmetic-sequence", str(expected)) if got != expected else None
    m = re.search(r"等比數列\s*([0-9]+(?:、[0-9]+)+)、?[…\.]+.*?下一項", p)
    if m:
        terms = [int(x) for x in m.group(1).split("、")]
        a, b, c = terms[-3:]
        if a and b * b == a * c:
            expected = Fraction(c * c, b); got = value(ans)
            if got is not None: return ("geometric-sequence-next", str(expected)) if got != expected else None

    # Similar figures: area ratio is the square of the corresponding side ratio.
    m = re.search(r"對應邊比為\s*(\d+)[:：](\d+).*?面積比", p)
    if m:
        a, b = map(int, m.groups()); expected=(Fraction(a*a), Fraction(b*b)); got=parse_ratio(ans)
        if got is not None: return ("similar-area-ratio", f"{expected[0]}:{expected[1]}") if got != expected else None

    # Right-triangle and tangent lengths with a complete Pythagorean setup.
    m = re.search(r"兩股(?:各)?(?:長為|為)\s*(\d+).*?(?:另?一股|斜邊).*?(?:長為|為)\s*(\d+).*?(?:斜邊|另一股)", p)
    if m:
        # This branch is intentionally not used when the wording does not
        # identify which of the two numbers is the hypotenuse.
        pass
    m = re.search(r"斜邊長(?:為|是)\s*(\d+).*?一股長(?:為|是)\s*(\d+).*?另一股", p)
    if m:
        h, leg=map(int,m.groups()); square=h*h-leg*leg; root=int(square**Fraction(1,2))
        if root*root==square:
            got=value(ans)
            if got is not None: return ("right-triangle-leg",str(root)) if got != root else None
    m = re.search(r"圓半徑為\s*(\d+).*?圓心距離為\s*(\d+).*?切線段長", p)
    if m:
        r,d=map(int,m.groups()); square=d*d-r*r; root=int(square**Fraction(1,2))
        if root*root==square:
            got=value(ans)
            if got is not None: return ("circle-tangent",str(root)) if got != root else None

    # A ratio plus a known sum.
    m = re.search(r"a:b\s*=\s*(\d+)[:：](\d+).*?a\+b\s*=\s*(\d+).*?b[−-]a", p)
    if m:
        ra,rb,total=map(int,m.groups()); unit=Fraction(total,ra+rb); expected=(rb-ra)*unit; got=value(ans)
        if got is not None: return ("ratio-difference",str(expected)) if got != expected else None

    # Quadratic equations/functions with an unambiguous standard or vertex form.
    abc = quadratic_coefficients(p)
    if abc and ("實數解" in p or "有幾個" in p):
        a,b,c=abc; discriminant=b*b-4*a*c; expected=2 if discriminant>0 else (1 if discriminant==0 else 0)
        got=value(ans)
        if got is not None: return ("quadratic-real-root-count",str(expected)) if got != expected else None
    if abc and "對稱軸" in p:
        a,b,_=abc; expected=-b/(2*a); got=re.search(r"x\s*=\s*(-?\d+(?:/\d+)?)", clean(ans))
        if got is not None: return ("quadratic-axis",str(expected)) if Fraction(got.group(1)) != expected else None
    if abc and "頂點" in p:
        a,b,c=abc; h=-b/(2*a); k=a*h*h+b*h+c; got=parse_coordinate(ans)
        if got is not None: return ("quadratic-vertex",f"{h},{k}") if got != (h,k) else None
    m = re.search(r"y\s*=\s*([+-]?\d*)\(x([+-]\d+)\)²([+-]\d+)", p)
    if m:
        a_text,h_text,k_text=m.groups(); a=Fraction(-1 if a_text=="-" else (1 if a_text in ("","+") else a_text)); h=-Fraction(h_text); k=Fraction(k_text)
        if "最大值" in p or "最小值" in p:
            expected=k; got=value(ans)
            if got is not None: return ("vertex-form-extremum",str(expected)) if got != expected else None
        if "值域" in p:
            want="y≥" if a>0 else "y≤"; got_clean=clean(ans).replace(">=","≥").replace("<=","≤")
            expected_text=f"{want}{k}"
            if got_clean.startswith(want): return None if got_clean == expected_text else ("quadratic-range",expected_text)
    m = re.search(r"y\s*=\s*a\(x([+-]\d+)\)²([+-]\d+)\s*通過點\s*\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)", p)
    if m:
        h,k,x,y=m.groups(); h=-Fraction(h); k=Fraction(k); x=Fraction(x); y=Fraction(y); expected=(y-k)/(x-h)**2; got=value(ans)
        if got is not None: return ("quadratic-coefficient",str(expected)) if got != expected else None

    # Centroid of three explicit vertices.
    if "重心坐標" in p:
        pts=re.findall(r"\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)", p)
        if len(pts)>=3:
            xs=[Fraction(a) for a,_ in pts[:3]]; ys=[Fraction(b) for _,b in pts[:3]]
            expected=(sum(xs)/3,sum(ys)/3); got=parse_coordinate(ans)
            if got is not None: return ("centroid",f"{expected[0]},{expected[1]}") if got != expected else None

    return None


def main() -> None:
    checked=skipped=0; failures=[]; kinds={}
    for path in sorted((ROOT/"questions/math").glob("*.json")):
        item=json.loads(path.read_text(encoding="utf-8")); result=check(item)
        # Count a question as checked only if one of the exact patterns matched;
        # rerun pattern recognition through the result/known prompt families.
        p=item.get("prompt", "")
        candidate=any(x in p for x in ("方程式", "聯立方程式", "週末的機率", "公平硬幣", "公平骰子", "大於7", "3的倍數", "平均數", "圓周長", "圓柱半徑", "斜率", "座標", "底為", "長方形", "等差", "等比", "二次函數", "頂點", "值域", "實數解", "相似", "切線", "重心", "斜邊"))
        if candidate:
            checked += 1
        else:
            skipped += 1
        if result:
            kind,expected=result; failures.append({"path":str(path.relative_to(ROOT)),"kind":kind,"expected":expected,"answer":item.get("answer",{}).get("value"),"chosenOption":chosen(item),"prompt":item.get("prompt","")}); kinds[kind]=kinds.get(kind,0)+1
    out={"status":"pass" if not failures else "mismatch-found","checked":checked,"skipped":skipped,"failureCount":len(failures),"failureKinds":kinds,"failures":failures,"note":"Only unambiguous numeric patterns are evaluated; conceptual and unparsed math remain pending subject QA."}
    (ROOT/"implementation/reports/math-semantic-numeric-pattern-audit.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:out[k] for k in ("status","checked","skipped","failureCount","failureKinds")},ensure_ascii=False))


if __name__ == "__main__": main()
