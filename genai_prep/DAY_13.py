# GenAI Prep Day 13 practice
# Write code that:
# - imports FastAPI
# - imports BaseModel
# - creates app = FastAPI()
# - creates PromptRequest with prompt: str
# - creates PromptResponse with reply: str
# - adds one POST route for "/mock-ai"
# - uses response_model=PromptResponse
# - returns {"reply": f"Mock reply: {data.prompt}"}

from fastapi import FastAPI
from pydantic import BaseModel
# Add the request model, response model, and POST route below.

from fastapi.testclient import TestClient



app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    reply: str

@app.post("/mock-ai" , response_model=PromptResponse)
async def mock_ai(data: PromptRequest):
    return PromptResponse(reply=f"Mock reply: {data.prompt}")
    

client = TestClient(app)

response = client.post("/mock-ai", json={"prompt": "Jo"})
print(response.json())