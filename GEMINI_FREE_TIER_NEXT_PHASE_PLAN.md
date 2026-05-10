# Ideal Next Phase Plan

## Version
This is the Gemini-first free-tier version of the roadmap.

It is designed to help you learn with the Gemini API free tier first, then switch to paid Gemini or another provider later without rewriting your whole codebase.

## Goal
Move from mock GenAI practice into real GenAI app building.

This phase should turn your current foundation into practical skills you can use to build:
- a real terminal chatbot
- a small FastAPI AI app
- a basic retrieval app later

## Why Gemini Free Tier Fits This Phase
For this phase, Gemini free tier is enough for:
- first real API calls
- prompt experiments
- response parsing
- saving outputs
- chatbot practice
- simple FastAPI wrapping
- basic structured output practice

Later, if you hit limits, want stronger production habits, or want a different model family, you can switch providers by changing only the helper function that calls the model.

## Why This Is The Right Next Step
You have already covered:
- Python basics
- functions, debugging, files, exceptions, and complexity
- dictionaries, sets, nested data, and JSON-like structures
- FastAPI basics
- request/response models
- mock AI routes
- a simple terminal chatbot flow

So the best next move is not more generic Python.

The best next move is:
1. real provider workflow
2. better GenAI app patterns
3. small real projects
4. RAG and production awareness after that

## Recommended Study Length
- 14 days
- 60 to 90 minutes per day

If you have more time, spend it on building and testing, not on reading only.

## Main Focus Areas
- making a real Gemini API call
- environment variables and safe secret handling
- prompt and message design
- structured outputs
- retries, timeouts, logging, and cost awareness
- streaming and chat history
- tool calling / function calling basics
- wrapping model logic in FastAPI
- beginner retrieval and RAG thinking
- simple eval and deployment awareness

## What You Need To Register
Before Day 1, you only need a few things.

### Minimum Setup
- one Google account
- access to Google AI Studio
- one Gemini API key created in Google AI Studio

### What To Do
1. Sign in to Google AI Studio.
2. Create or view your Gemini API key there.
3. Save the key safely.
4. Set it in your environment as `GEMINI_API_KEY`.

### What You Do Not Need Immediately
- you do not need to start with a different provider
- you do not need a production app
- you do not need to learn every Gemini feature first

### Important Safety Note
Do not put private, personal, or company-sensitive data into the free tier while learning.

## Free-Tier Learning Strategy
To stay comfortable on the free tier:
- keep prompts short
- test with small examples
- avoid unnecessary repeated calls
- save useful outputs so you do not repeat the same experiments
- build local retrieval logic before using heavier retrieval patterns

## Default Model Strategy
Use the current Gemini free-tier text model that is available in Google AI Studio at the time you start.

For learning:
- start with a Gemini Flash or Flash-Lite style model if available
- prefer the cheaper / lighter free-tier option for repeated tests
- use a stronger free-tier model only when you need better quality for comparison

## Study Rules
- Keep lessons practical and code-first.
- Build something small every few days.
- Reuse your revision guide when stuck.
- Prefer one clean final solution over many partial versions.
- Track mistakes that repeat:
  - nested JSON access
  - error handling
  - function structure
  - exact output formatting

## Daily Structure
- 10 min: quick revision from [FULL_REVISION_GUIDE.md](./FULL_REVISION_GUIDE.md)
- 15 min: learn one new pattern
- 25 min: code one focused exercise
- 20 min: build or improve one mini feature
- 5 to 10 min: note mistakes, questions, and next step

## The Ideal Order
This order is designed to give you momentum fast:

1. Real Gemini call
2. Better prompt and response patterns
3. Real chatbot flow
4. FastAPI wrapper
5. Retrieval and eval basics
6. Deployment and platform awareness

---

## 14-Day Roadmap

### Day 1: Gemini Setup and First Real Call
- sign in to Google AI Studio
- create a Gemini API key
- load the API key safely from the environment
- install the Gemini Python SDK
- send one real Gemini request
- print the returned text only
- understand what changed from the mock version

### Day 2: Prompt and Input Design
- single prompt vs structured input
- clearer instructions
- asking for exact output shape
- short prompt experiments
- compare weak prompt vs better prompt

