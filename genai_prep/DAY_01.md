# GenAI Prep Day 1: Context Managers

## Quick Revision
- `open()` lets Python work with files.
- Files should be closed after use.
- Cleaner code is often safer code.

## Today's Goal
- Understand what `with` does
- See why files use `with open(...)`
- Learn the basic idea of automatic cleanup
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a file is opened and never closed, could that cause problems later?

If you can explain why, you're ready.

## Tiny Lesson

### 1. The Problem
When Python opens a file, it should close it after the work is done.

You can do that manually:

```python
file = open("notes.txt", "r")
content = file.read()
file.close()
print(content)
```

This works, but it is easy to forget `close()`.

### 2. The Better Way
Python often uses `with` for this:

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

When the block ends, Python closes the file automatically.

### 3. Why This Matters
Context managers help with:
- safer file handling
- automatic cleanup
- cleaner code

### 4. Simple Meaning of "Context Manager"
For now, think of a context manager like this:

- start a resource safely
- use it inside the block
- clean it up automatically at the end

You do not need advanced details yet.

## Hint
Today's exercise is about using `with`, not about exception handling.

## One Small Exercise
Write code that:
- opens `notes.txt` in read mode using `with`
- stores the file content in `content`
- prints `content`

## Hint 1
Start with:

```python
with open("notes.txt", "r") as file:
```

## Hint 2
Use:

```python
content = file.read()
```

## When You Finish
Send me only your GenAI Prep Day 1 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## Next Content For Day 1
Nice. After using `with open(...)`, the next thing to understand is that `with` can work with more than files.

You can also create your own simple context manager.

## Tiny Extension

### 5. A Very Small Custom Context Manager
Python has a helper called `contextmanager` in `contextlib`.

It lets you create a simple context manager with a function.

Example:

```python
from contextlib import contextmanager

@contextmanager
def message():
    print("Starting")
    yield
    print("Ending")

with message():
    print("Inside block")
```

This prints:
- `Starting`
- `Inside block`
- `Ending`

### 6. Why This Helps
This teaches the deeper idea of a context manager:
- setup happens before `yield`
- the block runs at `yield`
- cleanup happens after `yield`

That same idea is why `with open(...)` works so well.

### 7. Simple Revision View
Keep this mental model:

- `with` is the syntax
- a context manager is the thing that works with `with`
- before `yield` means setup
- `yield` is where the `with` block runs
- after `yield` means cleanup

So a custom context manager is useful when you want your own before-and-after behavior around a block.

Real examples:
- open a database connection, then close it
- start a timer, then stop it
- lock something, then unlock it

Very short version:

```python
with something():
    do_work()
```

means:
- prepare `something`
- run `do_work()`
- clean up `something`

## Extra Clarification
Why use a custom context manager if `with` already exists?

Because `with` is only the language feature.

A custom context manager lets you define what should happen:
- before the block
- during the block
- after the block

That is why custom context managers exist.

## Day 1 Follow-Up Exercise
Write code that:
- imports `contextmanager` from `contextlib`
- defines a context manager function named `simple_timer`
- prints `"Start"` before `yield`
- prints `"End"` after `yield`
- uses `with simple_timer():`
- prints `"Working"` inside the block

## Hint 3
Start with:

```python
from contextlib import contextmanager
```

## Hint 4
Then write:

```python
@contextmanager
def simple_timer():
```

## When You Finish The Follow-Up
Send me only your Day 1 follow-up code.

## LeetCode-Style Basics Problem
This is the small basics problem for Day 1 from the roadmap.

### Problem
Write code that counts how many vowels are in a string.

Use this string:

```python
text = "hello world"
```

Your program should count these vowels:
- `a`
- `e`
- `i`
- `o`
- `u`

Then print the final count.

### Example
For:

```python
text = "hello world"
```

The answer should be:

```python
3
```

because the vowels are:
- `e`
- `o`
- `o`

### Hint 5
You can loop through each character in the string.

### Hint 6
Check whether each character is in:

```python
"aeiou"
```

### When You Finish The Basics Problem
Send me only your Day 1 basics-problem code.
