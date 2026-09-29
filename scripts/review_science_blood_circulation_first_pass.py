#!/usr/bin/env python3
"""First-pass, unit-specific review for blood circulation; never promotes reviewStatus."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={i:"A" for i in range(1,11)}
ANCHORS=("右心房", "右心室", "左心房", "左心室", "肺循環", "全身循環", "肺動脈", "肺靜脈", "瓣膜", "逆流", "流向", "含氧")
def main()->int:
    lesson=json.loads((ROOT/'lessons/science/lesson-science-blood-circulation.json').read_text()); failures=[]; checks=[]
    if lesson.get('reviewStatus')!='draft': failures.append({'scope':'lesson','reason':'reviewStatus must remain draft'})
    for path in sorted((ROOT/'questions/science').glob('question-science-blood-circulation-*.json')):
        n=int(path.stem.rsplit('-',1)[1]); d=json.loads(path.read_text()); a=d.get('answer',{}); text=' '.join([d.get('prompt',''),d.get('solutionStrategy',''),*d.get('solutionSteps',[])])
        row={'question':n,'path':str(path.relative_to(ROOT)),'draftPreserved':d.get('reviewStatus')=='draft','answerMatchesManualKey':a.get('value')==EXPECTED[n],'expectedAnswer':EXPECTED[n],'explanationPresent':bool(str(a.get('explanation','')).strip()),'unitSpecificAnchors':sorted({x for x in ANCHORS if x in text}),'detailedSteps':len(d.get('solutionSteps',[]))>=5 and all(str(x).strip() for x in d.get('solutionSteps',[])),'publicPatternRefs':bool(d.get('examPatternRefs'))}
        row['passed']=all((row['draftPreserved'],row['answerMatchesManualKey'],row['explanationPresent'],len(row['unitSpecificAnchors'])>=2,row['detailedSteps'],row['publicPatternRefs']))
        if not row['passed']: failures.append(row)
        checks.append(row)
    summary={'status':'pass' if not failures else 'blocked','unit':'science-blood-circulation','questions':len(checks),'passed':sum(x['passed'] for x in checks),'failed':len(failures),'reviewStatusChange':'none; lesson and questions remain draft','limitation':'Does not replace three-publisher full-text evidence, distractor/copyright review, Terra second review, or release approval.'}
    (ROOT/'implementation/reports/science-blood-circulation-first-pass-review.json').write_text(json.dumps({'summary':summary,'failures':failures,'checks':checks},ensure_ascii=False,indent=2)+'\n'); print(json.dumps(summary,ensure_ascii=False)); return 0 if summary['status']=='pass' else 1
if __name__=='__main__': raise SystemExit(main())
