from datetime import datetime, tzinfo

import requests


def pull_sundai_projects():
    response = requests.get('https://www.sundai.club/api/projects', params={'status': 'APPROVED'})
    return response.json()


def parse_relevant_json(projects):
    filtered_projects = []
    for project in projects:
        filtered_projects.append({
            'title': project['title'],
            'description': project['description'],
            'date': datetime.fromisoformat(project['createdAt']),
            'lead': project['launchLead']['name'],
            'participants': [p['hacker']['name'] for p in project['participants']],
        })


if __name__ == '__main__':
    print(parse_relevant_json(pull_sundai_projects()))
