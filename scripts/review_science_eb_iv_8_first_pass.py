import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / 'questions/science').glob('question-science-content-eb-iv-8-*.json'))
failures = []
for path in files:
    item = json.loads(path.read_text())
    if item['answer']['value'] not in {o['id'] for o in item['options']} or len(item.get('solutionSteps', [])) < 5 or item.get('reviewStatus') != 'draft': failures.append(path.name)
report = {'unit': 'Eb-Ⅳ-8', 'checked': len(files), 'passed': len(files)-len(failures), 'failures': failures, 'status': 'pass' if len(files) == 10 and not failures else 'fail'}
(ROOT / 'implementation/reports/science-eb-iv-8-first-pass-review.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report['status'] == 'pass' else 1)
