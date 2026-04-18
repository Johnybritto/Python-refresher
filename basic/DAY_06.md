# Day 6: Lists II

## Today's Goal
- Loop through a list
- Use `len()` with a list
- Change one value in a list
- Do one small exercise

## Tiny Lesson

### 1. Looping Through a List
Use a `for` loop to look at each item one by one.

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

### 2. `len()`
Use `len()` to count how many items are in the list.

```python
numbers = [10, 20, 30]
print(len(numbers))
```

### 3. Changing One Value
Lists are mutable, which means we can change an item.

```python
numbers = [10, 20, 30]
numbers[1] = 99
print(numbers)
```

Output:

```python
[10, 99, 30]
```

## One Small Exercise

Create a list of numbers and:
- print each number
- print the total count using `len()`
- change one value in the list

## Hint 1
Start like this:

```python
numbers = [5, 10, 15, 20]
```

## Hint 2
Use:

```python
for num in numbers:
    print(num)

print(len(numbers))

numbers[1] = 99
print(numbers)
```

## When You Finish
Send me only your Day 6 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
