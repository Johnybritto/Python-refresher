# Gemini Free Tier Day 5 practice
# Goal:
# - wrap one Gemini call in try/except
# - print the reply if it works
# - print a friendly fallback message if it fails

import os

from google import genai

MODEL_NAME = "gemini-3-flash-preview"
prompt = "Explain what a Python list is in one short sentence."

try:
    key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    print(response.text)
except Exception:
    print("Could not get a Gemini reply right now.")
