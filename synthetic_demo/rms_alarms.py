"""Synthetic vibration RMS per zone with ISO-style alert/alarm thresholds.

All data is generated here (seeded noise). No plant data is read or written.
Units: mm/s RMS. Thresholds are illustrative, not from any real machine.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

ALERT_MM_S = 4.5
ALARM_MM_S = 7.1
ZONES = ("A", "B", "C", "D")


def synthetic_rms(days: int = 7, seed: int = 42, fault_zone: str = "C") -> pd.DataFrame:
    """1-minute RMS per zone; `fault_zone` drifts upward during the last 2 days."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range("2026-01-01", periods=days * 24 * 60, freq="1min")
    n = len(idx)
    out = {}
    for i, z in enumerate(ZONES):
        base = 2.0 + 0.3 * i
        daily = 0.2 * np.sin(2 * np.pi * np.arange(n) / (24 * 60))
        series = base + daily + rng.normal(0, 0.08, n)
        if z == fault_zone:
            start = n - 2 * 24 * 60
            series[start:] += np.linspace(0, 5.5, n - start)
        out[z] = series
    return pd.DataFrame(out, index=idx)


def classify(df: pd.DataFrame, window: str = "10min") -> pd.DataFrame:
    """Rolling-mean level per zone: 0 = normal, 1 = alert, 2 = alarm."""
    smooth = df.rolling(window).mean()
    level = (smooth >= ALERT_MM_S).astype(int) + (smooth >= ALARM_MM_S).astype(int)
    return level


def first_crossings(level: pd.DataFrame) -> dict[str, dict[str, pd.Timestamp | None]]:
    res = {}
    for z in level.columns:
        a = level.index[level[z] >= 1]
        b = level.index[level[z] >= 2]
        res[z] = {"alert": a[0] if len(a) else None, "alarm": b[0] if len(b) else None}
    return res


if __name__ == "__main__":
    for zone, t in first_crossings(classify(synthetic_rms())).items():
        print(f"zone {zone}: alert={t['alert']} alarm={t['alarm']}")
