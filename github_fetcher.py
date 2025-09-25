import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = 'ulaluya'
REPO_NAME = 'github-sheets-integration'

GOOGLE_APPS_SCRIPT_URL = os.getenv('APPS_SCRIPT_URL')

github_api_url = f"https://api.github.com/repos/{USERNAME}/{REPO_NAME}/commits"

response = requests.get(github_api_url)

if response.status_code == 200:
    commits = response.json()

    data_to_send = []

    for commit in commits[:5]:
        commit_data = {
            'sha': commit['sha'],
            'author': commit['commit']['author']['name'],
            'message': commit['commit']['message'],
            'date': commit['commit']['author']['date']
        }
        data_to_send.append(commit_data)

    try:
        post_response = requests.post(
            GOOGLE_APPS_SCRIPT_URL,
            data=json.dumps(data_to_send),
            headers={'Content-Type': 'application/json'}
        )
        print("Данные успешно отправлены в Google Таблицу!")
        print(f"Ответ от сервера: {post_response.text}")

    except Exception as e:
        print(f"Ошибка при отправке данных: {e}")

else:
    print(f"Ошибка при запросе к GitHub API: {response.status_code}")
    print(response.json())