# Next Phase Day 4: Custom Modules

## Quick Revision
- `json.dump(...)` writes Python data to a JSON file.
- `json.load(...)` reads JSON from a file into Python data.
- `json.dumps(...)` gives JSON text as a string.
- `json.loads(...)` converts JSON text into Python data.

## Today's Goal
- Understand what a custom module is
- Create your own helper file
- Import your own function from another file
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If one file has a useful function, how can another file use it without copying the same code again?

If you can explain that we should import it, you're ready.

## Tiny Lesson

### 1. What Is a Custom Module?
A custom module is just your own Python file that contains reusable code.

Example:
- `helper.py` can store functions
- `main.py` can import and use them

### 2. Simple Example

`helper.py`

```python
def greet(name):
    return "Hello " + name
```

`main.py`

```python
import helper

print(helper.greet("Ravi"))
```

### 3. Why This Matters
Custom modules help you:
- avoid repeating code
- organize bigger programs
- keep related code together

### 4. Beginner Idea
One file can define functions.

Another file can import that file and use those functions.

## Hint
For today's exercise, keep the helper file very small.

## One Small Exercise
Create two files:

1. `helper.py`
- define a function `add_numbers(a, b)`
- return `a + b`

2. `DAY_04.py`
- import `helper`
- print the result of `helper.add_numbers(2, 3)`

## Hint 1
In `helper.py`, start with:

```python
def add_numbers(a, b):
    return a + b
```

## Hint 2
In `DAY_04.py`, use:

```python
import helper
```

## When You Finish
Send me your Next Phase Day 4 code from both files.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
