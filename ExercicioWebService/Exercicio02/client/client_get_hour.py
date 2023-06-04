import requests

nickname = "leo.brito"
password = "32154"

url = f"http://localhost:5000/hour"

request = {
    "nickname" : nickname,
    "password" : password
}

res = requests.post(url=url, json=request)

print(res.content)