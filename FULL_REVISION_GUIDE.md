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

### 4.9 Binary Search Interval Pattern
The hardest part is usually not `mid`.

The hardest part is deciding what `low` and `high` mean.

Ask first:
- what is my search space?
- is the right end included or excluded?

#### Closed Interval: `[low, high]`
Use this when both ends are valid indices.

```python
arr = [2, 5, 8, 12]
target = 8

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
```

Pattern to remember:
- `low = 0`
- `high = len(arr) - 1`
- loop with `while low <= high`
- use this for normal Python index-based binary search

Why:
- `low` points to a real index
- `high` points to a real index
- when `low == high`, one element is still left to check

#### Half-Open Interval: `[low, high)`
Use this when `high` is one past the last valid index.

```python
arr = [2, 5, 8, 12]
target = 8

low = 0
high = len(arr)

while low < high:
    mid = (low + high) // 2

    if arr[mid] < target:
        low = mid + 1
    else:
        high = mid

print(low)
```

Pattern to remember:
- `low = 0`
- `high = len(arr)`
- loop with `while low < high`
- `high` itself is not a valid index

#### Why Some Problems Use `1` And `len(arr) - 1`
That is usually because:
- the problem is using `1`-based positions
- index `0` is being skipped on purpose
- the search space is not normal array indices

For beginner array search questions in Python, the safest starting pattern is usually the closed interval version.

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

---

## 8. GenAI Foundations Revision

### 8.1 Tokens
A token is a small chunk of text that a model reads.

Important idea:
- a token is not always one full word
- punctuation also takes space
- longer prompts usually use more tokens

Quick example:
- `cat` uses fewer tokens than a long instruction with many words

### 8.2 Context Window
A context window is the amount of text the model can pay attention to at one time.

That can include:
- the current prompt
- earlier chat messages
- pasted notes or documents

Important idea:
- the context window is limited
- if too much text is included, the model may miss details or give weaker answers

### 8.3 Why It Matters
Shorter and more relevant prompts are usually better because they:
- stay focused
- use less context space
- make the task clearer

Weak prompt:
`Tell me everything about Python and also help me understand dictionaries somewhere in all this.`

Better prompt:
`Explain Python dictionaries to a beginner in 3 simple points with 1 example.`

### 8.4 Prompt Quality Basics
A weak prompt is often too broad or too vague.

Weak prompts often miss:
- the exact topic
- the audience
- the answer format
- the answer size

Example of a weak prompt:
`Teach me coding.`

Why it is weak:
- it does not say which coding topic
- it does not say how deep the answer should go
- it does not say what output format is wanted

### 8.5 Constraints Improve Output
Constraints are small limits or instructions inside a prompt.

Useful constraints:
- `for a beginner`
- `in 3 bullet points`
- `with 1 example`
- `in simple language`

These help because they:
- reduce vagueness
- guide the answer shape
- make the output more useful

Weak prompt:
`Tell me about functions.`

Better prompt:
`Explain Python functions to a beginner in 4 short bullet points with 1 example.`

### 8.6 System Instructions vs User Prompt
A user prompt is the message typed by the user.

Examples:
- `Explain Python dictionaries to a beginner.`
- `Write a function to count vowels.`

The user prompt usually gives the task.

A system instruction is a higher-level rule given before the user prompt.

System instructions can define:
- the model's role
- the answer style
- rules to follow
- things to avoid

Example system instruction:
`You are a beginner-friendly Python tutor. Use simple language and short examples.`

Example user prompt:
`Explain functions.`

Important idea:
- the system instruction guides behavior
- the user prompt gives the current task
- a good answer should follow both

### 8.7 Base Request vs Guided Request
A base request only gives the task.

Base request:
`Explain functions.`

A guided request adds role, audience, style, or output limits.

Guided request:
`You are a beginner-friendly Python tutor. Explain Python functions in 3 or 4 simple points with 1 small example.`

Guided requests are usually better because they give the model more useful direction.

### 8.8 Output Variability and Temperature
Normal code usually gives the same output for the same input.

GenAI output can vary because the model generates text using probabilities.

The same prompt can produce:
- slightly different wording
- different examples
- a different order of points
- sometimes a stronger or weaker answer

Temperature is a setting that controls how predictable or creative the answer can be.

Simple idea:
- lower temperature means more predictable
- higher temperature means more varied or creative

Use low temperature for:
- code help
- factual answers
- structured output
- valid JSON or strict formats

Use higher temperature for:
- brainstorming
- creative writing
- naming ideas
- exploring many options

Example:
- `Return valid JSON with exactly 3 keys.` -> low temperature
- `Brainstorm 10 fun app ideas for beginners.` -> higher temperature

### 8.9 Simple Rule To Remember
- more text usually means more tokens
- long chats can become messy because context space is limited
- keep only the useful details in the prompt
- better prompts usually name the topic, audience, format, and length
- system instructions guide behavior; user prompts give the task
- low temperature is better for consistency; higher temperature is better for variety

### 8.10 Structured Output Basics
Structured output means asking the model to return data in a fixed shape instead of loose free text.

Common example:
- JSON with exact keys

Why apps prefer it:
- easier to parse
- easier to validate
- more reliable than long free-form answers

Free-text example:
`The sentiment looks positive and the score is around 0.8.`

Structured example:

```json
{
  "sentiment": "positive",
  "score": 0.8
}
```

Simple rule:
- use structured output when code needs to read the answer safely

### 8.11 Parsing and Validation
Parsing means reading the returned structure in code.

Validation means checking that the structure really matches what you expected.

Important idea:
- something can look correct to a human and still break code

Useful checks:
- required keys exist
- value types are correct
- lists or strings are not missing

Python example:

