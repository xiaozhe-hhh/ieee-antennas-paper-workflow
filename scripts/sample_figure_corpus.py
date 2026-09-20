"""Create private and public manifests for an antenna-figure corpus sample."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from scripts.figure_corpus import inventory_pdfs, select_stratified


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tap-root", type=Path, required=True)
    parser.add_argument("--awpl-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--per-venue", type=int, default=40)
    parser.add_argument("--seed", type=int, default=20250920)
    args = parser.parse_args()

    tap = inventory_pdfs(args.tap_root, "tap")
    awpl = inventory_pdfs(args.awpl_root, "awpl")
    selected = select_stratified(
        tap + awpl,
        {"tap": args.per_venue, "awpl": args.per_venue},
        seed=args.seed,
    )
    payload = {
        "schema_version": 1,
        "seed": args.seed,
        "selection_policy": "venue plus available month and antenna subtype",
        "papers": selected,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
