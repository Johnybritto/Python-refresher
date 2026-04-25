# GenAI Prep Day 2: Generators

## Quick Revision
- A function usually returns one final value with `return`.
- Lists store all their values in memory at once.
- Loops help process values one by one.

## Today's Goal
- Understand what `yield` does
- Learn the idea of a generator
- Compare a generator with a list
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If you only need values one at a time, do you always need to build a full list first?

If you can explain why not, you're ready.

## Tiny Lesson

### 1. What a Generator Does
A generator gives values one at a time instead of building the full result at once.

### 2. `return` vs `yield`
With `return`, a function ends and gives back one value.

Example:

```python
def get_number():
    return 1
```

With `yield`, a function can give values one by one.

Example:

```python
def count_up():
    yield 1
    yield 2
    yield 3
```

### 3. Using a Generator

```python
for number in count_up():
    print(number)
```

This prints:

```python
1
2
3
```

### 4. Why This Matters
Generators are useful when:
- values can be produced one at a time
- you do not want to store everything at once
- you work with large data or streams later

### 5. Simple Mental Model
- list: creates all values now
- generator: creates values when needed

## Hint
Today's goal is not advanced generator logic.

Just get comfortable seeing `yield` produce multiple values.

## One Small Exercise
Write code that:
- defines a generator function `count_numbers()`
- uses `yield` to give `1`, `2`, and `3`
- loops through the generator
- prints each number

## Hint 1
Start with:

```python
def count_numbers():
```

## Hint 2
Inside the function, use:

```python
yield 1
yield 2
yield 3
```

## When You Finish
Send me only your GenAI Prep Day 2 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
