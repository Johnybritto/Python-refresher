# Gemini Free Tier Day 5 reference
# Stronger version with timeout and retry

import os

from google import genai
from google.genai import errors, types

MODEL_NAME = "gemini-3-flash-preview"
prompt = "Explain what a Python list is in one short sentence."

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(
        timeout=10_000,
        retry_options=types.HttpRetryOptions(
            attempts=3,
            initial_delay=1.0,
            max_delay=8.0,
            exp_base=2.0,
            jitter=1.0,
            http_status_codes=[408, 429, 500, 502, 503, 504],
        ),
    ),
)

try:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    print(response.text)
except errors.APIError:
    print("Could not get a Gemini reply right now.")
