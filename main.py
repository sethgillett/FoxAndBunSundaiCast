from parse_projects import parse_relevant_json, pull_sundai_projects
from combine_whole_transcript import combine_whole_transcript
from transcript_to_speech_assets import transcript_to_speech
import json 
from merge_all_audio_files import merge_mp3_files

def run_pipeline():
    print("Pulling projects...")
    projects = parse_relevant_json(pull_sundai_projects())
    print("Generating transcript...")
    transcript = combine_whole_transcript(projects[:10])
    print("Saving transcript...")
    with open("transcript.json", "w") as f:
        f.write(json.dumps(transcript))
    print("Converting transcript to speech...")
    transcript_to_speech(json.load(open("transcript.json"))["dialogue"])
    print("Merging audio files...")
    merge_mp3_files("./audio_assets", "merged.mp3")
    print("Done")
    

if __name__ == "__main__":
    output = run_pipeline()
