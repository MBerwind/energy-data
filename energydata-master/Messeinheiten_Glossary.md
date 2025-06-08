# 📏 Messeinheiten – Beschreibung der Messgrößen

Diese Tabelle listet alle erfassten Messvariablen im Datensatz auf – inklusive Beschreibung, Einheit und Skalierung.

| Variablenname | Beschreibung | Einheit | Skalierung / Hinweis |
|---------------|--------------|---------|------------------------|
| `timeval` | Zeitstempel der Messung | Datum/Zeit | ISO 8601 Format |
| `L1PhaseVoltage_Vx10` | Spannung Phase 1 | V | /10 (z.B. 2314 = 231.4 V) |
| `L1Current_mA` | Stromstärke Phase 1 | mA | - |
| `L1ActivePower_W` | Wirkleistung Phase 1 | W | - |
| `L1InductivePower_var` | Induktive Blindleistung Phase 1 | var | - |
| `L1CapacitivePower_var` | Kapazitive Blindleistung Phase 1 | var | - |
| `L1ApparentPower_VA` | Scheinleistung Phase 1 | VA | - |
| `L1PowerFactor_x100` | Leistungsfaktor Phase 1 | % | /100 (z.B. 100 = 1.00) |
| `CosPhiL1_x100` | Cosinus Phi Phase 1 | % | /100 (z.B. 100 = 1.00) |
| `L2PhaseVoltage_Vx10` | Spannung Phase 2 | V | /10 |
| `L2Current_mA` | Stromstärke Phase 2 | mA | - |
| `L2ActivePower_W` | Wirkleistung Phase 2 | W | - |
| `L2InductivePower_var` | Induktive Blindleistung Phase 2 | var | - |
| `L2CapacitivePower_var` | Kapazitive Blindleistung Phase 2 | var | - |
| `L2ApparentPower_VA` | Scheinleistung Phase 2 | VA | - |
| `L2PowerFactor_x100` | Leistungsfaktor Phase 2 | % | /100 |
| `CosPhiL2_x100` | Cosinus Phi Phase 2 | % | /100 |
| `L3PhaseVoltage_Vx10` | Spannung Phase 3 | V | /10 |
| `L3Current_mA` | Stromstärke Phase 3 | mA | - |
| `L3ActivePower_W` | Wirkleistung Phase 3 | W | - |
| `L3InductivePower_var` | Induktive Blindleistung Phase 3 | var | - |
| `L3CapacitivePower_var` | Kapazitive Blindleistung Phase 3 | var | - |
| `L3ApparentPower_VA` | Scheinleistung Phase 3 | VA | - |
| `L3PowerFactor_x100` | Leistungsfaktor Phase 3 | % | /100 |
| `CosPhiL3_x100` | Cosinus Phi Phase 3 | % | /100 |
| `ActiveThreePhasePower_W` | Gesamtwirkleistung (3 Phasen) | W | Summe |
| `InductiveThreePhasePower_var` | Gesamtblindleistung induktiv | var | Summe |
| `CapacitiveThreePhasePower_var` | Gesamtblindleistung kapazitiv | var | Summe |
| `ApparentThreePhasePower_VA` | Gesamtscheinleistung | VA | Summe |
| `ThreePhasePowerFactor_x100` | Gesamtleistungsfaktor | % | /100 |
| `ThreePhaseCosPhi_x100` | Cos φ gesamt | % | /100 |
| `L1Frequency_Hzx100` | Netzfrequenz Phase 1 | Hz | /100 (z.B. 5003 = 50.03 Hz) |
| `L1L2Voltage_Vx10` | Spannung zwischen Phase 1 und 2 | V | /10 |
| `L2L3Voltage_Vx10` | Spannung zwischen Phase 2 und 3 | V | /10 |
| `L3L1Voltage_Vx10` | Spannung zwischen Phase 3 und 1 | V | /10 |
| `NeutralCurrentN_mA` | Stromstärke im Neutralleiter | mA | - |
| `L1VoltageTHD_x10` | Spannungs-THD Phase 1 | % | /10 |
| `L2VoltageTHD_x10` | Spannungs-THD Phase 2 | % | /10 |
| `L3VoltageTHD_x10` | Spannungs-THD Phase 3 | % | /10 |
| `L1CurrentTHD_x10` | Strom-THD Phase 1 | % | /10 |
| `L2CurrentTHD_x10` | Strom-THD Phase 2 | % | /10 |
| `L3CurrentTHD_x10` | Strom-THD Phase 3 | % | /10 |
| `MaximumDemandkWIII_W` | Max. Wirkleistungsbedarf (3 Phasen) | W | historischer Peak |
| `MaximumDemandkVAIII_VA` | Max. Scheinleistungsbedarf | VA | historischer Peak |
| `MaximumDemandIAVG_mA` | Max. durchschnittlicher Strom | mA | - |
| `MaximumDemandIL1_mA` | Max. Stromstärke Phase 1 | mA | - |
| `MaximumDemandIL2_mA` | Max. Stromstärke Phase 2 | mA | - |
| `MaximumDemandIL3_mA` | Max. Stromstärke Phase 3 | mA | - |
| `ConsumedActiveEnergykW_kWh` | Verbrauchte Wirkarbeit (kWh) | kWh | Zählerstand |
| `ConsumedActiveEnergyW_Wh` | Verbrauchte Wirkarbeit (Wh) | Wh | Zählerstand |
| `ConsumedInductiveReactiveEnergykvarhL_kvarh` | Verbrauchte Blindarbeit (induktiv, kvarh) | kvarh | Zählerstand |
| `ConsumedInductiveReactiveEnergyvarhL_varh` | Verbrauchte Blindarbeit (induktiv, varh) | varh | Zählerstand |
| `ConsumedCapacitiveReactiveEnergykvarhC_kvarh` | Verbrauchte Blindarbeit (kapazitiv, kvarh) | kvarh | Zählerstand |
| `ConsumedCapacitiveReactiveEnergyvarhC_varh` | Verbrauchte Blindarbeit (kapazitiv, varh) | varh | Zählerstand |
| `ConsumedApparentEnergykVAh_kVAh` | Verbrauchte Scheinarbeit | kVAh | Zählerstand |
| `ConsumedApparentEnergyVAh_VAh` | Verbrauchte Scheinarbeit | VAh | Zählerstand |
| `ConsumedCO2Emissions_x10` | CO₂-Emissionen (geschätzt) | kg | /10 (z.B. 153 = 15.3 kg) |

_Letzte Aktualisierung: 2025-06-08_