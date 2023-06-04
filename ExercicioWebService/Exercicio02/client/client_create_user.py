import requests

url_create = "http://localhost:5000/user/"

test = {"nickname" : "felipe.correia", "password" : "123456789", "plan" : 2}

res = requests.post(url=url_create, json=test)

print(res.content)