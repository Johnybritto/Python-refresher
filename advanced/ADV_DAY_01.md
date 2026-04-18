# Advanced Day 1: Return Values and Function Design

## Quick Revision From the First 14 Days
- A function is a reusable block of code.
- `print()` shows something on the screen.
- Good function names make code easier to understand.
- We often want functions to do one small clear job.

## Today's Goal
- Understand the difference between `print` and `return`
- Write a small function that returns a value
- See why returned values are more reusable
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a function creates a result, do you always want to show it immediately, or might you want to store it and use it later?

If you can explain why using it later is helpful, you're ready.

## Tiny Lesson

### 1. `print()` vs `return`
`print()` shows a value on the screen.

```python
def greet(name):
    print("Hello", name)
```

`return` sends a value back from the function.

```python
def make_greeting(name):
    return "Hello " + name
```

### 2. Why `return` Is Powerful
If a function returns a value, you can:
- store it in a variable
- print it later
- use it inside another function

Example:

```python
message = make_greeting("Ravi")
print(message)
```

### 3. Good Function Design
Try to make functions:
- small
- clear
- focused on one job

## Hint
Build the exercise in two tiny steps:

1. Write a function that takes a name
2. Return a greeting string instead of printing it directly

## One Small Exercise
Write a function named `make_greeting` that takes a name and returns:

`"Hello <name>"`

After that:
- call the function
- store the result in a variable
- print the variable

## Hint 1
Start like this:

```python
def make_greeting(name):
```

## Hint 2
Use `return`, not `print`, inside the function.

## Hint 3
After calling the function, print the returned value outside the function.

## When You Finish
Send me only your Advanced Day 1 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
