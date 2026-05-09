# GenAI Prep Day 10: Error Handling for AI APIs

## Quick Revision
- Nested API-style responses often need an exact access path.
- Direct indexing can fail if a key or list item is missing.
- Safe fallback handling is important when the response shape is not guaranteed.

## Today's Goal
- Understand common API failure cases
- Use `try` and `except` for unsafe operations
- Use safe fallback messages instead of crashing
- See why timeouts and basic logging help
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If `"choices"` is missing from a response, what might happen if you write `response_data["choices"][0]`?

If you can explain why that can fail, you're ready.

## Tiny Lesson

### 1. Common API Problems
When working with AI APIs, a request may fail because:
- the server returns an error
- the request takes too long
- the response is missing expected keys
- too many requests are sent too quickly

### 2. Why `try` and `except` Help
`try` lets you run code that may fail.

`except` lets you handle the error safely.

Example:

```python
try:
    content = response_data["choices"][0]["message"]["content"]
    print(content)
except (KeyError, IndexError, TypeError):
    print("No response text available")
```

### 3. Timeout Idea
For real requests, use a timeout so the program does not wait forever.

Example:

```python
response = requests.post(url, headers=headers, json=payload, timeout=10)
```

### 4. Basic Logging Idea
A simple first step is to print what failed.

Example:

```python
except requests.exceptions.RequestException as error:
    print("Request failed:", error)
```

### 5. Rate-Limit and Cost Awareness
Real AI APIs can:
- limit how many requests you send
- charge per request or per token

So avoid:
- unnecessary repeated calls
- blind retry loops

## Hint
Today's exercise is about handling failure safely, not writing perfect production code yet.

## One Small Exercise
Write code that:
- creates this dictionary:

```python
response_data = {
    "choices": [
        {
            "message": {
                "content": "AI reply here"
            }
        }
    ]
}
```

- uses `try` and `except` to read:

```python
response_data["choices"][0]["message"]["content"]
```

- prints the content if it exists
- otherwise prints:

```python
No response text available
```

## Hint 1
Start with the Day 9 access path inside the `try` block.

## Hint 2
Catch:

```python
KeyError
```

and:

```python
IndexError
```

## When You Finish
Send me only your GenAI Prep Day 10 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the small basics problem for Day 10 from the roadmap.

### Problem
Write code that safely divides two numbers using `try` and `except`.

Use:

```python
a = 10
b = 0
```

Your program should:
- try to print `a / b`
- if division fails, print:

```python
Cannot divide by zero
```

### Hint 3
Catch:

```python
ZeroDivisionError
```

## When You Finish The Basics Problem
Send me only your Day 10 basics-problem code.
