# Full Revision Guide

Use this file as a quick revision notebook from the `basic` track through the `advanced` track and the `genai_prep` track.

## How To Use This File
- Read one section at a time.
- Run the code snippets by hand when possible.
- Focus extra on the recurring weak spots:
  - string reversal
  - time complexity vs space complexity
  - duplicates in lists
  - nested dictionary/list access
  - clear function design

---

## 1. Basic Python Revision

### 1.1 Variables and `print()`
Variables store values. `print()` shows output.

```python
name = "Johny"
age = 25

print(name)
print(age)
print(f"My name is {name} and I am {age}")
```

### 1.2 Data Types and Operators
Main beginner types:
- `int`
- `float`
- `str`
- `bool`

```python
number = 10
price = 19.5
text = "python"
is_ready = True

print(number + 2)
print(number / 2)
print(number // 3)
print(number % 3)
print(type(price))
```

### 1.3 Strings
Important ideas:
- indexing
- slicing
- methods

```python
word = "python"

print(word[0])
print(word[-1])
print(word[1:4])
print(word[::-1])
print(word.upper())
print(word.strip())
```

### 1.4 F-Strings
Use f-strings for clean output building.

```python
name = "Johny"
score = 95

print(f"{name} scored {score}")
```

### 1.5 Lists
Lists hold multiple values in order.

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[-1])

fruits.append("orange")
print(fruits)
print(len(fruits))
```

### 1.6 Looping Through Lists

```python
numbers = [1, 2, 3, 4]

for number in numbers:
    print(number)
```

### 1.7 Dictionaries
Dictionaries store `key: value` pairs.

```python
student = {
    "name": "Johny",
    "age": 25,
    "grade": "A"
}

print(student["name"])

student["city"] = "Hyderabad"
student["age"] = 26
print(student)
```

### 1.8 Sets
Sets keep unique values.

```python
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)

print(unique_numbers)
print(2 in unique_numbers)
```

### 1.9 Conditionals

```python
number = -2

if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")
```

### 1.10 Loops
`for` is common for fixed collections. `while` repeats until a condition changes.

```python
for i in range(1, 6):
    print(i)

count = 1
while count <= 3:
    print(count)
    count += 1
```

### 1.11 Functions
Functions help you reuse logic.

```python
def greet(name):
    return f"Hello {name}"

message = greet("Johny")
print(message)
```

### 1.12 Debugging Basics
Use tracebacks and simple `print()` checks.

```python
def add_numbers(a, b):
    print("a =", a)
    print("b =", b)
    return a + b

print(add_numbers(2, 3))
```

### 1.13 Complexity Basics
- Time complexity = how runtime grows
- Space complexity = how extra memory grows

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
```

The loop above is `O(n)` time and `O(1)` extra space.

### 1.14 Mini Combined Example

```python
def count_vowels(text):
    total = 0
    for ch in text.lower():
        if ch in "aeiou":
            total += 1
    return total

word = "Education"
print(count_vowels(word))
```

---

## 2. Advanced Python Revision

### 2.1 `print()` vs `return`
`print()` shows output. `return` gives a value back.

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print(result)
```

### 2.2 Scope
Variables inside a function are usually local.

```python
def show_name():
    name = "Johny"
    print(name)

show_name()
```

### 2.3 String Reversal and Palindrome

```python
word = "level"

reversed_word = ""
for ch in word:
    reversed_word = ch + reversed_word

print(reversed_word)
print(word == reversed_word)
```

### 2.4 List Problem Solving
Find duplicates with a set.

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
seen = set()
duplicates = []

for number in numbers:
    if number in seen and number not in duplicates:
        duplicates.append(number)
    seen.add(number)

print(duplicates)
```

### 2.5 List Comprehension

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
```

### 2.6 Nested Data

```python
student = {
    "name": "Johny",
    "marks": [80, 90, 95]
}

print(student["marks"][1])
```

### 2.7 Tuples and Sets

```python
point = (10, 20)
print(point[0])

