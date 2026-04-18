# Advanced Day 3: More With Strings

## Quick Revision From Advanced Day 2
- A variable created outside a function can be global.
- A variable created inside a function is usually local.
- Using a local variable outside its function can raise a `NameError`.
- Scope helps keep variables organized.

## Today's Goal
- Count characters in a string
- Understand what a palindrome is
- Reverse a string manually with a loop
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a word reads the same forward and backward, how could you check that with Python?

If you can explain one idea, you're ready.

## Tiny Lesson

### 1. What Is a Palindrome?
A palindrome is a word that reads the same forward and backward.

Examples:
- `madam`
- `level`

### 2. Reverse a String With a Loop
You already know this revision pattern:

```python
word = "python"
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word = reversed_word + word[i]
```

After the loop, `reversed_word` becomes `"nohtyp"`.

### 3. Palindrome Idea
One simple way to check a palindrome:
- reverse the word
- compare the reversed word to the original word

If they are the same, it is a palindrome.

### 4. Character Counting
You can also count characters with `len(word)`.

That tells you how many characters are in the string.

## Hint
For today's exercise, focus on one word only.

Do not worry about uppercase letters or spaces yet.

## One Small Exercise
Write code that:
- stores a word in a variable
- reverses it using a `for` loop
- prints the reversed word
- prints `"palindrome"` if the reversed word matches the original word
- otherwise prints `"not palindrome"`

## Hint 1
Start with:

```python
word = "level"
reversed_word = ""
```

## Hint 2
Use:

```python
for i in range(len(word) - 1, -1, -1):
```

## Hint 3
After building `reversed_word`, compare it with `word`.

## When You Finish
Send me only your Advanced Day 3 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
