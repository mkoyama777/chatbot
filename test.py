
import os

import openai
import requests
import urllib3

# APIキーの設定
# openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_key = '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'
openai.organization = 'org-kTy14g90SrWDqHV2L2WEcRFA'
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "大谷翔平について教えて"},
    ],
)
print(response.choices[0]["message"]["content"].strip())