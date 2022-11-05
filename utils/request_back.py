import requests
import json

URL = 'http://localhost:8000/api/matchs/finish'

URL_START = 'http://localhost:8000/api/matchs/start'

def send_data_task(data):
    r = requests.post(url=URL, data=json.dumps(data), headers={"content-type":"application/json"})
    return r.text

def send_data_start(data):
    r = requests.post(url=URL_START, data=json.dumps(data), headers={"content-type":"application/json"})
    return r.text