first = {1, 2, 3}
second = {3, 4, 5}

print(first | second)
print(first & second)
print(first - second)
```

### 2.8 Exceptions

```python
text = "abc"

try:
    number = int(text)
    print(number)
except ValueError:
    print("Invalid number")
```

### 2.9 File Handling
Use `with open(...)` so files close safely.

```python
with open("hello.txt", "w") as file:
    file.write("Hello Python")

with open("hello.txt", "r") as file:
    data = file.read()

print(data)
```

### 2.10 Modules and Imports

```python
import math

print(math.sqrt(25))
print(math.floor(3.9))
print(math.ceil(3.1))
```

### 2.11 Classes and Objects

```python
class Dog:
    def bark(self):
        return "Woof"

my_dog = Dog()
print(my_dog.bark())
```

### 2.12 `__init__`

```python
class Cat:
    def __init__(self, name):
        self.name = name

my_cat = Cat("Milo")
print(my_cat.name)
```

### 2.13 Testing Basics

```python
def add_numbers(a, b):
    return a + b

assert add_numbers(2, 3) == 5
```

### 2.14 Complexity Tradeoffs
Two correct solutions can have different performance.

```python
numbers = [1, 2, 2, 3, 4]

# O(n^2) style
duplicates = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

print(duplicates)
```

---

## 3. GenAI Prep Revision

### 3.1 Context Managers
`with` manages setup and cleanup.

```python
with open("notes.txt", "r") as file:
    data = file.read()
    print(data)
```

### 3.2 Generators
`yield` gives one value at a time.

```python
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1

for value in count_up_to(3):
    print(value)
```

### 3.3 Decorators
Decorators wrap a function.

```python
def simple_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello")

say_hello()
```

### 3.4 OOP Quick Finish

```python
class Student:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

student = Student("Johny")
student.show_name()
```

### 3.5 Class Methods, Static Methods, Inheritance

```python
class Person:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_school(cls):
        return cls.school

    @staticmethod
    def helper():
        return "Helper method"

class Student(Person):
    pass

print(Student.show_school())
print(Student.helper())
```

### 3.6 Virtual Environments and `pip`
Common commands:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install requests
pip freeze > requirements.txt
```

### 3.7 Environment Variables

```python
import os

api_key = os.getenv("API_KEY")
print(api_key)
```

### 3.8 API Workflow Basics
Real APIs often need:
- URL
- headers
- JSON payload
- response parsing

```python
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer DEMO_KEY"
}

payload = {
    "model": "demo-model",
    "messages": [
        {"role": "user", "content": "Hello"}
    ]
}
```

### 3.9 Reading Nested AI-Style Responses

```python
response_data = {
    "choices": [
        {
            "message": {
                "content": "Hello from the model"
            }
        }
    ]
}

print(response_data["choices"][0]["message"]["content"])
```

### 3.10 Safe Parsing
Use `try/except` or `.get(...)` when the structure may be missing parts.

```python
try:
    content = response_data["choices"][0]["message"]["content"]
    print(content)
except (KeyError, IndexError, TypeError):
    print("No response text available")
```

### 3.11 Error Handling For APIs

```python
a = 10
b = 0

try:
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### 3.12 FastAPI Basics

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}
```

Run with:

```powershell
uvicorn genai_prep.DAY_11:app --reload
```

### 3.13 Path vs Route
- path = address like `"/hello"`
- route = the rule that connects a path to a function

```python
@app.get("/hello")
def say_hello():
    return {"message": "Hello"}
```

### 3.14 FastAPI With Request Data

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/echo")
def echo_data(data: dict):
    return {"received": data}
```

### 3.15 Pydantic Models
Pydantic describes the expected data structure.

```python
from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    reply: str
```

### 3.16 FastAPI Mini API

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    reply: str

@app.post("/mock-ai", response_model=PromptResponse)
async def mock_ai(data: PromptRequest):
    return PromptResponse(reply=f"Mock reply: {data.prompt}")
```

