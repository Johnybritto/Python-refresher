# Gemini Free Tier Day 13 practice
# Goal:
# - check a few AI-style answers
# - record simple evaluation results
# - print the results clearly

# Step 1:
# Create 3 test cases with prompt and answer.
tests = [
    {
        "prompt": "What is Python?",
        "answer": "Python is a programming language.",
    },
    {
        "prompt": "What is FastAPI?",
        "answer": "FastAPI is a Python web framework.",
    },
    {
        "prompt": "What is an API key?",
        "answer": "An API key is used to access a service.",
    },
]

# Step 2:
# Create an empty list for evaluation results.
eval = []

# Step 3:
# Loop through the test cases.
# For each one, create a result dictionary with:
# - prompt
# - answer
# - correct
# - clear
# - well_formatted

for i in tests:
    result = {
        "prompt": i["prompt"],
        "answer": i["answer"],
        "correct": "yes",
        "clear": "yes",
        "well_formatted": "yes",
    }

    eval.append(result)


# Step 4:
# Add each result dictionary to the results list.


# Step 5:
# Print each result clearly.
for r in eval:
    print(r)

