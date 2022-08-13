import os
import requests

TOKEN = os.getenv("TOKEN")

def conect_palavras_clave(data):
    url = 'https://api.nlpcloud.io/v1/gpu/es/finetuned-gpt-neox-20b/kw-kp-extraction'
    headers = {"Content-Type": "application/json", "Authorization": TOKEN}

    text = {
        "text":data
    }

    response = requests.post(url, json=text, headers=headers)

    if response.status_code == 200:
        return response.json(), response.status_code
    else:
        return {"Error": response.status_code}, response.status_code
