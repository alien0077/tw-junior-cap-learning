"""Attach traceable public-source pointers without copying external content."""
import json,glob
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
COURSE='https://stv.naer.edu.tw/teaching/course_outline.jsp'
CAP='https://cap.rcpet.edu.tw/index.html'
counts={}
for subject in ['chinese','english','math','science','social']:
    n=0
    for p in glob.glob(str(ROOT/f'lessons/{subject}/*.json')):
        x=json.loads(Path(p).read_text()); refs=x.get('studyReferences',[])
        x['studyReferences']=sorted(set(refs+[COURSE,CAP]))
        Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n'); n+=1
    for p in glob.glob(str(ROOT/f'questions/{subject}/*.json')):
        x=json.loads(Path(p).read_text()); prov=x.setdefault('provenance',{})
        prov['sourceUrl']=COURSE
        prov['sourceLocator']=','.join(x.get('knowledgeIds',[]))
        Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
    counts[subject]=n
print('lessons annotated',counts,'questions annotated',sum(len(glob.glob(str(ROOT/f'questions/{s}/*.json'))) for s in counts))
