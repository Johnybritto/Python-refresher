# Gemini Free Tier Day 6 practice
# Goal:
# - build a tiny Gemini terminal chatbot
# - keep a conversation history list
# - stop when the user types "exit"
# - print a friendly fallback message if the request fails

import os

from google import genai

MODEL_NAME = "gemini-3-flash-preview"

conversation = []

while True:
    user_text = input("You: ").strip()

    if user_text == "exit":
        break

    conversation.append({"role": "user", "text": user_text})

    history_prompt = "Continue this conversation in a short helpful way:\n\n"
    for message in conversation:
        role = message["role"]
        text = message["text"]
        history_prompt += f"{role}: {text}\n"

    try:
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=history_prompt,
        )
        reply_text = response.text
        print("Gemini:", reply_text)
        conversation.append({"role": "model", "text": reply_text})
    except Exception:
        print("Could not get a Gemini reply right now.")
