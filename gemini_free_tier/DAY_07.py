# Gemini Free Tier Day 7 practice
# Goal:
# - compare one normal Gemini response with one streaming response
# - print streaming chunks as they arrive
# - keep the script small and clear

import os

from google import genai

MODEL_NAME = "gemini-3-flash-preview"
prompt = "Explain what a Python list is in one short beginner-friendly sentence."

try:
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Step 1:
    # Get one normal full response and print it.

    response = client.models.generate_content(model=MODEL_NAME,contents=prompt)

    print(response.text)


    print("/n")

    # Step 2:
    # Print a label like "Streaming reply:".


    # Step 3:
    # Use generate_content_stream(...) with the same prompt.

    for ch in client.models.generate_content_stream(model=MODEL_NAME, contents=prompt):
        print(ch.text , end="")

    
    print("/n")


    # Step 4:
    # Loop through each chunk and print chunk.text with end="".


    # Step 5:
    # Print one extra blank line after streaming finishes.
except Exception:
    print("Could not get a Gemini reply right now.")
