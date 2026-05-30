# Gemini Free Tier Day 5 reference
# Your simple try/except version

import os

from google import genai

MODEL_NAME = "gemini-3-flash-preview"
prompt = "explain in short sentene what is list"

key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=key)

try:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    print(response.text)
except:
    print("invalid")
