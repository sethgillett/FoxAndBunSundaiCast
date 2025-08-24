import json 
from singular_dialog_to_speech import dialog_to_speech

"""
Input: Entire JSON transcript
e.g. 
   [
      {
        "speaker": "BUNNY",
        "text": "Welcome back to another episode of Sunday Weekly Updates! I’m your host Bunny, and with me is my co-host Fox. How are you doing today, Fox?"
      },
      {
        "speaker": "FOX",
        "text": "Hey Bunny! I’m doing alright, I guess. What's the first project we're looking at?"
      },
      .....
    ] 

    ]

Output:
all mp3 files at specified folder location with file name corresponding to order in transcript
e.g.
audio_assets/0.mp3 --- "Welcome back..."
audio_assets/1.mp3 --- "Hey Bunny..."


"""
def transcript_to_speech(sections: list[dict]):
    for i, section in enumerate(sections):
        print(f"Processing {i} of {len(sections)}")
        dialog_to_speech(section, str(i), "./")

if __name__ == "__main__":
    transcript_to_speech(json.load(open("example_transcript.json"))["dialogue"])