# Gemini Free Tier Day 13: Eval and Monitoring Basics

## Quick Revision
- In Day 12, you retrieved one note and used it to build a simple answer.
- That showed a tiny retrieval-plus-answer flow.
- Even if the code runs, the answer can still be weak or wrong.
- Today, you will start checking output quality in a simple, practical way.

## Today's Goal
- understand what evaluation means in a tiny AI app
- test a few sample prompts
- check whether each answer is correct, clear, and well formatted
- record results in a small Python structure

## Check Your Current Level
Before starting, ask yourself:

If an AI app runs without crashing, does that automatically mean the answer is good?

If you can say "no, the answer still needs to be checked," you're ready.

## Tiny Lesson

### 1. What Evaluation Means
Evaluation means checking the quality of the answer.

For today, keep it simple:
- Is the answer correct?
- Is it clear?
- Does it follow the format you wanted?

### 2. What Monitoring Means
Monitoring means keeping track of what happened over time.

In a tiny beginner version, that can just mean saving:
- the prompt
- the answer
- a few check results

### 3. Keep Day 13 Small
Today you do not need:
- automatic scoring systems
- dashboards
- production logging tools

Today you only need:
- a few sample prompts
- a few sample answers
- a loop
- a small result record

### 4. Beginner Example
You might test something like:

```python
prompt = "What is Python?"
answer = "Python is a programming language."
```

Then record:

```python
{
    "prompt": prompt,
    "answer": answer,
    "correct": "yes",
    "clear": "yes",
    "well_formatted": "yes",
}
```

### 5. One Safe Beginner Pattern
Use a list of dictionaries for your test results.

For each test case:
- read the prompt
- read the answer
- store simple check values

## Hint
Do not overthink the scoring yet. Manual checks like `"yes"` and `"no"` are enough for today.

## One Small Exercise
Complete [DAY_13.py](./DAY_13.py) so it:
- creates 3 test cases
- stores `prompt` and `answer` for each one
- records whether the answer was `correct`, `clear`, and `well_formatted`
- prints each result clearly

## Hint 1
You can store test cases like this:

```python
tests = [
    {"prompt": "...", "answer": "..."},
]
```

## Hint 2
You can build a new dictionary for each evaluation result.

## Hint 3
For today, you can write the check values manually.

## When You Finish
Send me only your Gemini Free Tier Day 13 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the short Python basics problem for Day 13 from the roadmap.

### Problem
Write three `assert` tests for a small function like `add_numbers(a, b)`.

Example idea:

```python
def add_numbers(a, b):
    return a + b
```

Then write three tests with `assert`.

### Hint 4
Each test should compare the real result with the expected result, such as:

```python
assert add_numbers(2, 3) == 5
```

## When You Finish The Basics Problem
Send me only your [DAY_13_BASICS.py](./DAY_13_BASICS.py) code.
