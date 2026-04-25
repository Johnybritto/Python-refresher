# Next Phase Day 13 practice
# Write code that:
# - imports requests
# - uses try
# - sends a request to https://api.github.com
# - stores response.json() in data
# - prints data.get("current_user_url")
# - prints "API error" in except if something goes wrong

import requests 

try:
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        data =response.json()
        print(data.get("current_user_url"))
    else:
        print("API Error ")
except:
    print("API Error")