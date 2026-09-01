#!/usr/bin/env python3
"""驗證版本研究 manifest 所指向的本機來源快取。

本工具只驗證檔案存在、大小與 SHA-256；不把受著作權來源檔案寫入儲存庫，
也不把「下載成功」誤當成「已完成逐單元研究或內容審查」。
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        default="data/version-source-manifest.json",
        help="版本來源 manifest 路徑",
    )
    parser.add_argument(
        "--cache-root",
        default=None,
        help="覆蓋 manifest 的 cacheRoot，供本機或 CI 驗證",
    )
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    cache_root = Path(args.cache_root or manifest["cacheRoot"])
    failures: list[str] = []
    checked = 0

    for source in manifest["sources"]:
        local_file = source.get("localFile")
        if not local_file:
            continue
        path = cache_root / local_file
        if not path.is_file():
            failures.append(f"missing: {source['publisher']}/{source['subject']} {path}")
            continue
        if path.stat().st_size == 0:
            failures.append(f"empty: {path}")
            continue
        expected_size = source.get("sizeBytes")
        if expected_size is not None and path.stat().st_size != expected_size:
            failures.append(
                f"size: {path} expected={expected_size} actual={path.stat().st_size}"
            )
            continue
        expected_hash = source.get("sha256")
        if expected_hash and sha256(path) != expected_hash:
            failures.append(f"sha256: {path}")
            continue
        checked += 1

    result = {
        "manifest": str(manifest_path),
        "cacheRoot": str(cache_root),
        "checked": checked,
        "sourceCount": len(manifest["sources"]),
        "failureCount": len(failures),
        "failures": failures,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
