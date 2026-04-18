# Advanced Day 4: More With Lists

## Quick Revision From Advanced Day 3
- A string can be reversed with a loop.
- A palindrome reads the same forward and backward.
- `len(...)` counts how many characters are in a string.
- Keeping one clear final solution makes code easier to read.

## Today's Goal
- Build a new list from an old list
- Find duplicates in a list
- Understand the idea behind list comprehensions
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a list has repeated values, how could you collect only the repeated ones without writing the same answer many times?

If you can explain one idea, you're ready.

## Tiny Lesson

### 1. Building a New List
Sometimes we want to create a second list from an existing list.

Example:

```python
numbers = [1, 2, 3]
doubled = []

for number in numbers:
    doubled.append(number * 2)
```

Now `doubled` becomes `[2, 4, 6]`.

### 2. Finding Duplicates
If a value appears more than once, it is a duplicate.

Example:

```python
items = [1, 2, 2, 3, 1]
```

Here, `1` and `2` are duplicates.

### 3. One Simple Duplicate Pattern
You can build a `duplicates` list and only add an item if:
- it has appeared before
- it is not already in `duplicates`

### 4. List Comprehension Idea
A list comprehension is a shorter way to build a list.

Example:

```python
squares = [number * number for number in [1, 2, 3]]
```

You do not need to master it today. Just notice the idea.

## Hint
For today's exercise, use a normal `for` loop first.

Do not use a list comprehension unless you want to compare later.

## One Small Exercise
Write code that:
- stores a list like `[1, 2, 2, 3, 4, 4, 5]`
- creates an empty list named `duplicates`
- uses a loop to find the duplicate values
- prints the `duplicates` list

The final printed result should be:

```python
[2, 4]
```

## Hint 1
Use one loop over the original list.

## Hint 2
Inside the loop, think:

```python
if item already appeared before and item not already in duplicates
```

## Hint 3
One way to check "appeared before" is to look at the part of the list before the current item.

## When You Finish
Send me only your Advanced Day 4 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
