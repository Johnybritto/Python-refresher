# Advanced Day 8: File Handling

## Quick Revision From Advanced Day 7
- An exception is an error that happens while code is running.
- `try` lets Python attempt risky code.
- `except` handles the error more safely.
- If an error happens in `try`, the rest of that block is skipped.

## Today's Goal
- Understand what a file is in Python
- Read from a file
- Write to a file
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If Python wants to save text for later, where should that text go besides the screen?

If you can explain that it should go into a file, you're ready.

## Tiny Lesson

### 1. What Is a File?
A file lets your program store text outside the code itself.

That means data can still be there later, even after the program stops.

### 2. Writing to a File
You can open a file in write mode using `"w"`.

Example:

```python
with open("notes.txt", "w") as file:
    file.write("Hello")
```

This writes `Hello` into `notes.txt`.

### 3. Reading From a File
You can open a file and read its content.

Example:

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

### 4. Why `with open(...)` Helps
`with` helps Python close the file automatically after the work is done.

That is the safe beginner pattern to use.

## Hint
For today's exercise, do the writing and reading in two separate `with` blocks.

## One Small Exercise
Write code that:
- creates a file named `day8_note.txt`
- writes `Python file practice` into it
- reads the text back from the file
- prints the text

## Hint 1
Use:

```python
with open("day8_note.txt", "w") as file:
```

## Hint 2
Then use another `with open(..., "r")`.

## Hint 3
Use `file.read()` to get the text back.

## When You Finish
Send me only your Advanced Day 8 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
