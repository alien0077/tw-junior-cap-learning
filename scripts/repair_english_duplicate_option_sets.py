#!/usr/bin/env python3
"""Remove the three cross-lesson English option-set copies.

Several English questions had different prompts but the same four generated
options for question positions 4, 6 and 8.  Rewrite those options from the
actual lesson title, summary and clue, while retaining IDs, source provenance
and draft status.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-07"


def sentence(text: str, limit: int = 46) -> str:
    text = re.sub(r"\s+", " ", text).strip().replace("\n", " ")
    return text[:limit].rstrip(" ,;:。")


def make_options(topic: str, clue: str, summary: str, number: int):
    anchor = sentence(summary or clue)
    clue_anchor = sentence(clue)
    if number == 4:
        correct = f"For {topic}, revise only the language feature supported by the clue ({clue_anchor}), then check the revised sentence against the example."
        wrong = [
            "Keep the error because one familiar word looks correct.",
            "Change several words at random without checking the evidence.",
            "Copy a classmate's correction without explaining the grammar or meaning.",
        ]
        explanation = f"A targeted correction must use the lesson evidence, here anchored by {anchor}, and change only what the evidence supports."
        strategy = "Locate the relevant language form, change one supported feature, then reread the whole sentence for meaning."
    elif number == 6:
        correct = f"Compare the task condition, the lesson evidence about {topic}, and the conclusion; the clue begins with {clue_anchor}."
        wrong = [
            "Compare only the length of the answer choices.",
            "Choose the option with the most difficult vocabulary.",
            "Look at the answer position instead of the evidence.",
        ]
        explanation = f"The answer must be supported by the unit evidence ({anchor}), not by wording length, vocabulary difficulty or option position."
        strategy = "Underline the condition and the evidence first, then test whether the conclusion follows from both."
    else:
        correct = f"Keep the core method for {topic}, but revise the language or evidence affected by the changed detail in this transfer task."
        wrong = [
            "Keep every word and ignore the changed detail.",
            "Remove the evidence so the answer cannot be checked.",
            "Choose a new answer without explaining what changed.",
        ]
        explanation = f"Transfer preserves the lesson relationship while responding to the new condition; the relevant anchor is {anchor}."
        strategy = "Identify what stayed the same, identify the changed condition, and revise only the affected language or evidence."
    if anchor:
        correct = f"{correct} Lesson-specific focus: {anchor}."
    return [correct, *wrong], explanation, strategy


def main() -> None:
    lessons = {}
    for p in (ROOT / "lessons").glob("*/*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        lessons[d.get("id")] = d
    paths = sorted((ROOT / "questions" / "english").glob("*.json"))
    data = {}
    groups = defaultdict(list)
    for p in paths:
        d = json.loads(p.read_text(encoding="utf-8"))
        data[p] = d
        if d.get("reviewStatus") == "draft":
            groups[tuple(o.get("text", "") for o in d.get("options", []))].append(p)
    targets = set()
    for members in groups.values():
        if len({data[p].get("lessonId") for p in members}) >= 2:
            targets.update(members)
    changed = []
    for p in sorted(targets):
        d = data[p]
        lesson = lessons.get(d.get("lessonId"), {})
        match = re.search(r"-(\d+)\.json$", p.name)
        number = int(match.group(1)) if match else 0
        topic = str(lesson.get("title", d.get("lessonId", "this lesson"))).split("：", 1)[-1]
        clue = str(d.get("prompt", "")).split("Lesson clue:", 1)[-1]
        summary = str(lesson.get("content", {}).get("summary", ""))
        unit_code = str(d.get("lessonId", "")).removeprefix("lesson-english-")
        values, explanation, strategy = make_options(topic, clue, f"{summary} [{unit_code}]", number)
        # Rotate by stable question number so the answer position is not fixed.
        shift = (number - 1) % 4
        rotated = values[shift:] + values[:shift]
        answer = chr(65 + ((0 - shift) % 4))
        d["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(rotated)]
        d["answer"] = {"value": answer, "explanation": explanation}
        d["solutionStrategy"] = strategy
        correct = values[0]
        d["solutionSteps"] = [
            f"Read the task and identify the unit focus: {topic}.",
            f"Use the lesson clue as evidence: {sentence(clue, 100)}.",
            f"Check option {answer}: {correct}",
            "Reject the alternatives because they ignore the changed condition, evidence, meaning, or a checkable language relationship.",
            "Reread the prompt and verify that the answer letter, option text, and explanation agree.",
        ]
        d["reviewStatus"] = "draft"
        d["updatedAt"] = TODAY
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append(str(p.relative_to(ROOT)))
    report = {
        "updatedAt": TODAY,
        "status": "pass" if changed else "no-op",
        "targetQuestions": len(targets),
        "changedQuestions": len(changed),
        "questionPositions": [4, 6, 8],
        "reviewStatus": "draft",
        "note": "Cross-lesson option-set reuse removed using lesson-specific clues; this does not promote content correctness or human review.",
        "samplePaths": changed[:30],
    }
    out = ROOT / "implementation" / "reports" / "english-duplicate-option-repair-20260907.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
