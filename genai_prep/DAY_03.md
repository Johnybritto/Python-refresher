# GenAI Prep Day 3: Decorators

## Quick Revision
- A function can return one value with `return`.
- A generator can give values one at a time with `yield`.
- Functions can be passed around and reused.

## Today's Goal
- Understand the idea of a decorator
- See how one function can wrap another function
- Learn why decorators are useful
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If you want to add extra behavior before and after a function runs, should you rewrite that function every time?

If you can explain why not, you're ready.

## Tiny Lesson

### 1. The Main Idea
A decorator lets you wrap one function with extra behavior.

For now, think of it like this:
- run something before the function
- run the function
- run something after the function

### 2. Simple Wrapping Example

```python
def greet():
    print("Hello")

def wrapper():
    print("Before")
    greet()
    print("After")
```

This works, but it is not reusable yet.

### 3. Decorator Pattern

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
```

Now we can do:

```python
def greet():
    print("Hello")

decorated_greet = my_decorator(greet)
decorated_greet()
```

This prints:

```python
Before
Hello
After
```

### 4. Why This Matters
Decorators are useful when you want to add repeated behavior like:
- logging
- timing
- checking access
- wrapping API routes later

### 5. Simple Mental Model
- `func` is the original function
- `wrapper` adds extra behavior
- the decorator returns the new wrapped function

## Revision Notes

### What a Decorator Does
A decorator takes one function and replaces it with a wrapped function.

That wrapped function can:
- do something before the original function
- call the original function
- do something after the original function

### Why `wrapper()` Is Needed
The wrapper is needed because a decorator must return a function.

If you only write the logic directly inside the decorator:
- it runs immediately
- it does not return a new callable function
- Python has nothing to use later as the wrapped version

So the normal pattern is:

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
```

### Key Idea
`@my_decorator` means the original function gets replaced by the wrapped function.

So:

```python
@my_decorator
def greet():
    print("Hello")
```

is similar in idea to:

```python
def greet():
    print("Hello")

greet = my_decorator(greet)
```

### Why Decorators Are Useful
You do not always need decorators.

For small code, you can still call one function inside another function.

Decorators become useful when the same wrapping behavior repeats across many functions.

Examples:
- logging
- timing
- checking access
- wrapping routes in frameworks later

### Extra Example: `genai` Decorator

```python
def genai(func):
    def wrapper():
        print("hello welcome to the class")
        func()
        print("end of class")
    return wrapper

@genai
def new():
    print("day1")

@genai
def last():
    print("lastday")

new()
last()
```

### What This Example Shows
- the same decorator can wrap many functions
- the extra repeated behavior is written once
- each wrapped function still keeps its own main job

## Hint
Today is only about the basic wrapping idea.

Do not worry about advanced decorator syntax yet.

## One Small Exercise
Write code that:
- defines a decorator function `my_decorator(func)`
- defines `wrapper()` inside it
- prints `"Before"` before calling `func()`
- prints `"After"` after calling `func()`
- defines a function `greet()` that prints `"Hello"`
- creates `decorated_greet = my_decorator(greet)`
- calls `decorated_greet()`

## Hint 1
Start with:

```python
def my_decorator(func):
```

## Hint 2
Inside it, define:

```python
def wrapper():
```

## Hint 3
Return `wrapper` at the end of the decorator.

## When You Finish
Send me only your GenAI Prep Day 3 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the small basics problem for Day 3 from the roadmap.

### Problem
Write code that checks whether a string is a palindrome.

Use this string:

```python
text = "level"
```

Your program should print:

```python
palindrome
```

if the string reads the same forward and backward.

Otherwise print:

```python
not palindrome
```

### Hint 4
You can reverse the string first, then compare it with the original.

## When You Finish The Basics Problem
Send me only your Day 3 basics-problem code.