### 3.17 `async def`
For now, remember:
- `def` = normal function
- `async def` = async function, common in API code

```python
def normal_func():
    return "string"

async def async_func():
    return "string"
```

### 3.18 `TestClient`

```python
from fastapi.testclient import TestClient

client = TestClient(app)
response = client.post("/mock-ai", json={"prompt": "Hello"})
print(response.json())
```

### 3.19 Terminal Chatbot Mock Flow

```python
def get_model_reply(user_text):
    return f"Mock reply: {user_text}"

while True:
    user_text = input("You: ")
    if user_text == "exit":
        break
    print(get_model_reply(user_text))
```

### 3.20 Save Output As JSON

```python
import json

result = {"reply": "Hello"}

with open("last_reply.json", "w") as file:
    json.dump(result, file, indent=2)
```

---

## 4. Must-Revise Code Patterns

### 4.1 Reverse a String With Slicing

```python
text = "python"
print(text[::-1])
```

### 4.2 Reverse a String With a Loop

```python
text = "python"
reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print(reversed_text)
```

### 4.3 Count Frequency With a Dictionary

```python
text = "banana"
counts = {}

for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

print(counts)
```

### 4.4 Second Largest Number

```python
numbers = [5, 2, 9, 1, 7]
largest = float("-inf")
second = float("-inf")

for number in numbers:
    if number > largest:
        second = largest
        largest = number
    elif largest > number > second:
        second = number

print(second)
```

### 4.5 Sum Of Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]
total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print(total)
```

### 4.6 Prime Check

```python
number = 7
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("prime")
else:
    print("not prime")
```

### 4.7 Flatten One Level Of Nested List

```python
items = [[1, 2], [3, 4], [5]]
flattened = []

for group in items:
    flattened.extend(group)

print(flattened)
```

### 4.8 Two-Sum With A Dictionary

```python
numbers = [2, 7, 11, 15]
target = 9
seen = {}

for number in numbers:
    needed = target - number
    if needed in seen:
        print(needed, number)
        break
    seen[number] = True
```

---

## 5. Common Mistakes To Avoid

### 5.1 Printing Too Early Instead Of Returning

```python
def add_numbers(a, b):
    return a + b
```

### 5.2 Using Short Variable Names Without Need
Prefer:

```python
total = 0
flattened = []
student_name = "Johny"
```

instead of unclear names like `A`, `B`, or `x` when the meaning matters.

### 5.3 Catching Every Error With Bare `except`
Prefer:

```python
except ZeroDivisionError:
```

or:

```python
except (KeyError, IndexError, TypeError):
```

### 5.4 Mixing Function Jobs
Bad pattern:
- function reads input
- function stops the loop
- function prints

Better pattern:
- function returns data
- loop handles input and `break`
- caller prints

### 5.5 Confusing A Value With An Index
If you write:

```python
for number in numbers:
```

then `number` is the value itself, not the index.

### 5.6 Forgetting Exact Output Requirements
Match the required text exactly when an exercise gives a specific string.

### 5.7 Leaving Old Code In The File
Try to keep one final clean version when you finish.

---

## 6. High-Value Revision Order

If you want a fast revision pass, revise in this order:

1. Strings, lists, dictionaries, sets
2. Conditionals, loops, functions
3. Debugging, scope, exceptions, files
4. Nested data, duplicates, complexity
5. Context managers, generators, decorators
6. Environment variables, API payloads, JSON parsing
7. FastAPI routes, Pydantic, `async def`, `TestClient`
8. Terminal chatbot flow and mock AI response pattern

---

## 7. Final Reminder

You do not need to memorize everything at once.

Your strongest long-term revision targets are:
- writing small clean functions
- understanding list/dict/set patterns
- reading nested JSON confidently
- handling errors safely
- building small FastAPI routes
- explaining time complexity in simple words
