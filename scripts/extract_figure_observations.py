"""Extract conservative figure-caption observations from sampled PDFs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess

from scripts.figure_observations import validate_observation


CAPTION = re.compile(r"(?im)^\s*Fig\.\s*(\d+)\s*[.:]\s*(.+?)(?=\n\s*Fig\.|\n\s*\n|\Z)", re.S)


def archetype(caption: str) -> str:
    text = caption.lower()
    if "s-parameter" in text or "reflection coefficient" in text:
        return "s-parameters"
    if "radiation pattern" in text:
        return "radiation-patterns"
    if "sar" in text or "surface current" in text or "electric field" in text:
        return "sar-fields-currents"
    if "efficiency" in text or "gain" in text:
        return "efficiency-gain"
    if "prototype" in text or "measurement setup" in text or "fabricated" in text:
        return "prototype-measurement"
    if "geometry" in text or "dimensions" in text or "configuration" in text:
        return "geometry-dimensions"
    if "parametric" in text or "varying" in text:
        return "parametric-studies"
    if "ecc" in text or "envelope correlation" in text:
        return "ecc-mimo"
    return "other-antenna-figure"


def _pages(path: Path):
    try:
        import fitz
    except ImportError:
        completed = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(f"pdftotext failed for {path.name}: {completed.stderr.strip()}")
        for text in completed.stdout.split("\f"):
            yield text, "not-observable"
        return
    with fitz.open(path) as document:
        for page in document:
            medium = "raster-or-mixed" if page.get_images(full=True) else "vector-or-mixed"
            yield page.get_text("text"), medium


def extract_pdf(path: Path, paper: dict) -> list[dict]:
    observations = []
    for page_index, (text, medium) in enumerate(_pages(path)):
        for match in CAPTION.finditer(text):
                caption = " ".join(match.group(2).split())[:800]
                labels = set(re.findall(r"\(([a-z])\)", caption.lower()))
                record = {
                    "paper_id": paper["paper_id"],
                    "venue": paper["venue"],
                    "page": page_index + 1,
                    "figure_number": match.group(1),
                    "caption": f"Fig. {match.group(1)}. {caption}",
                    "archetype": archetype(caption),
                    "medium": medium,
                    "panel_count": max(1, len(labels)),
                    "simulated_measured": (
                        "both" if "simulat" in caption.lower() and "measur" in caption.lower()
                        else "not-observable"
                    ),
                    "source_class": "corpus-observed",
                    "source_location": f"page {page_index + 1}, Fig. {match.group(1)}",
                    "source_font_size": "not-observable",
                    "source_line_width": "not-observable",
                }
                observations.append(validate_observation(record))
    return observations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--tap-root", type=Path, required=True)
    parser.add_argument("--awpl-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    roots = {"tap": args.tap_root, "awpl": args.awpl_root}
    rows = []
    for paper in manifest["papers"]:
        rows.extend(extract_pdf(roots[paper["venue"]] / paper["relative_id"], paper))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
