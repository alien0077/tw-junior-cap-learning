"""補齊缺少 authoringNote 的題目來源界線，並避免不完整資料被標成已審查。"""
import glob
import json
from pathlib import Path

changed = 0
downgraded = 0
for filename in glob.glob("questions/**/*.json", recursive=True):
    path = Path(filename)
    data = json.loads(path.read_text(encoding="utf-8"))
    provenance = data.get("provenance")
    if not isinstance(provenance, dict) or provenance.get("authoringNote"):
        continue
    origin = provenance.get("origin", "unknown")
    if origin == "official-open":
        note = "來源標示為公開資料；本題的原文使用界線與改寫程度尚待第二輪 AI／Terra 複核，未據此宣稱可自由重製。"
    else:
        note = "原創題目來源界線 metadata 已補齊；內容與題型仍待第二輪 AI／Terra 複核，未據此宣稱真人或專家審定。"
    provenance["authoringNote"] = note
    data["provenance"] = provenance
    if data.get("reviewStatus") == "content-reviewed":
        data["reviewStatus"] = "draft"
        downgraded += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    changed += 1
print(f"backfilled {changed} provenance notes; downgraded {downgraded} incomplete reviews")
