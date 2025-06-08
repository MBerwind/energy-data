
# 📘 Data Dictionary – Energy Monitoring Dataset

This document explains the structure, file naming, and attribute meanings for the energy monitoring data used in the project.

---

## 📁 File Naming Convention

Each file follows this naming pattern:

```
<Device>_<Type>_original.csv
<Device>_<Type>_resampled_<interval>.csv
```

- **Device**: e.g. `CRAC3`, `ULC5`, etc.
- **Type**: describes data content, e.g. `Full`, `Power`, etc.
- **resampled_<interval>**: indicates temporal aggregation:
  - `10min` → 10-minute average
  - `1h` → hourly average
  - `1d` → daily average or sum

---

## 📦 Folder Structure (example)

```
csv/
├── CRAC3_original.csv
├── CRAC3_resampled_10min.csv
├── CRAC3_resampled_1h.csv
├── ULC5_original.csv
└── ...
```

---

## 📊 Column / Attribute Definitions

| Column Name                         | Description                                               | Unit       | Notes                           |
|------------------------------------|-----------------------------------------------------------|------------|----------------------------------|
| `timeval`                          | Timestamp of measurement                                  | ISO 8601   | Used as time index              |
| `L1PhaseVoltage_Vx10`              | Voltage phase 1                                           | V ×10      | Divide by 10                    |
| `L1Current_mA`                     | Current in phase 1                                        | mA         |                                 |
| `L1ActivePower_W`                  | Real power phase 1                                        | W          |                                 |
| `L1InductivePower_var`            | Inductive reactive power phase 1                          | var        |                                 |
| `L1CapacitivePower_var`           | Capacitive reactive power phase 1                         | var        |                                 |
| `L1ApparentPower_VA`              | Apparent power phase 1                                    | VA         |                                 |
| `L1PowerFactor_x100`              | Power factor phase 1                                      | ×100       | Divide by 100                   |
| `L1Frequency_Hzx100`              | Frequency                                                 | Hz ×100    | Divide by 100                   |
| `L1VoltageTHD_x10`                | Voltage total harmonic distortion                         | % ×10      | Divide by 10                    |
| `L1CurrentTHD_x10`                | Current total harmonic distortion                         | % ×10      | Divide by 10                    |
| `NeutralCurrentN_mA`              | Current in neutral conductor                              | mA         | High value = imbalance          |
| `ActiveThreePhasePower_W`         | Total active power (L1 + L2 + L3)                          | W          |                                 |
| `InductiveThreePhasePower_var`    | Total inductive reactive power                            | var        |                                 |
| `CapacitiveThreePhasePower_var`   | Total capacitive reactive power                           | var        |                                 |
| `ApparentThreePhasePower_VA`      | Total apparent power                                      | VA         |                                 |
| `ThreePhasePowerFactor_x100`      | Average power factor (3 phases)                           | ×100       | Divide by 100                   |
| `MaximumDemandkWIII_W`            | Max active demand (3 phases)                              | W          |                                 |
| `ConsumedActiveEnergykW_kWh`      | Cumulative active energy consumed                         | kWh        | Key target variable             |
| `ConsumedApparentEnergykVAh_kVAh` | Cumulative apparent energy                                | kVAh       |                                 |
| `ConsumedCO2Emissions_x10`        | Estimated CO₂ emissions                                    | kg ×10     | Divide by 10                    |

> _Note_: Many values exist separately for L1, L2, and L3 phases.

---

## 🧭 Usage Notes

- Use `*_original.csv` for high-resolution analysis (1-minute data)
- Use resampled files for trend analysis, modeling, or reporting
- Focus on:
  - `ConsumedActiveEnergykW_kWh` for total consumption
  - `ActiveThreePhasePower_W` for short-term performance
  - `MaximumDemandkWIII_W` for load management
  - `ConsumedCO2Emissions_x10` for sustainability metrics



