# Next Phase Day 12: Reading API Data

## Quick Revision
- An API request sends a request and gets a response.
- `response.status_code` helps check whether the request worked.
- `response.json()` often gives Python data like a dictionary.

## Today's Goal
- Read real values from API JSON data
- Store the JSON response in a variable
- Access specific keys from the response
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If `response.json()` gives a dictionary, how can you get one specific value from it?

If you can explain that we use a key, you're ready.

## Tiny Lesson

### 1. Store the JSON Data

Example:

```python
import requests

response = requests.get("https://api.github.com")
data = response.json()
```

Now `data` often behaves like a dictionary.

### 2. Read a Specific Key

Example:

```python
print(data["current_user_url"])
```

This prints one value from the response.

### 3. Why This Matters
Real API work usually means:
- request data
- convert it with `.json()`
- read the fields you need

## Hint
For today's exercise, focus on reading one key only.

## One Small Exercise
Write code that:
- imports `requests`
- sends a request to `https://api.github.com`
- stores `response.json()` in `data`
- prints `data["current_user_url"]`

## Hint 1
Start with:

```python
import requests
```

## Hint 2
Use:

```python
data = response.json()
```

## When You Finish
Send me only your Next Phase Day 12 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
