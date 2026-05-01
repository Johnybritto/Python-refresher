# GenAI Prep Day 6: Virtual Environments and `pip`

## Quick Revision
- `self` works with one object.
- `cls` works with the class.
- `@staticmethod` is for helper logic that does not need `self` or `cls`.

## Today's Goal
- Understand what a virtual environment is
- Understand why `pip` is used
- See why project dependencies should stay organized
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If two Python projects need different package versions, should they both always use the same global environment?

If you can explain why not, you're ready.

## Tiny Lesson

### 1. What Is a Virtual Environment?
A virtual environment is a separate Python environment for one project.

It helps keep:
- packages
- versions
- project setup

separate from other projects.

### 2. Why This Matters
Without a virtual environment:
- packages from one project can affect another
- version conflicts become harder to manage

### 3. What `pip` Does
`pip` installs Python packages.

Example:

```powershell
pip install requests
```

### 4. Common Beginner Workflow

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install a package:

```powershell
pip install requests
```

Save dependencies:

```powershell
pip freeze > requirements.txt
```

### 5. Why `requirements.txt` Helps
It records the packages used by the project so they can be reinstalled later.

## Hint
Today's exercise is about understanding the workflow, not memorizing every command perfectly yet.

## One Small Exercise
Write a short note in comments inside `DAY_06.py` that shows:
- the command to create a virtual environment
- the command to activate it in PowerShell
- the command to install `requests`
- the command to create `requirements.txt`

## Hint 1
Use comment lines that start with `#`.

## Hint 2
You do not need to run the commands inside the file.

## When You Finish
Send me only your GenAI Prep Day 6 code.

Then I will review it for:
- Correctness
- Readability
- What to improve next

## LeetCode-Style Basics Problem
This is the small basics problem for Day 6 from the roadmap.

### Problem
Write code that reverses a string.

Use this string:

```python
text = "python"
```

Your program should print:

```python
nohtyp
```

### Hint 3
You can use a loop or slicing.

## When You Finish The Basics Problem
Send me only your Day 6 basics-problem code.
