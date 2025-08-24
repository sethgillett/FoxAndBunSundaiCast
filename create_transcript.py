
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Ensure API key is set in environment variable OPENAI_API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_transcript(project_json: dict) -> str:
    """
    Generate a transcript between Bunny and Fox discussing a project.

    Input schema:
        {
            "name": str,
            "description": str,
            "creators": list[str]
        }

    Output schema:
        "BUNNY: text\nFOX: text\n..."
    """

    name = project_json.get("name", "")
    description = project_json.get("description", "")
    creators = ", ".join(project_json.get("creators", []))

    prompt = f"""
You are tasked with creating a podcast-style transcript.

Podcast: "Sunday Weekly Updates"
Hosts: Bunny (super nice) and Fox (slightly skeptical)

Context:
Project Name: {name}
Description: {description}
Creators: {creators}

Task:
Create a discussion between Bunny and Fox about the project.
They should discuss the merits of the project in a natural, conversational way.

Output schema:
BUNNY: text
FOX: text
BUNNY: text
FOX: text
...
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4.1" if available
        messages=[
            {"role": "system", "content": "You are a transcript generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
    )

    transcript = response.choices[0].message.content.strip()
    return transcript
