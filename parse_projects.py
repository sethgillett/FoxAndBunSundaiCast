from datetime import datetime, timedelta, timezone

import requests


def pull_sundai_projects():
    response = requests.get('https://www.sundai.club/api/projects', params={'status': 'APPROVED'})
    return response.json()


def parse_relevant_json(projects, lookback_days=14):
    filtered_projects = []
    for project in projects:
        filtered_projects.append({
            'title': project['title'],
            'description': project['description'],
            'date': datetime.fromisoformat(project['createdAt']),
        })
    return [p for p in filtered_projects if p['date'] >= datetime.now(tz=timezone.utc) - timedelta(lookback_days)]


if __name__ == '__main__':
    print(parse_relevant_json(pull_sundai_projects()))
