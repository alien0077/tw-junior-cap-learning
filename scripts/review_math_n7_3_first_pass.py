#!/usr/bin/env python3
"""First-pass, unit-specific review for N-7-3; never promotes reviewStatus."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={1:"C",2:"B",3:"A",4:"B",5:"A",6:"A",7:"A",8:"A",9:"C",10:"A"}
ANCHORS=("負數", "符號", "數線", "絕對值", "優先", "通分", "分母", "小數點", "平方", "溫度")
def main()->int:
    lesson=json.loads((ROOT/'lessons/math/lesson-math-content-n-7-3.json').read_text())
    failures=[]; checks=[]
    if lesson.get('reviewStatus')!='draft': failures.append({'scope':'lesson','reason':'reviewStatus must remain draft'})
    for path in sorted((ROOT/'questions/math').glob('question-math-content-n-7-3-*.json')):
        n=int(path.stem.rsplit('-',1)[1]); d=json.loads(path.read_text()); a=d.get('answer',{}); text=' '.join([d.get('prompt',''),d.get('solutionStrategy',''),*d.get('solutionSteps',[])])
        row={'question':n,'path':str(path.relative_to(ROOT)),'draftPreserved':d.get('reviewStatus')=='draft','answerMatchesManualKey':a.get('value')==EXPECTED[n],'expectedAnswer':EXPECTED[n],'explanationPresent':bool(str(a.get('explanation','')).strip()),'unitSpecificAnchors':sorted({x for x in ANCHORS if x in text}),'detailedSteps':len(d.get('solutionSteps',[]))>=5 and all(str(x).strip() for x in d.get('solutionSteps',[])),'publicPatternRefs':bool(d.get('examPatternRefs'))}
        row['passed']=all((row['draftPreserved'],row['answerMatchesManualKey'],row['explanationPresent'],len(row['unitSpecificAnchors'])>=1,row['detailedSteps'],row['publicPatternRefs']))
        if not row['passed']: failures.append(row)
        checks.append(row)
    summary={'status':'pass' if not failures else 'blocked','unit':'N-7-3','questions':len(checks),'passed':sum(x['passed'] for x in checks),'failed':len(failures),'reviewStatusChange':'none; lesson and questions remain draft','limitation':'Does not replace three-publisher full-text evidence, distractor/copyright review, Terra second review, or release approval.'}
    (ROOT/'implementation/reports/math-n7-3-first-pass-review.json').write_text(json.dumps({'summary':summary,'failures':failures,'checks':checks},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False)); return 0 if summary['status']=='pass' else 1
if __name__=='__main__': raise SystemExit(main())
