# Next Phase Day 14 practice
# Write code that:
# - imports requests
# - uses try
# - sends a request to https://api.github.com
# - stores response.json() in data
# - prints data.get("current_user_url")
# - prints data.get("current_user_authorizations_html_url")
# - prints "API error" if something goes wrong

import requests
try:
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        data = response.json()
        print(data.get("current_user_url"))
        print(data.get("current_user_authorizations_html_url"))
        with open("API_data", "w") as file:
            file.write(data.get("current_user_url") + "\n")
            file.write(data.get("current_user_authorizations_html_url") + "\n")
    else:
        print(" Error not Found ")
except:
    print("API error ")

