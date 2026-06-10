# Gemini Free Tier Day 6: Terminal Chatbot With History

## Quick Revision
- A Gemini call can fail, so `try` / `except` keeps the script safer.
- A friendly fallback message is better than a crash for a beginner app.
- Small, clear prompts are still easier to debug.

## Today's Goal
- build a tiny terminal chatbot
- keep a conversation history list
- append both user and model messages
- stop the loop when the user types `exit`
- keep one small `try` / `except` around the risky Gemini part

## Check Your Current Level
Before starting, ask yourself:

Why is a conversation history list more useful than sending only the newest user message every time?

If you can answer that in simple words, you're ready.

## Tiny Lesson

### 1. A Chatbot Is A Loop
A small terminal chatbot usually does this:
- ask for user input
- stop if the user types `exit`
- get the model reply
- print the reply
- repeat

### 2. History Helps The Model Keep Context
If you only send the newest message, the model may forget what was said earlier.

So for Day 6, keep a small list like:

```python
conversation = []
```

Then append messages as the chat grows.

### 3. Store User And Model Messages
One simple beginner shape is:

```python
{"role": "user", "text": "Hello"}
{"role": "model", "text": "Hi there"}
```

That makes the history easier to inspect later.

### 4. Build One Simple History Prompt
For now, keep the SDK usage simple.

You can turn the saved history into one text block and send that text to Gemini.

That means you do not need a more advanced chat API yet.

### 5. Keep The Risky Part Protected
The risky part is still:
- creating the client
- calling Gemini
- reading the reply

Wrap that part in `try` / `except`.

## Hint
Reuse your Day 5 safe pattern and add a `while True` loop around it.

## One Small Exercise
Complete [DAY_06.py](./DAY_06.py) so it:
- creates a Gemini client safely
- keeps a `conversation` list
- asks the user for input in a loop
- stops if the user types `"exit"`
- appends the user message to the history
- sends the conversation to Gemini
- prints the reply
- appends the model reply to the history

## Hint 1
You will likely need:

```python
conversation = []
```

## Hint 2
Use:

```python
user_text = input("You: ").strip()
```

## Hint 3
After getting a reply, append it to the history too.

## When You Finish
Send me only your Gemini Free Tier Day 6 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the short Python basics problem for Day 6 from the roadmap.

### Problem
Given:

```python
messages = ["hi", "hello", "bye"]
```

Print each message together with its position starting from `1`.

Expected output:

```python
1 hi
2 hello
3 bye
```

### Hint 4
You can keep a counter starting at `1`, or use `enumerate(..., start=1)`.

## When You Finish The Basics Problem
Send me only your [DAY_06_BASICS.py](./DAY_06_BASICS.py) code.
