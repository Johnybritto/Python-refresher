# Gemini Free Tier Day 8: Tool Calling Basics

## Quick Revision
- A normal Gemini call returns text.
- A streaming Gemini call returns the reply in chunks.
- Longer prompts make streaming easier to notice.

## Today's Goal
- understand what a tool is in simple words
- see how a normal Python function can act like a tool
- return structured data from that function
- explain when a model might want to use that tool

## Check Your Current Level
Before starting, ask yourself:

If a model needs an exact number, date, or calculation, is it safer to guess in plain text or ask a function for the result?

If you can explain why a function can be safer, you're ready.

## Tiny Lesson

### 1. What A Tool Means
For today, a tool is just a Python function the model could use to get a specific job done.

Example jobs:
- calculate something
- look up data
- return a small structured answer

### 2. Why Tools Help
A model is good at language.

A function is better when you need:
- exact output
- repeatable logic
- structured data

### 3. Beginner Tool Example
A tiny tool can be:

```python
def get_square(n):
    return {"number": n, "square": n * n}
```

This returns structured data instead of a paragraph.

### 4. What "Model Might Want To Call It" Means
If a user asks:

```text
What is the square of 5?
```

then a model might want to call `get_square(5)` instead of guessing.

### 5. Keep Day 8 Small
Today you do not need real automatic Gemini tool calling yet.

Just build one small Python function that behaves like a tool.

## Hint
Pick a tiny function with one clear job.

## One Small Exercise
Complete [DAY_08.py](./DAY_08.py) so it:
- defines one small function that acts like a tool
- returns a dictionary
- calls the function once
- prints the returned dictionary
- prints one short sentence about when a model might want to use that tool

## Hint 1
Start with:

```python
def ...
```

## Hint 2
A dictionary result can look like:

```python
{"number": 5, "square": 25}
```

## Hint 3
Keep the explanation sentence short and simple.

## When You Finish
Send me only your Gemini Free Tier Day 8 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the short Python basics problem for Day 8 from the roadmap.

### Problem
Write a function:

```python
square_number(n)
```

that returns the square of `n`.

Then call it with `5` and print the result.

### Hint 4
Use `return`, not just `print()` inside the function.

## When You Finish The Basics Problem
Send me only your [DAY_08_BASICS.py](./DAY_08_BASICS.py) code.
