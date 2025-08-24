import requests
import os 

bunny_voice = "bella"
fox_voice = "lewis"
"""
Input: DialogueLine
e.g. 
    {
        "speaker": "BUNNY",
        "text": "Welcome back to another episode of Sunday Weekly Updates! I’m your host Bunny, and with me is my co-host Fox. How are you doing today, Fox?"
      }

    file_name (str): Name of the output file (without extension)
    root_path (str): Root path of the project (default is current directory)

Output:
mp3 file at specified folder location
"""
def dialog_to_speech(section: dict, file_name: str, root_path: str):
    url = "https://api.lemonfox.ai/v1/audio/speech"
    headers = {
        "Authorization": "Bearer " + os.getenv("LEMONFOX_API_KEY"),
        "Content-Type": "application/json"
    }
    voice = bunny_voice if section["speaker"] == "BUNNY" else fox_voice
    

    # Create output directory: {root}/audio_assets/{speaker}/
    output_dir = os.path.join(root_path, "audio_assets")
    os.makedirs(output_dir, exist_ok=True)  # create directories if they don't exist

    output_file = os.path.join(output_dir, f"{file_name}.mp3")

    data = {
        "input": section["text"],
        "voice": voice,
        "response_format": "mp3"
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    with open(output_file, "wb") as f:
        f.write(response.content)
    
    print(f"Saved {output_file}")

if __name__ == "__main__":
    dialog_to_speech(
        {"speaker": "BUNNY", "text": "Welcome back to another episode of Sunday Weekly Updates! I'm your host Bunny, and with me is my co-host Fox. How are you doing today, Fox?"}, "test", "./")