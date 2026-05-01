# GenAI Prep Day 7 practice
# Write code that:
# - imports os
# - reads API_KEY using os.getenv("API_KEY")
# - stores it in api_key
# - prints api_key


import os 
API_KEY = os.getenv("API_KEY")

print(API_KEY)