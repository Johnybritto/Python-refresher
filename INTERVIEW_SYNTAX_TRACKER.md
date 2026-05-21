# Interview Syntax Tracker

Use this file to track small Python syntax forms and concept variations that are easy to miss in interviews.

Goal:
- avoid “I know the concept but missed the syntax”
- revise short patterns quickly
- mark weak spots clearly

## How To Use
- When we discover a missed syntax form, add it here.
- Revise this file before interviews.
- Treat each item like a short flashcard:
  - what it is
  - what it looks like
  - what it is often confused with

---

## 1. Covered But Easy To Miss

### 1.1 Generator Expression
Status: identified gap

What it is:
- a short inline way to create a generator

Syntax:

```python
a = (x for x in range(3))
print(list(a))
```

Output:

```python
[0, 1, 2]
```

Common confusion:
- confusing it with a list comprehension
- forgetting that a generator gets exhausted after use

Compare:

```python
a = [x for x in range(3)]
```

This creates a list immediately.

### 1.2 `yield` Generator
Status: covered

What it is:
- a function-based generator

Syntax:

```python
def gen():
    for x in range(3):
        yield x

for value in gen():
    print(value)
```

Common confusion:
- thinking `yield` prints by itself
- forgetting the generator still needs to be consumed

---

## 2. High-Value Syntax Checklist

These are short Python forms that commonly appear in interviews and quick code screens.

### 2.1 List Comprehension
Status: revise

```python
squares = [x * x for x in range(5)]
```

### 2.2 Conditional List Comprehension
Status: revise

```python
evens = [x for x in range(10) if x % 2 == 0]
```

### 2.3 Dictionary `.get()`
Status: covered, keep revising

```python
counts[ch] = counts.get(ch, 0) + 1
```

### 2.4 `enumerate()`
Status: must revise

```python
items = ["a", "b", "c"]

for index, value in enumerate(items):
    print(index, value)
```

### 2.5 `zip()`
Status: must revise

```python
names = ["Ana", "Bob"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)
```

### 2.6 `range(start, stop, step)`
Status: covered, keep revising

```python
for i in range(10, 0, -1):
    print(i)
```

### 2.7 Membership With `in`
Status: covered

```python
if "a" in text:
    print("found")
```

### 2.8 Tuple Unpacking
Status: must revise

```python
a, b = 10, 20
print(a, b)
```

### 2.9 Swap Without Temp Variable
Status: must revise

```python
a, b = b, a
```

### 2.10 `sorted(..., key=...)`
Status: future revise

```python
words = ["pear", "banana", "fig"]
print(sorted(words, key=len))
```

### 2.11 Lambda
Status: future revise

```python
add = lambda a, b: a + b
print(add(2, 3))
```

### 2.12 `any()` and `all()`
Status: future revise

```python
numbers = [2, 4, 6]
print(all(n % 2 == 0 for n in numbers))
```

### 2.13 `try` / `except`
Status: covered

```python
try:
    value = int(text)
except ValueError:
    print("invalid")
```

### 2.14 `with open(...)`
Status: covered

```python
with open("file.txt", "r") as file:
    data = file.read()
```

### 2.15 `os.getenv(...)`
Status: covered, keep revising

```python
import os
api_key = os.getenv("GEMINI_API_KEY")
```

---

## 3. Interview Habit Rules

Before answering a Python interview question, quickly ask:

1. Is there a short syntax form for this?
2. Am I mixing up list vs generator?
3. Am I using a value where an index is expected?
4. Is there a built-in like `enumerate`, `zip`, `.get`, `sorted`, `any`, or `all` that fits?
5. Do I know whether I need a list immediately or one value at a time?

---

## 4. Current Watchlist

These are the forms to revise more often right now:
- generator expressions
- list comprehensions
- `enumerate()`
- `zip()`
- tuple unpacking
- `sorted(..., key=...)`

---

## 5. Update Rule

Whenever you get stuck on:
- syntax
- a built-in function
- a short Python form
- a concept variation

add it here immediately.
