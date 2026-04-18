# Advanced Day 12: Testing Basics

## Quick Revision From Advanced Day 11
- A class is a blueprint.
- An object is created from a class.
- `__init__` runs when the object is created.
- `self.name` stores data inside that object.

## Today's Goal
- Understand why testing matters
- Use simple `assert` statements
- Check whether code gives the expected result
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a function should return `5` but returns `6`, how could we make Python check that automatically?

If you can explain that Python can compare expected and actual results, you're ready.

## Tiny Lesson

### 1. What Is a Test?
A test checks whether code gives the result we expect.

It helps us catch mistakes early.

### 2. Simple `assert`
Python has a simple way to test with `assert`.

Example:

```python
def add(a, b):
    return a + b

assert add(2, 3) == 5
```

If the result is correct, nothing special happens.

If the result is wrong, Python raises an error.

### 3. Why This Matters
Tests help us:
- check our logic
- avoid silent mistakes
- feel more confident when changing code later

### 4. Beginner Idea
Think of `assert` like this:

```python
assert actual_result == expected_result
```

## Hint
For today's exercise, keep the function very small.

## One Small Exercise
Write code that:
- defines a function `add(a, b)`
- returns `a + b`
- uses `assert` to check that `add(2, 3) == 5`
- prints `"test passed"` after the assert

## Hint 1
Start with:

```python
def add(a, b):
    return a + b
```

## Hint 2
Then write:

```python
assert add(2, 3) == 5
```

## When You Finish
Send me only your Advanced Day 12 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
