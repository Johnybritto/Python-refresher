# Gemini Free Tier Day 9 practice
# Goal:
# - create one FastAPI POST route
# - accept a prompt in request JSON
# - call Gemini inside the route
# - return the reply as JSON

import os

from fastapi import FastAPI
from google import genai
from pydantic import BaseModel

MODEL_NAME = "gemini-3-flash-preview"

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


class PromptResponse(BaseModel):
    reply: str


# Step 1:
# Add one POST route for "/gemini" with response_model=PromptResponse.

@app.post("/gemini", response_model=PromptResponse )
def res(data: PromptRequest):
    try:
        key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=key)
        response = client.models.generate_content(model=MODEL_NAME, contents=data.prompt)
        reply_text = response.text
    
        return PromptResponse(reply=reply_text)
    except Exception:
        return PromptResponse(reply="Could not get a Gemini reply right now.")



# Step 2:
# Inside the route, read GEMINI_API_KEY and create the Gemini client.

# Step 3:
# Call Gemini with data.prompt and store response.text in reply_text.


# Step 4:
# Return PromptResponse(reply=reply_text).


# Step 5:
# If anything fails, return a friendly fallback reply.
