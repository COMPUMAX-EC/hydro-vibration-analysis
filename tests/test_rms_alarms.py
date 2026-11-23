import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "synthetic_demo"))
from rms_alarms import classify, first_crossings, synthetic_rms  # noqa: E402


def test_only_fault_zone_alarms():
    cross = first_crossings(classify(synthetic_rms(fault_zone="C")))
    assert cross["C"]["alert"] is not None and cross["C"]["alarm"] is not None
    assert cross["C"]["alert"] < cross["C"]["alarm"]
    for z in "ABD":
        assert cross[z]["alert"] is None


def test_deterministic():
    assert synthetic_rms(seed=1).equals(synthetic_rms(seed=1))


def test_healthy_has_no_alerts():
    df = synthetic_rms(days=3, fault_zone="none")
    assert classify(df).to_numpy().max() == 0
