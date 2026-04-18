# Day 3: Strings I

## 5-Minute Revision of Day 1 and Day 2

### Day 1 Recall
- A variable is a name that stores a value.
- `print()` shows output on the screen.
- Strings are text like `"hello"`.
- Numbers are values like `5` and `3.14`.
- Use `=` to assign a value.

### Day 2 Recall
- `int` means whole number.
- `float` means decimal number.
- `str` means text.
- `bool` is only `True` or `False`.
- `/` gives division.
- `//` gives floor division.
- `%` gives remainder.

### Quick Mental Check
Try to answer these without running code:

```python
print("Hi" * 2)
print(9 % 4)
print(9 // 4)
```

Expected ideas:
- String repetition joins the text again.
- `%` gives remainder.
- `//` removes the decimal part.

## Today's Goal
- Understand string indexing
- Understand string slicing
- Read characters from a word
- Do one small exercise

## Tiny Lesson

We already know a string is text.

```python
word = "python"
```

Each character has a position called an index.

```python
word[0]   # 'p'
word[1]   # 'y'
word[2]   # 't'
```

Python starts counting from `0`, not `1`.

### Negative Index
You can also count from the end:

```python
word[-1]  # 'n'
word[-2]  # 'o'
```

### Slicing
Slicing means taking part of a string.

```python
word[0:3]   # 'pyt'
word[1:4]   # 'yth'
```

Important rule:
- start index is included
- end index is not included

So `word[0:3]` means:
- take index `0`
- take index `1`
- take index `2`
- stop before index `3`

## One Small Exercise

Given a word, print:
- the first character
- the last character
- the first three characters

Answer 
a="print"
print(a[0])
print(a[-1])
print(a[0:3])
Example word:

```python
word = "python"
```

## Hint 1
Use:

```python
word[0]
word[-1]
word[0:3]
```

## Hint 2
Print each result on a separate line.

## When You Finish
Send me only your Day 3 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
