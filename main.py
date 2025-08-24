import os
import sys
from parse_projects import parse_relevant_json, pull_sundai_projects
from combine_whole_transcript import combine_whole_transcript
from transcript_to_speech_assets import transcript_to_speech
import json 
from merge_all_audio_files import merge_mp3_files

def run_pipeline(lookback_days):
    if not os.path.exists("transcript.json"):
        print("Pulling projects...")
        projects = parse_relevant_json(pull_sundai_projects(), lookback_days=lookback_days)

        print("Generating transcript...")
        transcript = combine_whole_transcript(projects)

        print("Saving transcript...")
        with open("transcript.json", "w") as f:
            f.write(json.dumps(transcript))
    else:
        transcript = json.load(open("transcript.json"))

    if os.path.exists("./audio_assets"):
        num_files = len(os.listdir("./audio_assets"))
    else:
        num_files = 0

    if num_files != len(transcript['dialogue']):
        print("Converting transcript to speech...")
        transcript_to_speech(json.load(open("transcript.json"))["dialogue"])
    
    print("Merging audio files...")
    if not os.path.exists("./output/merged.mp3"):
        merge_mp3_files("./audio_assets", "./output", "merged.mp3")

    print("Done")
    

if __name__ == "__main__":
    output = run_pipeline(int(sys.argv[1]))
