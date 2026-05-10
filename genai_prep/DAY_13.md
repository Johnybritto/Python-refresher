# GenAI Prep Day 13: FastAPI Mini API

## Quick Revision
- `POST` is used when a client sends structured data to the server.
- FastAPI can read JSON into a function parameter.
- Returning a dictionary sends JSON back to the client.

## Today's Goal
- Build a tiny prompt-style mock endpoint
- Send input JSON to a FastAPI route
- Return structured output JSON
- See the beginner idea of Pydantic request and response models
- Notice the basic idea of `async def`
- See how testing can be done with `TestClient`
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a route expects a JSON body with a prompt, should the input have a clear structure?

If you can explain why yes, you're ready.

## Tiny Lesson

### 1. Why Structured Input Helps
When building GenAI-style APIs, it helps if the input has a clear shape.

Instead of "any random data", you can define:
- what fields are expected
- what type they should be

### 2. Pydantic Model Idea
FastAPI commonly uses Pydantic models for request and response data.

Example:

```python
from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str
```

This means the request should contain:
- one field named `prompt`
- and it should be a string

### 3. Response Model Idea
You can also define the output shape.

Example:

```python
class PromptResponse(BaseModel):
    reply: str
```

This helps keep the API response structured and predictable.

### 4. Tiny Mock AI Route
Example idea:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    reply: str

@app.post("/mock-ai", response_model=PromptResponse)
async def mock_ai(data: PromptRequest):
    return PromptResponse(reply=f"Mock reply: {data.prompt}")
```

### 5. Why `async def` Appears
You will often see:

```python
async def
```

in FastAPI routes.

For today, just remember:
- it is common in API code
- it helps with asynchronous work later
- you do not need deep async theory yet

### 6. Testing Idea
FastAPI can be tested without opening a browser by using `TestClient`.

Example idea:

```python
from fastapi.testclient import TestClient

client = TestClient(app)
response = client.post("/mock-ai", json={"prompt": "Hello"})
print(response.json())
```

For today, just notice the pattern.

## Hint
Keep today's API very small:
- one request model
- one response model
- one POST route

## One Small Exercise
Write code that:
- imports `FastAPI`
- imports `BaseModel`
- creates `app = FastAPI()`
- creates a request model named `PromptRequest` with:
  - `prompt: str`
- creates a response model named `PromptResponse` with:
  - `reply: str`
- adds one POST route for `"/mock-ai"`
- uses `response_model=PromptResponse`
- returns a reply like:

```python
{"reply": f"Mock reply: {data.prompt}"}
```

## Hint 1
Start with:

```python
from fastapi import FastAPI
from pydantic import BaseModel
```

## Hint 2
The route can use:

```python
async def
```

or:

```python
def
```

but `async def` is a good beginner exposure here.

## When You Finish
Send me only your GenAI Prep Day 13 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the small basics problem for Day 13 from the roadmap.

### Problem
Write code that flattens one level of a nested list.

Use:

```python
items = [[1, 2], [3, 4], [5]]
```

Your program should print:

```python
[1, 2, 3, 4, 5]
```

### Hint 3
Loop through the outer list, then loop through each inner list.

## When You Finish The Basics Problem
Send me only your Day 13 basics-problem code.
