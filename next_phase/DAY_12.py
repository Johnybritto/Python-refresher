# Next Phase Day 12 practice
# Write code that:
# - imports requests
# - sends a request to https://api.github.com
# - stores response.json() in data
# - prints data["current_user_url"]

import requests

response = requests.get("https://api.github.com")
data={}

if response.status_code == 200:
    data=response.json()
    print(data["current_user_url"])
else:
    print("404 error ")

