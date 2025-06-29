import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import matplotlib
import os
from pathlib import Path
import glob

# Use non-GUI backend for matplotlib
matplotlib.use("Agg")

# Forecast horizons in hours
horizons = {
    "7days": 24 * 7,
    "30days": 24 * 30,
    "1year": 24 * 365,
    "2years": 24 * 365 * 2
}

# Base directory setup
data_dir = Path("energydata-master/csv")
output_base = Path("energydata-master/forecast-results")
resampled_files = list(data_dir.glob("*_resampled_1h.csv"))

# Loop over files
for file_path in resampled_files:
    name = file_path.stem.replace("_resampled_1h", "")
    print(f"📊 Processing {name}")

    try:
        # Load and clean
        df = pd.read_csv(file_path, parse_dates=["timeval"], dayfirst=True)
        if "ActiveThreePhasePower_W" in df.columns:
            df = df[["timeval", "ActiveThreePhasePower_W"]].dropna()
        elif "L1ActivePower_W" in df.columns:
            df = df[["timeval", "L1ActivePower_W"]].dropna()
        else:
            print(f"⚠️  Skipping {name} – no valid target column.")
            continue

        df.columns = ["ds", "y"]  # Rename for Prophet

        # Prophet model setup
        model = Prophet(daily_seasonality=True, weekly_seasonality=True)
        model.fit(df)

        # Forecast for each horizon
        for label, hours in horizons.items():
            print(f"   🔮 Forecasting: {label}")

            future = model.make_future_dataframe(periods=hours, freq="H")
            forecast = model.predict(future)

            # Output folder
            outdir = output_base / name / label
            outdir.mkdir(parents=True, exist_ok=True)

            # Save forecast plot
            fig1 = model.plot(forecast)
            plt.title(f"{name} – Forecast ({label})")
            plt.xlabel("Time")
            plt.ylabel("Power (W)")
            plt.tight_layout()
            plt.savefig(outdir / f"{name}_forecast_{label}.png")
            plt.close()

            # Save component plot
            fig2 = model.plot_components(forecast)
            plt.tight_layout()
            plt.savefig(outdir / f"{name}_components_{label}.png")
            plt.close()

    except Exception as e:
        print(f"❌ Error with {name}: {e}")
