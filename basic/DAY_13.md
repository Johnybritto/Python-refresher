# Day 13: Complexity Basics

## Quick Revision From Day 12
- A bug is a mistake in code.
- A traceback helps you find the line and type of error.
- `NameError` happens when a variable name does not exist.
- Indentation matters inside `if`, `while`, and `def` blocks.
- `print()` can help you inspect values while debugging.

## Today's Goal
- Understand the basic idea of time complexity
- Understand the basic idea of space complexity
- Compare list search and dictionary key lookup in simple words
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If one program checks items one by one, and another program finds an answer almost immediately, which one feels faster as the input grows?

If you can explain that in simple words, you're ready.

## Tiny Lesson

### 1. What Is Time Complexity?
Time complexity is a simple way to describe how the work grows when the input gets bigger.

You do not need heavy math yet.

Just ask:

How much more work does this code do when the data gets larger?

### 2. List Search
If you look for a value in a list, Python may need to check items one by one.

Example idea:

```python
numbers = [4, 8, 1, 9, 3]
```

To find `3`, you may need to look through many items first.

### 3. Dictionary Key Check
If you check whether a key exists in a dictionary, that is usually much faster.

Example idea:

```python
student = {"name": "Ravi", "age": 12}
```

Checking `"age" in student` is usually fast.

### 4. What Is Space Complexity?
Space complexity is a simple way to describe how much extra memory a program uses.

If a program uses only a few variables, space use stays small.

If it creates another large list or dictionary, space use grows more.

## Hint
For today's exercise, you only need plain words.

You do not need to write a full program.

## One Small Exercise
Compare these operations in simple words:
- finding an item in a list
- checking whether a key exists in a dictionary

## Hint 1
Think:
- list: may check many items
- dictionary: usually finds the answer faster

## Hint 2
Use words like:
- slower as data grows
- faster for lookup

## When You Finish
Send me your Day 13 answer in simple words.

Then I will review it for:
- Correctness
- Readability
- Time complexity understanding
- Space complexity understanding
- What to improve next
