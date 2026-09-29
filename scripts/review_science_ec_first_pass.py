import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]; fs=[p for p in (R/'questions/science').glob('question-science-content-ec-*.json') if re.fullmatch(r'question-science-content-ec-\d+\.json',p.name)]
bad=[]
for p in fs:
 d=json.loads(p.read_text())
 if len(d.get('options',[]))!=4 or d.get('answer',{}).get('value') not in 'ABCD' or len(d.get('solutionSteps',[]))!=5: bad.append(p.name)
rep={'unit':'Ec','checked':len(fs),'passed':len(fs) if not bad and len(fs)==10 else 0,'failures':bad,'status':'pass' if not bad and len(fs)==10 else 'fail'}
(R/'implementation/reports/science-ec-first-pass-review.json').write_text(json.dumps(rep,ensure_ascii=False,indent=2)+'\n'); print(json.dumps(rep,ensure_ascii=False))
