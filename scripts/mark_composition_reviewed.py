#!/usr/bin/env python3
"""Record the completed second-round AI review without publishing composition content."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    registry_path = ROOT / "implementation/composition/module-registry.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    registry["sourceBoundary"] = "Modules have passed the repository's second-round AI content review; prompts remain original and publication remains draft until runtime/content integration gates pass."
    for module in registry["modules"]:
        module["status"] = "content-reviewed-draft"
    registry_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    content_path = ROOT / "implementation/composition/module-content.json"
    content = json.loads(content_path.read_text(encoding="utf-8"))
    content["reviewStatus"] = "content-reviewed-draft"
    content["reviewEvidence"] = "implementation/reports/composition-content-review.json"
    content_path.write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"modules": len(registry["modules"]), "status": "content-reviewed-draft"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
