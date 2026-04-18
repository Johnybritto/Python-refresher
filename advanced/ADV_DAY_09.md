# Advanced Day 9: Modules and Imports

## Quick Revision From Advanced Day 8
- A file can store text outside your Python code.
- `"w"` writes to a file.
- `"r"` reads from a file.
- `with open(...)` is the safe beginner pattern.

## Today's Goal
- Understand what a module is
- Use `import`
- Try a built-in module
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If Python already has useful tools like square root, how can we bring those tools into our program?

If you can explain that we import a module, you're ready.

## Tiny Lesson

### 1. What Is a Module?
A module is a file or built-in collection of useful Python code.

It can contain:
- functions
- variables
- constants

### 2. Using `import`
You use `import` to bring a module into your program.

Example:

```python
import math
```

Now you can use things from the `math` module.

### 3. Example With `math`

```python
import math
print(math.sqrt(16))
```

This prints `4.0`.

### 4. Another Example

```python
import math
print(math.pi)
```

This prints a precise value of pi.

## Hint
For today's exercise, use `import math` exactly as shown.

## One Small Exercise
Write code that:
- imports `math`
- prints `math.sqrt(25)`

## Hint 1
Start with:

```python
import math
```

## Hint 2
Use `print(math.sqrt(25))`.

## When You Finish
Send me only your Advanced Day 9 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
