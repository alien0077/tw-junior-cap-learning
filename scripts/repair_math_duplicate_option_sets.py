import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# 只改同課內重複的錯誤干擾項；正確選項、題幹與計算條件不變。
REPLACEMENTS = {
    "questions/math/question-math-performance-a-iv-6-9.json": {"D": "5 個"},
    "questions/math/question-math-content-s-9-7-2.json": {"D": "4 個"},
    "questions/math/question-math-content-s-9-12-4.json": {"D": "3 個"},
    "questions/math/question-math-content-a-8-3-10.json": {"D": "12"},
    "questions/math/question-math-performance-d-iv-1-1.json": {"D": "11"},
    "questions/math/question-math-performance-a-iv-2-6.json": {"D": "9"},
    "questions/math/question-math-content-n-8-6-10.json": {"D": "12"},
    "questions/math/question-math-content-a-8-7-6.json": {"D": "11"},
    "questions/math/question-math-performance-s-iv-3-5.json": {"D": "10"},
    "questions/math/question-math-performance-s-iv-11-3.json": {"D": "三條角平分線的交點"},
    "questions/math/question-math-performance-s-iv-11-4.json": {"D": "三條中線的交點"},
    "questions/math/question-math-performance-s-iv-11-10.json": {"C": "三條中線的交點"},
    "questions/math/question-math-performance-s-iv-11-1.json": {"D": "三條邊的垂直平分線交點"},
    "questions/math/question-math-content-d-9-3-7.json": {"D": "3/4"},
    "questions/math/question-math-content-d-9-3-5.json": {"D": "3/5"},
    "questions/math/question-math-content-a-7-3-9.json": {"D": "120"},
    "questions/math/question-math-content-a-7-3-4.json": {"D": "12"},
    "questions/math/question-math-content-a-7-3-1.json": {"D": "14"},
    "questions/math/question-math-content-g-8-1-4.json": {"D": "8"},
    "questions/math/question-math-content-g-8-1-1.json": {"D": "10"},
    "questions/math/question-math-content-s-9-3-7.json": {"C": "9 公分", "D": "12 公分"},
    "questions/math/question-math-content-s-9-3-3.json": {"D": "12 公分"},
    "questions/math/question-math-performance-s-iv-12-2.json": {"D": "3/4"},
    "questions/math/question-math-content-a-7-3-7.json": {"D": "12"},
    "questions/math/question-math-content-a-7-3-6.json": {"A": "3", "D": "12"},
    "questions/math/question-math-content-n-8-4-7.json": {"D": "8"},
    "questions/math/question-math-content-n-8-4-1.json": {"D": "7"},
    "questions/math/question-math-content-s-7-5-3.json": {"D": "4 條"},
    "questions/math/question-math-content-s-7-5-4.json": {"C": "5 條"},
    "questions/math/question-math-content-s-8-4-4.json": {"D": "SSA（不構成一般全等判定）"},
    "questions/math/question-math-content-s-8-4-3.json": {"D": "無此判定"},
    "questions/math/question-math-performance-s-iv-2-9.json": {"D": "14"},
    "questions/math/question-math-performance-s-iv-2-10.json": {"D": "11"},
    "questions/math/question-math-content-n-7-6-5.json": {"C": "3"},
    "questions/math/question-math-content-n-7-6-4.json": {"C": "5"},
}

for relative, changes in REPLACEMENTS.items():
    path = ROOT / relative
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {option["id"]: option for option in data.get("options", [])}
    for option_id, text in changes.items():
        if option_id not in by_id:
            raise SystemExit(f"missing option {option_id}: {relative}")
        if data.get("answer", {}).get("value") == option_id:
            raise SystemExit(f"refused to modify correct option {option_id}: {relative}")
        by_id[option_id]["text"] = text
    data["updatedAt"] = "2026-09-13"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"repaired {len(REPLACEMENTS)} questions")
