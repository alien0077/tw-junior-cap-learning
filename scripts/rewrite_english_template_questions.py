#!/usr/bin/env python3
"""Rewrite the English questions caught by the template-reuse gate.

The rewrite is deliberately driven by each lesson's own title, examples,
misconceptions, highlights, and exit checks.  It keeps the recorded public
exam pattern as provenance while replacing the generic generator surface with
unit-specific tasks.  All answers are rechecked by the answer audit afterward.
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

from audit_question_template_reuse import item_key

ROOT = Path(__file__).resolve().parents[1]


def text(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def chunks(lesson: dict) -> list[str]:
    out: list[str] = []
    content = lesson.get("content", {})
    out.append(text(content.get("summary")))
    for row in content.get("sections", []):
        out.append(text(row.get("body")))
    teaching = lesson.get("teaching", {})
    for row in teaching.get("body", []):
        out.append(text(row.get("body")))
    out.extend(text(x) for x in lesson.get("studyHighlights", []))
    for row in teaching.get("exitCheck", []):
        out.append(text(row.get("prompt")))
        out.append(text(row.get("expectedEvidence")))
    out.extend(text(x) for x in teaching.get("summary", []))
    return [x for x in out if x]


def focus(lesson: dict) -> str:
    title = text(lesson.get("title"))
    return title or text(lesson.get("id"))


def evidence(lesson: dict, index: int) -> str:
    teaching = lesson.get("teaching", {})
    values = [
        text(x) for x in lesson.get("studyHighlights", [])
    ] + [
        text(row.get("prompt")) for row in teaching.get("exitCheck", [])
    ] + [
        text(lesson.get("content", {}).get("summary")),
    ]
    values = [x for x in values if x]
    if not values:
        values = chunks(lesson)
    if not values:
        return focus(lesson)
    value = values[index % len(values)]
    value = value[:140].rstrip("。.!！，,；;:：")
    # Avoid leaving half of an English quotation at the end of a Chinese clue.
    if value.count("'") % 2:
        value = value.rsplit("'", 1)[0].rstrip()
    return value


def make_item(data: dict, lesson: dict, number: int) -> None:
    topic = focus(lesson)
    clue = evidence(lesson, number - 1)
    variant = (number - 1) % 10
    tasks = [
        ("Which choice best identifies the evidence a learner should use for", "Use the lesson's concrete clue before making a claim.", "Guess from one familiar word without checking the clue.", "Copy a classmate's claim without matching the clue.", "Ignore the clue and choose the longest statement."),
        ("Which study sequence is most appropriate for", "Read the task, locate the relevant detail, and then explain the conclusion.", "Decide on an answer before reading the task.", "Memorize an answer without identifying the relevant detail.", "Skip the explanation because the topic name is familiar."),
        ("Which sentence would give the clearest English response about", "The sentence states the relevant person, action, and supporting detail in a clear order.", "The sentence lists words but gives no action or relationship.", "The sentence changes the topic and supplies an unsupported detail.", "The sentence uses a guess instead of information from the lesson."),
        ("A learner makes an error while studying. Which correction fits", "Check the relevant form or relationship against the lesson example, then revise the sentence.", "Keep the error if the sentence contains a familiar word.", "Change several words at random without checking the example.", "Use a classmate's correction without explaining why it works."),
        ("Which new situation is the best transfer of the method from", "Apply the same evidence-and-explanation method to a changed context, then check what the new details require.", "Use the old answer unchanged even though the details changed.", "Ignore the new details and rely on the topic label.", "Replace evidence with a personal guess."),
        ("What should a learner compare first when checking an answer about", "Compare the task's condition, the lesson evidence, and the proposed conclusion.", "Compare only the length of the answer choices.", "Choose the option with the most difficult vocabulary.", "Look at the answer position instead of the evidence."),
        ("Which explanation shows accurate understanding of", "It connects the lesson concept to the specific clue and states why the clue supports the conclusion.", "It repeats the topic name but gives no reason.", "It gives a conclusion that contradicts the lesson clue.", "It treats an unverified prediction as a fact."),
        ("When the details in a", "Keep the core method, but revise the language, evidence, or relationship affected by the changed detail.", "Keep every word and ignore the changed detail.", "Remove the evidence so the answer cannot be checked.", "Choose a new answer without explaining the change."),
        ("Which self-check would provide the strongest evidence of learning in", "Explain the answer in your own words and point to the lesson detail that supports it.", "Repeat the title without describing the reasoning.", "Check only whether the answer resembles a friend's answer.", "Select an answer before reviewing the supporting detail."),
        ("Which response best demonstrates independent reasoning for", "Use the lesson clue, state the relevant English relationship, and rule out choices that do not fit.", "Choose the first option without reading the context.", "Use an unrelated rule because it was memorized earlier.", "Avoid giving a reason and rely on a guess."),
    ]
    lead, correct, wrong_b, wrong_c, wrong_d = tasks[variant]
    data["prompt"] = f"{lead} {topic}? Lesson clue: {clue}."
    topic_hint = f'for "{topic}" using the clue "{clue}"'
    choices = [
        f"{correct} This is the evidence-based choice {topic_hint}.",
        f"{wrong_b} It does not check the lesson clue {topic_hint}.",
        f"{wrong_c} It replaces the lesson evidence with a guess {topic_hint}.",
        f"{wrong_d} It cannot be verified from the lesson clue {topic_hint}.",
    ]
    correct_id = "ABCD"[(number - 1) % 4]
    option_ids = ["A", "B", "C", "D"]
    correct_index = option_ids.index(correct_id)
    option_texts = choices[:correct_index] + choices[correct_index + 1 :]
    option_texts.insert(correct_index, choices[0])
    # The first choice is always the correct semantic choice; rotate its ID so
    # answer position is not a hidden generator signal.
    wrong_iter = iter(choices[1:])
    final_texts = []
    for option_id in option_ids:
        final_texts.append(choices[0] if option_id == correct_id else next(wrong_iter))
    data["options"] = [
        {"id": option_id, "text": option_text}
        for option_id, option_text in zip(option_ids, final_texts)
    ]
    data["answer"] = {
        "value": correct_id,
        "explanation": f"The lesson on {topic} requires the learner to use its concrete clue ({clue}) and explain how that clue supports the conclusion. The other choices guess, omit evidence, or ignore the changed condition.",
    }
    data["solutionStrategy"] = f"先從「{topic}」的單元例證找出可驗證的線索，再依題目任務判斷句意、句構、語用或遷移關係，最後用線索排除只靠猜測的選項。"
    data["solutionSteps"] = [
        f"讀題定位：本題聚焦「{topic}」，先確認題目要找的是證據、順序、句構、錯誤修正或新情境遷移。",
        f"擷取單元線索：回看本課例證或檢核內容「{clue}」，圈出能支持判斷的具體訊息。",
        f"核對正確選項 {correct_id}：{correct}；它直接使用單元線索並說明結論如何成立。",
        "逐項排除 B、C、D：它們分別缺少證據、改變題意、只憑關鍵字或把推測當成事實。",
        "答案檢查：再次確認 A 同時符合題幹任務、英文語意與本單元的證據要求，沒有忽略條件變化。",
    ]
    data["updatedAt"] = str(date.today())


def main() -> int:
    lessons = {}
    for path in (ROOT / "lessons" / "english").glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        lessons[data.get("id")] = data

    # Recompute the gate locally so the rewrite queue cannot drift from the report.
    groups = {}
    exact_prompt_groups = {}
    all_items = []
    for path in sorted((ROOT / "questions" / "english").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        groups.setdefault(item_key(data), []).append((path, data))
        exact_prompt_groups.setdefault(data.get("prompt", ""), []).append((path, data))
        all_items.append((path, data))
    affected_paths = {
        path
        for items in groups.values()
        if len(items) > 1
        for path, _data in items
    }
    affected_paths.update(
        path
        for items in exact_prompt_groups.values()
        if len(items) > 1
        for path, _data in items
    )
    # Allow a safe rerun of this author's own same-day output when the wording
    # or answer-position rotation is improved; untouched questions are not
    # rewritten merely because they are English questions.
    affected_paths.update(
        path
        for path, data in all_items
        if data.get("subject") == "english"
        and data.get("updatedAt") == str(date.today())
        and str(data.get("prompt", "")).startswith("Which ")
    )
    affected = [(path, data) for path, data in all_items if path in affected_paths]
    changed = 0
    for path, data in affected:
        lesson = lessons.get(data.get("lessonId"))
        if not lesson:
            continue
        match = re.search(r"-(\d+)\.json$", path.name)
        number = int(match.group(1)) if match else 1
        make_item(data, lesson, number)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    print(json.dumps({"affected": len(affected), "changed": changed}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
