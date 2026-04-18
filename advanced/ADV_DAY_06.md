# Advanced Day 6: Tuples and Sets in Practice

## Quick Revision From Advanced Day 5
- `dictionary -> list` means getting a list from a dictionary, then getting one item from that list.
- `list -> dictionary` means getting one dictionary from a list, then reading one key.
- `dictionary -> dictionary` means going one level deeper into another dictionary.
- Loops can help read nested data one item at a time.

## Today's Goal
- Understand what a tuple is
- Understand what a set is
- See how a set removes duplicates
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a list has repeated values, what kind of collection could help keep only unique values?

If you can explain that idea, you're ready.

## Tiny Lesson

### 1. What Is a Tuple?
A tuple is a group of values, like a list, but we usually do not change it after creating it.

Example:

```python
point = (2, 5)
```

You can read tuple items by index:

```python
print(point[0])
```

This prints `2`.

### 2. What Is a Set?
A set stores unique values.

Example:

```python
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)
```

The repeated values are removed.

### 3. Why Sets Matter
Sets are useful when you want to:
- remove duplicates
- check membership quickly
- compare groups of values later

### 4. Important Beginner Idea
Sets do not keep duplicate values.

That is the main thing to notice today.

## Hint
For today's exercise, focus on the set idea first.

Do not worry about tuple operations beyond reading one item.

## One Small Exercise
Write code that:
- stores this list: `[1, 2, 2, 3, 4, 4, 5]`
- converts it into a set
- prints the set

You do not need to worry about the exact printed order of the set.

## Hint 1
Start with:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
```

## Hint 2
Use `set(numbers)`.

## Hint 3
Store the result in a variable like `unique_numbers`.

## When You Finish
Send me only your Advanced Day 6 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
