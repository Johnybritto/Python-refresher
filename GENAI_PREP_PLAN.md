# GenAI Prep Plan

## Goal
Finish the lower-priority Python topics quickly, then move into a more GenAI-focused path with API workflow, environments, and FastAPI.

## Recommended Study Time
- 2 to 3 hours per day
- 14 days

## Daily Structure
- 20 min: revise one older concept
- 40 min: study the new lesson
- 40 min: write code examples by hand
- 40 min: solve one exercise or mini task
- 20 min: review mistakes and write notes
- 10 to 20 min: one small LeetCode-style basics problem

## Recommended Order
1. Quick finish of lower-priority Python topics
2. Core GenAI/API workflow
3. Project setup and environments
4. FastAPI for serving apps
5. One real GenAI provider later

## Why This Order
- You already have most of the core Python foundation.
- The low-priority topics are still useful, but they should not delay GenAI too much.
- FastAPI is more useful after you understand APIs, JSON, and project structure.

## Important Topics Added
This expanded version now also includes:
- HTTP basics like headers, query params, and status codes
- request bodies and JSON payloads
- timeouts and safer request patterns
- `requirements.txt`
- `.env` / environment-variable workflow
- nested JSON parsing
- Pydantic request/response models in FastAPI
- basic async awareness
- logging and testing basics for small API apps
- token, cost, and rate-limit awareness for GenAI APIs

## Phase 1: Quick Finish of Lower-Priority Python Topics
Keep this short and practical.

### Day 1: Context Managers
- what `with` is really doing
- why files use `with open(...)`
- one custom example with a simple context manager idea
- where context managers matter in real apps
- Basics problem: count vowels in a string

### Day 2: Generators
- `yield`
- generator vs list
- simple number generator example
- when generators help with streaming or large data
- Basics problem: find max and min in a list without built-ins

### Day 3: Decorators
- function wrapping idea
- simple beginner decorator
- when decorators are useful
- why FastAPI uses decorators later
- Basics problem: palindrome check

### Day 4: OOP Quick Finish
- changing object data
- adding more methods
- one small object-based mini example
- Basics problem: count character frequency in a string

### Day 5: OOP Later Topics Overview
- class methods
- static methods
- inheritance
- only a light introduction, not deep mastery
- when classes help organize GenAI apps
- Basics problem: find duplicates in a list

## Phase 2: GenAI-Focused Core

### Day 6: Virtual Environments and `pip`
- create a virtual environment
- activate it
- install a package
- understand why this matters
- create `requirements.txt`
- reinstall dependencies from `requirements.txt`
- Basics problem: reverse a string

### Day 7: Environment Variables and Secrets
- why API keys should not be hardcoded
- environment variables
- `.gitignore`
- optional `.env` workflow
- keeping secrets out of Git
- Basics problem: count words in a sentence

### Day 8: Provider-Neutral AI API Workflow
- GET vs POST
- headers
- auth header idea
- `POST` requests
- JSON payload
- model field
- prompt/messages field
- response JSON
- timeouts
- Basics problem: merge two dictionaries

### Day 9: Reading Nested AI-Style Responses
- nested dictionaries/lists
- safe parsing with `.get(...)`
- extracting text from mock AI responses
- reading lists of messages or choices
- storing outputs in JSON files
- Basics problem: get the second largest number in a list

### Day 10: Error Handling for AI APIs
- failed requests
- missing keys
- timeouts
- safe fallback messages
- basic logging
- rate-limit and cost-awareness idea
- Basics problem: safe division with `try`/`except`

## Phase 3: FastAPI

### Day 11: FastAPI Basics
- what FastAPI is
- create a simple app
- one GET route
- run the app with Uvicorn
- understand path vs route
- Basics problem: check whether a number is prime

### Day 12: FastAPI With Request Data
- POST route
- read JSON body
- return JSON response
- query parameters
- path parameters
- status codes in responses
- Basics problem: sum of even numbers in a list

### Day 13: FastAPI Mini API
- build a tiny prompt-style mock endpoint
- send input JSON
- return structured output JSON
- Pydantic models for request/response
- basic async awareness
- simple testing with FastAPI TestClient
- Basics problem: flatten one level of a nested list

## Phase 4: First Real GenAI Provider

### Day 14: Transition to a Real Provider
- choose one provider later
- add authentication
- send a real model request
- read and save the result
- build a simple terminal chatbot
- optional FastAPI wrapper around one model call
- Basics problem: beginner two-sum style problem

## Notes
- FastAPI is worth learning for GenAI because it helps you turn Python code into APIs and small backend services.
- Decorators and generators are useful, but they are not early blockers for GenAI.
- Context managers are more practically important than decorators/inheritance for near-term GenAI work.
- You do not need deep inheritance or advanced decorator patterns before starting GenAI apps.
- The most important practical skills are environments, API workflow, JSON handling, and app structure.

## Priority Summary

### Finish Quickly
- context managers
- generators
- decorators
- class methods
- static methods
- inheritance

### Focus Hard
- virtual environments
- `pip`
- `requirements.txt`
- environment variables
- headers and POST requests
- API workflow
- nested JSON parsing
- JSON payload/response handling
- FastAPI
- Pydantic models
- logging and testing basics
- token and rate-limit awareness
- real provider integration later
