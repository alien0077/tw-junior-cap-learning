import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = [p for p in (ROOT / 'questions/science').glob('question-science-content-nc-iv-6-*.json') if re.fullmatch(r'question-science-content-nc-iv-6-\d+\.json', p.name)]
failures = []
for path in files:
    item = json.loads(path.read_text())
    ids = {option['id'] for option in item.get('options', [])}
    if len(item.get('options', [])) != 4 or item.get('answer', {}).get('value') not in ids or len(item.get('solutionSteps', [])) != 5 or item.get('reviewStatus') != 'draft': failures.append(path.name)
report = {'unit': 'Nc-Ⅳ-6', 'checked': len(files), 'passed': len(files) - len(failures), 'failures': failures, 'status': 'pass' if len(files) == 10 and not failures else 'fail'}
(ROOT / 'implementation/reports/science-nc-iv-6-first-pass-review.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report['status'] == 'pass' else 1)
