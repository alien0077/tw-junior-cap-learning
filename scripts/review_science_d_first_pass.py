import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
files=[p for p in (ROOT/'questions/science').glob('question-science-content-d-*.json') if re.fullmatch(r'question-science-content-d-\d+\.json',p.name)]
bad=[]
for p in files:
 x=json.loads(p.read_text())
 if len(x.get('options',[]))!=4 or x.get('answer',{}).get('value') not in 'ABCD' or len(x.get('solutionSteps',[]))!=5 or len(x.get('examPatternRefs',[]))<3 or x.get('reviewStatus')!='draft':bad.append(p.name)
r={'unit':'D','checked':len(files),'passed':len(files) if len(files)==10 and not bad else 0,'failures':bad,'status':'pass' if len(files)==10 and not bad else 'fail'}
(ROOT/'implementation/reports/science-d-first-pass-review.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False))
