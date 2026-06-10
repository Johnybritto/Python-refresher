# Gemini Free Tier Day 5 reference
# Your simple try/except version

import os

from google import genai

MODEL_NAME = "gemini-3-flash-preview"
prompt = "Explain what a Python list is in one short sentence."

key = os.getenv("GEMINI_API_KEY")

try:
    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    print(response.text)
except Exception:
    print("Could not get a Gemini reply right now.")
