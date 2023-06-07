import requests


localhost = "https://5000-snaptlec-programacaopar-ujjxf7y231w.ws-us98.gitpod.io"
url_create = f"{localhost}/user/"

test = {"nickname" : "felipe.correia", "password" : "123456789", "plan" : 2}

res = requests.post(url=url_create, json=test)

print(res.content)