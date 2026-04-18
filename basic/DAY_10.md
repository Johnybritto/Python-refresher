# Day 10: Loops

## Quick Revision From Day 9
- A conditional helps a program choose between different actions.
- `if` runs a block when a condition is true.
- `elif` checks another condition if the earlier one was false.
- `else` runs when none of the earlier conditions matched.

## Today's Goal
- Understand what a loop does
- Use a `for` loop to repeat an action
- Read the `range()` pattern
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If you want to print the numbers `1` to `5`, would you rather write `print(...)` five times or use repetition?

If you can explain why repetition helps, you're ready.

## Tiny Lesson

### 1. What Is a Loop?
A loop lets your program repeat a block of code.

This is useful when you want to do the same kind of step many times.

### 2. `for` Loop Idea
A `for` loop is great when you know how many times you want to repeat.

Read this pattern like plain English:

`for each number in a sequence, print the number`

### 3. `range()`
`range(1, 6)` gives the numbers:

`1, 2, 3, 4, 5`

The second number is not included.

## Hint
Try building the loop in two pieces:

1. Make the sequence with `range(1, 6)`
2. Print each number inside the loop

## One Small Exercise
Use a loop to print numbers from `1` to `5`.

## Hint 1
Start with the loop header:

```python
for number in range(1, 6):
```

## Hint 2
Inside the loop, print `number`.

## Hint 3
Check the indentation. The `print(...)` line should be inside the loop.

## When You Finish
Send me only your Day 10 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
