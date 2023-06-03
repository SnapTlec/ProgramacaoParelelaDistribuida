import requests

url_create = "http://localhost:5000/user/"

test = {"nickname" : "python.language", "password" : "123456789", "plan" : 0}

res = requests.post(url=url_create, json=test)

print(res.content)