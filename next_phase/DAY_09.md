# Next Phase Day 9: Simple CLI-Style Programs

## Quick Revision
- Dictionaries are useful when you want to store related values.
- Loops help programs repeat actions.
- `if` and `elif` help choose what code should run.

## Today's Goal
- Read user input
- Show simple menu choices
- run one small text-based program
- Practice choosing actions from user input

## Check Your Current Level
Before starting, ask yourself:

If a program shows a menu and the user types `1`, how can the program decide what to do next?

If you can answer "with `if` or `elif`", you're ready.

## Tiny Lesson

### 1. What CLI-Style Means
CLI means command-line interface.

That sounds big, but for now it just means:
- print options
- read input
- run code based on the choice

### 2. Simple Menu Example

```python
print("1. Say hello")
print("2. Say bye")

choice = input("Enter your choice: ")

if choice == "1":
    print("Hello")
elif choice == "2":
    print("Bye")
else:
    print("Invalid choice")
```

### 3. Why This Matters
This is the base for many small programs:
- calculators
- to-do apps
- contact books
- menu-driven file tools

### 4. Beginner Reminder
`input()` always gives back text.

So compare with `"1"`, not `1`.

## Hint
Keep today's program very small.

You do not need a loop yet unless you want extra practice.

## One Small Exercise
Write code that:
- prints:
  - `1. Add`
  - `2. Subtract`
- asks the user to enter a choice
- if the choice is `"1"`, prints `10 + 5`
- if the choice is `"2"`, prints `10 - 5`
- otherwise prints `"Invalid choice"`

## Hint 1
Start with:

```python
choice = input("Enter your choice: ")
```

## Hint 2
Use `if`, `elif`, and `else`.

## When You Finish
Send me only your Next Phase Day 9 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
