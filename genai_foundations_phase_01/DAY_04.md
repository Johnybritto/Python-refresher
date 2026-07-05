# Day 4: System Instructions vs User Prompt

## Today's Goal
- understand what system instructions are
- understand what a user prompt is
- see how rules and roles can guide model answers

## Check Your Current Level
Before starting, answer this in your own words:

If a user asks, `Explain Python lists`, and the system says, `Always answer like a beginner teacher`, which instruction should shape the answer?

If you say "the system instruction should guide the style," you are ready for today.

## Tiny Lesson

### 1. What a User Prompt Is
A user prompt is the message or request the user gives to the model.

Examples:
- `Explain Python lists.`
- `Write a function to count vowels.`
- `Summarize this paragraph in 3 bullet points.`

The user prompt usually tells the model what task to do.

## One Small Exercise
Write one short answer:

In this example, what is the user prompt?

`Explain Python dictionaries to a beginner.`

## Hint
The user prompt is the instruction typed by the user.

### 2. What System Instructions Are
System instructions are higher-level rules given to the model before the user prompt.

They can tell the model:
- what role to follow
- what style to use
- what rules to obey
- what it should avoid

Example system instruction:
`You are a beginner-friendly Python tutor. Use simple language and short examples.`

Example user prompt:
`Explain for loops.`

The final answer should follow both:
- the system instruction gives the behavior
- the user prompt gives the task

## One Small Exercise
Which part gives the model its role?

1. `You are a beginner-friendly Python tutor.`
2. `Explain for loops.`

Write one reason.

## Hint
A role usually sounds like "You are..."

### 3. Guided Request vs Base Request
A base request gives only the task.

Base request:
`Explain if statements.`

A guided request includes extra rules or role guidance.

Guided request:
`You are a beginner-friendly Python tutor. Explain if statements in simple language with 1 small example.`

The guided request is usually better because it tells the model:
- the role
- the audience
- the style
- the output size

## One Small Exercise
Rewrite this base request into a guided request:

`Explain functions.`

## Hint
Try adding:
- a role
- beginner-friendly language
- one small example

## When You Finish
Send me:
- the user prompt from the dictionary example
`Explain Python dictionaries to a beginner.`
- which part gives the model its role and why
 1. becuase its defines the model you are 
- your guided request for `Explain functions.`
`You are a beginner-friendly Python tutor. Use simple language and short examples and explain function in 3 -4 points with 1 example`.

