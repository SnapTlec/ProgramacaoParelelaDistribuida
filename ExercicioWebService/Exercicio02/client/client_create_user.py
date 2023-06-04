import requests

url_create = "http://localhost:5000/user/"

test = {"nickname" : "python.framework", "password" : "123456789", "plan" : 1}

res = requests.post(url=url_create, json=test)

print(res.content)