import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / "questions/social").glob("question-social-content-hist-hb-iv-2-*.json"))
failures = []
for path in files:
    item = json.loads(path.read_text(encoding="utf-8"))
    opts = item.get("options", [])
    refs = item.get("examPatternRefs", [])
    if (len(opts) != 4 or item.get("answer", {}).get("value") not in {o.get("id") for o in opts} or not item.get("answer", {}).get("explanation") or not item.get("solutionStrategy") or len(item.get("solutionSteps", [])) != 5 or len(refs) < 3 or any(r.get("status") != "recorded" or r.get("reuseDecision") != "pattern-only" for r in refs) or item.get("reviewStatus") != "draft" or item.get("lessonId") != "lesson-social-content-hist-hb-iv-2"):
        failures.append(path.name)
report = {"unit": "歷 Hb-Ⅳ-2", "checked": len(files), "passed": len(files) - len(failures), "failures": failures, "status": "pass" if len(files) == 10 and not failures else "fail", "sourceCountPerQuestion": 3, "note": "第一輪逐題契約檢查；題目以公立學校公開試題的能力與資料型態 pattern-only 參照，重新設計商貿網絡、商人社群、信用契約、宗教網絡、翻譯知識、技術生產、城市消費、文化混融、性別移動與多重證據情境，未複製原題。"}
(ROOT / "implementation/reports/social-hist-hb-iv-2-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report["status"] == "pass" else 1)
