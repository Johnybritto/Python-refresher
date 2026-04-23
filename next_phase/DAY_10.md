# Next Phase Day 10: Using External Libraries

## Quick Revision
- `input()` lets a program read text from the user.
- `if`, `elif`, and `else` help a program choose what to do.
- Small menu programs are built from simple steps.

## Today's Goal
- Learn what a library is
- Understand built-in vs external modules
- See why some packages need installation
- Do one small exercise with `requests`

## Check Your Current Level
Before starting, ask yourself:

If Python says `ModuleNotFoundError`, what might that mean?

If you can answer "the library may not be installed", you're ready.

## Tiny Lesson

### 1. What Is a Library?
A library is code written by someone else that you can use in your program.

Python already includes some built-in modules like:
- `math`
- `random`
- `json`

Other libraries must be installed first.

### 2. Built-in vs External
Built-in modules:
- come with Python
- work right away

External libraries:
- are installed separately
- give you extra features

One common example is `requests`.

### 3. Why `requests` Is Useful
`requests` helps your program talk to websites and APIs.

Example:

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```

### 4. Installing a Library
If `requests` is not installed, you can install it with:

```bash
pip install requests
```

### 5. Why This Matters
External libraries let you:
- work with APIs
- handle web data
- build more useful programs faster

## Hint
For today, the main goal is understanding the import and the idea of using a package.

Do not worry if the request part feels new.

## One Small Exercise
Write code that:
- imports `requests`
- uses `requests.get()` on `https://api.github.com`
- stores the result in `response`
- prints `response.status_code`

## Hint 1
Start with:

```python
import requests
```

## Hint 2
Use:

```python
response = requests.get("https://api.github.com")
```

## When You Finish
Send me only your Next Phase Day 10 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
