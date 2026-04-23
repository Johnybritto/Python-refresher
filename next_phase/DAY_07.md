# Next Phase Day 7: File Handling and Exception Practice

## Quick Revision
- `self.name` belongs to one object.
- A class attribute like `Dog.animal_type` is shared.
- Objects can have different data while sharing one class.

## Today's Goal
- Combine file handling with `try`/`except`
- Read a file safely
- Handle the case where a file does not exist
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If your program tries to read a file that is missing, should it crash or handle the problem safely?

If you can explain that it should handle the problem safely, you're ready.

## Tiny Lesson

### 1. Safe File Reading
Sometimes a file may not exist yet.

If we read it directly, Python can raise an error.

### 2. Using `try` and `except`

Example:

```python
try:
    with open("notes.txt", "r") as file:
        print(file.read())
except:
    print("File not found")
```

### 3. Why This Matters
Safer programs:
- do not crash suddenly
- show clearer messages
- help users understand what went wrong

### 4. Beginner Idea
This pattern is useful when working with:
- files
- input conversion
- API requests later

## Hint
For today's exercise, do not worry about creating the file first.

The goal is to practice safe reading.

## One Small Exercise
Write code that:
- uses `try`
- tries to open `notes.txt` in read mode
- prints the file content if it exists
- prints `"File not found"` in `except` if it does not exist

## Hint 1
Start with:

```python
try:
```

## Hint 2
Put the `with open("notes.txt", "r")` block inside `try`.

## When You Finish
Send me only your Next Phase Day 7 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
