
import requests
import os
jocke_url = "https://official-joke-api.appspot.com/random_joke"

def get_jockes():
    jock = requests.get(url=jocke_url)
    print(jock.json().get("setup")+jock.json().get("punchline"))

get_jockes()