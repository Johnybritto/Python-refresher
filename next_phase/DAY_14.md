# Next Phase Day 14: Mini Project and Wrap-Up

## Quick Revision
- `requests.get(...)` sends an API request.
- `response.json()` converts JSON response data into Python data.
- `.get(...)` is a safer way to access a key.
- `try` and `except` help handle API problems more safely.

## Today's Goal
- Combine API request, JSON reading, and safe handling
- Build one small practical script
- Review what this phase added

## Mini Project Idea
Build a small GitHub API reader.

The program should:
- send a request to `https://api.github.com`
- safely read the JSON response
- print `current_user_url`
- print `current_user_authorizations_html_url`
- handle API problems safely

## Tiny Lesson

### 1. Why This Project Helps
It combines:
- external library use
- API request
- JSON data reading
- safe key access
- error handling

### 2. Suggested Structure

```python
import requests

try:
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        data = response.json()
        print(data.get("current_user_url"))
        print(data.get("current_user_authorizations_html_url"))
    else:
        print("API error")
except:
    print("API error")
```

## Hint
Use the Day 13 pattern and extend it by printing one more key.

## One Small Exercise
Write code that:
- imports `requests`
- uses `try`
- sends a request to `https://api.github.com`
- stores `response.json()` in `data`
- prints `data.get("current_user_url")`
- prints `data.get("current_user_authorizations_html_url")`
- prints `"API error"` if something goes wrong

## When You Finish
Send me only your Next Phase Day 14 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
