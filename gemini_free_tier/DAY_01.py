# Gemini Free Tier Day 1 practice
# Goal:
# - use the GEMINI_API_KEY from your environment
# - create a Gemini client
# - send one short prompt
# - print only the model text
#
# If the import fails, install the SDK first:
# python -m pip install -q -U google-genai

# If Google AI Studio shows a newer free-tier text model later,
# update this constant to match it.
MODEL_NAME = "gemini-3-flash-preview"
prompt = "Explain what a Python list is in one short sentence."

# Step 1:
# from google import genai

from google import genai

path='.env'
with open(path, 'r') as f:
    key=f.read().split('=')[1].strip("''")

#print(key)


# Step 2:
# client = ...
client = genai.Client(api_key=key)
# Step 3:
# response = client.models.generate_content(
#     model=MODEL_NAME,
#     contents=prompt,
# )

response = client.models.generate_content(model=MODEL_NAME, contents=prompt)

# Step 4:
# reply_text = ...
reply_text = response.text
# Step 5:
# print(...)
print(reply_text)