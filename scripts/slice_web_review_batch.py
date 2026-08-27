#!/usr/bin/env python3
"""Slice a deterministic, non-upgrading web review batch from the queue."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
queue = json.loads((ROOT / "data/m4-web-review-queue.json").read_text())
items = queue["items"][:100]
out = {
    "schemaVersion": "1.0.0",
    "batchId": "m4-web-review-001",
    "method": "web-source-comparison",
    "status": "pending-review",
    "itemCount": len(items),
    "items": items,
}
(ROOT / "data/m4-web-review-batch-001.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2) + "\n"
)
print(f"wrote batch {out['batchId']} with {len(items)} items")
