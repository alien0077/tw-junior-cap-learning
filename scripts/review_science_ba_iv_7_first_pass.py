import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; files=sorted((ROOT/'questions/science').glob('question-science-content-ba-iv-7-*.json'),key=lambda p:int(p.stem.rsplit('-',1)[1])); expected=['A','A','A','A','A','A','B','A','A','A']; failures=[]
for p in files:
 d=json.loads(p.read_text()); q=[]
 if d['answer']['value']!=expected[int(p.stem.rsplit('-',1)[1])-1]: q.append('wrong answer')
 if not any(o['id']==d['answer']['value'] for o in d['options']): q.append('answer option missing')
 if len(d.get('solutionSteps',[]))<4: q.append('steps<4')
 if d.get('reviewStatus')!='draft': q.append('not draft')
 if q: failures.append({'file':p.name,'problems':q})
report={'unit':'Ba-Ⅳ-7','checked':len(files),'passed':len(files)-len(failures),'failures':failures,'status':'pass' if not failures else 'fail'}
(ROOT/'implementation/reports/science-ba-iv-7-first-pass-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n'); print(json.dumps(report,ensure_ascii=False)); raise SystemExit(bool(failures))
