# Análisis de vibraciones (mantenimiento predictivo)

Series de tiempo de RMS de vibración por zona (A–D) de una central hidroeléctrica, con `darts`.

- `01_build_timeseries.py`: lee el respaldo JSON, re-muestrea a 1 min por zona y guarda `rms_zone_*.csv`.
- `02_plot_zone_a.py`: gráfico general de la zona A.

**Los datos de planta (JSON, CSV, PNG) nunca se suben**: el `.gitignore` los excluye y el CI falla si aparece alguno.
Siguiente paso: detector de anomalías por zona con `darts.ad`, cruzado con la bitácora de mantenimiento.

No confundir con el Lector Modbus (medidor eléctrico PM556x).
