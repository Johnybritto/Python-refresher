# Gemini Free Tier Day 5 practice
# Goal:
# - wrap one Gemini call in try/except
# - print the reply if it works
# - print a friendly fallback message if it fails

import os

from google import genai

MODEL_NAME = "gemini-3-flash-preview"
prompt = "explain in short sentene what is list"

key=os.getenv("GEMINI_API_KEY")

#print(key)



client = genai.Client(api_key=key)
try:
    response = client.models.generate_content(model=MODEL_NAME,contents=prompt)
    print(response.text)
except:
    print("invalid")





