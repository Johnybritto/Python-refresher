# Advanced Day 2: Scope and Variable Lifetime

## Quick Revision From Advanced Day 1
- `print()` shows a value immediately.
- `return` gives a value back so it can be stored or reused later.
- Returned values make functions more flexible.
- Good function design keeps one job in one function.

## Today's Goal
- Understand what local scope means
- Understand what global scope means
- See why variable names inside functions can be separate from outside variables
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a variable is created inside a function, should code outside the function always be able to use it?

If you can explain why not, you're ready.

## Tiny Lesson

### 1. Local Variable
A variable created inside a function is usually local to that function.

```python
def greet():
    message = "Hello"
    print(message)
```

Here, `message` belongs to the function.

### 2. Global Variable
A variable created outside functions can usually be read from many places.

```python
name = "Ravi"

def show_name():
    print(name)
```

Here, `name` was created outside the function.

### 3. Why Scope Matters
Scope helps prevent variables from accidentally interfering with each other.

It also helps you know:
- where a variable was created
- where it can be used

### 4. Important Beginner Idea
Just because two variables have the same name does not always mean they are the same variable.

## Hint
For today's exercise, keep it simple:

Create one variable outside a function and one variable inside a function.

## One Small Exercise
Write code that:
- creates a variable `name = "Ravi"` outside a function
- defines a function `show_name()`
- inside the function, prints `name`
- calls the function

Then answer in one short line:

Is `name` local or global in this example?

## Hint 1
Start with:

```python
name = "Ravi"
```

## Hint 2
Then define:

```python
def show_name():
    print(name)
```

## Hint 3
After that, call `show_name()`.

## When You Finish
Send me only your Advanced Day 2 code and your one-line answer.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