```python
result = {"topic": "lists", "level": "beginner"}

if "topic" in result and "level" in result:
    print("Valid shape")
else:
    print("Missing required keys")
```

Simple rule:
- do not trust model output just because it looks neat

### 8.12 Reusable Model Helper Design
A reusable helper keeps model-call logic in one place.

This is useful because it helps you:
- avoid repeating the same request code everywhere
- keep prompting separate from parsing
- return a safe fallback when something fails

Beginner-friendly helper idea:

```python
def get_model_reply(prompt):
    try:
        reply = f"Mock reply for: {prompt}"
        return {"ok": True, "reply": reply}
    except Exception:
        return {"ok": False, "reply": "Fallback reply"}
```

Simple rule:
- one place for calling
- one place for parsing
- one safe fallback

### 8.13 Chat History vs Memory
Chat history is the earlier messages in the current conversation.

Memory is saved information that can be reused later.

Important difference:
- chat history is temporary conversation context
- memory is stored knowledge or saved facts

Example:
- chat history: what was said 5 messages ago
- memory: saved user preference like `prefers short Python examples`

Simple rule:
- chat history is not the same as true long-term memory

### 8.14 Failure Modes
Failure modes are common ways GenAI output can go wrong.

Important examples:
- wrong facts
- vague answers
- overconfident wording
- invalid format
- missing required details

Important idea:
- confidence is not correctness

When reviewing an answer, ask:
- is it actually correct?
- did it follow the format?
- did it answer the real question?
- did it invent anything unsupported?

### 8.15 Tool Calling Basics
Tool calling means the model can choose to use an external helper instead of answering only from text generation.

Simple flow:
1. user asks something
2. model decides a tool is needed
3. helper code gets exact data
4. model explains the result

Good use cases:
- calculations
- file lookup
- database lookup
- API calls

Simple rule:
- the model handles language
- the tool handles trusted data or actions

### 8.16 Evaluation Basics
Evaluation means checking whether outputs are good enough for the task.

Two simple styles:
- subjective review: `Does this answer feel useful and clear?`
- rule-based review: `Did it return valid JSON with all required keys?`

Helpful things to track:
- good outputs
- weak outputs
- failure cases

Beginner evaluation questions:
- was the answer correct?
- was the format correct?
- was it clear?
- was anything missing?

### 8.17 Phase 1 End Goals
By the end of GenAI Foundations, you should be able to explain simply:
- what a model is doing at a basic level
- why prompt quality changes output quality
- why token and context limits matter
- why confident answers can still be wrong
- why structured output helps apps
- why validation and evaluation matter
- why chat history is not true memory

You should also be able to build small examples such as:
- one clean GenAI helper
- one structured output example
- one validation example
- one short evaluation script

---

## 9. Retrieval Basics Revision

### 9.1 What Retrieval Means
Retrieval means finding the most useful saved information before answering a question.

Simple idea:
- the model should not guess when useful source text already exists
- first find the right information
- then answer using that information

Example:
- question: `What does our refund policy say about cancellations?`
- retrieval step: find the saved note or document section about cancellations

### 9.2 Similarity Search
Similarity search tries to find text that is closest in meaning to the question.

Keyword search:
- looks for exact words

Similarity search:
- tries to match meaning

Simple example:
- question: `How do I stop my plan?`
- a useful note might say `subscription cancellation steps`

The words are different, but the meaning is close.

### 9.3 What RAG Means
RAG means Retrieval-Augmented Generation.

Simple flow:
1. retrieve useful source text
2. give that source text to the model
3. let the model answer using that context

Short version:
- retrieval gets the facts
- generation turns them into a natural answer

### 9.4 Simple Rule To Remember
- bad retrieval leads to bad answers
- retrieval helps reduce hallucinations, but does not fully remove them
- keep the flow simple first:

`saved information -> retrieve -> answer`

---

## 10. Gemini Tool Calling Revision

### 10.1 When You Need A Tool
Use plain code when the task is fixed and structured.

Examples:
- totals
- filters
- comparisons
- exact lookups

Use a model plus a tool when the user asks in flexible natural language and your app must connect that request to real data or actions.

### 10.2 Core Production Idea
- the model understands the user request
- the tool gets exact data from a trusted source
- the model explains the result naturally

The tool is the trusted data/action layer.

The model is the language and reasoning layer.

### 10.3 Transaction Example Without A Model

```python
transactions = [
    {"category": "food", "amount": 200, "month": "2026-05"},
    {"category": "travel", "amount": 500, "month": "2026-05"},
    {"category": "food", "amount": 100, "month": "2026-04"},
]

def get_total_for_month(transactions, month):
    total = 0
    for item in transactions:
        if item["month"] == month:
            total += item["amount"]
    return total

print(get_total_for_month(transactions, "2026-05"))
```

This is best when the input is already structured.

### 10.4 Same Example With Gemini Function Calling

```python
from google import genai
from google.genai import types

transactions = [
    {"category": "food", "amount": 200, "month": "2026-05"},
    {"category": "travel", "amount": 500, "month": "2026-05"},
    {"category": "food", "amount": 100, "month": "2026-04"},
]

def get_total_for_month(month: str) -> dict:
    total = 0
    for item in transactions:
        if item["month"] == month:
            total += item["amount"]
    return {"month": month, "total": total}

client = genai.Client()

config = types.GenerateContentConfig(
    tools=[get_total_for_month]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="How much did I spend last month? Use the tool if needed.",
    config=config,
)

print(response.text)
```

In this example:
- Gemini understands `"last month"`
- the tool returns the exact total
- Gemini turns the result into a natural answer

### 10.5 Simple Rule To Remember
- If rules are enough, use rules.
- If language understanding is the hard part, add a model.
