# GenAI Prep Day 8: Provider-Neutral AI API Workflow

## Quick Revision
- Secrets should stay outside your code.
- `os.getenv(...)` reads values from the environment.
- `.gitignore` helps prevent secret files from being tracked.

## Today's Goal
- Understand the common shape of an AI API request
- See the role of headers, JSON payload, and response JSON
- Learn the difference between GET and POST at a practical level
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If you are sending a prompt or message to an AI API, does that sound more like "getting a page" or "sending structured data"?

If you can explain why it is sending structured data, you're ready.

## Tiny Lesson

### 1. GET vs POST
- `GET` is usually for fetching data
- `POST` is usually for sending structured data

For AI APIs, you often send:
- a model name
- a prompt or messages
- settings

So `POST` is very common.

### 2. What Headers Do
Headers give extra information about the request.

Common examples:
- authentication
- content type

Example:

```python
headers = {
    "Authorization": "Bearer DEMO_KEY",
    "Content-Type": "application/json"
}
```

### 3. What the JSON Payload Does
The payload is the structured data you send.

Example:

```python
payload = {
    "model": "demo-model",
    "messages": [
        {"role": "user", "content": "Hello"}
    ]
}
```

### 4. Common Workflow
The usual pattern is:
- build headers
- build payload
- send a POST request
- read the JSON response

## Revision Notes

### Auth Header Idea
Many real APIs need an authentication header.

Example:

```python
headers = {
    "Authorization": "Bearer DEMO_KEY",
    "Content-Type": "application/json"
}
```

You do not need a real key for this lesson.

Just remember the pattern.

### Timeout Idea
A timeout helps prevent the request from waiting forever.

Example:

```python
response = requests.post(url, headers=headers, json=payload, timeout=10)
```

This means:
- wait up to 10 seconds
- if the request takes too long, stop and raise an error

### What To Remember From Day 8
- `POST` is common when sending AI-style request data
- headers often include content type and auth
- payload holds the model and messages
- response JSON holds the returned data
- timeouts make requests safer

## Hint
For today's exercise, use a public echo service so you can practice the request shape without needing a paid AI provider.

## One Small Exercise
Write code that:
- imports `requests`
- creates a `headers` dictionary with `"Content-Type": "application/json"`
- creates a `payload` dictionary with:
  - `"model": "demo-model"`
  - `"messages": [{"role": "user", "content": "Hello"}]`
- sends a POST request to `https://httpbin.org/post`
- prints `response.status_code`
- prints `response.json()["json"]`

## Hint 1
Use:

```python
response = requests.post(url, headers=headers, json=payload, timeout=10)
```

## Hint 2
`response.json()["json"]` should show the JSON body that was sent.

## When You Finish
Send me only your GenAI Prep Day 8 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the small basics problem for Day 8 from the roadmap.

### Problem
Write code that merges two dictionaries.

Use:

```python
first = {"a": 1, "b": 2}
second = {"c": 3, "d": 4}
```

Your program should produce one merged dictionary.

### Hint 3
You can create a new dictionary and add items from both.

## When You Finish The Basics Problem
Send me only your Day 8 basics-problem code.
