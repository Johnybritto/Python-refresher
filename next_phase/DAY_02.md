# Next Phase Day 2: JSON Basics

## Quick Revision
- Clear variable names make code easier to read.
- A function should usually do one small clear job.
- Returning a value is often better than printing too early.

## Today's Goal
- Understand what JSON is
- See how JSON looks like a Python dictionary
- Convert a Python dictionary into JSON text
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If we want to store structured data as text, what should that text look like so both humans and programs can read it?

If you can explain that it should have clear key-value structure, you're ready.

## Tiny Lesson

### 1. What Is JSON?
JSON is a text format used to store and share structured data.

It often looks similar to a Python dictionary.

Example JSON text:

```python
{"name": "Ravi", "score": 95}
```

### 2. Python Dictionary vs JSON Text
Python dictionary:

```python
student = {"name": "Ravi", "score": 95}
```

JSON text is text, not a real Python dictionary object.

### 3. Using `json.dumps(...)`
Python has a built-in module named `json`.

Example:

```python
import json

student = {"name": "Ravi", "score": 95}
json_text = json.dumps(student)
print(json_text)
```

### 4. Why This Matters
JSON is very common in:
- files
- APIs
- data exchange between programs

## Hint
For today's exercise, focus only on converting a Python dictionary into JSON text.

## One Small Exercise
Write code that:
- imports `json`
- creates a dictionary `student = {"name": "Ravi", "score": 95}`
- converts it into JSON text using `json.dumps(...)`
- stores the result in `json_text`
- prints `json_text`

## Hint 1
Start with:

```python
import json
```

## Hint 2
Use:

```python
json_text = json.dumps(student)
```

## When You Finish
Send me only your Next Phase Day 2 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
