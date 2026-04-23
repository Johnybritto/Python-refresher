# Next Phase Day 1: Clean Code and Better Function Design

## Quick Revision
- Good code should be correct.
- Good code should also be easy to read.
- Clear names make code easier to understand later.
- A function should usually do one small clear job.

## Today's Goal
- Use better variable names
- Write one small clean function
- Return a value instead of printing too early
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a function both calculates something and prints many things, can that make the code harder to reuse?

If you can explain why, you're ready.

## Tiny Lesson

### 1. Better Variable Names
Compare these:

```python
a = 10
b = 20
print(a + b)
```

```python
first_number = 10
second_number = 20
print(first_number + second_number)
```

The second version is easier to understand.

### 2. One Function, One Job
Try to make one function do one small clear task.

Example:

```python
def add_numbers(first_number, second_number):
    return first_number + second_number
```

This function:
- takes two numbers
- returns the answer
- does not print too early

### 3. Why `return` Helps
If a function returns a value, you can:
- print it later
- store it in a variable
- test it with `assert`

### 4. Clean Final Version
Try to keep one final clean solution instead of many half-finished versions in the same file.

## Hint
For today's exercise, keep the function simple and focus on naming clearly.

## One Small Exercise
Write code that:
- defines a function `add_numbers(first_number, second_number)`
- returns the sum
- stores the result of `add_numbers(10, 20)` in `total`
- prints `total`

## Hint 1
Start with:

```python
def add_numbers(first_number, second_number):
```

## Hint 2
Use `return`, not `print`, inside the function.

## Hint 3
Call the function outside and store the result in `total`.

## When You Finish
Send me only your Next Phase Day 1 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
