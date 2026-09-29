#!/usr/bin/env python3
"""Compile extracted YAML unit specs into a browser-readable JSON bundle."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    files = sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml"))
    units = []
    for path in files:
        spec = yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"]
        units.append(spec)
    out = ROOT / "implementation/unit-specs.bundle.json"
    out.write_text(json.dumps({"specVersion": "1.0", "units": units}, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({"units": len(units), "output": str(out)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
