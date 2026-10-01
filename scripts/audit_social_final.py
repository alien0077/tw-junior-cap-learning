#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
import yaml
R=Path(__file__).resolve().parents[1]
LESSON_RE=re.compile(r"lesson-social-content-(geo|hist|civ)-.+-iv-\d+\.json$")
SPEC_RE=re.compile(r"cur-social-content-(geo|hist|civ)-.+-iv-\d+\.yaml$")
GENERIC=re.compile(r"開始「|依 unit spec|不可只換名詞|先提交預測|本課聚焦「.*」，以自編範例練習概念、證據與新情境遷移。")
lessons=sorted(p for p in (R/"lessons/social").glob("*.json") if LESSON_RE.fullmatch(p.name))
specs=sorted(p for p in (R/"implementation/unit-specs/social").glob("*.yaml") if SPEC_RE.fullmatch(p.name))
errors=[]; units={}
for p in lessons:
 d=json.loads(p.read_text()); lid=d.get("id"); units[lid]=p
 if d.get("reviewStatus")!="reviewed": errors.append([str(p.relative_to(R)),"reviewStatus"])
 if GENERIC.search(json.dumps(d.get("interactive",{}),ensure_ascii=False)): errors.append([str(p.relative_to(R)),"generic-interactive"])
 if GENERIC.search(str(d.get("content",{}).get("summary",""))): errors.append([str(p.relative_to(R)),"generic-summary"])
 if len(d.get("interactive",{}).get("steps",[]))<3: errors.append([str(p.relative_to(R)),"interactive-steps<3"])
for p in specs:
 d=yaml.safe_load(p.read_text()); u=d.get("unitImplementationSpec",{})
 if u.get("qaStatus")!="content-reviewed": errors.append([str(p.relative_to(R)),"qaStatus"])
 locator=json.dumps(u.get("sourceEvidence",u.get("sourceLocator",{})),ensure_ascii=False)
 if not locator or locator in ("{}","null","[]"): errors.append([str(p.relative_to(R)),"source-locator-missing"])
qby={}
for p in (R/"questions/social").glob("*.json"):
 d=json.loads(p.read_text()); lid=d.get("lessonId",""); qby.setdefault(lid,[]).append((p,d))
for lid,p in units.items():
 qs=qby.get(lid,[])
 if len(qs)<10: errors.append([str(p.relative_to(R)),f"questions={len(qs)}"])
 for qp,q in qs:
  if not str(q.get("answer",{}).get("value","")).strip(): errors.append([str(qp.relative_to(R)),"answer"])
  if not str(q.get("answer",{}).get("explanation","")).strip(): errors.append([str(qp.relative_to(R)),"explanation"])
  if not str(q.get("solutionStrategy","")).strip(): errors.append([str(qp.relative_to(R)),"strategy"])
  if len(q.get("solutionSteps",[]))<3: errors.append([str(qp.relative_to(R)),"solutionSteps<3"])
out={"status":"pass" if not errors else "blocked","lessonCount":len(lessons),"specCount":len(specs),"questionUnits":len(qby),"errors":errors}
(R/"implementation/reports/social-final-audit.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
from collections import Counter\nprint(json.dumps({k:out[k] for k in ("status","lessonCount","specCount","questionUnits")}|{"errorCount":len(errors),"errorKinds":Counter(e[1] for e in errors),"firstErrors":errors[:80]},ensure_ascii=False))
sys.exit(0 if not errors else 1)
