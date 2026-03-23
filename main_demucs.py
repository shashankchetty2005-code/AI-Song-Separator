import os
import subprocess

INPUT_PATH = "input/song3.mp3"
OUTPUT_DIR = "output"

print("\n=== STEP 1: RUNNING DEMUCS ===\n")

# Run Demucs
subprocess.run([
    "demucs",
    INPUT_PATH,
    "-o", OUTPUT_DIR,
    "--mp3"
])

print("\n=== STEP 2: FETCHING OUTPUT FILES ===\n")

song_name = os.path.splitext(os.path.basename(INPUT_PATH))[0]
base_path = f"{OUTPUT_DIR}/htdemucs/{song_name}"

files = {
    "vocals": f"{base_path}/vocals.mp3",
    "drums": f"{base_path}/drums.mp3",
    "bass": f"{base_path}/bass.mp3",
    "other": f"{base_path}/other.mp3"
}

# Check and print
for key, path in files.items():
    if os.path.exists(path):
        print(f"✅ {key.upper()}: {path}")
    else:
        print(f"❌ {key.upper()} not found")

print("\n=== DONE ===\n")