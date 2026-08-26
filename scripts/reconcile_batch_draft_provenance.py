#!/usr/bin/env python3
"""Downgrade lessons explicitly marked as batch-generated drafts."""
from __future__ import annotations
import glob, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    draft=set(); changed_l=0; changed_q=0
    for f in glob.glob(str(ROOT/"lessons/**/*.json"),recursive=True):
        p=Path(f); d=json.loads(p.read_text(encoding='utf-8'))
        note=str(d.get('provenance',{}).get('authoringNote',''))
        if 'Batch-generated draft' in note or str(d.get('title','')).startswith('草稿'):
            draft.add(d['id'])
            if d.get('reviewStatus')!='draft':
                d['reviewStatus']='draft'; p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n'); changed_l+=1
    for f in glob.glob(str(ROOT/"questions/**/*.json"),recursive=True):
        p=Path(f); d=json.loads(p.read_text(encoding='utf-8'))
        if d.get('lessonId') in draft and d.get('reviewStatus')!='draft':
            d['reviewStatus']='draft'; p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n'); changed_q+=1
    mpath=ROOT/'data/m4-coverage-matrix.json'; m=json.loads(mpath.read_text(encoding='utf-8')); changed_m=0
    for row in m['rows']:
        if row.get('lessonId') in draft and row.get('reviewStatus')!='draft':
            row['reviewStatus']='draft'; row['contentStatus']='draft'; changed_m+=1
    mpath.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
    print(f'draft lessons={len(draft)}; downgraded lessons={changed_l}, questions={changed_q}, rows={changed_m}')
    return 0
if __name__=='__main__': raise SystemExit(main())
