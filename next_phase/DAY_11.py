# Next Phase Day 11 practice
# Write code that:
# - imports requests
# - uses requests.get() on https://api.github.com
# - stores the result in response
# - prints response.status_code
# - prints type(response.json())

import requests

response = requests.get("https://api.github.com")

print(response.status_code)

print(type(response.json()))