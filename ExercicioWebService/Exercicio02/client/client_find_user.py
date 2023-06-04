import requests

nickname = "python.framework"
url = f"http://localhost:5000/user/{nickname}"

res = requests.get(url=url)

print(res.content)