import pytest

from scripts.figure_observations import aggregate_observations, validate_observation


def observation(**changes):
    item = {
        "paper_id": "tap-123",
        "venue": "tap",
        "page": 3,
        "figure_number": "4",
        "caption": "Fig. 4. Simulated and measured S-parameters.",
        "archetype": "s-parameters",
        "medium": "vector-or-mixed",
        "panel_count": 2,
        "simulated_measured": "both",
        "source_class": "corpus-observed",
        "source_location": "page 3, Fig. 4",
        "source_font_size": "not-observable",
        "source_line_width": "not-observable",
    }
    item.update(changes)
    return item


def test_observation_requires_source_location_and_allowed_source_class():
    validate_observation(observation())
    with pytest.raises(ValueError, match="source_location"):
        validate_observation(observation(source_location=""))
    with pytest.raises(ValueError, match="source_class"):
        validate_observation(observation(source_class="official-required"))


def test_publisher_pdf_source_settings_are_not_claimed_observable():
    with pytest.raises(ValueError, match="source_font_size"):
        validate_observation(observation(source_font_size="7 pt"))


def test_aggregate_keeps_venues_separate_and_reports_denominators():
    records = [observation(), observation(paper_id="tap-2"), observation(paper_id="awpl-1", venue="awpl")]
    result = aggregate_observations(records)
    assert result["tap"]["effective_sample_count"] == 2
    assert result["awpl"]["effective_sample_count"] == 1
    assert result["tap"]["archetypes"]["s-parameters"] == 2
