# Day 5: Lists I

## Today's Goal
- Understand what a list is
- Read values from a list using indexes
- Get the last item from a list
- Add a new item using `append()`
- Do one small exercise

## Tiny Lesson

A list stores multiple values in one variable.

```python
fruits = ["apple", "banana", "mango"]
```

### Indexing
Lists also use indexes just like strings.

```python
fruits[0]   # "apple"
fruits[1]   # "banana"
fruits[-1]  # "mango"
```

### `len()`
`len()` tells us how many items are in the list.

```python
print(len(fruits))
```

### `append()`
Use `append()` to add one new item at the end.

```python
fruits.append("grapes")
print(fruits)
```

Output:

```python
['apple', 'banana', 'mango', 'grapes']
```

## One Small Exercise

Create a list of 4 fruits and:
- print the first fruit
- print the last fruit
- add one more fruit

## Hint 1
Start like this:

```python
fruits = ["apple", "banana", "mango", "orange"]
```

## Hint 2
Use:

```python
fruits[0]
fruits[-1]
fruits.append("grapes")
```

## When You Finish
Send me only your Day 5 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
