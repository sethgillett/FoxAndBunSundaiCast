
import create_transcript_section
from schemas import TranscriptResponse, DialogueLine
from create_transcript_section import create_transcript_section

opening_lines = [
       DialogueLine(
            speaker="BUNNY",
            text="Welcome back to another episode of Sunday Weekly Updates! I’m your host Bunny, and with me is my co-host Fox. How are you doing today, Fox?"
        ),
        DialogueLine(
            speaker="FOX",
            text="Hey Bunny! I’m doing alright, I guess. What's the first project we're looking at?"
        ),
]

closing_lines = [
     DialogueLine(
        speaker="BUNNY",
        text="Thanks for listening to this week's Sunday projects, folks!"
    ),
    DialogueLine(
        speaker="FOX",
        text="See you next week, I guess!"
    )
]

transcript = TranscriptResponse(
    dialogue=opening_lines
)

section_opener_initial = "First up is {name}."
section_opener_following = "Next up is {name}."
section_opener_final = "Lastly, but not least, is {name}."

"""
Output format:
{
  "dialogue": [
    {"speaker": "BUNNY", "text": "Welcome back to another episode!"},
    {"speaker": "FOX", "text": "Hey Bunny, I’m skeptical as usual."}
  ]
}
"""
def combine_whole_transcript(projects: list[dict]) -> dict:
    for i, project in enumerate(projects):
        
        name = project.get("name", "")

        section_transcript = create_transcript_section(project)
        if i == 0:
            transcript.dialogue.append(DialogueLine(speaker="BUNNY", text= section_opener_initial.format(name=name)))
        elif i == len(projects) - 1:
            transcript.dialogue.append(DialogueLine(speaker="BUNNY", text= section_opener_final.format(name=name)))
        else:
            transcript.dialogue.append(DialogueLine(speaker="BUNNY", text= section_opener_following.format(name=name)))
        transcript.dialogue += section_transcript.dialogue
    return transcript.model_dump()


if __name__ == "__main__":
    trans = combine_whole_transcript(
        [
            {
                "name": "EcoTrack",
                "description": "A mobile app that helps users track their carbon footprint and reduce their carbon emissions."
            },
            {
                "name": "Doughnut eater",
                "description": "A mobile app uses AI to generate images of people eating doughnuts"
            }
        ]
    )
    print("\n\n".join(f"{line['speaker']}: {line['text']}" for line in trans["dialogue"]))

    
        