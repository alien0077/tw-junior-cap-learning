#!/usr/bin/env python3
"""Remove residual generator labels from older English question surfaces."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def clean_text(value: str) -> str:
    value = re.sub(r"\bIn question \d+,\s*", "", value, flags=re.I)
    value = re.sub(r"\bFor item \d+ in the [^,]+ notice,\s*", "", value, flags=re.I)
    value = re.sub(r"\s+in the [A-Za-z0-9ⅰ-ⅹ-]+／[^ ]+ lesson", "", value, flags=re.I)
    value = re.sub(r"\s+in the [A-Za-z0-9ⅰ-ⅹ-]+／[^ ]+ task", "", value, flags=re.I)
    value = re.sub(r"\s+about [A-Za-z0-9ⅰ-ⅹ-]+／[^?]+", "", value, flags=re.I)
    return re.sub(r"\s+", " ", value).strip()


def update_solution(data: dict, old_prompt: str) -> None:
    answer_id = str(data.get("answer", {}).get("value", ""))
    option = next((item.get("text", "") for item in data.get("options", []) if str(item.get("id")) == answer_id), "")
    steps = data.get("solutionSteps", [])
    if steps:
        steps[0] = f"讀題定位：先找出本題要判斷的核心條件與限制；題幹是「{data.get('prompt', '')}」。"
    if len(steps) >= 3:
        steps[2] = f"核對正確選項 {answer_id}：{option}。依題目解析，{data.get('answer', {}).get('explanation', '')}"
    data["solutionSteps"] = steps
    data["updatedAt"] = str(date.today())


def main() -> int:
    lessons = {}
    for lesson_path in (ROOT / "lessons" / "english").glob("*.json"):
        lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
        lessons[lesson.get("id")] = lesson
    changed = 0
    for path in sorted((ROOT / "questions" / "english").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        old_prompt = str(data.get("prompt", ""))
        prompt = old_prompt
        match = re.fullmatch(r"In thewhat does [“\"]([^”\"]+)[”\"] mean in question \d+\?", prompt, flags=re.I)
        if not match:
            match = re.fullmatch(r"In this lesson context, what does [“\"]([^”\"]+)[”\"] mean\?", prompt, flags=re.I)
        if not match:
            match = re.fullmatch(r"In the lesson “[^”]+”, what does [“\"]([^”\"]+)[”\"] mean\?", prompt, flags=re.I)
        if match:
            title = lessons.get(data.get("lessonId"), {}).get("title", data.get("lessonId", "this lesson"))
            prompt = f'In the lesson “{title}”, what does “{match.group(1)}” mean?'
        elif prompt.startswith("Read this「") or ", Read this notice" in prompt:
            if ", Read this notice" in prompt:
                prompt = prompt.split(", Read this notice", 1)[1].strip()
                prompt = "Read this notice" + prompt
            prompt = re.sub(r"^Read this「[^」]+」notice", "Read this notice", prompt)
            prompt = re.sub(r", item \d+:", ":", prompt)
            title = lessons.get(data.get("lessonId"), {}).get("title", data.get("lessonId", "this lesson"))
            prompt = f'In the lesson “{title}”, {prompt}'
        elif prompt.startswith("Read this notice"):
            title = lessons.get(data.get("lessonId"), {}).get("title", data.get("lessonId", "this lesson"))
            prompt = f'In the lesson “{title}”, {prompt}'
        prompt = clean_text(prompt)
        options = [{**option, "text": clean_text(str(option.get("text", "")))} for option in data.get("options", [])]
        if prompt != old_prompt or options != data.get("options", []):
            data["prompt"] = prompt
            data["options"] = options
            update_solution(data, old_prompt)
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
    print(json.dumps({"changed": changed}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
