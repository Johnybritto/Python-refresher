# Gemini Free Tier Day 2: Prompt and Input Design

## Quick Revision
- The API key should stay outside your code.
- A Gemini call needs a client, a model name, and prompt content.
- A small prompt makes the first test easier to debug.

## Today's Goal
- understand that prompt wording changes the answer
- compare two prompts for the same question
- notice what makes one answer clearer than another
- keep using a real Gemini call

## Check Your Current Level
Before starting, ask yourself:

If two prompts ask almost the same thing, can the answers still feel very different in clarity?

If you can explain why yes, you're ready.

## Tiny Lesson

### 1. Prompt Wording Matters
Models do not only react to the topic.

They also react to:
- how specific you are
- how short or detailed you ask
- what output shape you request

### 2. Weak Prompt vs Clear Prompt
Example weak prompt:

```python
"Explain Python lists"
```

Example clearer prompt:

```python
"Explain what a Python list is in one short beginner-friendly sentence."
```

Both ask about the same topic, but the second one gives better guidance.

### 3. Compare Answers, Not Just Prompts
For today, do not worry about perfect prompting.

Just compare:
- which answer is clearer
- which answer is shorter
- which answer feels more beginner-friendly

### 4. Keep The Program Small
You only need:
- one client
- one model
- two prompts
- two responses
- two `print()` calls

## Hint
Use the same Gemini setup as Day 1.

Only the prompts should change.

## One Small Exercise
Complete [DAY_02.py](./DAY_02.py) so it:
- uses the Gemini client
- sends two different prompts about the same topic
- stores both returned texts
- prints both replies clearly

## Hint 1
You can keep the same `MODEL_NAME`.

## Hint 2
Try prompts like:

```python
"Explain Python lists"
```

and:

```python
"Explain what a Python list is in one short beginner-friendly sentence."
```

## Hint 3
Print a label before each reply so you know which prompt produced which answer.

## When You Finish
Send me only your Gemini Free Tier Day 2 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the short Python basics problem for Day 2 from the roadmap.

### Problem
Reverse the string `"prompt"` without using slicing.

Use:

```python
text = "prompt"
```

Your program should print:

```python
tpmorp
```

### Hint 4
Use a loop and build the reversed string one character at a time.

## When You Finish The Basics Problem
Send me only your [DAY_02_BASICS.py](./DAY_02_BASICS.py) code.
