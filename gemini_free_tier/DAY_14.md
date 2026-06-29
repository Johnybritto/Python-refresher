# Gemini Free Tier Day 14: Mini Project and Decision Day

## Quick Revision
- In Day 13, you checked answers by looking at correctness, clarity, and formatting.
- That introduced the idea that an AI app should be tested, not just run.
- You now have practice with prompts, saving outputs, FastAPI structure, retrieval basics, and simple evaluation.

## Today's Goal
- build one small end-to-end Gemini-style mini project
- reuse ideas from earlier days
- keep the flow simple and practical
- decide what you want to improve next

## Check Your Current Level
Before starting, ask yourself:

Can you explain a tiny AI app as: input, model or logic step, and output?

If you can say yes, you're ready for Day 14.

## Tiny Lesson

### 1. What Day 14 Is For
Day 14 is not about learning one brand-new concept.

It is about combining several small ideas into one usable script.

### 2. Keep The Project Small
Today you do not need:
- a big app
- a database
- advanced UI
- production deployment

Today you only need:
- one clear purpose
- one input
- one output
- one clean Python flow

### 3. Good Beginner Mini Project Shape
A strong beginner project can do something like:
- ask for a prompt
- generate or simulate an answer
- print the answer
- save the result

### 4. Example Project Ideas
You can build:
- a tiny prompt tester
- a notes Q&A script
- a simple terminal helper
- a mini response logger

### 5. One Safe Beginner Pattern
Split the project into small steps:
- get input
- produce answer
- show answer
- save or review result

## Hint
Do not try to make Day 14 impressive. Make it clean and understandable.

## One Small Exercise
Complete [DAY_14.py](./DAY_14.py) so it:
- asks for one user prompt
- builds one simple answer
- stores the prompt and answer in a dictionary
- prints the final result
- prints one sentence about what you want to improve next

## Hint 1
You can start with:

```python
user_prompt = input("Enter your prompt: ")
```

## Hint 2
Your answer can stay simple for now, such as:

```python
answer = f"Generated answer for: {user_prompt}"
```

## Hint 3
Store the result in one dictionary with keys like:

```python
"prompt"
"answer"
```

## When You Finish
Send me only your Gemini Free Tier Day 14 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the short Python basics problem for Day 14 from the roadmap.

### Problem
Given a list of numbers, print the total and the average.

Example idea:

```python
numbers = [10, 20, 30]
```

The total is `60` and the average is `20.0`.

### Hint 4
You can use:

```python
sum(numbers)
len(numbers)
```

## When You Finish The Basics Problem
Send me only your [DAY_14_BASICS.py](./DAY_14_BASICS.py) code.
