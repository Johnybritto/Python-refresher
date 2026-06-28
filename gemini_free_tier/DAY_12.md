# Gemini Free Tier Day 12: Tiny RAG-Style Flow

## Quick Revision
- Retrieval means finding the right saved note before answering.
- In Day 11, retrieval was a simple loop through a list of notes.
- A helper function can keep one job in one place.
- If the query was `"api"`, the first matching note was `"api key"`.

## Today's Goal
- use one retrieved note together with a user question
- build a tiny retrieval-plus-answer flow
- print both the final answer and the source note
- keep the code small and beginner-friendly

## Check Your Current Level
Before starting, ask yourself:

If you already found the most relevant saved note, what should you do next before answering the question?

If you can say "use that note to build the answer," you're ready.

## Tiny Lesson

### 1. What Day 12 Adds
Yesterday, you only found the note.

Today, you will do one extra step:
- find the relevant note
- use that note to create an answer

That is the beginning of a tiny RAG-style flow.

### 2. Keep RAG Very Small Today
You do not need:
- embeddings
- vector databases
- multiple ranking steps

Today you only need:
- a list of notes
- a query
- a function to retrieve one note
- a function or step to build an answer from that note

### 3. Source Note Idea
When answering, it is useful to know:
- the answer
- the source note used to make that answer

For today, print both clearly.

### 4. Beginner Example
If the query is:

```python
"What is an API key?"
```

and the retrieved note is:

```python
"api key"
```

then your answer can be very simple, such as:

```python
"Answer based on note: api key"
```

### 5. One Safe Beginner Pattern
You can use two small steps:

```python
source_note = find_relevant_note(notes, query)
```

then:

```python
answer = build_answer(query, source_note)
```

The answer does not need to be smart yet.

It only needs to show the flow clearly.

## Hint
Reuse your Day 11 retrieval helper, then add one tiny answer-building step.

## One Small Exercise
Complete [DAY_12.py](./DAY_12.py) so it:
- creates a list of notes
- reuses or writes `find_relevant_note(notes, query)`
- gets one `source_note` for the question
- builds one simple answer string from that source note
- prints both the answer and the source note

## Hint 1
Your source note can be stored in:

```python
source_note = find_relevant_note(notes, query)
```

## Hint 2
If nothing matches, you can still handle it with:

```python
"No matching note found"
```

## Hint 3
Your answer can stay simple, for example:

```python
f"Answer based on note: {source_note}"
```

## When You Finish
Send me only your Gemini Free Tier Day 12 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the short Python basics problem for Day 12 from the roadmap.

### Problem
Given a list of dictionaries with `question` and `answer`, print the answer for a matching question.

Example idea:

```python
faq = [
    {"question": "What is Python?", "answer": "A programming language"},
    {"question": "What is FastAPI?", "answer": "A Python API framework"},
]
```

If the query matches one question exactly, print the matching answer.

### Hint 4
Loop through the list and compare:

```python
item["question"] == query
```

## When You Finish The Basics Problem
Send me only your [DAY_12_BASICS.py](./DAY_12_BASICS.py) code.
