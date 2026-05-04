# GenAI Prep Day 8 practice
# Write code that:
# - imports requests
# - creates headers = {"Content-Type": "application/json"}
# - creates payload with model and messages
# - sends a POST request to https://httpbin.org/post
# - prints response.status_code
# - prints response.json()["json"]

import requests

url = "https://httpbin.org/post"
#headers = {"Content-Type": "application/json",}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer DEMO_KEY"
}

#response = requests.post(url, headers=headers, json=payload, timeout=10)


payload = {
    "model" : "demo-model",
   "messages": [{"role": "user", "content": "Hello"}] 
}


response = requests.post(url, headers=headers, json=payload,timeout=10)

print(response.status_code)
print(response.json()["json"])