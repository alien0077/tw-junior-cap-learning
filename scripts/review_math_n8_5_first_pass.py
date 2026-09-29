#!/usr/bin/env python3
"""First-pass, unit-specific review for N-8-5; never promotes reviewStatus."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={1:"C",2:"B",3:"B",4:"B",5:"B",6:"B",7:"C",8:"C",9:"C",10:"B"}
ANCHORS=("等差", "級數", "首項", "末項", "首尾", "平均", "項數", "總和", "公式", "公差")
def main()->int:
    lesson=json.loads((ROOT/'lessons/math/lesson-math-content-n-8-5.json').read_text())
    failures=[]; checks=[]
    if lesson.get('reviewStatus')!='draft': failures.append({'scope':'lesson','reason':'reviewStatus must remain draft'})
    for path in sorted((ROOT/'questions/math').glob('question-math-content-n-8-5-*.json')):
        n=int(path.stem.rsplit('-',1)[1]); d=json.loads(path.read_text()); a=d.get('answer',{}); text=' '.join([d.get('prompt',''),d.get('solutionStrategy',''),*d.get('solutionSteps',[])])
        row={'question':n,'path':str(path.relative_to(ROOT)),'draftPreserved':d.get('reviewStatus')=='draft','answerMatchesManualKey':a.get('value')==EXPECTED[n],'expectedAnswer':EXPECTED[n],'explanationPresent':bool(str(a.get('explanation','')).strip()),'unitSpecificAnchors':sorted({x for x in ANCHORS if x in text}),'detailedSteps':len(d.get('solutionSteps',[]))>=5 and all(str(x).strip() for x in d.get('solutionSteps',[])),'publicPatternRefs':bool(d.get('examPatternRefs'))}
        row['passed']=all((row['draftPreserved'],row['answerMatchesManualKey'],row['explanationPresent'],len(row['unitSpecificAnchors'])>=2,row['detailedSteps'],row['publicPatternRefs']))
        if not row['passed']: failures.append(row)
        checks.append(row)
    summary={'status':'pass' if not failures else 'blocked','unit':'N-8-5','questions':len(checks),'passed':sum(x['passed'] for x in checks),'failed':len(failures),'reviewStatusChange':'none; lesson and questions remain draft','limitation':'Does not replace three-publisher full-text evidence, distractor/copyright review, Terra second review, or release approval.'}
    (ROOT/'implementation/reports/math-n8-5-first-pass-review.json').write_text(json.dumps({'summary':summary,'failures':failures,'checks':checks},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False)); return 0 if summary['status']=='pass' else 1
if __name__=='__main__': raise SystemExit(main())
