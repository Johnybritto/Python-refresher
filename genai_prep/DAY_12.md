# GenAI Prep Day 12: FastAPI With Request Data

## Quick Revision
- FastAPI helps you build APIs in Python.
- `app = FastAPI()` creates the app object.
- A GET route connects a path like `"/"` to a function.

## Today's Goal
- Understand what a POST route does
- Read JSON request data in FastAPI
- Return JSON data from a route
- See the idea of query parameters and path parameters
- Notice how status codes fit into API responses
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a client wants to send text into your API, does that sound more like a GET request or a POST request?

If you can explain why it is usually POST, you're ready.

## Tiny Lesson

### 1. Why POST Matters
GET is often used to fetch data.

POST is often used to send structured data to the server.

For example, if someone sends:
- a prompt
- a name
- a message

that is usually a POST request.

### 2. Reading JSON Data
In FastAPI, one simple beginner pattern is to accept a dictionary.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/message")
def create_message(data: dict):
    return {"received": data}
```

If a client sends JSON, FastAPI reads it into `data`.

### 3. Returning JSON
When you return a dictionary, FastAPI sends it back as JSON.

Example:

```python
return {"message": "Hello"}
```

### 4. Query Parameters
Query parameters are values in the URL.

Example idea:

```python
@app.get("/hello")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
```

A request could look like:

```text
/hello?name=Johny
```

### 5. Path Parameters
Path parameters are part of the path itself.

Example:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

Here, `item_id` comes from the URL path.

### 6. Status Code Idea
Every response has a status code.

Common examples:
- `200` for success
- `404` for not found

For today, just remember that APIs return both:
- data
- a status code

## Hint
For today's exercise, keep it simple:
- one POST route
- one input dictionary
- one returned dictionary

## One Small Exercise
Write code that:
- imports `FastAPI`
- creates `app = FastAPI()`
- adds one POST route for `"/echo"`
- accepts one parameter `data: dict`
- returns:

```python
{"received": data}
```

## Hint 1
Use:

```python
@app.post("/echo")
```

## Hint 2
The function can look like:

```python
def echo_data(data: dict):
```

## When You Finish
Send me only your GenAI Prep Day 12 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the small basics problem for Day 12 from the roadmap.

### Problem
Write code that finds the sum of even numbers in a list.

Use:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

Your program should print the total of only the even numbers.

### Hint 3
Loop through the list and check:

```python
number % 2 == 0
```

## When You Finish The Basics Problem
Send me only your Day 12 basics-problem code.
