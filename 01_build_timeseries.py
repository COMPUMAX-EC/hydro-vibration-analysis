import json

import pandas as pd

from darts import TimeSeries
from darts.utils.missing_values import fill_missing_values

BACKUP_FILE = r"C:\Users\Geovanny\Desktop\backups\db_historical_data_2026-08-28_030001.json"
RESAMPLE_FREQ = "1min"

with open(BACKUP_FILE) as f:
    records = json.load(f)

df = pd.DataFrame(records)
df = df[df["zona"].isin(["A", "B", "C", "D"])]
df["ts"] = pd.to_datetime(df["ts"], utc=True, format="ISO8601")

series_by_zone: dict[str, TimeSeries] = {}
for zona, group in df.groupby("zona"):
    group = group.set_index("ts").sort_index()
    resampled = group["rms"].resample(RESAMPLE_FREQ).mean()
    ts = TimeSeries.from_series(resampled, freq=RESAMPLE_FREQ)
    ts = fill_missing_values(ts)
    series_by_zone[zona] = ts
    print(
        f"zone {zona}: {len(ts)} points, "
        f"{ts.start_time()} -> {ts.end_time()}, "
        f"{ts.freq_str}"
    )

for zona, ts in series_by_zone.items():
    ts.to_csv(rf"C:\Users\Geovanny\Documents\hydro-vibration-analysis\rms_zone_{zona}.csv")
