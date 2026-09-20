"""Inventory and sample an antenna-paper figure corpus."""
from __future__ import annotations

from collections import Counter, defaultdict, deque
from hashlib import sha256
from pathlib import Path
import random
import re


EXCLUDED_TITLE_SIGNALS = (
    "award",
    "editorial",
    "erratum",
    "correction",
    "call for papers",
    "reviewers list",
    "society news",
)

ANTENNA_TITLE_SIGNALS = (
    "antenna",
    "array",
    "reflectarray",
    "transmitarray",
    "metasurface",
    "radiator",
    "beam-steering",
    "beamforming",
)


def _subtype(title: str) -> str:
    lowered = title.lower()
    if "sar" in lowered or "mobile phone" in lowered or "handset" in lowered:
        return "low-sar-mobile"
    if "reconfigurable" in lowered or "tunable" in lowered:
        return "reconfigurable"
    if "millimeter" in lowered or re.search(r"\b(?:[3-9]\d|\d{3})\s*ghz\b", lowered):
        return "millimeter-wave"
    if "mimo" in lowered or "array" in lowered:
        return "array-mimo"
    if "multiband" in lowered or "multi-band" in lowered or "wideband" in lowered:
        return "multiband-wideband"
    return "general-antenna"


def _month(relative: Path) -> int | None:
    for part in relative.parts[:-1]:
        match = re.fullmatch(r"(?:month[-_ ]*)?(1[0-2]|0?[1-9])", part, re.I)
        if match:
            return int(match.group(1))
    return None


def inventory_pdfs(root, venue):
    root = Path(root).resolve()
    venue = str(venue).lower()
    if venue not in {"tap", "awpl"}:
        raise ValueError("venue must be 'tap' or 'awpl'")

    records = []
    for path in sorted(root.rglob("*.pdf"), key=lambda item: item.as_posix().lower()):
        title = path.stem.strip()
        lowered = title.lower()
        if any(signal in lowered for signal in EXCLUDED_TITLE_SIGNALS):
            continue
        if not any(signal in lowered for signal in ANTENNA_TITLE_SIGNALS):
            continue
        relative = path.relative_to(root)
        relative_id = relative.as_posix()
        digest = sha256(relative_id.encode("utf-8")).hexdigest()
        records.append(
            {
                "paper_id": f"{venue}-{digest[:16]}",
                "venue": venue,
                "title": title,
                "relative_id": relative_id,
                "path_hash": digest,
                "month": _month(relative),
                "subtype": _subtype(title),
                "author_team": None,
            }
        )
    return records


def select_stratified(records, quotas, seed=0, max_per_author_team=2):
    rng = random.Random(seed)
    selected = []
    for venue, quota in quotas.items():
        candidates = [dict(item) for item in records if item.get("venue") == venue]
        buckets = defaultdict(list)
        for item in candidates:
            buckets[(item.get("month"), item.get("subtype", "unknown"))].append(item)
        queues = []
        for key in sorted(buckets, key=lambda value: (str(value[0]), str(value[1]))):
            rng.shuffle(buckets[key])
            queues.append(deque(buckets[key]))
        rng.shuffle(queues)

        venue_selected = []
        team_counts = Counter()
        while queues and len(venue_selected) < quota:
            next_round = []
            progress = False
            for queue in queues:
                while queue:
                    item = queue.popleft()
                    team = item.get("author_team")
                    if team and team_counts[team] >= max_per_author_team:
                        continue
                    venue_selected.append(item)
                    if team:
                        team_counts[team] += 1
                    progress = True
                    break
                if queue:
                    next_round.append(queue)
                if len(venue_selected) >= quota:
                    break
            queues = next_round
            if not progress:
                break
        if len(venue_selected) != quota:
            raise ValueError(
                f"venue {venue!r} has {len(venue_selected)} eligible papers; {quota} required"
            )
        selected.extend(venue_selected)
    return selected
