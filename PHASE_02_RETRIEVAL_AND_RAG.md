# Phase 2: Retrieval and RAG Foundations

## Goal
Understand how systems fetch useful knowledge before answering.

## Why This Phase Matters
This is the phase where common industry words start becoming real:
- chunking
- embeddings
- similarity search
- vector DB
- RAG
- grounding
- hallucination reduction

## Main Topics
- what retrieval means
- chunking and why it exists
- fixed-size vs simple semantic chunking
- embeddings in simple words
- similarity search
- keyword search vs vector search
- vector databases at a conceptual level
- what RAG means
- grounding and source-based answers
- hallucinations and why retrieval helps but does not fully solve them

## What You Should Understand By The End
- why long documents are split
- why raw keyword matching is limited
- what an embedding is trying to represent
- why vector DBs exist
- how retrieved context is inserted into a prompt
- why bad retrieval causes bad answers

## Practical Focus
Keep this phase local and simple:
- split a short document into chunks
- retrieve the best chunk
- compare keyword vs similarity intuition
- return an answer with the source text

## Mini Outcomes
By the end of this phase, you should build:
- one chunking demo
- one retrieval demo
- one source-grounded answering demo
- one short note comparing retrieval failure cases

## Important Reminder
Do not start with heavy infrastructure.

Understand the flow first:
document -> chunk -> embed -> store -> retrieve -> answer

## Suggested Difficulty
Medium.

This phase introduces more new terms, so it should stay slow and practical.
