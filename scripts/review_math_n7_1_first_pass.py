#!/usr/bin/env python3
"""First-pass, unit-specific review for N-7-1; never promotes reviewStatus."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={1:"B",2:"D",3:"A",4:"B",5:"C",6:"C",7:"B",8:"C",9:"B",10:"C"}
ANCHORS=("質數", "合數", "因數", "質因數", "分解", "倍數", "正因數", "試除", "範圍")
def main()->int:
    lesson=json.loads((ROOT/'lessons/math/lesson-math-content-n-7-1.json').read_text())
    failures=[]; checks=[]
    if lesson.get('reviewStatus')!='draft': failures.append({'scope':'lesson','reason':'reviewStatus must remain draft'})
    for path in sorted((ROOT/'questions/math').glob('question-math-content-n-7-1-*.json')):
        n=int(path.stem.rsplit('-',1)[1]); d=json.loads(path.read_text()); a=d.get('answer',{}); text=' '.join([d.get('prompt',''),d.get('solutionStrategy',''),*d.get('solutionSteps',[])])
        row={'question':n,'path':str(path.relative_to(ROOT)),'draftPreserved':d.get('reviewStatus')=='draft','answerMatchesManualKey':a.get('value')==EXPECTED[n],'expectedAnswer':EXPECTED[n],'explanationPresent':bool(str(a.get('explanation','')).strip()),'unitSpecificAnchors':sorted({x for x in ANCHORS if x in text}),'detailedSteps':len(d.get('solutionSteps',[]))>=5 and all(str(x).strip() for x in d.get('solutionSteps',[])),'publicPatternRefs':bool(d.get('examPatternRefs'))}
        row['passed']=all((row['draftPreserved'],row['answerMatchesManualKey'],row['explanationPresent'],len(row['unitSpecificAnchors'])>=1,row['detailedSteps'],row['publicPatternRefs']))
        if not row['passed']: failures.append(row)
        checks.append(row)
    summary={'status':'pass' if not failures else 'blocked','unit':'N-7-1','questions':len(checks),'passed':sum(x['passed'] for x in checks),'failed':len(failures),'reviewStatusChange':'none; lesson and questions remain draft','limitation':'Does not replace three-publisher full-text evidence, distractor/copyright review, Terra second review, or release approval.'}
    (ROOT/'implementation/reports/math-n7-1-first-pass-review.json').write_text(json.dumps({'summary':summary,'failures':failures,'checks':checks},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False)); return 0 if summary['status']=='pass' else 1
if __name__=='__main__': raise SystemExit(main())
