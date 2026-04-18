# Day 4: Strings II

## Today's Goal
- Build strings more comfortably
- Use common string methods
- Clean and inspect text
- Do one small exercise

## Tiny Lesson

### 1. `upper()`
Turns text into uppercase.

```python
text = "hello"
print(text.upper())
```

Output:

```python
HELLO
```

### 2. `lower()`
Turns text into lowercase.

```python
text = "HeLLo"
print(text.lower())
```

Output:

```python
hello
```

### 3. `strip()`
Removes extra spaces from the beginning and end.

```python
text = "  python  "
print(text.strip())
```

Output:

```python
python
```

### 4. `find()`
Gives the index of the first match.

```python
word = "python"
print(word.find("th"))
```

Output:

```python
2
```

If Python does not find it, it returns `-1`.

### 5. `replace()`
Replaces one part with another.

```python
text = "I like cats"
print(text.replace("cats", "dogs"))
```

Output:

```python
I like dogs
```

## One Small Exercise

Given a sentence, print:
- the sentence in uppercase
- the sentence in lowercase
- the sentence with extra spaces removed

Example:

```python
sentence = "  Python Is Fun  "
```

## Hint 1
Use:

```python
sentence.upper()
sentence.lower()
sentence.strip()
```

## Hint 2
Print each result on a separate line.

## When You Finish
Send me only your Day 4 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
