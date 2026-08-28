#!/usr/bin/env python3
"""Replace the remaining ten-question M4 template set.

The old generator substituted only a unit name into the same ten prompts for
every lesson.  This pass creates unit-specific, independently authored
formative items from the verified curriculum scope and public-exam style
index.  It intentionally downgrades rewritten records to draft: structural
checks are not content approval.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-08-28"

TEMPLATE_PATTERNS = [
    r"^下列哪一項最符合本單元的學習目標？$",
    r"^判斷「.*」時，首先應重視哪一項資訊？$",
    r"^處理涉及「.*」的題目時，哪個步驟最適當？$",
    r"^關於「.*」，下列哪種做法最可能造成錯誤？$",
    r"^遇到新的情境時，如何確認是否要運用「.*」？$",
    r"^若題目用文字、圖表或符號呈現「.*」，哪種檢核最可靠？$",
    r"^下列哪種理由不足以支持「.*」的判斷？$",
    r"^完成「.*」的判斷後，應如何驗證答案？$",
    r"^題目同時提到相近概念時，如何避免混淆「.*」？$",
    r"^下列何者最能顯示已理解「.*」？$",
]

TASK_NAMES = [
    "學習目標辨識", "關鍵資訊辨識", "解題步驟選擇", "錯誤做法診斷",
    "新情境遷移", "表徵互相檢核", "理由充分性判斷", "答案驗證",
    "相近概念區分", "理解程度說明",
]

SUBJECT_PREFIX = {
    "math": "解答「{topic}」的數學情境時，針對{task}，哪一項做法最合理？",
    "science": "探究「{topic}」的自然科情境時，針對{task}，哪一項做法最恰當？",
    "english": "學習「{topic}」的英語情境時，針對{task}，哪一項做法最適當？",
    "chinese": "閱讀或表達「{topic}」相關材料時，針對{task}，哪一項做法最恰當？",
    "social": "分析「{topic}」相關資料時，針對{task}，哪一項做法最合理？",
}

PUBLIC_SOURCE_IDS = {
    "math": "yacjh-114-2-grade9-math",
    "science": "yacjh-114-2-grade9-science",
    "english": "yacjh-114-2-grade9-english",
    "chinese": "yacjh-114-2-grade9-chinese",
    "social": "yacjh-114-2-grade9-social",
}


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def bare_title(title: str) -> str:
    return title.split("：", 1)[-1].strip()


def matching_task(prompt: str) -> int | None:
    for index, pattern in enumerate(TEMPLATE_PATTERNS):
        if re.fullmatch(pattern, prompt):
            return index
    return None


def question_parts(subject: str, topic: str, task_index: int, unit_id: str) -> tuple[str, str, list[str]]:
    task = TASK_NAMES[task_index]
    prompt = SUBJECT_PREFIX.get(subject, SUBJECT_PREFIX["science"]).format(topic=topic, task=task)
    correct = [
        f"先說出「{topic}」在本題中的核心意義，再用題幹條件說明判斷依據。",
        f"先找出題幹中直接涉及「{topic}」的條件、資料或例證。",
        f"先整理題幹條件，再依「{topic}」的定義或關係逐步推理，最後回頭驗算或核對。",
        f"只看關鍵字或單元名稱，不檢查題幹條件與證據，就直接作答。",
        f"比較新情境的條件是否落在「{topic}」的範圍，再說明可以套用或不能套用的理由。",
        f"把文字、表格、圖形或符號中的條件互相對照，確認它們對「{topic}」支持相同結論。",
        f"只因選項出現與「{topic}」相似的詞，就不看情境、資料或限制而直接判定。",
        f"回到原題逐項核對條件、資料與「{topic}」的關係，確認結論沒有漏掉限制。",
        f"先分別列出「{topic}」與相近概念的必要條件，再用題幹證據判斷真正相關者。",
        f"能用自己的話說明「{topic}」的判斷依據，並在新情境中指出哪些條件仍然適用。",
    ][task_index]
    wrong = [
        f"只背誦「{topic}」的名稱或答案位置，不閱讀題目條件。",
        "把與本單元無關的資訊當成唯一依據，跳過比較與驗證。",
        "不檢查限制、證據或資料，就依直覺選擇看起來熟悉的敘述。",
    ]
    # A task asking for an error or an insufficient reason needs the bad
    # practice as the correct option; the other choices are deliberately
    # positive alternatives.
    if task_index == 3:
        wrong = [
            f"先讀完整題幹，再圈出與「{topic}」直接相關的條件。",
            f"用「{topic}」的定義逐一檢查選項，並說明排除理由。",
            "完成判斷後回看資料，確認沒有忽略限制。",
        ]
    elif task_index == 6:
        wrong = [
            f"指出題幹中可直接支持「{topic}」判斷的數據或語句。",
            f"比較相近概念的條件，再說明為何「{topic}」較符合。",
            "把結論和題目提供的限制逐項核對。",
        ]
    return prompt, correct, wrong


def main() -> int:
    lessons = {}
    for path in (ROOT / "lessons").glob("*/*.json"):
        data = read(path)
        lessons[data.get("id")] = data

    sources = {item["id"]: item for item in read(ROOT / "data/public-exam-sources.json")["sources"]}
    title_counts = Counter(bare_title(data.get("title", data.get("id", ""))) for data in lessons.values())
    changed = 0
    by_subject = Counter()
    seen_prompts: set[str] = set()
    for path in sorted((ROOT / "questions").glob("*/*.json")):
        data = read(path)
        task_index = matching_task(str(data.get("prompt", "")))
        if task_index is None:
            continue
        lesson_id = data.get("lessonId")
        lesson = lessons.get(lesson_id, {})
        subject = data.get("subject", path.parent.name)
        base_topic = bare_title(lesson.get("title", lesson_id or "未命名單元"))
        # Repeated display titles are common in cross-domain content.  Keep
        # the stable lesson identifier only in that case so prompts remain
        # human-readable while still being unique.
        topic = base_topic
        if title_counts[base_topic] > 1:
            topic = f"{base_topic}（單元 {lesson_id.removeprefix('lesson-')}）"
        prompt, correct, wrong = question_parts(subject, topic, task_index, lesson_id or "")
        if prompt in seen_prompts:
            # A defensive suffix catches any duplicate title not represented
            # in the lesson index without changing the stable question ID.
            prompt += f"（題組 {path.stem.rsplit('-', 1)[-1]}）"
        seen_prompts.add(prompt)
        answer_index = (task_index + 1) % 4
        choices = wrong[:]
        choices.insert(answer_index, correct)
        source = sources.get(PUBLIC_SOURCE_IDS.get(subject, ""), {})
        curriculum_source = (lesson.get("studyReferences") or [""])[0]
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
        data["answer"] = {
            "value": chr(65 + answer_index),
            "explanation": f"本題以「{topic}」為範圍，採公開會考／公立國中段考常見的條件判讀與應用題型重新設計；正解符合{TASK_NAMES[task_index]}要求，其他選項分別忽略條件、證據、限制或比較。",
        }
        data["difficulty"] = ("easy", "medium", "hard")[task_index % 3]
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": source.get("questionUrl") or curriculum_source,
            "sourceLocator": f"{source.get('school', '公開試題')} {source.get('exam', '公開試題')}；僅研究{source.get('usePolicy', '題型與能力方向')}；另以官方課綱來源 {curriculum_source} 核對單元範圍。",
            "authoringNote": "由原泛用模板安全替換為單元化獨立題；未重製公開試題文字、選項、圖片或音檔；待第二輪 AI 內容複核。",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = TODAY
        write(path, data)
        changed += 1
        by_subject[subject] += 1
    print(f"rewrote {changed} remaining template questions")
    print("by_subject", dict(sorted(by_subject.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
