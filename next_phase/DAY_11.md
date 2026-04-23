# Next Phase Day 11: API Basics

## Quick Revision
- External libraries add features that Python does not include by default.
- `requests.get()` sends a request to a URL.
- `response.status_code` helps you check whether a request worked.

## Today's Goal
- Understand what an API is
- Learn the idea of request and response
- See how APIs often return JSON data
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a website sends data back to your Python program, what should your program do with that response?

If you can answer "read and use the data", you're ready.

## Tiny Lesson

### 1. What Is an API?
API stands for Application Programming Interface.

For now, think of it like this:
- your program asks for data
- another service sends data back

### 2. Request and Response
Your program sends a request.

The server sends a response.

Example:

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```

### 3. JSON Responses
Many APIs send data in JSON format.

JSON often looks like this:

```python
{
    "name": "John",
    "age": 25
}
```

After converting JSON in Python, it often becomes a dictionary.

### 4. Why This Matters
APIs help programs:
- get live data
- connect to other services
- build useful tools with real information

## Hint
Today is about understanding the idea, not mastering every API detail.

Focus on request, response, and JSON.

## One Small Exercise
Write code that:
- imports `requests`
- uses `requests.get()` on `https://api.github.com`
- stores the result in `response`
- prints `response.status_code`
- prints `type(response.json())`

## Hint 1
Start with:

```python
import requests
```

## Hint 2
You can use:

```python
print(type(response.json()))
```

## When You Finish
Send me only your Next Phase Day 11 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
