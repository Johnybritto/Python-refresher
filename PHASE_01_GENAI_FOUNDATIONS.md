# Phase 1: GenAI Foundations

## Goal
Build a clear beginner-friendly understanding of how modern GenAI systems behave before moving into RAG, agents, or larger app architecture.

## Study Length
- 14 days
- 1 hour per day

## Why This Phase Matters
If GenAI basics are weak, later topics like retrieval, evaluation, memory, and tool use become confusing.

This phase keeps the ideas small, practical, and testable.

## What You Should Understand By The End
- what a model is doing at a simple level
- why prompts change output quality
- why token limits and context windows matter
- why model output can sound confident and still be wrong
- why structured outputs are useful in apps
- why validation and evaluation matter
- why chat history is not the same as true memory

## Daily Study Structure
- 10 min: revise yesterday's idea
- 15 min: learn one new concept
- 20 min: inspect 2 or 3 examples
- 10 min: do one small exercise
- 5 min: write one short note about what was confusing

## Main Topics
- GenAI vs normal software behavior
- tokens
- context windows
- prompts
- system instructions
- output variability
- temperature in simple terms
- structured outputs
- parsing and validation
- tool calling basics
- chat history vs memory
- evaluation basics

## 14-Day Roadmap

### Day 1: What GenAI Is
- understand the difference between normal code and model-generated output
- learn simple words: model, prompt, response
- observe that the same task can be asked in better or worse ways

### Day 2: Tokens and Context Windows
- learn what tokens are in simple terms
- understand why long input can cause problems
- see why context is limited

### Day 3: Prompt Quality Basics
- compare weak prompts vs clear prompts
- learn how constraints improve output
- practice asking for specific format and scope

### Day 4: System Instructions vs User Prompt
- understand why system instructions exist
- see how role and rules affect answers
- compare base request vs guided request

### Day 5: Output Variability and Temperature
- learn why model outputs can vary
- understand temperature in simple practical language
- observe predictable vs creative behavior

### Day 6: Structured Output Basics
- ask for JSON instead of plain text
- understand why apps prefer fixed shapes
- compare free text vs structured output

### Day 7: Parsing and Validation
- read structured output safely
- check for required keys
- understand why "looks correct" is not enough

### Day 8: Reusable Model Helper Design
- keep model-call logic in one helper
- separate prompt text from parsing logic
- return safe fallback output

### Day 9: Chat History vs Memory
- understand plain chat history
- learn why long chats become messy
- compare temporary context vs stored knowledge

### Day 10: Failure Modes
- observe wrong facts, vague answers, and format mistakes
- learn that confidence is not correctness
- practice spotting risky outputs

### Day 11: Tool Calling Basics
- understand the idea of letting a model choose an external tool
- compare "model answers directly" vs "model routes to helper code"
- keep the tool concept simple and practical

### Day 12: Evaluation Basics
- learn how to judge outputs with simple checks
- compare subjective review vs rule-based checks
- track good output, weak output, and failure cases

### Day 13: Mini Practice Day
- combine prompt design, structured output, and validation
- build one tiny end-to-end example
- note repeated mistakes

### Day 14: Review and Readiness Check
- review the whole phase
- list strongest concepts
- list weak areas to revisit before Phase 2
- decide whether you are ready for retrieval and RAG

## Practical Outcomes
By the end of this phase, you should build:
- one clean GenAI helper
- one structured output example
- one small validation example
- one short evaluation script

## Success Rule
This phase is successful if you can explain each concept simply and also show it with a tiny code example.
