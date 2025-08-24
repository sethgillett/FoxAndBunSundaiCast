from pydub import AudioSegment
import os

def merge_mp3_files(folder_path: str, output_file: str = "merged.mp3"):
    """
    Merge all mp3 files in the folder (0.mp3, 1.mp3, 2.mp3, ...) into a single MP3 file.
    
    Args:
        folder_path (str): Path to the folder containing MP3 files.
        output_file (str): Name/path of the merged MP3 output file.
    """
    # Collect and sort MP3 files numerically
    mp3_files = sorted(
        [f for f in os.listdir(folder_path) if f.endswith(".mp3")],
        key=lambda x: int(os.path.splitext(x)[0])
    )

    if not mp3_files:
        raise ValueError("No mp3 files found in the folder.")

    # Initialize with the first audio segment
    combined = AudioSegment.from_mp3(os.path.join(folder_path, mp3_files[0]))

    # Append the rest
    for mp3_file in mp3_files[1:]:
        audio = AudioSegment.from_mp3(os.path.join(folder_path, mp3_file))
        combined += audio

    # Export merged file
    combined.export(os.path.join(folder_path, output_file), format="mp3")
    print(f"Merged {len(mp3_files)} files into {output_file}")

if __name__ == "__main__":
    merge_mp3_files("./audio_assets", "merged.mp3")