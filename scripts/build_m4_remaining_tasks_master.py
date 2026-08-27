#!/usr/bin/env python3
"""Build a single current M4 remaining-work checklist from repository data."""
from __future__ import annotations

import collections
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def count_status(directory: str):
    counter = collections.Counter()
    for path in glob.glob(str(ROOT / directory / "*" / "*.json")):
        counter[json.loads(Path(path).read_text()).get("reviewStatus", "unknown")] += 1
    return counter


def main() -> None:
    rows = json.loads((ROOT / "data/m4-coverage-matrix.json").read_text())["rows"]
    lessons = count_status("lessons")
    questions = count_status("questions")
    manifests = []
    unresolved = 0
    for path in sorted((ROOT / "migrations").glob("*-question-migration-pilot.json")):
        data = json.loads(path.read_text())
        count = sum(item.get("targetUnitId") is None for item in data["items"])
        unresolved += count
        manifests.append(f"| {data['subject']} | {len(data['items'])} | {count} |")
    lines = [
        "# M4 未完成任務總表（目前快照）",
        "",
        "更新：2026-08-26。此文件由目前 repo 資料產生；不可把結構驗證、固定題數或 `mapped` 當成教師／出版社正式審核。",
        "",
        "## 已有客觀證據的完成項目",
        "",
        f"- coverage rows：{len(rows)}/{len(rows)}。",
        f"- lessons：{sum(lessons.values())}（content-reviewed {lessons['content-reviewed']}、draft {lessons['draft']}）。",
        f"- questions：{sum(questions.values())}（content-reviewed {questions['content-reviewed']}、draft {questions['draft']}）。",
        "- 每 lesson 至少 10 題；數學／自然每 lesson 至少 3 步互動；本地與 GitHub Actions validator 均通過。",
        "",
        "## 尚未完成一：逐題 migration target",
        "",
        "以下 manifest 中 targetUnitId 為 null 的題目，必須依題目語意與官方課綱決定，不可自動猜測：",
        "",
        "| 科目 | manifest 題數 | 無唯一 target 題數 |",
        "|---|---:|---:|",
        *manifests,
        f"| 合計 | — | {unresolved} |",
        "",
        "逐題清單：`docs/M4_UNRESOLVED_MIGRATION_HANDOFF.md`。",
        "",
        "## 尚未完成二：draft 內容 QA",
        "",
        f"- {lessons['draft']} 個 draft lesson 尚未完成學科內容核對與重寫。",
        f"- {questions['draft']} 題 draft question 尚未完成逐題答案／解析／選項核對。",
        "- 重複題幹逐題清單：`docs/M4_DRAFT_DUPLICATE_QUESTION_HANDOFF.md`。",
        "- aggregate QA：`docs/M4_DRAFT_QA_REPORT.md`。",
        "- 需要外部學科判斷的回傳欄位：questionId、decision、targetUnitId、reason、sourceUrl、sourceLocator、重寫建議。",
        "",
        "## 尚未完成三：canonical unit 語意核驗",
        "",
        "- 161 個 canonical units 目前只代表資料層候選與 mapping；尚未全部 verified。",
        "- 國文 Ab child 分組、英文 Ae child 分組仍需確認教學粒度。",
        "- 自然跨科主題與社會地理／歷史／公民 grouping 需逐項確認是否 teachable。",
        "- 不可升級項目與建議來源欄位：`docs/CHATGPT_M4_BLOCKERS_HANDOFF.md`。",
        "",
        "## 尚未完成四：出版社章節來源",
        "",
        "- 南一 30 冊：缺完整出版社正式章節目次與逐碼 KG 對照。",
        "- 翰林非國文 24 冊：缺完整出版社正式逐冊目次與逐碼 KG 對照。",
        "- 校方課程計畫／教育平台只能作交叉證據，不能宣稱出版社背書。",
        "",
        "## 外部 ChatGPT 必須回傳",
        "",
        "1. 每個 unit 或題目決策：keep／split／merge／classification-only／blocked。",
        "2. 官方 curriculum code、公開 URL、PDF 頁碼／章節／表格定位。",
        "3. 哪些資料可升級 `verified`，哪些只能維持 `mapped`／`pending-review`。",
        "4. 找不到來源時明確標記 `blocked`，不得捏造頁碼或出版社章名。",
        "",
        "## Repo 接手後驗收",
        "",
        "Codex 只在收到上述可追溯結果後套用資料、更新狀態、執行 validator、更新文件並推送；不會自行把 draft 或 mapped 冒充 verified。",
    ]
    (ROOT / "docs/M4_REMAINING_TASKS_MASTER.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote master checklist; unresolved migration={unresolved}")


if __name__ == "__main__":
    main()
