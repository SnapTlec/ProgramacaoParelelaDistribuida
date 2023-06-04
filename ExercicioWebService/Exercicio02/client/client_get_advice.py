import requests


url = f"http://localhost:5000/advice/"
request_auth = {
    "nickname" : "camila.silva",
    "password" : "124587"
}

res = requests.post(url=url, json=request_auth)

print(res.json())
