import requests

url_delete = "http://localhost:5000/user/delete"

test = {"nickname" :'leo.brito', 'password' : '32154'}

res = requests.post(url=url_delete, json=test)

print(res.content)