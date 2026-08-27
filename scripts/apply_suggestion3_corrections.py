#!/usr/bin/env python3
"""Apply the source-backed structural corrections from ChatGPT suggestion 3."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def curriculum(subject: str) -> dict[str, dict]:
    return {json.loads(p.read_text())["id"]: json.loads(p.read_text()) for p in (ROOT / "curriculum" / subject).glob("*.json")}


def source(subject: str) -> str:
    return next(json.loads(p.read_text())["source"]["url"] for p in (ROOT / "curriculum" / subject).glob("*.json"))


def write_unit(subject: str, unit_id: str, title: str, ids: list[str], teachable: bool, source_type: str, locator: str, confidence: str) -> None:
    data = {"id": unit_id, "subject": subject, "title": title, "teachable": teachable, "gradeRange": ["7", "8", "9"], "curriculumIds": ids, "status": "mapped", "source": {"type": source_type, "url": source(subject), "locator": locator, "verifiedAt": "2026-08-26", "confidence": confidence}}
    (ROOT / "canonical-units" / subject / f"{unit_id}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def write_mapping(subject: str, key: str, unit_id: str, ids: list[str], relation: str, source_type: str, locator: str, confidence: str) -> None:
    data = {"id": f"unit-map-{subject}-{key}", "subject": subject, "unitId": unit_id, "curriculumIds": ids, "relation": relation, "status": "mapped", "evidence": {"type": source_type, "url": source(subject), "locator": locator, "verifiedAt": "2026-08-26", "confidence": confidence}}
    (ROOT / "canonical-units" / subject / "mappings" / f"unit-map-{subject}-{key}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def main() -> None:
    # Root/domain nodes are taxonomy only.
    for subject, filename, title, curriculum_id, locator in [
        ("chinese", "canonical-unit-chinese-language-arts-domain.json", "語文領域－國語文", "cur-chinese-learning-content", "PDF p.1 封面；伍、學習重點；二、學習內容，PDF p.13-14；領域／科目根節點。"),
        ("english", "canonical-unit-english-language-domain.json", "語文領域－英語文", "cur-english-learning-content", "PDF p.17-18；伍、學習重點／二、學習內容；領域／科目根節點。"),
    ]:
        unit_path = ROOT / "canonical-units" / subject / filename
        unit = json.loads(unit_path.read_text())
        unit.update({"title": title, "teachable": False, "status": "mapped"})
        unit["source"].update({"type": "official-curriculum", "locator": locator, "confidence": "high"})
        unit_path.write_text(json.dumps(unit, ensure_ascii=False, indent=2) + "\n")
        key = filename.removeprefix(f"canonical-unit-{subject}-").removesuffix(".json")
        mapping_path = ROOT / "canonical-units" / subject / "mappings" / f"unit-map-{subject}-{key}.json"
        mapping = json.loads(mapping_path.read_text())
        mapping.update({"relation": "classifies", "status": "mapped"})
        mapping["evidence"].update({"type": "official-curriculum", "locator": locator, "confidence": "high"})
        mapping_path.write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n")

    ch = curriculum("chinese")
    ab_groups = {
        "character-foundations": [f"cur-chinese-content-ab-iv-{i}" for i in (1, 2, 3)],
        "vocabulary": [f"cur-chinese-content-ab-iv-{i}" for i in (4, 5)],
        "classical-lexicon": [f"cur-chinese-content-ab-iv-{i}" for i in (6, 7)],
        "calligraphy": ["cur-chinese-content-ab-iv-8"],
    }
    ab_locator = "伍、學習重點／二、學習內容／文字篇章／2.字詞；PDF viewer P15；Ab-Ⅳ-1～Ab-Ⅳ-8。"
    parent = json.loads((ROOT / "canonical-units/chinese/canonical-unit-chinese-content-ab.json").read_text())
    parent["teachable"] = False
    parent["source"].update({"type": "official-curriculum", "locator": ab_locator, "confidence": "high"})
    (ROOT / "canonical-units/chinese/canonical-unit-chinese-content-ab.json").write_text(json.dumps(parent, ensure_ascii=False, indent=2) + "\n")
    parent_map = json.loads((ROOT / "canonical-units/chinese/mappings/unit-map-chinese-content-ab.json").read_text())
    parent_map.update({"relation": "classifies", "status": "mapped"})
    parent_map["evidence"].update({"type": "official-curriculum", "locator": ab_locator, "confidence": "high"})
    (ROOT / "canonical-units/chinese/mappings/unit-map-chinese-content-ab.json").write_text(json.dumps(parent_map, ensure_ascii=False, indent=2) + "\n")
    titles = {"character-foundations": "常用字、字形音義與造字原則", "vocabulary": "常用語詞的認念與使用", "classical-lexicon": "文言詞義、虛字與古今義變", "calligraphy": "各體書法與名家碑帖欣賞"}
    for key, ids in ab_groups.items():
        unit_id = f"canonical-unit-chinese-content-ab-{key}"
        write_unit("chinese", unit_id, titles[key], ids, True, "canonical-design", f"官方 Ab-Ⅳ 條目分組；{ab_locator}；child unit 為本專案教學設計。", "medium")
        write_mapping("chinese", f"content-ab-{key}", unit_id, ids, "covers", "canonical-design", f"官方 Ab-Ⅳ 條目分組；{ab_locator}；child mapping 為本專案教學設計。", "medium")

    en_groups = {
        "narrative-literary": ([1, 6, 7, 8], "敘事與文學篇章理解"),
        "public-multimodal": ([2, 3], "圖表與公共廣播資訊"),
        "functional-multigenre": ([4, 5], "實用與多體裁文本"),
    }
    ae_ids = [f"cur-english-content-ae-iv-{i}" for i in range(1, 9)]
    ae_locator = "學習內容表，PDF p.17-18，A.語言知識／e.篇章；Ae-Ⅳ-1～Ae-Ⅳ-8。"
    parent = json.loads((ROOT / "canonical-units/english/canonical-unit-english-content-ae.json").read_text())
    parent["teachable"] = False
    parent["source"].update({"type": "official-curriculum", "locator": ae_locator, "confidence": "high"})
    (ROOT / "canonical-units/english/canonical-unit-english-content-ae.json").write_text(json.dumps(parent, ensure_ascii=False, indent=2) + "\n")
    parent_map = json.loads((ROOT / "canonical-units/english/mappings/unit-map-english-content-ae.json").read_text())
    parent_map.update({"relation": "classifies", "status": "mapped"})
    parent_map["evidence"].update({"type": "official-curriculum", "locator": ae_locator, "confidence": "high"})
    (ROOT / "canonical-units/english/mappings/unit-map-english-content-ae.json").write_text(json.dumps(parent_map, ensure_ascii=False, indent=2) + "\n")
    for key, (numbers, title) in en_groups.items():
        ids = [f"cur-english-content-ae-iv-{i}" for i in numbers]
        unit_id = f"canonical-unit-english-content-ae-{key}"
        write_unit("english", unit_id, title, ids, True, "canonical-design", f"官方 Ae-Ⅳ 條目分組；{ae_locator}；child unit 為本專案教學設計。", "medium")
        write_mapping("english", f"content-ae-{key}", unit_id, ids, "covers", "canonical-design", f"官方 Ae-Ⅳ 條目分組；{ae_locator}；child mapping 為本專案教學設計。", "medium")

    # Repoint only questions whose declared KG endpoint identifies a split child.
    target_by_code = {**{f"kg-chinese-content-ab-iv-{i}": f"canonical-unit-chinese-content-ab-{key}" for key, nums in ab_groups.items() for i in nums}, **{f"kg-english-content-ae-iv-{i}": f"canonical-unit-english-content-ae-{key}" for key, (nums, _) in en_groups.items() for i in nums}}
    for subject in ("chinese", "english"):
        manifest_path = ROOT / "migrations" / f"{subject}-question-migration-pilot.json"
        manifest = json.loads(manifest_path.read_text())
        for item in manifest["items"]:
            qpath = next(ROOT.rglob(f"{item['questionId']}.json"))
            question = json.loads(qpath.read_text())
            targets = [target_by_code[k] for k in question.get("knowledgeIds", []) if k in target_by_code]
            if len(targets) == 1:
                item["targetUnitId"] = targets[0]
                item["migrationStatus"] = "pending-review"
                item["notes"] = "已依 split child 的官方 leaf code 指向候選 unit；題目語意仍待內容審核。"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print("applied domain, Chinese Ab, English Ae, and question target corrections")


if __name__ == "__main__":
    main()