### Day 3: Reading and Saving Gemini Responses
- inspect the real response shape
- extract the useful text safely
- save output to JSON
- store prompt, response, and timestamp

### Day 4: Structured Outputs
- ask for JSON-style output
- validate the shape carefully
- handle bad or partial output
- compare plain text vs structured reply

### Day 5: Safe Gemini API Patterns
- timeout
- retries
- fallback messages
- basic logging
- free-tier usage awareness

### Day 6: Terminal Chatbot With History
- keep a conversation list
- append user and model messages
- continue the conversation over multiple turns
- add `exit` and simple error handling

### Day 7: Streaming Awareness
- understand what streaming is
- print output in chunks if your current Gemini free-tier model supports it
- compare normal full response vs streaming response
- note where streaming helps UX

### Day 8: Tool Calling / Function Calling Basics
- what tool calling means
- when it is useful
- create one tiny example tool
- return simple structured tool input/output

### Day 9: Wrap A Gemini Call In FastAPI
- create one POST route
- accept prompt input
- call Gemini inside the route
- return a clean JSON response
- keep the model call in a separate helper function

### Day 10: Small FastAPI AI App Structure
- split app code into smaller parts
- config file or config section
- helper function for model call
- request/response models
- basic test with `TestClient`

### Day 11: Retrieval Basics Before Embeddings
- what retrieval means
- what chunking means
- what similarity search means in simple words
- local retrieval first, embeddings later

### Day 12: Tiny RAG-Style Prototype
- store a few notes or text chunks
- retrieve relevant text for a question
- build a tiny retrieval flow
- return both answer and source text

### Day 13: Eval and Monitoring Basics
- compare answers manually
- create 3 to 5 test prompts
- check correctness, consistency, and formatting
- log failures and bad outputs

### Day 14: Mini Project and Decision Day
- build one small but complete GenAI app
- review weak spots
- choose the next deeper branch

Good Day 14 project choices:
- terminal chatbot with saved history
- text summarizer API
- notes Q&A mini RAG app
- prompt-to-JSON generator

---

## What To Build During This Phase

### Minimum Build Targets
By the end of this plan, you should ideally build:
- one real Gemini script
- one terminal chatbot
- one FastAPI AI route
- one tiny retrieval demo

### Good Mini Project Ideas
- prompt tester
- JSON output generator
- small FAQ bot
- notes summarizer
- one-topic Q&A bot

---

## What Success Looks Like

By the end of this phase, you should be able to:
- call a real model safely
- handle secrets properly
- design cleaner prompts and message lists
- save and inspect AI outputs
- build a chatbot with conversation history
- expose a model call through FastAPI
- explain what structured outputs, streaming, and tool calling are
- build a tiny retrieval-based app
- evaluate small AI app behavior in a basic way

## Exact Setup Checklist For Day 1

### Registration
- create or use an existing Google account
- open Google AI Studio
- generate a Gemini API key there

### Local Setup
- install Python package: `google-genai`
- set environment variable: `GEMINI_API_KEY`
- run one first request from a Python file

### Keep Ready
- one folder for experiments
- one file for saved prompts and outputs
- one note of what model name you used

---

## Best Follow-Up Branch After This Plan

After this phase, choose one main direction.

### Branch 1: GenAI App Builder
Best if you want to build practical apps quickly.

Main topics:
- stronger prompt engineering
- better structured outputs
- tool calling
- streaming UX
- multi-step workflows
- better FastAPI AI services

### Branch 2: RAG and Evaluation
Best if you want to build knowledge-based assistants.

Main topics:
- embeddings deeper
- chunking strategies
- vector databases
- retrieval quality
- eval datasets
- answer grading and citation quality

### Branch 3: Production and AI Platform Basics
Best if you want stronger backend / infra direction later.

Main topics:
- observability
- latency and token monitoring
- tracing
- Docker
- deployment
- serving patterns
- cost control

---

## My Recommendation For You

The ideal order for you now is:

1. This 14-day real-builder plan
2. RAG and evaluation phase
3. Production GenAI / AI platform phase

That order fits your current level because:
- your Python base is already good enough
- your FastAPI base is already started
- your biggest growth now will come from real GenAI workflows

---

## Important Note

Do not go back into long generic Python-only study right now unless a real project exposes a gap.

From here, project-driven learning will teach you faster than isolated topic study.
