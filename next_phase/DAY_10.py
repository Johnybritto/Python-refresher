# Next Phase Day 10 practice
# Write code that:
# - imports requests
# - uses requests.get() on https://api.github.com
# - stores the result in response
# - prints response.status_code

import requests

response = requests.get("https://api.github.com")
print(response.status_code)
#print(response.content)

print(type(response.json))

print(response.text)

