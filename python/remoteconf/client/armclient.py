import requests
import json

URL = "http://127.0.0.1:9998/"

def show_config():

    r = requests.get(URL+"getconfig")
    print r.json()
    return r.json()

def add_config(**kwargs):

    my_json = json.dumps(kwargs)
    r = requests.post(URL+"configure", data=my_json)
    return r.json()