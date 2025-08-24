from typing import List, Literal
from pydantic import BaseModel

# Output schema
class DialogueLine(BaseModel):
    speaker: Literal["BUNNY", "FOX"]
    text: str

class TranscriptResponse(BaseModel):
    dialogue: List[DialogueLine]
