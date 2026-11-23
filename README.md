# Análisis de vibraciones (mantenimiento predictivo)

Series de tiempo de RMS de vibración por zona (A–D) de una central hidroeléctrica, con `darts`.

- `01_build_timeseries.py`: lee el respaldo JSON, re-muestrea a 1 min por zona y guarda `rms_zone_*.csv`.
- `02_plot_zone_a.py`: gráfico general de la zona A.

**Los datos de planta (JSON, CSV, PNG) nunca se suben**: el `.gitignore` los excluye y el CI falla si aparece alguno.
Siguiente paso: detector de anomalías por zona con `darts.ad`, cruzado con la bitácora de mantenimiento.

No confundir con el Lector Modbus (medidor eléctrico PM556x).

## Synthetic demo (public-safe)
`synthetic_demo/rms_alarms.py` generates seeded synthetic RMS per zone (mm/s), with one zone drifting upward, and flags alert (4.5) and alarm (7.1) crossings on a 10-minute rolling mean. `python synthetic_demo/rms_alarms.py` prints the first crossings; `pytest tests` runs in CI. No plant data is used.
