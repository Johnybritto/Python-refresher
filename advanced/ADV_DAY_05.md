# Advanced Day 5: Dictionaries and Nested Data

## Quick Revision From Advanced Day 4
- A loop can build a new list from an old list.
- A duplicate should only be added once to the `duplicates` list.
- Clear variable names make list code easier to read.
- A list comprehension is a shorter way to build some lists.

## Revision: Looping Through Lists and Dictionaries

### 1. Loop Through a List
When you loop through a list, you get each item one by one.

Example:

```python
students = ["Ravi", "Asha"]

for name in students:
    print(name)
```

This prints:

```python
Ravi
Asha
```

### 2. Loop Through a Dictionary
When you loop through a dictionary directly, you get the keys one by one.

Example:

```python
student = {"name": "Ravi", "city": "Delhi"}

for key in student:
    print(key, student[key])
```

This prints the key and its value.

### 3. Why This Revision Matters
Nested data often combines lists and dictionaries.

That means you may need to:
- loop through a list of dictionaries
- loop through a dictionary and read each value

### 4. Nested Access Patterns to Remember
These are the main patterns from this lesson:

- `dictionary -> list`
- `list -> dictionary`
- `dictionary -> dictionary`
- `outer dictionary -> inner dictionary -> key/value`

Examples:

```python
student = {"marks": [80, 90, 85]}
print(student["marks"][1])
```

```python
students = [
    {"name": "Ravi", "city": "Delhi"},
    {"name": "Asha", "city": "Mumbai"}
]
print(students[1]["name"])
```

```python
student = {
    "address": {
        "city": "Delhi",
        "pin": 110001
    }
}
print(student["address"]["city"])
```

```python
students = {
    "student1": {"name": "Ravi", "city": "Delhi"},
    "student2": {"name": "Asha", "city": "Mumbai"}
}

for outer_key in students:
    inner_dict = students[outer_key]
    for inner_key in inner_dict:
        print(inner_key, inner_dict[inner_key])
```

```
students = {
    "student1": {
        "name": "Johny",
        "city": "Delhi"
    },
    "student2": {
        "name": "Asha",
        "city": "Mumbai"
    }
}

for i in students:
    print(students[i]["city"])
```

## Today's Goal
- Read values inside nested data
- Understand a dictionary of lists
- Understand a list of dictionaries
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a dictionary stores a list, how would you get just one item from that list?

If you can explain the two-step access idea, you're ready.

## Tiny Lesson

### 1. Dictionary of Lists
Sometimes one dictionary key stores a whole list.

Example:

```python
student = {
    "name": "Ravi",
    "marks": [80, 90, 85]
}
```

Here:
- `student["name"]` gives `"Ravi"`
- `student["marks"]` gives `[80, 90, 85]`

### 2. Two-Step Access
If the value is a list, access happens in two steps:
- get the list from the dictionary
- get one item from that list

Example:

```python
first_mark = student["marks"][0]
```

This means:
- first get `student["marks"]`
- then get index `0`

### 3. List of Dictionaries
Sometimes a list stores multiple dictionaries.

Example:

```python
students = [
    {"name": "Ravi", "city": "Delhi"},
    {"name": "Asha", "city": "Mumbai"}
]
```

To get `"Asha"`:

```python
students[1]["name"]
```

### 4. Why Nested Data Matters
Real programs often group related information together.

Nested data helps organize:
- student records
- product details
- scores and names

## Hint
For today's exercise, focus on reading data first.

Do not worry about loops yet.

## One Small Exercise
Write code that:
- creates this dictionary:

```python
student = {
    "name": "Ravi",
    "marks": [80, 90, 85]
}
```

- prints the student's name
- prints the second mark

The final output should be:

```python
Ravi
90
```

## Hint 1
Use `student["name"]` for the name.

## Hint 2
Use `student["marks"]` to get the whole marks list.

## Hint 3
The second mark is at index `1`, not `2`.

## When You Finish
Send me only your Advanced Day 5 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
