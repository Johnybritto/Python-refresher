# Next Phase Day 3: Working With JSON Files

## Quick Revision
- JSON is a text format for structured data.
- `json.dumps(...)` gives JSON text as a string.
- `json.dump(...)` writes JSON directly to a file.

## Today's Goal
- Write a Python dictionary into a JSON file
- Read JSON data back from a file
- Understand `json.dump(...)` and `json.load(...)`
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If JSON text is saved in a file, how can Python turn that file content back into usable data?

If you can explain that Python should load it back, you're ready.

## Tiny Lesson

### 1. Writing JSON to a File

Example:

```python
import json

student = {"name": "Ravi", "score": 95}

with open("student.json", "w") as file:
    json.dump(student, file)
```

This writes JSON into `student.json`.

### 2. Reading JSON From a File

Example:

```python
import json

with open("student.json", "r") as file:
    data = json.load(file)
    print(data)
```

Here, `data` becomes a Python dictionary again.

### 3. `dump` vs `load`
- `json.dump(...)` writes Python data to a JSON file
- `json.load(...)` reads JSON from a file back into Python data

### 4. Why This Matters
JSON files are common for:
- saving settings
- saving small app data
- working with API responses

## Revision: `dump`, `dumps`, `load`, `loads`

- `json.dump(data, file)`:
  writes Python data directly to a JSON file

- `json.dumps(data)`:
  converts Python data into a JSON string

- `json.load(file)`:
  reads JSON from a file and converts it into Python data

- `json.loads(text)`:
  converts a JSON string into Python data

### Memory Trick
- `dump` = to file
- `dumps` = to string
- `load` = from file
- `loads` = from string

### Quick Examples

```python
import json

student = {"name": "Ravi", "score": 95}

json_text = json.dumps(student)
print(json_text)
```

```python
import json

text = '{"name": "Ravi", "score": 95}'
data = json.loads(text)
print(data)
```

## Hint
For today's exercise, use one write block and one read block.

## One Small Exercise
Write code that:
- imports `json`
- creates `student = {"name": "Ravi", "score": 95}`
- writes it to `student.json` using `json.dump(...)`
- reads it back using `json.load(...)`
- prints the loaded data

## Hint 1
Use:

```python
with open("student.json", "w") as file:
```

## Hint 2
Then use another block with:

```python
with open("student.json", "r") as file:
```

## When You Finish
Send me only your Next Phase Day 3 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
