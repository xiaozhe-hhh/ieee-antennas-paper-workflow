"""Schema and aggregation for source-grounded figure observations."""
from collections import Counter, defaultdict


REQUIRED = (
    "paper_id", "venue", "page", "figure_number", "caption", "archetype",
    "medium", "panel_count", "source_class", "source_location",
    "source_font_size", "source_line_width",
)


def validate_observation(record):
    for field in REQUIRED:
        if field not in record or record[field] in (None, ""):
            raise ValueError(f"missing {field}")
    if record["source_class"] != "corpus-observed":
        raise ValueError("source_class must be corpus-observed")
    for field in ("source_font_size", "source_line_width"):
        if record[field] != "not-observable":
            raise ValueError(f"{field} must be not-observable for publisher PDFs")
    return record


def aggregate_observations(records):
    by_venue = defaultdict(list)
    for record in records:
        validate_observation(record)
        by_venue[record["venue"]].append(record)
    result = {}
    for venue, items in sorted(by_venue.items()):
        result[venue] = {
            "effective_sample_count": len({item["paper_id"] for item in items}),
            "figure_count": len(items),
            "archetypes": dict(Counter(item["archetype"] for item in items)),
            "medium": dict(Counter(item["medium"] for item in items)),
        }
    return result
