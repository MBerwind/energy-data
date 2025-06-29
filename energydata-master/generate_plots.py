import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
import glob

# Set paths
data_dir = Path("csv")
output_base = Path("energydata-master")

# Find all component data files (.txt)
txt_files = glob.glob(str(data_dir / "*.txt"))

# Make sure plots use non-interactive backend
import matplotlib
matplotlib.use("Agg")

# Go through each file
for file_path in txt_files:
    file_name = Path(file_path).stem  # e.g. "crac1"
    print(f"Processing {file_name}...")

    try:
        # Use 'timeval' instead of 'Timestamp'
        df = pd.read_csv(
            file_path,
            parse_dates=["timeval"],
            dayfirst=True,
            low_memory=False
        )
        df.set_index("timeval", inplace=True)

        # Create output folder
        output_dir = output_base / file_name
        output_dir.mkdir(parents=True, exist_ok=True)

        # Pick relevant numeric columns (power, energy, cos phi, etc.)
        plot_columns = [col for col in df.columns if any(x in col.lower() for x in [
            "power", "energy", "cos", "current", "voltage", "thd", "demand", "co2"
        ]) and pd.api.types.is_numeric_dtype(df[col])]

        # Generate plots
        for col in plot_columns:
            plt.figure(figsize=(14, 4))
            df[col].plot(title=f"{file_name} – {col}", ylabel=col)
            plt.tight_layout()
            plt.savefig(output_dir / f"{col}.png")
            plt.close()

    except Exception as e:
        print(f"❌ Error processing {file_name}: {e}")

