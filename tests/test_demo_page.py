import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "synthetic_demo"))
from build_demo_page import build_html  # noqa: E402


def test_page_is_self_contained_and_shows_fault():
    html = build_html()
    assert "<svg" in html and "alarm 7.1 mm/s" in html
    assert "http://" not in html.replace("http://www.w3.org", "") and "https://" not in html
    assert "Zone C" in html


def test_page_is_deterministic():
    assert build_html(seed=3) == build_html(seed=3)
