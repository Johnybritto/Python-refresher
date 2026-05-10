# GenAI Prep Day 14: Transition to a Real Provider

## Quick Revision
- FastAPI can accept structured request data and return structured JSON.
- Pydantic models help define clear input and output shapes.
- `POST` routes are common when sending prompt-style data.

## Today's Goal
- Understand how a real GenAI provider call is usually structured
- See where authentication fits in
- Build a simple terminal chatbot flow
- See how saving a response can help later
- Notice how the same logic could later be wrapped in FastAPI
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If you later switch from a mock reply to a real model API, which part should change: the whole program or just the function that gets the reply?

If you can explain why it should mostly be one function, you're ready.

## Tiny Lesson

### 1. What Changes With a Real Provider
The overall chatbot flow stays similar:
- get user input
- send it to a model
- receive the reply
- print the reply

What changes is the part that talks to the provider.

### 2. Authentication Idea
Real providers usually need an API key.

That key should stay outside your code.

Common pattern:

```python
import os

api_key = os.getenv("API_KEY")
```

### 3. Request Pattern
A real provider call often needs:
- a URL
- headers
- a JSON payload

Example shape:

```python
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "demo-model",
    "messages": [
        {"role": "user", "content": "Hello"}
    ]
}
```

### 4. Why A Small Function Helps
It is easier to start with one small function like:

```python
def get_model_reply(user_text):
    return f"Mock reply: {user_text}"
```

Later, you can replace only this function with a real API request.

### 5. Saving A Result
Saving model output can help for:
- debugging
- review
- comparing replies later

Simple idea:

```python
import json

result = {"reply": "Hello"}

with open("last_reply.json", "w") as file:
    json.dump(result, file, indent=2)
```

### 6. Simple Terminal Chatbot Flow
A tiny terminal chatbot can look like:
- ask for input
- stop if the user types `exit`
- get a reply
- print the reply

### 7. FastAPI Later
The same reply function could later be used:
- in a terminal chatbot
- in a FastAPI route

That is why separating the reply logic is useful.

## Hint
For today, practice the chatbot flow with a mock reply function.

That keeps the lesson simple while still preparing you for a real provider later.

## One Small Exercise
Write code that:
- defines a function `get_model_reply(user_text)`
- returns:

```python
f"Mock reply: {user_text}"
```

- uses a `while True` loop
- asks the user to enter a message
- stops if the user types `"exit"`
- otherwise prints the reply from `get_model_reply(...)`

## Hint 1
Start with:

```python
def get_model_reply(user_text):
```

## Hint 2
Inside the loop, use:

```python
user_text = input("You: ")
```

## Hint 3
Use:

```python
if user_text == "exit":
    break
```

## When You Finish
Send me only your GenAI Prep Day 14 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the small basics problem for Day 14 from the roadmap.

### Problem
Write code for a beginner two-sum style problem.

Use:

```python
numbers = [2, 7, 11, 15]
target = 9
```

Your program should print the two numbers that add up to `9`.

For this beginner version, printing:

```python
2 7
```

is enough.

### Hint 4
Use two loops and check whether:

```python
first + second == target
```

## When You Finish The Basics Problem
Send me only your Day 14 basics-problem code.
