# Gemini Free Tier Day 12 practice
# Goal:
# - retrieve one relevant note
# - use that note to build a simple answer
# - print both the answer and the source note
from DAY_11 import find_relevant_note 

# Step 1:
# Create a list of notes.
notes = ["python list", "api key", "fastapi route"]

query ="route"
# Step 2:
# Define find_relevant_note(notes, query).


# Step 3:
# Get one source_note from the query.

source_note=find_relevant_note(notes,query)

# Step 4:
# Build one simple answer using the source_note.
answer = f"Answer based on note: { source_note }"
print(answer)
print(source_note)

# Step 5:
# Print both:
# - the answer
# - the source note
