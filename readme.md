# 🎵 M4A to MP3 Converter (Python)

This simple Python script converts `.m4a` audio files to `.mp3` format using the `pydub` and `ffmpeg` libraries.

---

## ✅ Features

- Converts `.m4a` files to `.mp3` easily  
- Cross-platform: works on both macOS and Windows  
- Lightweight script with no GUI — perfect for quick terminal use

---

## 🧠 Requirements

- Python 3.10 or 3.11 (recommended)  
- [ffmpeg](https://ffmpeg.org/download.html)  
- `pydub` Python library

---

## 💻 Setup Instructions

### 🔷 macOS

1. **Install Homebrew (if not already installed):**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install Python & ffmpeg:
brew install pyenv ffmpeg
pyenv install 3.11.7
pyenv local 3.11.7
pip install pydub


Run the script:
python3 m4a_to_mp3.py


🟦 Windows
Install Python 3.10+ from python.org


✅ Be sure to check “Add Python to PATH” during setup
Install ffmpeg:
Download from https://ffmpeg.org/download.html
Extract it, and copy the bin folder path
Add the path to System Properties > Environment Variables > Path
Install Python dependencies:
pip install pydub


Run the script:
python m4a_to_mp3.py

📂 How to Use

Place your .m4a file in the same folder as m4a_to_mp3.py
Run the script
When prompted, enter the .m4a file name (example: audio.m4a)

The .mp3 file will be saved in the same folder
📌 Notes

Ensure ffmpeg is correctly installed and accessible from your system PATH
The converted file will have the same name as the input, but with .mp3
Only works with valid audio files