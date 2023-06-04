import json 
import requests

name="USA"

url = f"https://restcountries.com/v3.1/name/{name}"


res = requests.get(url=url)

#json_object = json.dumps(res.content.decode('utf-8'), indent = 4) 

print(res.json())
