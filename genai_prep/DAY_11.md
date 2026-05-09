# GenAI Prep Day 11: FastAPI Basics

## Quick Revision
- `try` and `except` help your program fail safely.
- API code should return useful fallback messages instead of crashing.
- Timeouts and clear errors are part of safer API work.

## Today's Goal
- Understand what FastAPI is
- Create a simple FastAPI app
- Add one GET route
- Learn how to run the app with Uvicorn
- Understand the idea of a path and a route
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If someone opens `/` in a browser, should your app be able to send back a small response?

If you can explain why yes, you're ready.

## Tiny Lesson

### 1. What FastAPI Is
FastAPI is a Python framework for building APIs.

It helps you:
- define routes
- receive requests
- return JSON responses

### 2. The App Object
You first create an app object.

Example:

```python
from fastapi import FastAPI

app = FastAPI()
```

This `app` will hold your routes.

### 3. One GET Route
A GET route is a path your app responds to.

Example idea:

```python
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}
```

Here:
- `"/"` is the path
- `@app.get("/")` tells FastAPI to handle GET requests for that path
- the function returns JSON-style data

### 4. Path vs Route
- a path is something like `"/"` or `"/hello"`
- a route is the rule that connects that path to a function

### 5. Running the App
If you are inside the `genai_prep` folder, a common command is:

```powershell
uvicorn DAY_11:app --reload
```

If FastAPI and Uvicorn are not installed yet, the usual install command is:

```powershell
pip install fastapi uvicorn
```

## Hint
For today's exercise, focus on the pattern:
- create `app`
- add one route
- return one small dictionary

## One Small Exercise
Write code that:
- imports `FastAPI`
- creates `app = FastAPI()`
- adds one GET route for `"/"`
- returns:

```python
{"message": "Hello from FastAPI"}
```

## Hint 1
Start with:

```python
from fastapi import FastAPI
```

## Hint 2
Use:

```python
@app.get("/")
```

above the function.

## When You Finish
Send me only your GenAI Prep Day 11 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the small basics problem for Day 11 from the roadmap.

### Problem
Write code that checks whether a number is prime.

Use:

```python
number = 7
```

Your program should print:
- `"prime"` if the number is prime
- otherwise `"not prime"`

### Hint 3
Check whether any number from `2` up to `number - 1` divides it evenly.

## When You Finish The Basics Problem
Send me only your Day 11 basics-problem code.
