# Gemini Free Tier Day 10: Move Gemini Logic Into A Helper

## Quick Revision
- A FastAPI route can accept JSON input and return JSON output.
- `response.text` gives you the Gemini reply text.
- A function is a good place to hide repeated or risky logic.

## Today's Goal
- move the Gemini call into one helper function
- keep the FastAPI route focused on input and output
- return one plain reply string from the helper
- keep the code small and readable

## Check Your Current Level
Before starting, ask yourself:

If `get_gemini_reply(prompt)` already returns the final reply text, what should the route still need to do?

If you can say "read the request, call the helper, and return the response model," you're ready.

## Tiny Lesson

### 1. Why Refactor Today
Yesterday, everything lived inside the route.

That worked, but the route had too many jobs:
- read the request
- create the Gemini client
- call Gemini
- handle errors
- build the response

Today we split that into smaller parts.

### 2. What The Helper Should Do
Make one function with one clear job:

```python
get_gemini_reply(prompt)
```

That helper should:
- read the API key
- create the client
- call Gemini
- return the reply text
- return a friendly fallback string if something fails

### 3. What The Route Should Do
The route should stay simple:
- receive `data.prompt`
- call `get_gemini_reply(data.prompt)`
- return `PromptResponse(reply=reply_text)`

### 4. Why This Is Better
This version is easier to read because:
- the route is shorter
- the Gemini logic has one home
- later changes are easier

### 5. Beginner Refactor Rule
Do not change everything at once.

First move the Gemini logic into the helper.

Then keep the route as a thin wrapper around that helper.

## Hint
Start by copying the working Gemini code from Day 9 into a helper function, then remove that logic from the route.

## One Small Exercise
Complete [DAY_10.py](./DAY_10.py) so it:
- defines `get_gemini_reply(prompt)`
- moves the Gemini client and model call into that function
- keeps the fallback message inside that function
- keeps the route short
- returns `PromptResponse(reply=reply_text)`

## Hint 1
The helper should return a string, not a full `PromptResponse`.

## Hint 2
Your route can stay close to:

```python
reply_text = get_gemini_reply(data.prompt)
return PromptResponse(reply=reply_text)
```

## Hint 3
If the Gemini call fails, the helper can return:

```python
"Could not get a Gemini reply right now."
```

## When You Finish
Send me only your Gemini Free Tier Day 10 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the short Python basics problem for Day 10 from the roadmap.

### Problem
Given a list of numbers, write a helper function that returns only the even numbers.

Then call the function once and print the result.

### Hint 4
Check each number with:

```python
number % 2 == 0
```

## When You Finish The Basics Problem
Send me only your [DAY_10_BASICS.py](./DAY_10_BASICS.py) code.
