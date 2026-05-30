# Gemini Free Tier Day 4: Structured Outputs

## Quick Revision
- `response.text` gives the main beginner-friendly reply text.
- Saving prompt and reply to JSON helps you keep useful experiments.
- Today we are not saving yet. We are first learning how to ask the model for a cleaner output shape.

## Today's Goal
- ask Gemini for JSON-style output
- request exactly two keys
- print the raw returned text
- compare plain text thinking with structured output thinking

## Check Your Current Level
Before starting, ask yourself:

Why is it useful to ask the model for a fixed shape like JSON instead of a free-form paragraph?

If you can answer that in simple words, you're ready.

## Tiny Lesson

### 1. Plain Text vs Structured Output
A normal prompt may give a paragraph.

That is fine for reading.

But sometimes your program needs a predictable shape.

Example:
- easier to save
- easier to parse later
- easier to check whether the answer is complete

### 2. Ask For The Exact Shape
If you want structured output, say so clearly.

For Day 4, ask for exactly two keys.

Example idea:

```python
Return valid JSON with exactly these two keys:
"topic"
"summary"
```

### 3. Do Not Parse Too Early
Today, only print the raw returned text.

We want to first see what the model actually gives back.

Parsing can come later.

### 4. Keep The Task Small
You only need:
- one client
- one prompt
- one response
- one `print(response.text)`

## Hint
Reuse your Day 3 Gemini setup, but do not print the API key.

## One Small Exercise
Complete [DAY_04.py](./DAY_04.py) so it:
- sends one prompt to Gemini
- asks for valid JSON
- asks for exactly two keys: `"topic"` and `"summary"`
- prints the raw returned text

## Hint 1
Your prompt can tell the model:

```python
Return valid JSON with exactly two keys: "topic" and "summary".
```

## Hint 2
Pick one simple topic like Python lists or JSON.

## Hint 3
Do not use `json.loads(...)` yet.

## When You Finish
Send me only your Gemini Free Tier Day 4 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the short Python basics problem for Day 4 from the roadmap.

### Problem
Given:

```python
data = {"name": "Ana", "age": 20}
```

Print `"valid"` only if:
- `"name"`
- `"age"`
- `age` is at least `18`

Otherwise print `"invalid"`.

### Hint 4
Use `in` with the dictionary first.

### Hint 5
After checking the keys, compare `data["age"]` with `18`.

## When You Finish The Basics Problem
Send me only your [DAY_04_BASICS.py](./DAY_04_BASICS.py) code.
