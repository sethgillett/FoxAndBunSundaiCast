
import os
from openai import OpenAI
from dotenv import load_dotenv
from schemas import TranscriptResponse, DialogueLine
load_dotenv()

# Ensure API key is set in environment variable OPENAI_API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
use_mock_response=os.getenv("USE_MOCK_RESPONSE", False)

def create_transcript_section(project_json: dict) -> TranscriptResponse:
    """
    Generate a transcript between Bunny and Fox discussing a project.

    Input schema:
        {
            "name": str,
            "description": str
        }
    """

    name = project_json.get("name", "")
    description = project_json.get("description", "")

    if use_mock_response == "True":
        return TranscriptResponse(
            dialogue=[
                DialogueLine(
                    speaker="BUNNY",
                    text=f"{name} is a fascinating one."
                ),
                DialogueLine(
                    speaker="FOX",
                    text="Are you sure???"
                ),
                DialogueLine(
                    speaker="BUNNY",
                    text="A really cool one."
                ),
                DialogueLine(
                    speaker="FOX",
                    text="Great! This one was very interesting"
                ),
            ]
        )

    prompt = f"""
You are tasked with creating a section of a podcast transcript.

Podcast: "Sunday Weekly Updates"
Hosts: Bunny (super nice, happy and upbeat) and Fox (slightly skeptical, but also open-minded, depressed)

Context:
The two hosts are discussing a single project. 
Project Name: {name}
Description: {description}

Task:
Create a discussion between Bunny and Fox about the project. 
The discussion should start with the words "{name} is a" and continue with a description of the project.
They should discuss the merits of the project in a natural, conversational way.
They should spend maximum 4 lines discussing the project.
They should wrap up the discussion with a pithy, exciting summary of the project. 
...
    """

    if use_mock_response == 'True':
        response = TranscriptResponse(
            dialogue=[
                DialogueLine(speaker="BUNNY", text=f"{name} is a ..."),
                DialogueLine(speaker="FOX", text="Sounds interesting, but do people actually use these kinds of apps?"),
                DialogueLine(speaker="BUNNY", text="Absolutely! It empowers users to make environmentally friendly choices and see the impact of their actions in real-time."),
                DialogueLine(speaker="FOX", text="I guess that’s a good way to encourage accountability, huh?"),
                DialogueLine(speaker="BUNNY", text="Exactly! By making it fun and interactive, EcoTrack can really change the way we think about our daily habits!"),
            ]
        )
        transcript = response
    else:
        response = client.chat.completions.parse(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": "You are a transcript generator."},
                {"role": "user", "content": prompt}
            ],
            response_format=TranscriptResponse,
            temperature=0.8,
        ) 
        transcript = response.choices[0].message.parsed  

    # print("\n".join(f"{line.speaker}: {line.text}" for line in transcript.dialogue))
    return transcript

if __name__ == "__main__":
    create_transcript_section({
        "name": "EcoTrack",
        "description": "A mobile app that helps users track their carbon footprint and reduce their carbon emissions."
        }
    )