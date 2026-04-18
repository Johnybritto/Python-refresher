# Day 11: Functions I

## Quick Revision From Day 10
- A loop repeats code.
- `for` is useful when you know the pattern of repetition.
- `while` is useful when you want to continue until a condition changes.
- `range()` can move forward or backward.
- Reversing a string with `[::-1]` and with a backward loop is worth revising often.

## Today's Goal
- Understand what a function is
- Learn how to define a function with `def`
- Pass one value into a function with a parameter
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If you need to print the same greeting for many different names, would you rather rewrite the same code each time or put it in one reusable block?

If you can explain why reuse helps, you're ready.

## Tiny Lesson

### 1. What Is a Function?
A function is a reusable block of code.

Instead of writing the same logic again and again, we can give that logic a name and call it when we need it.

### 2. Basic Function Shape

```python
def greet():
    print("Hello")
```

`def` starts the function definition.

### 3. Function With a Parameter
A parameter lets the function receive a value.

```python
def greet(name):
    print("Hello", name)
```

If we call `greet("Asha")`, the function prints a greeting for that name.

### 4. Why This Helps
- less repeated code
- easier to read
- easier to reuse later

## Hint
Build the solution in two small steps:

1. Define a function named `greet` with one parameter called `name`
2. Print a greeting using that parameter

## One Small Exercise
Write a function that takes a name and prints a greeting.

## Hint 1
Start like this:

```python
def greet(name):
```

## Hint 2
Inside the function, print `"Hello"` and the name.

## Hint 3
After defining the function, call it with one name like `"Ravi"`.

## When You Finish
Send me only your Day 11 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
