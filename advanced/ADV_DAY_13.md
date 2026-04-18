# Advanced Day 13: Intermediate Complexity and Problem Solving

## Quick Revision From Advanced Day 12
- `assert` checks whether something is true.
- If the check is correct, the program continues.
- If the check is wrong, Python raises `AssertionError`.
- Tests help catch mistakes early.

## Today's Goal
- Compare two solutions to the same problem
- Think about readability and performance
- Revisit duplicate-finding with stronger complexity thinking
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If two pieces of code both work, how could we decide which one is better?

If you can explain that readability and performance both matter, you're ready.

## Tiny Lesson

### 1. Two Solutions Can Both Be Correct
Sometimes two solutions both give the right answer.

But they may differ in:
- readability
- speed
- memory use

### 2. Example Problem: Find Duplicates
Suppose we have:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
```

We want:

```python
[2, 4]
```

### 3. Loop-Based Idea
One simple approach:
- loop through the list
- check whether the item appeared before
- add it once to `duplicates`

This is readable, but not the fastest.

### 4. Better Complexity Idea
If we use a set to remember seen values, we can often do the job faster.

You do not need the full optimized version yet.

For today, just notice:
- one solution may be simpler to understand
- another may be better for performance

### 5. Two Duplicate-Finding Patterns to Remember

Loop-based version:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
duplicates = []

for i in range(len(numbers)):
    if numbers[i] in numbers[:i] and numbers[i] not in duplicates:
        duplicates.append(numbers[i])

print(duplicates)
```

Set-based version:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]

seen = set()
duplicates = set()

for item in numbers:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(duplicates)
```

## Hint
For today's exercise, stay with the loop-based pattern you already know.

Then we will talk about why it is not the fastest.

## One Small Exercise
Write code that:
- stores `[1, 2, 2, 3, 4, 4, 5]` in `numbers`
- creates an empty list `duplicates`
- uses a loop to collect duplicate values only once
- prints `duplicates`

The final output should be:

```python
[2, 4]
```

## Hint 1
Use the pattern:

```python
if item in numbers_before and item not in duplicates
```

## Hint 2
You can use slicing like `numbers[:i]`.

## When You Finish
Send me only your Advanced Day 13 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
