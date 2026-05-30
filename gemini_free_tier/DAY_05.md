# Gemini Free Tier Day 5: Safe Gemini API Patterns

## Quick Revision
- A clear prompt gives the model better direction.
- A JSON-style prompt can make replies more predictable.
- Real API calls can fail, so a program should handle that safely.

## Today's Goal
- wrap one Gemini call in `try` / `except`
- print the model reply when the request works
- print a friendly fallback message when the request fails
- keep the program small and readable

## Check Your Current Level
Before starting, ask yourself:

Why is `try` / `except` better than letting the whole program crash for a beginner API script?

If you can answer that in simple words, you're ready.

## Tiny Lesson

### 1. Real Requests Can Fail
Even if your code looks correct, a real API call can still fail because of:
- missing API key
- network issues
- wrong model name
- temporary service problems

### 2. Use A Friendly Fallback
If the request fails, do not show a huge confusing failure to the user.

For Day 5, print one simple fallback message like:

```python
print("Could not get a Gemini reply right now.")
```

### 3. Keep The `try` Block Small
Only put the risky Gemini call part inside `try`.

That makes the code easier to read.

### 4. Keep Day 5 Focused
You only need:
- one client
- one prompt
- one `try`
- one `except`
- one fallback message

## Hint
Reuse your earlier Gemini setup, but avoid printing the API key.

## One Small Exercise
Complete [DAY_05.py](./DAY_05.py) so it:
- creates a Gemini client
- sends one prompt
- prints the reply text if the request works
- prints a friendly fallback message if the request fails

## Hint 1
You will need:

```python
try:
    ...
except Exception:
    ...
```

## Hint 2
Keep the fallback message short and clear.

## Hint 3
Use a simple prompt so the main focus stays on error handling.

## When You Finish
Send me only your Gemini Free Tier Day 5 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the short Python basics problem for Day 5 from the roadmap.

### Problem
Given:

```python
values = ["10", "20", "x", "30"]
```

Add only the valid integers and print the total.

Expected idea:
- `"10"` should be added
- `"20"` should be added
- `"x"` should be skipped
- `"30"` should be added

### Hint 4
Loop through the list one value at a time.

### Hint 5
Use `try` / `except` around `int(...)`.

## When You Finish The Basics Problem
Send me only your [DAY_05_BASICS.py](./DAY_05_BASICS.py) code.
