from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_skill_routes_scientific_figures_to_antenna_workflow():
    skill = read("SKILL.md").lower()
    routing = read("references/skill-routing.md").lower()
    assert "figure-workflow.md" in skill
    assert "tap" in routing and "awpl" in routing
    assert "figure brief" in routing


def test_figure_brief_contract_requires_evidence_and_delivery_fields():
    contract = read("references/artifact-contracts.md").lower()
    for field in (
        "target venue",
        "primary conclusion",
        "evidence source",
        "final physical width",
        "figure archetype",
        "editable source",
        "author checks",
    ):
        assert field in contract


def test_figure_workflow_and_profiles_exist():
    required = (
        "references/figure-workflow.md",
        "references/figure-style-methodology.md",
        "references/venues/tap-figure-profile.md",
        "references/venues/awpl-figure-profile.md",
        "assets/figure-presets/tap.yaml",
        "assets/figure-presets/awpl.yaml",
    )
    for relative in required:
        assert (ROOT / relative).is_file(), relative


def test_all_antenna_figure_type_references_exist():
    names = (
        "s-parameters",
        "efficiency-gain",
        "radiation-patterns",
        "ecc-mimo",
        "sar-fields-currents",
        "parametric-studies",
        "geometry-dimensions",
        "prototype-measurement",
        "multipanel-assembly",
    )
    for name in names:
        assert (ROOT / "references" / "figure-types" / f"{name}.md").is_file(), name


def test_profiles_use_explicit_source_classes():
    allowed = ("official-required", "corpus-observed", "workflow-recommended")
    for venue in ("tap", "awpl"):
        text = read(f"references/venues/{venue}-figure-profile.md")
        assert all(label in text for label in allowed)


def test_workflow_blocks_unsupported_sar_and_origin_only_delivery():
    workflow = read("references/figure-workflow.md").lower()
    assert ".opju" in workflow
    assert "raw data" in workflow
    assert "sar" in workflow
    assert "free-space" in workflow
    assert "block" in workflow

