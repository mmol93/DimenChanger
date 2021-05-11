import json
import requests

url = "https://kauth.kakao.com/oauth/token"

data = {
     "grant_type": "authorization_code",
    "client_id": "4d4bd473939a8ac4326e19d3f960470d",
    "redirect_uri": "https://localhost.com",
    "code": "ug_dkMc4etjHaA9HrGDLAjMIuadB53uHgnOS6AaMdS5cGwxaEpMnB2JHp6b2GwLxv11-LAo9c5oAAAF24gnMsg"
}

response = requests.post(url, data=data)

tokens = response.json()

with open("kakao_token.json", "w") as fp:
    json.dump(tokens, fp)