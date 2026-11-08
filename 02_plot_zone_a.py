import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from darts import TimeSeries

ts = TimeSeries.from_csv(
    r"C:\Users\Geovanny\Documents\hydro-vibration-analysis\rms_zone_A.csv",
    time_col="ts",
)

fig, axes = plt.subplots(2, 1, figsize=(12, 8))
ts.plot(ax=axes[0])
axes[0].set_title("Zone A - rms (full range)")

last_2_days = ts[-2 * 24 * 60 :]
last_2_days.plot(ax=axes[1])
axes[1].set_title("Zone A - rms (last 2 days, zoomed in)")

plt.tight_layout()
plt.savefig(r"C:\Users\Geovanny\Documents\hydro-vibration-analysis\zone_a_overview.png", dpi=120)
print("saved plot")
