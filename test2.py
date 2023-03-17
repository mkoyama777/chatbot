import requests
import json

headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'question': '換金の仕方を教えてください',
    'markdown': True,
    'full_source': False,
}

response = requests.post(
    'https://api.docsbot.ai/teams/ZDhaL3IauO3emJQENvdX/bots/fFGiIfhrYMZEARG1rEsr/ask',
    headers=headers,
    json=json_data,
)
res = json.loads(response.text)

print(res['answer'])