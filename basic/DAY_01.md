# Day 1: Assessment + Basics

## Today's Goal
- Find your current Python level
- Refresh basic syntax
- Do one small exercise

## How We Will Work
- You answer 4 short questions first.
- I will use your answers to adjust difficulty.
- Then you do exactly one small exercise.
- I will review your code for:
  - Correctness
  - Readability
  - Time complexity
  - Space complexity
  - What to improve next
- I will give hints first if you get stuck.

## Part 1: 4 Short Assessment Questions

Answer these in your own words.

1. What is the difference between a variable and a value in Python?
variable is used to store the values , it can be done by assigning values to the variables by using the = operator 
2. What will this print?

```python
name = "Sam"
print(name * 2)
```
Ans: Sam Sam
3. What is the difference between a list and a dictionary?
dictionary is used to store key value pair and List is colletion of items in brackets 

4. If your code gives an error, what is the first thing you would check?
i would check the exception thrown
## Part 2: Tiny Lesson

### Variables
A variable is a name that stores a value.

```python
age = 14
city = "Delhi"
```

### `print()`
Use `print()` to show output.

```python
print(age)
print(city)
```
14
Delhi

### Strings and Numbers
Strings are text values.
Numbers are numeric values like `3`, `10`, and `4.5`.

```python
user_name = "Ava"
score = 10
```

## Part 3: One Small Exercise

Write a Python program that:
- stores your name in a variable
- stores your favorite number in another variable
- prints this sentence:

```text
My name is <name> and my favorite number is <number>
```
name="John"
favorite_number=10
print("My name is" + name + "and my favorite number is " +str(favorite_number) )

## Hints
- Use two variables.
- Use `print()`.
- You can use commas inside `print()` or an f-string.

## When You Finish
Send me:
- your 4 answers
- your exercise code

Then I will review it and tell you what to study next.

## 5-Minute Revision

Use this only for a fast revision before Day 2.

### What to Remember
- A variable is a name. A value is the actual data stored in it.
- `print()` shows output on the screen.
- Strings are text like `"Sam"`.
- Numbers are values like `5`, `10`, and `3.14`.
- `=` assigns a value to a variable.

### Quick Checks
1. What does this print?

```python
name = "Sam"
print(name * 2)
```

2. What is the difference between a list and a dictionary?
3. Why did we use `str(favorite_number)` in the exercise?

### Tiny Correct Example

```python
name = "John"
favorite_number = 10
print(f"My name is {name} and my favorite number is {favorite_number}")
```

### Common Mistakes
- Forgetting spaces when joining strings
- Mixing strings and integers without conversion
- Confusing `=` with "is equal to"

### Exit Check
If you can explain variables, strings, numbers, and `print()` in simple words, you are ready for Day 2.
