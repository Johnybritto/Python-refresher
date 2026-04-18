# Day 9: Conditionals

## Quick Revision From Day 8
- A set keeps only unique values.
- We can use `in` to check membership.
- We can count repeated items with a loop and a dictionary.
- The same counting idea works for both characters and numbers.

## Today's Goal
- Understand `if` and `else`
- Compare values with `>`
- Print different output based on a condition
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

What should happen if a number is bigger than `0`?

If you can answer that in words, you're ready.

## Tiny Lesson

### 1. What Is a Conditional?
A conditional lets your program make a decision.

```python
number = 5

if number > 0:
    print("positive")
else:
    print("zero or negative")
```

### 2. How It Works
- `if` checks a condition
- if the condition is true, that block runs
- otherwise, the `else` block runs

### 3. Important Detail
The code inside `if` and `else` must be indented.

```python
number = -2

if number > 0:
    print("positive")
else:
    print("zero or negative")
```

## Hint
Read this like plain English:

If the number is greater than zero, print `"positive"`.
Otherwise, print `"zero or negative"`.

## One Small Exercise
Write a program that:
- stores a number
- prints `"positive"` if it is greater than 0
- otherwise prints `"zero or negative"`

## Hint 1
Start like this:

```python
number = 7
```

## Hint 2
Use:

```python
if number > 0:
    print("positive")
else:
    print("zero or negative")
```

## When You Finish
Send me only your Day 9 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
