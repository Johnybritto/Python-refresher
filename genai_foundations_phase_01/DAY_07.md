# Day 7: Parsing and Validation

## Today's Goal
- understand what parsing means
- understand what validation means
- see why "looks correct" is not enough for code

## Check Your Current Level
Before starting, answer this in your own words:

If a model returns:

```json
{"topic": "lists", "level": "beginner"}
```

what should your code check before using it?

If you say something like "check the required keys are present," you are ready for today.

## Tiny Lesson

### 1. What Parsing Means
Parsing means taking data in some format and turning it into a form your code can understand and use.

In this lesson, we are using it in a simpler way:
- reading structured output in code
- pulling out the values your program needs

Example:

```python
result = {
    "topic": "lists",
    "level": "beginner"
}

print(result["topic"])
```

The code above reads the value from a fixed key.

## One Small Exercise
Write one short answer:

What does parsing mean in simple words?

## Hint
Think: "turning data into something code can understand and use."

### 2. What Validation Means
Validation means checking that the structured output really has the shape you expect.

Useful checks:
- required keys exist
- values are the right type
- important fields are not missing

Example:

```python
result = {
    "topic": "lists",
    "level": "beginner"
}

if "topic" in result and "level" in result:
    print("Valid")
else:
    print("Invalid")
```

## One Small Exercise
Which is better?

1. use the data immediately without checking
2. validate the keys first

Write one reason.

## Hint
Think about what happens if a key is missing.

### 3. Why "Looks Correct" Is Not Enough
Something can look correct to a human and still break code.

Example:

```json
{"topic_name": "lists", "level": "beginner"}
```

This looks close, but if your code expects `topic`, then `topic_name` will still cause a problem.

That is why validation matters.

## One Small Exercise
Which response should fail validation if the required keys are `topic` and `level`?

1. `{"topic": "lists", "level": "beginner"}`
2. `{"topic_name": "lists", "level": "beginner"}`

## Hint
The key names must match exactly.

## When You Finish
Send me:
- your simple meaning of parsing
 taking the data in some format and passsing it to the code so that it can understand 
- which option is better before using structured output and why
validate the keys , if would check the keys are present before proceeding th code otherwise we will get errors 
- which response should fail validation
2 
