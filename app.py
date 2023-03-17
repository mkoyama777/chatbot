import json
import os
from flask import *
import requests;
import openai

app = Flask(__name__)
app.secret_key = 'user'

url = "https://api.line.me/v2/bot/message/reply"
access_token = '63qMWXPLN7JbDn5utlUzUs3w2pa+G3BEyJF7yfcqjTSi7TfYdi6i7kyNHnExzmCUZ5ZiuUj3d3vPGJ3eK2BHglSEuPGjQwwZZcr8WbZQuaspiT6EAj6bMKL9WRxTuwOhaO55NKynFLHQadj6xk8kBQdB04t89/1O/w1cDnyilFU='
headers = { 'Content-Type': 'application/json','Authorization': 'Bearer ' + access_token}
headers_bot = {
    'Content-Type': 'application/json',
}
@app.route('/',methods=["GET","POST"])
def index():   
     return json.dumps({'code':200})

@app.route('/webhook',methods=["GET","POST"])
def webhook():
    print("-------webhook start")
    openai.api_key = os.environ['api']
    # openai.organization = 'org-kTy14g90SrWDqHV2L2WEcRFA'
    try:
        # signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        body = json.loads(body)
        print(body)
        message = body['events'][0]['message']['text']
        print(message)
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "user", "content": message},
        #     ],
        # )
        json_data = {
            'question': message,
            'markdown': True,
            'full_source': False,
        }
        response = requests.post(
            'https://api.docsbot.ai/teams/ZDhaL3IauO3emJQENvdX/bots/fFGiIfhrYMZEARG1rEsr/ask',
            headers=headers,
            json=json_data,
        )
        res = json.loads(response.text)
    # response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{'role': 'user', 'content': message}],temperature=0.0)
    
        print("---gpt response")
        # print(response)
        # message = response.choices[0]["message"]["content"].strip()
        message = res['answer']
        print(message)
        replyToken = body['events'][0]['replyToken']
        messages = {'type':'text','text':message}
    
        
        print("---body")
        print("message:"+message)
        print("replyToken:"+replyToken)
        
        
        message = body
        payload = {'replyToken':replyToken,'messages': [messages]}
        print(json.dumps(payload))
        r = requests.post(url, data=json.dumps(payload), headers=headers)
    except Exception as e:
        print(e)    
    
    return json.dumps({'code':200})

