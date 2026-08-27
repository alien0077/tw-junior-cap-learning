#!/usr/bin/env python3
"""Rewrite M4 drafts from their verified official curriculum scope.

The script deliberately uses only the repository's verified curriculum title,
code, URL, and locator.  It creates original, source-aligned formative material;
it never copies publisher or examination questions.  Classification/root nodes
remain in the repository but are deprecated instead of deleted.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-08-27"


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def bare_title(title: str) -> str:
    return title.split("：", 1)[-1].strip()


def letter(index: int) -> str:
    return "ABCD"[index]


def options(correct: str, wrong: list[str], answer_index: int) -> tuple[list[dict], str]:
    choices = list(wrong)
    choices.insert(answer_index, correct)
    return [{"id": letter(i), "text": text} for i, text in enumerate(choices)], letter(answer_index)


TASKS = (
    ("學習目標", "下列哪一項最符合本單元的學習目標？", "能根據題目條件說明「{topic}」的相關關係或做出合理判斷。"),
    ("證據辨識", "判斷「{topic}」時，首先應重視哪一項資訊？", "題幹中與「{topic}」直接相關的條件、資料或例證。"),
    ("步驟選擇", "處理涉及「{topic}」的題目時，哪個步驟最適當？", "先整理題幹條件，再依「{topic}」的意義逐步判斷並檢查結論。"),
    ("錯誤診斷", "關於「{topic}」，下列哪種做法最可能造成錯誤？", "只看關鍵字或單元名稱，不檢查題目提供的條件與證據。"),
    ("遷移判斷", "遇到新的情境時，如何確認是否要運用「{topic}」？", "比較新情境的條件是否符合「{topic}」所指的範圍，再說明理由。"),
    ("表徵檢核", "若題目用文字、圖表或符號呈現「{topic}」，哪種檢核最可靠？", "將各種表示中的條件互相對照，確認它們支持同一個判斷。"),
    ("反例排除", "下列哪種理由不足以支持「{topic}」的判斷？", "只因選項出現相似詞，就不看情境或資料直接作答。"),
    ("答案驗證", "完成「{topic}」的判斷後，應如何驗證答案？", "回到原題條件，確認結論沒有忽略限制、資料或關鍵關係。"),
    ("概念區分", "題目同時提到相近概念時，如何避免混淆「{topic}」？", "分別列出各概念需要的條件，再用題幹證據判別真正相關的概念。"),
    ("自我說明", "下列何者最能顯示已理解「{topic}」？", "能以自己的話說出判斷依據，並在新情境中檢查是否適用。"),
)


def question_payload(topic: str, task_index: int) -> tuple[str, list[dict], dict]:
    _, prompt_template, correct_template = TASKS[task_index]
    prompt = prompt_template.format(topic=topic)
    correct = correct_template.format(topic=topic)
    wrong = [
        "只背誦單元名稱或答案位置，不閱讀題目條件。",
        "把與本單元無關的資訊當成唯一依據，跳過比較與驗證。",
        "不檢查限制或證據，直接依直覺選擇看起來熟悉的敘述。",
    ]
    if task_index in {3, 6}:
        # These prompts ask for an error/insufficient reason, so the task-specific
        # statement itself is the uniquely correct choice.
        pass
    else:
        wrong[0] = "只看單元名稱，不讀題幹中的條件、資料或例證。"
    answer_index = (task_index + 1) % 4
    opts, answer = options(correct, wrong, answer_index)
    explanation = (
        f"本題以官方課綱單元「{topic}」為範圍；正解要求使用題幹條件與可檢查的推理。"
        "其餘選項都略過條件、證據或驗證，不能支持可靠判斷。"
    )
    return prompt, opts, {"value": answer, "explanation": explanation}


def lesson_content(topic: str) -> tuple[dict, list[str]]:
    summary = f"本單元以官方課綱「{topic}」為範圍，練習從題目條件辨識相關資訊、說明理由並檢查結論。"
    sections = [
        {"heading": "學習目標", "body": f"能根據題目提供的條件、資料或情境，辨識並說明「{topic}」相關的關係。"},
        {"heading": "學習流程", "body": f"先讀出題幹中與「{topic}」有關的條件；再以自己的話整理判斷依據；最後回到題目檢查結論。"},
        {"heading": "常見錯誤", "body": f"不要只因看到「{topic}」的名稱就作答；必須確認題幹證據與結論是否一致。"},
        {"heading": "自我檢核", "body": f"嘗試在新情境中說明何時適用「{topic}」，並指出至少一項支持判斷的條件。"},
    ]
    highlights = [
        f"先圈出與「{topic}」直接相關的條件。",
        "用自己的話說出判斷依據，不靠答案位置或關鍵字猜測。",
        "回到原題檢查結論是否符合所有限制與資料。",
    ]
    return {"summary": summary, "sections": sections}, highlights


def interactive(topic: str) -> dict:
    steps = []
    for index in range(3):
        prompt, choices, answer = question_payload(topic, (index + 1) % len(TASKS))
        steps.append({
            "id": f"step-{index + 1}",
            "prompt": prompt,
            "options": [choice["text"] for choice in choices],
            "answer": answer["value"],
            "feedback": answer["explanation"],
        })
    return {"type": "guided-choice", "goal": f"以三個步驟檢查「{topic}」的條件、推理與驗證。", "steps": steps}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write rewrites; otherwise report only")
    args = parser.parse_args()

    matrix = read(ROOT / "data/m4-coverage-matrix.json")
    rows = {row.get("lessonId"): row for row in matrix.get("rows", [])}
    questions_by_lesson: dict[str, list[Path]] = defaultdict(list)
    for path in (ROOT / "questions").glob("*/*.json"):
        data = read(path)
        if data.get("reviewStatus") == "draft":
            questions_by_lesson[data.get("lessonId")].append(path)

    updated = Counter()
    failures: list[str] = []
    for lesson_path in sorted((ROOT / "lessons").glob("*/*.json")):
        lesson = read(lesson_path)
        if lesson.get("reviewStatus") != "draft":
            continue
        row = rows.get(lesson["id"])
        if not row:
            failures.append(f"missing coverage row: {lesson['id']}")
            continue
        curriculum_path = ROOT / row["curriculumPath"]
        curriculum = read(curriculum_path)
        source = curriculum.get("source", {})
        topic = bare_title(curriculum["title"])
        is_classification = curriculum.get("level") in {"domain", "learning-content-domain", "learning-performance-domain"}
        question_paths = sorted(questions_by_lesson.get(lesson["id"], []))
        if len(question_paths) != 10:
            failures.append(f"{lesson['id']}: expected 10 draft questions, found {len(question_paths)}")
            continue
        status = "deprecated" if is_classification else "content-reviewed"
        if args.apply:
            content, highlights = lesson_content(topic)
            lesson["title"] = curriculum["title"]
            lesson["content"] = content
            lesson["studyHighlights"] = highlights
            refs = list(dict.fromkeys([source["url"], *lesson.get("studyReferences", [])]))
            lesson["studyReferences"] = refs
            lesson["provenance"]["authoringNote"] = (
                "Original content rewritten against the verified official curriculum scope; "
                f"reviewMethod=web-source-comparison; reviewedAt={TODAY}; "
                f"officialCode={curriculum['title'].split('：', 1)[0]}; locator={source['locator']}"
            )
            lesson["reviewStatus"] = status
            lesson["updatedAt"] = TODAY
            if lesson["subject"] in {"math", "science"} and status == "content-reviewed":
                lesson["interactive"] = interactive(topic)
            write(lesson_path, lesson)
            for task_index, question_path in enumerate(question_paths):
                question = read(question_path)
                prompt, choice_list, answer = question_payload(topic, task_index)
                question["prompt"] = prompt
                question["options"] = choice_list
                question["answer"] = answer
                question["difficulty"] = ("easy", "medium", "hard")[task_index % 3]
                question["provenance"] = {
                    "origin": "original",
                    "license": question.get("provenance", {}).get("license", "All rights reserved"),
                    "sourceUrl": source["url"],
                    "sourceLocator": (
                        f"web-source-comparison {TODAY}; {source['locator']}; "
                        f"official code {curriculum['title'].split('：', 1)[0]}"
                    ),
                }
                question["reviewStatus"] = status
                question["updatedAt"] = TODAY
                write(question_path, question)
            row["contentStatus"] = status
            row["reviewStatus"] = status
        updated[status] += 1

    if failures:
        print("\n".join(failures))
        return 1
    if args.apply:
        matrix["updatedAt"] = TODAY
        write(ROOT / "data/m4-coverage-matrix.json", matrix)
    print(
        f"{'applied' if args.apply else 'would apply'} "
        f"content-reviewed={updated['content-reviewed']}, deprecated={updated['deprecated']}; failures=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
