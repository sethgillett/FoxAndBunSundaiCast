from datetime import datetime, timedelta, timezone

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
        })
    return filtered_projects


if __name__ == '__main__':
    print(parse_relevant_json(pull_sundai_projects()))
