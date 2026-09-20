from pathlib import Path

from scripts.figure_corpus import inventory_pdfs, select_stratified


def make_pdf(root: Path, relative: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"%PDF-1.4\n%%EOF")


def test_inventory_filters_non_research_items_and_hides_absolute_paths(tmp_path):
    make_pdf(tmp_path, "01/A Compact MIMO Antenna for Handsets.pdf")
    make_pdf(tmp_path, "01/2025 Distinguished Achievement Award.pdf")

    records = inventory_pdfs(tmp_path, venue="awpl")

    assert len(records) == 1
    assert records[0]["venue"] == "awpl"
    assert records[0]["relative_id"].endswith("A Compact MIMO Antenna for Handsets.pdf")
    assert "source_path" not in records[0]
    assert len(records[0]["path_hash"]) == 64


def test_inventory_classifies_antenna_design_subtypes(tmp_path):
    names = (
        "Low-SAR Multiband Mobile Phone Antenna.pdf",
        "Wideband Phased Array Antenna.pdf",
        "Reconfigurable Slot Antenna.pdf",
        "Millimeter-Wave MIMO Antenna.pdf",
    )
    for name in names:
        make_pdf(tmp_path, name)

    records = inventory_pdfs(tmp_path, venue="tap")

    assert {record["subtype"] for record in records} >= {
        "low-sar-mobile",
        "array-mimo",
        "reconfigurable",
        "millimeter-wave",
    }


def test_seeded_sampling_is_deterministic_and_respects_venue_quotas(tmp_path):
    tap = tmp_path / "tap"
    awpl = tmp_path / "awpl"
    for index in range(12):
        make_pdf(tap, f"{index % 4 + 1:02d}/Wideband Array Antenna {index}.pdf")
        make_pdf(awpl, f"{index % 4 + 1:02d}/Compact MIMO Antenna {index}.pdf")
    records = inventory_pdfs(tap, "tap") + inventory_pdfs(awpl, "awpl")

    first = select_stratified(records, {"tap": 5, "awpl": 6}, seed=17)
    second = select_stratified(records, {"tap": 5, "awpl": 6}, seed=17)

    assert [item["paper_id"] for item in first] == [item["paper_id"] for item in second]
    assert sum(item["venue"] == "tap" for item in first) == 5
    assert sum(item["venue"] == "awpl" for item in first) == 6
    assert len({item["paper_id"] for item in first}) == 11


def test_sampling_limits_author_team_when_metadata_exists():
    records = []
    for index in range(8):
        records.append(
            {
                "paper_id": f"tap-{index}",
                "venue": "tap",
                "title": f"Antenna {index}",
                "relative_id": f"Antenna {index}.pdf",
                "path_hash": str(index).zfill(64),
                "month": None,
                "subtype": "general-antenna",
                "author_team": "same-team" if index < 5 else f"team-{index}",
            }
        )

    selected = select_stratified(records, {"tap": 5}, seed=4, max_per_author_team=2)

    assert sum(item["author_team"] == "same-team" for item in selected) <= 2
    assert len(selected) == 5
