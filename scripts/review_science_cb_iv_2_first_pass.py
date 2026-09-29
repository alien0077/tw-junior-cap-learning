import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / 'questions/science').glob('question-science-content-cb-iv-2-*.json'))
failures = []
for p in files:
    x = json.loads(p.read_text())
    if x['answer']['value'] not in {o['id'] for o in x['options']} or len(x.get('solutionSteps', [])) < 5 or x.get('reviewStatus') != 'draft':
        failures.append(p.name)
report = {'unit': 'Cb-Ⅳ-2', 'checked': len(files), 'passed': len(files)-len(failures), 'failures': failures, 'status': 'pass' if not failures and len(files) == 10 else 'fail'}
out = ROOT / 'implementation/reports/science-cb-iv-2-first-pass-review.json'
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report['status'] == 'pass' else 1)
