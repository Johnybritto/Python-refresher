# Day 8: Dictionaries II and Sets

## Quick Revision From Day 7
- A dictionary stores data as `key: value` pairs.
- We can get one value using a key like `student["name"]`.
- We can update a value like `student["grade"] = "A+"`.
- We can add a new key like `student["city"] = "Mumbai"`.

## Today's Goal
- Review simple dictionary methods
- Learn why sets are useful
- Convert a list with repeated values into a set
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

Can you answer this?

If a list is `[1, 2, 2, 3]`, which value is repeated?

If you can spot repeated values, you're ready for today.

## Tiny Lesson

### 1. Dictionary Review
Some useful dictionary methods:

```python
student = {
    "name": "Johny",
    "age": 12,
    "grade": "A+"
}

print(student.keys())
print(student.values())
print(student.items())
```

- `keys()` gives all keys
- `values()` gives all values
- `items()` gives key-value pairs

### 2. What Is a Set?
A set stores unique values only.

```python
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)

print(unique_numbers)
```

The repeated values are removed.

### 3. Why Use a Set?
Use a set when:
- you want unique items only
- you want to check if something exists

Example:

```python
colors = {"red", "blue", "green"}
print("red" in colors)
```

## Hint
Think of a set like a bag that does not allow duplicates.

If you put `2` in the bag three times, it still keeps only one `2`.

## One Small Exercise
Create a list with repeated numbers and:
- convert it to a set
- print the unique values

## Extra Practice: Count Repeated Values
You can also count how many times a value appears.

### Count a Number in a List

```python
numbers = [1, 2, 3, 3, 3]
target_number = 3

print(numbers.count(target_number))
```

### Count a Character in a String

```python
word = "banana"
target_character = "a"

print(word.count(target_character))
```

`count()` tells you how many times the given value appears.

## Hint 1
Start like this:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
```

## Hint 2
Use:

```python
unique_numbers = set(numbers)
print(unique_numbers)
```

## When You Finish
Send me only your Day 8 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
