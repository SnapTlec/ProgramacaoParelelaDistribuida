import json 
import requests

name="Brasil"
nickname = "leo.brito"
password = "32154"

url = f"http://localhost:5000/country/?country={name}"

request = {
    "nickname" : nickname,
    "password" : password
}
res = requests.post(url=url, json=request)

print(res.json())
