# Advanced Day 14: Intermediate Mini Project

## Quick Revision From Advanced Day 13
- Two solutions can both be correct.
- Readability and performance both matter.
- The loop-based duplicate solution is simpler to read.
- The set-based duplicate solution is usually faster.

## Today's Goal
- Combine several ideas in one small program
- Use a function
- Use a dictionary
- Use file handling
- Use simple error handling

## Check Your Current Level
Before starting, ask yourself:

If we want one small useful program instead of many tiny examples, how can we combine the skills you already know?

If you can explain that we can put multiple small ideas into one script, you're ready.

## Mini Project Idea
Build a small student score saver.

The program should:
- create a dictionary with a student's name and score
- write that data to a file
- read the file back
- print the saved text

## Tiny Lesson

### 1. Why This Project Helps
This project combines ideas you already know:
- dictionaries
- functions
- files
- `try` and `except`

### 2. Suggested Data

```python
student = {
    "name": "Ravi",
    "score": 95
}
```

### 3. Suggested File Text
You can save text like:

```python
Name: Ravi
Score: 95
```

### 4. Suggested Function
Write one function that takes the dictionary and returns the formatted text.

Example idea:

```python
def format_student(student):
    return "Name: " + student["name"] + "\nScore: " + str(student["score"])
```

## Hint
Build it in tiny steps:

1. create the dictionary
2. write one formatting function
3. write to a file
4. read and print
5. wrap file work in `try`/`except`

## One Small Exercise
Write code that:
- creates a student dictionary with `"name"` and `"score"`
- defines a function `format_student(student)`
- writes the formatted text to `student_report.txt`
- reads the file back
- prints the file content
- uses `try`/`except` around the file operations

## Hint 1
Start with:

```python
student = {
    "name": "Ravi",
    "score": 95
}
```

## Hint 2
Use `str(student["score"])` when building the text.

## Hint 3
Use one `try` block with file writing and reading inside it.

## When You Finish
Send me only your Advanced Day 14 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
