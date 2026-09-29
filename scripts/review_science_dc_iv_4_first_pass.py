import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / 'questions/science').glob('question-science-content-dc-iv-4-*.json'))
failures = []
for path in files:
    item = json.loads(path.read_text())
    option_ids = {option['id'] for option in item['options']}
    if item['answer']['value'] not in option_ids or len(item.get('solutionSteps', [])) < 5 or item.get('reviewStatus') != 'draft':
        failures.append(path.name)
report = {'unit': 'Dc-Ⅳ-4', 'checked': len(files), 'passed': len(files) - len(failures), 'failures': failures,
          'status': 'pass' if not failures and len(files) == 10 else 'fail'}
(ROOT / 'implementation/reports/science-dc-iv-4-first-pass-review.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report['status'] == 'pass' else 1)
