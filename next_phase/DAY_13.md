# Next Phase Day 13: Error Handling With APIs

## Quick Revision
- `requests.get()` sends a request to a URL.
- `response.json()` often gives Python data like a dictionary.
- API data should be checked before using it.

## Today's Goal
- Handle failed API requests more safely
- Avoid crashing if a key is missing
- Use `try`/`except` with API code
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If an API response does not contain the key you expect, should the program crash or handle it safely?

If you can explain that it should handle it safely, you're ready.

## Tiny Lesson

### 1. Why API Code Needs Safety
Sometimes:
- the request fails
- the response is not what you expect
- a key may be missing

### 2. Safe Key Access With `.get(...)`

Example:

```python
data = {"name": "Ravi"}
print(data.get("name"))
print(data.get("age"))
```

`data.get("age")` gives `None` instead of crashing.

### 3. `try`/`except` Around Request Code

Example:

```python
import requests

try:
    response = requests.get("https://api.github.com")
    data = response.json()
    print(data.get("current_user_url"))
except:
    print("API error")
```

### 4. Why This Matters
Safer API programs:
- crash less
- are easier to debug
- are friendlier to users

## Hint
For today's exercise, use `.get(...)` instead of direct key access.

## One Small Exercise
Write code that:
- imports `requests`
- uses `try`
- sends a request to `https://api.github.com`
- stores `response.json()` in `data`
- prints `data.get("current_user_url")`
- prints `"API error"` in `except` if something goes wrong

## Hint 1
Start with:

```python
import requests
```

## Hint 2
Use:

```python
print(data.get("current_user_url"))
```

## When You Finish
Send me only your Next Phase Day 13 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
