# Gemini Free Tier Day 10 practice
# Goal:
# - move the Gemini call into a helper function
# - keep the FastAPI route focused on input and output
# - return one reply string from the helper

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


def get_gemini_reply(prompt: str) -> str:
    try:
        key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=key)
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )
        return response.text
    except Exception:
        return "Could not get a Gemini reply right now."


@app.post("/gemini", response_model=PromptResponse)
def ask_gemini(data: PromptRequest):
    reply_text = get_gemini_reply(data.prompt)
    return PromptResponse(reply=reply_text)
