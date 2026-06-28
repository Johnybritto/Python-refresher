# Gemini Free Tier Day 11: Retrieval Basics Before Embeddings

## Quick Revision
- Yesterday, you moved the Gemini-specific logic into `get_gemini_reply(prompt)`.
- That helper handles the API key, client creation, model call, and fallback message.
- The FastAPI route now has a smaller job: accept input, call the helper, and return `PromptResponse`.
- A helper function is useful when one part of the code has one clear job.
- Retrieval means: first find the relevant saved note, then use that note.
- In today's tiny version, retrieval is just looping through notes and returning the first match.

## Today's Goal
- understand what retrieval means in simple words
- use local notes before embeddings or vector databases
- find the first relevant note with basic keyword matching
- keep the code small and beginner-friendly

## Check Your Current Level
Before starting, ask yourself:

What does "retrieval" mean in simple words when you have a few saved notes and one user question?

If you can explain it as "finding the most useful saved note," you're ready.

## Tiny Lesson

### 1. What Retrieval Means
Retrieval means finding useful stored information before answering a question.

For today, that stored information is just a small Python list of notes.

### 2. Why Retrieval Helps
Sometimes the model should not answer by guessing from its general knowledge alone.

It is often better to first look up the most relevant saved note, then use that note.

That is the basic idea behind retrieval.

### 3. Keep Day 11 Very Small
Today you do not need:
- embeddings
- vector databases
- ranking systems

Today you only need:
- a list of notes
- a query
- a loop that checks for a keyword match

### 4. Beginner Retrieval Example
If your notes are:

```python
notes = ["python list", "api key", "fastapi route"]
```

and the query is:

```python
"api"
```

then the first useful match should be:

```python
"api key"
```

### 5. One Safe Beginner Pattern
Make one helper function such as:

```python
find_relevant_note(notes, query)
```

That function should:
- check each note
- return the first note that contains the query
- return a simple fallback if nothing matches

## Hint
Start with a loop through the notes and compare lowercase text so matching is easier.

## One Small Exercise
Complete [DAY_11.py](./DAY_11.py) so it:
- creates a list of notes
- defines `find_relevant_note(notes, query)`
- returns the first matching note
- returns `"No matching note found"` if nothing matches
- calls the function once with query `"api"`
- prints the result

## Hint 1
You can compare lowercase strings with:

```python
query.lower() in note.lower()
```

## Hint 2
Return as soon as you find the first match.

## Hint 3
If the loop finishes with no match, return:

```python
"No matching note found"
```

## When You Finish
Send me only your Gemini Free Tier Day 11 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
