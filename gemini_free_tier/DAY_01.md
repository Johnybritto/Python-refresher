# Gemini Free Tier Day 1: Setup and First Real Call

## Quick Revision
- A helper function is easier to replace later than a whole program.
- API keys should stay outside your code.
- Small test prompts make debugging easier.

## Today's Goal
- understand where the Gemini API key belongs
- see the current SDK shape at a beginner level
- make one real model call
- print only the returned text

## Check Your Current Level
Before starting, ask yourself:

Why is `GEMINI_API_KEY` safer in the environment than directly inside a Python file?

If you can explain that in simple words, you're ready.

## Tiny Lesson

### 1. Keep The Secret Out Of The Code
Your program should use the API key, but the key should not be written inside the script.

That is why we use the `GEMINI_API_KEY` environment variable.

### 2. Start With The Smallest Working Flow
For Day 1, the whole path is:
- create a client
- send one short prompt
- get the response
- print only the text

### 3. Use One Clear Model Call
The official Python SDK uses:
- `from google import genai`
- `genai.Client()`
- `client.models.generate_content(...)`

That is enough for your first real request.

### 4. Keep The Prompt Tiny
A short prompt is better for the first run because it makes errors easier to spot.

Example idea:

```python
"Explain what a Python list is in one short sentence."
```

### 5. Compare This With The Mock Version
In a mock version, you returned a string yourself.

In the real version:
- the SDK sends the prompt
- Gemini creates the reply
- you read `response.text`

## Hint
Do not hardcode the API key in `DAY_01.py`.

## One Small Exercise
Complete [DAY_01.py](./DAY_01.py) so it:
- imports `genai`
- creates a client
- sends one short prompt to Gemini
- stores the returned text in `reply_text`
- prints only `reply_text`

## Hint 1
Start with:

```python
from google import genai
```

## Hint 2
The client object is created with:

```python
client = genai.Client()
```

## Hint 3
The response object should come from:

```python
client.models.generate_content(...)
```

## When You Finish
Send me only your Gemini Free Tier Day 1 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the short Python basics problem for Day 1 from the roadmap.

### Problem
Write code that counts how many vowels are in a string.

Use this string:

```python
text = "hello world"
```

Your program should count these vowels:
- `a`
- `e`
- `i`
- `o`
- `u`

Then print the final count.

### Example
For:

```python
text = "hello world"
```

the answer should be:

```python
3
```

because the vowels are:
- `e`
- `o`
- `o`

### Hint 4
Loop through each character in the string.

### Hint 5
Check whether each character is in:

```python
"aeiou"
```

## When You Finish The Basics Problem
Send me only your [DAY_01_BASICS.py](./DAY_01_BASICS.py) code.
