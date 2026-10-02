# Apple ASE/SRE Python Practice

This folder follows the supplied seven-day Apple ASE/SRE plan with P0 coding first.
See [the source](Apple_ASE_SRE_7_Day_Interview_Preparation_Plan.md),
[revised order](LEARNING_PLAN.md), and [coverage mapping](PLAN_MAPPING.md).
The exercises are interview preparation and are not claimed to be Apple interview questions.

## How we will work

1. Read the current day's Markdown lesson.
2. Answer the level-check question before coding.
3. Attempt the one active exercise in its Python file.
4. Run the file from this folder.
5. Share the code for review and receive progressively stronger hints if needed.
6. Mark progress only after the solution, boundary tests, and complexity explanation pass.

Start here:

```bash
cd "Apple SRE"
python3 priority_drills/ipv4_validation.py
```

The first run intentionally raises `NotImplementedError`. Implement the marked section,
then run it again.

## Folder map

- `day01`: dictionaries, sets, strings, and log aggregation
- `day02`: pointers, linked lists, and stacks
- `day03`: sliding windows, queues, and intervals
- `day04`: deferred SLO Summary supplement
- `priority_drills`: source AP exercises, starting with AP1 IPv4 validation

The current priority order is represented by `LEARNING_PLAN.md`. `DAILY_EXERCISES.md` tells you
which exercise is currently active, and `PROGRESS_LOG.md` records completed work and mistakes.
