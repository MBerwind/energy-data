from pathlib import Path

# Define the folder
csv_folder = Path("csv")

# Loop through all .txt files
for txt_file in csv_folder.glob("*.txt"):
    if "readme" in txt_file.name.lower():
        print(f"🟡 Skipping readme file: {txt_file.name}")
        continue

    # Build new file name
    new_name = txt_file.with_name(f"{txt_file.stem}_original.csv")

    # Rename file
    txt_file.rename(new_name)
    print(f"✅ Renamed: {txt_file.name} → {new_name.name}")
