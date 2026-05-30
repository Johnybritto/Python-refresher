# Gemini Free Tier Day 3 practice
# Goal:
# - send one prompt to Gemini
# - read the returned text
# - store prompt, reply, model, and timestamp
# - save the result to a JSON file

import json
import os
from datetime import datetime

from google import genai

MODEL_NAME = "gemini-3-flash-preview"
OUTPUT_FILE = "day3_response.json"
prompt = "Explain what JSON is in one short beginner-friendly sentence."

api_key = os.getenv("GEMINI_API_KEY")

with open(".env", "r") as f:
    key=f.read().split("=")[1].strip("''")
#print(key)



# Step 1:
client = genai.Client(api_key=key)


# Step 2:
# response = client.models.generate_content(
#     model=MODEL_NAME,
#     contents=prompt,
# )

response = client.models.generate_content(model=MODEL_NAME,contents=prompt)


# Step 3:
# reply_text = ...
reply_text =response.text
print(reply_text)

# Step 4:
# result = {
#     "prompt": ...,
#     "reply": ...,
#     "model": ...,
#     "timestamp": ...,
# }

result = {
    "prompt": prompt,
    "reply": reply_text,
    "model": MODEL_NAME,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

}

print(result)
# Step 5:
# with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
#     json.dump(..., file, indent=2)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(result,file, indent=2)

#OUTPUT_FILE : is decalred at the top 

# Step 6:
print("Saved Gemini response to JSON.")
