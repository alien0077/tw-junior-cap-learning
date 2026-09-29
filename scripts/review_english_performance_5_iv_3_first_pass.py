#!/usr/bin/env python3
"""First-pass answer and provenance review for English 5-IV-3."""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
 1:("D","At 7:30 this evening."), 2:("B","Because it may rain later."), 3:("C","Twice a week."),
 4:("A","Yes, please. No sugar, thanks."), 5:("D","Not yet. I will add the title tonight."),
 6:("C","Sure. Here you are."), 7:("B","The number 12 bus stops near it."),
 8:("A","Not at all. It is warm in here."), 9:("C","It went well, and everyone shared the work."),
 10:("B","Let us check the lost-and-found office together."),
}

def main() -> None:
    keys: Counter[str] = Counter(); prompts=[]; strategies=[]; steps=[]
    for n,(key,correct) in EXPECTED.items():
        item=json.loads((ROOT/f"questions/english/question-english-performance-5-iv-3-{n}.json").read_text(encoding="utf-8"))
        options={o["id"]:o["text"] for o in item["options"]}
        assert item["reviewStatus"]=="draft" and item["answer"]["value"]==key and options[key]==correct
        assert len(item["solutionSteps"])==5 and item["solutionSteps"][-1]==item["answer"]["explanation"]
        refs=item["examPatternRefs"]
        assert len(refs)==3 and len({r["url"] for r in refs})==3
        assert all(r["status"]=="recorded" and r["reuseDecision"]=="pattern-only" and "PDF第" in r["locator"] and "題" in r["locator"] for r in refs)
        keys[key]+=1; prompts.append(item["prompt"]); strategies.append(item["solutionStrategy"]); steps.extend(item["solutionSteps"])
    assert keys==Counter({"A":2,"B":3,"C":3,"D":2}),keys
    assert len(set(prompts))==len(set(strategies))==10 and len(set(steps))==50
    print(json.dumps({"status":"pass","reviewed":10,"answerDistribution":dict(sorted(keys.items())),"recordedPatternOnlyRefs":30,"distinctStrategies":10,"uniqueSteps":50,"reviewStatus":"draft"},ensure_ascii=False))

if __name__=="__main__": main()
