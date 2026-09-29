import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / 'questions/social').glob('question-social-content-geo-bh-iv-1-*.json'))
failures = []
for path in files:
    item = json.loads(path.read_text())
    if (len(item['options']) != 4 or item['answer']['value'] not in {o['id'] for o in item['options']} or len(item.get('solutionSteps', [])) != 5 or len(item.get('examPatternRefs', [])) < 3 or item.get('reviewStatus') != 'draft'):
        failures.append(path.name)
report = {'unit': '地 Bh-Ⅳ-1', 'checked': len(files), 'passed': len(files)-len(failures), 'failures': failures, 'status': 'pass' if len(files) == 10 and not failures else 'fail', 'sourceCountPerQuestion': 3, 'note': '第一輪結構與內容契約；公開試題僅作能力與資料型態 pattern-only 參照，未複製原題。'}
(ROOT / 'implementation/reports/social-geo-bh-iv-1-first-pass-review.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report['status'] == 'pass' else 1)
