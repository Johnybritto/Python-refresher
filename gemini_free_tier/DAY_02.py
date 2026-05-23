# Gemini Free Tier Day 2 practice
# Goal:
# - use the Gemini client again
# - send two prompts about the same topic
# - print both replies clearly

import os

from google import genai

MODEL_NAME = "gemini-3-flash-preview"

prompt_1 = "Explain Python lists"
prompt_2 = "Explain what a Python list is in one short beginner-friendly sentence."

api_key = os.getenv("GEMINI_API_KEY")
print(api_key)
# Step 1:
# client = ...
client = genai.Client(api_key=api_key)


# Step 2:
# response_1 = ...

response_1 = client.models.generate_content(model=MODEL_NAME,contents=prompt_1)

# Step 3:
# response_2 = ...
response_2 = client.models.generate_content(model=MODEL_NAME,contents=prompt_2)


# Step 4:
# reply_text_1 = ...
# reply_text_2 = ...

reply_text_1= response_1.text
reply_text_2 = response_2.text
# Step 5:
# print("Prompt 1 reply:")
# print(...)
# print("Prompt 2 reply:")
# print(...)
print("Prompt 1 reply:")
print(reply_text_1)
print("Prompt 2 reply:")
print(reply_text_2)