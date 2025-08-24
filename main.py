from parse_projects import parse_relevant_json, pull_sundai_projects
from combine_whole_transcript import combine_whole_transcript
import json 

def run_pipeline():
    projects = parse_relevant_json(pull_sundai_projects())
    transcript = combine_whole_transcript(projects[:10])
    return transcript

if __name__ == "__main__":
    output = run_pipeline()
    print(json.dumps(output))