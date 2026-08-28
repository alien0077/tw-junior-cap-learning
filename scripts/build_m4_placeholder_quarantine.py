#!/usr/bin/env python3
"""Record V2 destructive candidates as reversible quarantine, without deleting files."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
src = Path('/private/tmp/m4v2')
records = []
for name, key in [('02_migration_FINAL_ACTIONS.jsonl', 'questionId'), ('04_questions_WITH_ACTUAL_REWRITES.jsonl', 'questionId'), ('03_lessons_WITH_REPLACEMENTS.jsonl', 'lessonId')]:
    for line in (src / name).read_text().splitlines():
        r = json.loads(line)
        action = r.get('resolutionAction', '')
        if 'delete' not in action and 'remove-student' not in action:
            continue
        records.append({'recordType': 'question' if key == 'questionId' else 'lesson', 'id': r[key], 'subject': r.get('subject'), 'resolutionAction': action, 'reason': r.get('reason') or r.get('answerReason') or r.get('rewriteBrief'), 'studentVisible': False, 'preserveSourceFile': True, 'requiresReplacementBeforeRemoval': True})
out = ROOT / 'data/m4-placeholder-quarantine.json'
out.write_text(json.dumps({'version':'m4-placeholder-quarantine-v1','generatedAt':'2026-08-27','policy':'reversible quarantine; no source deletion','records':records}, ensure_ascii=False, indent=2) + '\n')
print(f'wrote quarantine manifest: {len(records)} records')
