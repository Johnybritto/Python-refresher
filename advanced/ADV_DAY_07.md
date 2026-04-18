# Advanced Day 7: Exceptions and Error Handling

## Quick Revision From Advanced Day 6
- A tuple uses parentheses like `(2, 5)`.
- A tuple supports index access like `point[0]`.
- A set stores unique values.
- A set is useful for removing duplicates and checking membership with `in`.

## Today's Goal
- Understand what an exception is
- Learn `try` and `except`
- See how Python can handle bad input more safely
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If code crashes because the input is not a number, how could we stop the whole program from breaking?

If you can explain that we should catch the error, you're ready.

## Tiny Lesson

### 1. What Is an Exception?
An exception is an error that happens while the program is running.

Example:

```python
number = int("hello")
```

This causes an error because `"hello"` cannot be converted to an integer.

### 2. Why `try` and `except` Help
`try` lets Python attempt risky code.

`except` lets Python handle the error instead of crashing.

Example:

```python
try:
    number = int("hello")
    print(number)
except:
    print("Invalid number")
```

### 3. Beginner Idea
Think of it like this:
- `try`: try to do the job
- `except`: if it fails, do something safer

### 4. Why This Matters
Real users may type wrong input.

Error handling helps programs:
- stay running
- show clearer messages
- avoid sudden crashes

## Hint
For today's exercise, use the exact `try` and `except` structure first.

Do not worry about naming the exact error type yet.

## One Small Exercise
Write code that:
- stores `"25"` in a variable
- uses `int(...)` to convert it to a number inside a `try` block
- prints the number if conversion works
- prints `"Invalid number"` in `except` if conversion fails

## Hint 1
Start with:

```python
value = "25"
```

## Hint 2
Put `int(value)` inside `try`.

## Hint 3
If conversion works, print the converted number.

## When You Finish
Send me only your Advanced Day 7 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
