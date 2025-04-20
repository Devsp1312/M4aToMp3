from pydub import AudioSegment
import os

def convert_m4a_to_mp3(m4a_file, mp3_file):
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    audio.export(mp3_file, format="mp3")
    print(f"Converted {m4a_file} to {mp3_file}")

if __name__ == "__main__":
    m4a_file = input("Enter the path to the .m4a file: ").strip()

    if not os.path.isfile(m4a_file):
        print("File not found. Please check the path.")
    else:
        mp3_file = os.path.splitext(m4a_file)[0] + ".mp3"
        convert_m4a_to_mp3(m4a_file, mp3_file)
        print(f"Converted {m4a_file} to {mp3_file}")
        print("Conversion completed successfully.")
        