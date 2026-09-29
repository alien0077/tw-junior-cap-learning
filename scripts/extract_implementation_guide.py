#!/usr/bin/env python3
"""Extract the per-unit YAML contracts from the implementation guide.

The guide is the source document for the implementation contract. Extraction is
deliberately lossless at the YAML-object level and never changes completion
status or evidence claims.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


UNIT_RE = re.compile(r"^### (cur-[^ —]+) —", re.MULTILINE)
BLOCK_RE = re.compile(r"```yaml\n(.*?)\n```", re.DOTALL)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("guide", type=Path)
    parser.add_argument("--output", type=Path, default=Path("implementation/unit-specs"))
    parser.add_argument("--manifest", type=Path, default=Path("implementation/unit-specs.manifest.json"))
    args = parser.parse_args()

    text = args.guide.read_text(encoding="utf-8")
    raw_blocks = BLOCK_RE.findall(text)
    # The guide begins with YAML examples and schema fragments before its
    # per-unit sections. Select only actual unit contracts instead of assuming
    # the first fenced YAML block is the sole non-unit block.
    blocks = []
    for block in raw_blocks:
        try:
            document = yaml.safe_load(block)
        except yaml.YAMLError:
            continue
        if isinstance(document, dict) and isinstance(document.get("unitImplementationSpec"), dict):
            blocks.append(block)
    headings = UNIT_RE.findall(text)
    if len(blocks) != len(headings):
        raise SystemExit(f"guide extraction mismatch: headings={len(headings)} blocks={len(blocks)}")

    args.output.mkdir(parents=True, exist_ok=True)
    manifest = []
    for heading_id, block in zip(headings, blocks):
        document = yaml.safe_load(block)
        spec = document.get("unitImplementationSpec")
        if not isinstance(spec, dict):
            raise SystemExit(f"missing unitImplementationSpec for {heading_id}")
        if spec.get("lessonId") != heading_id:
            raise SystemExit(f"heading/spec mismatch: {heading_id} != {spec.get('lessonId')}")
        subject = spec["subject"]
        out = args.output / subject / f"{spec['lessonId']}.yaml"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(yaml.safe_dump(document, allow_unicode=True, sort_keys=False), encoding="utf-8")
        manifest.append({
            "lessonId": spec["lessonId"],
            "subject": subject,
            "path": str(out),
            "component": spec["interactiveBlocks"][0]["component"],
            "status": spec["status"],
            "publisherEvidence": {
                publisher: evidence["status"]
                for publisher, evidence in spec["fusedScope"]["publisherEvidence"].items()
            },
        })

    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps({"specVersion": "1.0", "units": manifest}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"units": len(manifest), "output": str(args.output), "manifest": str(args.manifest)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
