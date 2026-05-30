# Gemini Free Tier Day 4 practice
# Goal:
# - ask Gemini for valid JSON
# - ask for exactly two keys
# - print the raw returned text

import os

from google import genai

MODEL_NAME = "gemini-3-flash-preview"
prompt = "print a valid JSON with two keys"


with open(".env", "r") as f:
    key=f.read().split("=")[1].strip("''")

client = genai.Client(api_key=key)

response = client.models.generate_content(model=MODEL_NAME,contents=prompt)

print(response.text)