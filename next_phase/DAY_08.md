# Next Phase Day 8: List, Set, and Dictionary Problem Solving

## Quick Revision
- `try` and `except` help programs fail more safely.
- File handling often needs safe error handling.
- `print(file.read())` shows file content after reading it.

## Today's Goal
- Revisit duplicates with cleaner thinking
- Compare list-based and set-based approaches
- Use a dictionary for counting
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If you want to count how many times each value appears, which structure is most useful: list, set, or dictionary?

If you can explain why, you're ready.

## Tiny Lesson

### 1. Lists
Lists are good for:
- keeping order
- storing repeated values
- looping through items

### 2. Sets
Sets are good for:
- unique values
- fast membership checking
- removing duplicates

### 3. Dictionaries
Dictionaries are good for:
- storing key-value pairs
- counting how many times something appears

Example:

```python
numbers = [1, 2, 2, 3, 3, 3]
counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

print(counts)
```

This gives:

```python
{1: 1, 2: 2, 3: 3}
```

### 4. Why This Matters
Many problems become easier when you choose the right structure.

## Hint
For today's exercise, focus on counting with a dictionary.

## One Small Exercise
Write code that:
- stores `[1, 2, 2, 3, 3, 3]` in `numbers`
- creates an empty dictionary `counts`
- uses a loop to count each value
- prints `counts`

## Hint 1
Start with:

```python
counts = {}
```

## Hint 2
Inside the loop:
- if the number is already in `counts`, add 1
- otherwise start it at 1

## When You Finish
Send me only your Next Phase Day 8 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
