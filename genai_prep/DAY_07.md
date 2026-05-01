# GenAI Prep Day 7: Environment Variables and Secrets

## Quick Revision
- A virtual environment keeps project packages separate.
- `pip` installs packages.
- `pip freeze > requirements.txt` saves installed packages.

## Today's Goal
- Understand why API keys should not be hardcoded
- Understand what an environment variable is
- Learn the basic idea of storing secrets safely
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If you put an API key directly inside your Python file, could that become risky later?

If you can explain why yes, you're ready.

## Tiny Lesson

### 1. Why Hardcoding Secrets Is Risky
If you write an API key directly in code:
- it can be leaked
- it can be pushed to Git by mistake
- it is harder to change later

### 2. What an Environment Variable Is
An environment variable stores a value outside your code.

Your Python program can read it when needed.

### 3. Example Idea

In Python:

```python
import os

api_key = os.getenv("API_KEY")
print(api_key)
```

This asks the environment for the value of `API_KEY`.

### 4. Why This Matters
This is the common pattern for:
- API keys
- tokens
- secret settings

## Revision Notes

### Main Python Pattern To Remember
For this lesson, the key thing to remember is:

```python
os.getenv("API_KEY")
```

This reads a value from the environment.

### Important Idea
- `os` does not store the secret
- `os.getenv(...)` only reads it
- the value comes from the shell, system environment, or another environment source

### Temporary vs Project-Specific
- a shell session variable is often temporary
- a `.env` file is a common project-specific way to provide values later

### What Matters Today
For today, focus on:
- keep secrets outside code
- read them with `os.getenv(...)`

You do not need to learn the full `.env` workflow yet.

## Basics Problem Revision

### Word Count With `split()`

```python
text = "python is fun to learn"
print(len(text.split()))
```

### Word Count Without `split()`

```python
text = "python is fun to learn"

count = 1

for ch in text:
    if ch == " ":
        count += 1

print(count)
```

### What These Show
- `split()` is shorter and cleaner
- manual counting is useful for loop practice

## `.gitignore` Revision

### What `.gitignore` Does
`.gitignore` tells Git which files and folders should not be tracked.

This is useful for things like:
- secret files
- virtual environments
- cache files

### Why It Matters Here
When working with API keys and project setup, you often do not want Git to track:
- `.env`
- `.venv/`
- `__pycache__/`

### Simple Example

```gitignore
.venv/
.env
__pycache__/
```

### What To Remember
- `.gitignore` helps prevent accidental commits of files you do not want in version control
- it is especially important for secrets and environment files

## Hint
For today's exercise, you do not need a real API key.

Just practice the reading pattern.

## One Small Exercise
Write code that:
- imports `os`
- reads `API_KEY` using `os.getenv("API_KEY")`
- stores it in `api_key`
- prints `api_key`

## Hint 1
Start with:

```python
import os
```

## Hint 2
Use:

```python
api_key = os.getenv("API_KEY")
```

## When You Finish
Send me only your GenAI Prep Day 7 code.

Then I will review it for:
- Correctness
- Readability
- What to improve next

## LeetCode-Style Basics Problem
This is the small basics problem for Day 7 from the roadmap.

### Problem
Write code that counts how many words are in a sentence.

Use this text:

```python
text = "python is fun to learn"
```

Your program should print the total word count.

### Hint 3
You can use:

```python
text.split()
```

## When You Finish The Basics Problem
Send me only your Day 7 basics-problem code.
