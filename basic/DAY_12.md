# Day 12: Functions II and Debugging

## Quick Revision From Day 11
- A function is a reusable block of code.
- `def` is used to define a function.
- A parameter lets a function receive a value.
- Good function names make code easier to read.
- A function can print something now, and later we will also use functions that return values.

## Today's Goal
- Understand what a simple bug looks like
- Read a traceback without panic
- Use `print()` to check what your code is doing
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a program crashes, do you want to guess the problem, or read the error message and inspect the code step by step?

If you can explain why checking step by step is better, you're ready.

## Tiny Lesson

### 1. What Is a Bug?
A bug is a mistake in the code that causes the wrong output or an error.

Example:

```python
name = "Ravi"
print(age)
```

This crashes because `age` was never created.

### 2. What Is a Traceback?
When Python crashes, it shows a traceback.

The traceback helps you find:
- which line caused the problem
- what kind of error happened

### 3. Use `print()` for Debugging
If your code is not doing what you expect, print important values.

Example:

```python
number = 3
print("number is", number)
```

This helps you see what the program is using at that moment.

### 4. Fixing Bugs Step by Step
Try this order:

1. Read the error message
2. Find the line number
3. Check the variable names or logic on that line
4. Add a small `print()` if needed

## Hint
For today's exercise, you do not need a big program.

Make one small buggy program, run it, notice the error, then fix it.

## One Small Exercise
Write a small buggy program, run it, and note:
- the error message
- what caused it
- how you fixed it

## Hint 1
You can start with a variable name mistake.

Example idea:

```python
name = "Asha"
print(nam)
```

### Hint 2
After you see the error, correct the variable name.

## When You Finish
Send me:
- your Day 12 code
- the error message in your own words
- what caused it
- how you fixed it

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
