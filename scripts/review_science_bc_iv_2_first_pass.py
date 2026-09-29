import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; files=sorted((ROOT/'questions/science').glob('question-science-content-bc-iv-2-*.json'),key=lambda p:int(p.stem.rsplit('-',1)[1])); expected=['A','B','A','C','A','D','A','B','A','C']; failures=[]
for i, p in enumerate(files):
 d=json.loads(p.read_text()); q=[]
 if d['answer']['value']!=expected[i]: q.append('wrong answer')
 if not any(o['id']==d['answer']['value'] for o in d['options']): q.append('answer option missing')
 if len(d.get('solutionSteps',[]))<4: q.append('steps<4')
 if d.get('reviewStatus')!='draft': q.append('not draft')
 if q: failures.append({'file':p.name,'problems':q})
report={'unit':'Bc-Ⅳ-2','checked':len(files),'passed':len(files)-len(failures),'failures':failures,'status':'pass' if not failures else 'fail'}
(ROOT/'implementation/reports/science-bc-iv-2-first-pass-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n'); print(json.dumps(report,ensure_ascii=False)); raise SystemExit(bool(failures))
