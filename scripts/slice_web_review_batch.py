#!/usr/bin/env python3
"""Slice a deterministic, non-upgrading web review batch from the queue."""
import json
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--batch", type=int, default=1)
parser.add_argument("--size", type=int, default=100)
args = parser.parse_args()
queue = json.loads((ROOT / "data/m4-web-review-queue.json").read_text())
start = (args.batch - 1) * args.size
items = queue["items"][start:start + args.size]
batch_id = f"m4-web-review-{args.batch:03d}"
out = {
    "schemaVersion": "1.0.0",
    "batchId": batch_id,
    "method": "web-source-comparison",
    "status": "pending-review",
    "itemCount": len(items),
    "items": items,
}
(ROOT / f"data/m4-web-review-batch-{args.batch:03d}.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2) + "\n"
)
print(f"wrote batch {out['batchId']} with {len(items)} items")
