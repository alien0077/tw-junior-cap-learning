#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SUBJECTS=("chinese","english","math","science","social")
errors=[]; counts={s:0 for s in SUBJECTS}; covered={s:0 for s in SUBJECTS}
for subject in SUBJECTS:
    for path in sorted((ROOT/"lessons"/subject).rglob("*.json")):
        try: data=json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}"); continue
        # Visual-first completion gate is unit-level (IV leaf units); strand/domain overview files are navigation/synthesis records.
        if "-iv-" not in str(data.get("id","")).lower():
            continue
        counts[subject]+=1
        interactive=data.get("interactive")
        simulation=data.get("simulation")
        if subject in {"math","science"}:
            if isinstance(simulation,dict):
                semantic=bool(simulation.get("visualContract") or simulation.get("learningDesign") or (simulation.get("model") and simulation.get("model") != "general") or any(k in simulation for k in ("prismModel","similarityModel","ticketEquation","equationMeaning")))
                if semantic:
                    covered[subject]+=1
                else:
                    errors.append(f"{path.relative_to(ROOT)}: simulation lacks semantic visualContract/learningDesign")
            elif isinstance(interactive,dict):
                covered[subject]+=1
            else:
                errors.append(f"{path.relative_to(ROOT)}: no interactive/simulation learning surface")
        else:
            if isinstance(interactive,dict) and str(interactive.get("goal","")).strip():
                covered[subject]+=1
            else:
                errors.append(f"{path.relative_to(ROOT)}: no goal-bearing interactive learning surface")
print("visual-first audit counts:",", ".join(f"{s}={covered[s]}/{counts[s]}" for s in SUBJECTS))
if errors:
    print("\n".join(errors))
    raise SystemExit(1)
print("VISUAL_FIRST_ALL_LESSONS_PASS")
