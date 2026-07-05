# Day 2: Tokens and Context Windows

## Today's Goal
- learn what a token is in simple words
- understand what a context window means
- see why shorter, more relevant prompts usually work better

## Check Your Current Level
Before starting, answer this in your own words:

If you give an AI one short sentence and then 20 large paragraphs, which input is more likely to cause a limit problem?

If you say "the 20 large paragraphs," you are ready for today.

## Tiny Lesson

### 1. What a Token Is
A token is a small chunk of text that a model reads.

It is not always:
- one full word
- one single character
- one full sentence

You can think of it like this:
- words are often split into small pieces
- punctuation also takes space
- longer input usually uses more tokens

Simple idea:

`Hello` uses fewer tokens than a long instruction with many sentences.

## One Small Exercise
Which one likely uses more tokens?

1. `cat`
2. `Explain Python lists to a beginner in 5 short bullet points with one example.`

## Hint
Look at which option has more text pieces for the model to read.

### 2. What a Context Window Is
A context window is the amount of text the model can pay attention to at one time.

That can include:
- your current prompt
- earlier chat messages
- pasted notes or documents

If too much text is included, the model may:
- miss details
- forget earlier parts
- give weaker answers

Simple idea:

The context window is like a limited work area, not unlimited memory.

## One Small Exercise
Write one short sentence:

Why can a very long chat become harder for a model to handle well?

## Hint
Use the idea of "limited space" or "too much text."

### 3. Why This Matters for Prompting
Because context is limited, a better prompt usually keeps only the useful parts.

Weak version:

`Here is a huge story about my whole week. Somewhere inside it, please find the part about Python lists and explain it.`

Better version:

`Explain Python lists to a beginner in 3 short bullet points with 1 example.`

The better version helps because it:
- stays focused
- uses less space
- makes the task clearer

## One Small Exercise
Rewrite this into a tighter prompt:

`I have many thoughts about programming, learning, confusion, websites, and many topics, but somewhere in all that I want help understanding Python dictionaries.`

## Hint
Keep only the useful goal, audience, and format.

## When You Finish
Send me:
- your answer for which text uses more tokens
cat
- your one-sentence explanation of long chats
long chats has too much text and as there is limited space  becuase of that the model may give weak answers and miss details 
- your rewritten prompt about Python dictionaries
explain python dictionaries to a begineer in  3 simple points with 1 example 