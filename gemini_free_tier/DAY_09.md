# Gemini Free Tier Day 9: FastAPI Gemini Route

## Quick Revision
- A tool is a small trusted function that does one exact job.
- A model is helpful when the input is flexible natural language.
- FastAPI can accept JSON and return JSON.

## Today's Goal
- create one FastAPI `POST` route
- accept a prompt from request JSON
- call Gemini inside the route
- return the Gemini reply as JSON
- keep the code small and readable

## Check Your Current Level
Before starting, ask yourself:

If a client sends `{"prompt": "Explain Python lists"}`, should a FastAPI route usually use `GET` or `POST`?

If you can explain why it should be `POST`, you're ready.

## Tiny Lesson

### 1. Why `POST` Fits Here
For this kind of route, the client is sending structured input data.

That is a common `POST` pattern.

### 2. Request And Response Shapes
For Day 9, keep the shapes tiny.

Request idea:

```python
{"prompt": "Explain Python lists"}
```

Response idea:

```python
{"reply": "A Python list is ..."}
```

### 3. Keep Gemini Logic Inside The Route For Today
Later, we will move the Gemini call into a helper function.

But today, keep it all in one route so the FastAPI flow is easy to see.

### 4. Safe Beginner Pattern
Inside the route:
- read the API key
- create the Gemini client
- call Gemini
- return the reply

If anything fails, return a friendly fallback reply.

### 5. Reuse Familiar Pieces
Today combines ideas you already know:
- `BaseModel`
- `@app.post(...)`
- `os.getenv(...)`
- `genai.Client(...)`
- `try` / `except`

## Hint
Start from your earlier mock FastAPI route and replace the mock reply with a Gemini call.

## One Small Exercise
Complete [DAY_09.py](./DAY_09.py) so it:
- imports `FastAPI`
- imports `BaseModel`
- creates `app = FastAPI()`
- defines `PromptRequest` with `prompt: str`
- defines `PromptResponse` with `reply: str`
- adds one `POST` route for `"/gemini"`
- calls Gemini with `data.prompt`
- returns the reply in JSON shape

## Hint 1
Use:

```python
@app.post("/gemini", response_model=PromptResponse)
```

## Hint 2
Inside the route, the Gemini reply text can go into:

```python
reply_text = response.text
```

## Hint 3
If the Gemini call fails, you can still return:

```python
PromptResponse(reply="Could not get a Gemini reply right now.")
```

## When You Finish
Send me only your Gemini Free Tier Day 9 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the short Python basics problem for Day 9 from the roadmap.

### Problem
Write a function that takes:

```python
name
age
```

and returns:

```python
{"name": ..., "age": ...}
```

Then call the function once and print the result.

### Hint 4
Return a dictionary from the function.

## When You Finish The Basics Problem
Send me only your [DAY_09_BASICS.py](./DAY_09_BASICS.py) code.
