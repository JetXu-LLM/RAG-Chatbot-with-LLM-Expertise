import requests
import json

url = "http://172.20.10.6:80/answer"
headers = {"Content-Type": "application/json"}
data = {"question": "Who are you?", "context": "First, remember: You are Jet Xu."}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())