# Day 7: Dictionaries I

## Quick Revision From Day 6
- A list stores multiple items in order.
- We can loop through a list with a `for` loop.
- We can count list items with `len()`.
- We can change a list value by index.

Example:

```python
numbers = [5, 10, 15]

for num in numbers:
    print(num)

print(len(numbers))

numbers[0] = 99
print(numbers)
```

## Today's Goal
- Understand what a dictionary is
- Access values using keys
- Add or update values
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

Can you explain this sentence in your own words?

`A list uses positions. A dictionary uses keys.`

If yes, you're ready for today.

## Tiny Lesson

### 1. What Is a Dictionary?
A dictionary stores data as `key: value` pairs.

```python
student = {
    "name": "Rahul",
    "age": 14,
    "grade": "A"
}
```

Here:
- `"name"` is a key
- `"Rahul"` is the value for that key

### 2. Access a Value
Use the key inside square brackets.

```python
print(student["name"])
print(student["age"])
```

### 3. Add or Update a Value
Use a key on the left side.

```python
student["age"] = 15
student["city"] = "Delhi"

print(student)
```

## Hint
Think of a dictionary like a labeled box:
- In a list, we ask: "What is at position 0?"
- In a dictionary, we ask: "What is stored under the label `name`?"

## One Small Exercise
Create a dictionary for one student with:
- `name`
- `age`
- `grade`

Then print each value.

## Hint 1
Start like this:

```python
student = {
    "name": "Asha",
    "age": 13,
    "grade": "B"
}
```

## Hint 2
Use the keys to print the values:

```python
print(student["name"])
```

## When You Finish
Send me only your Day 7 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
