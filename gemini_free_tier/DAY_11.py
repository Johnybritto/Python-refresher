# Gemini Free Tier Day 11 practice
# Goal:
# - understand retrieval in a tiny local example
# - scan saved notes
# - return the first relevant note


# Step 1:
# Create a list of notes like:
# ["python list", "api key", "fastapi route"]
notes = ["python list", "api key", "fastapi route"]



# Step 2:
# Define find_relevant_note(notes, query).
def find_relevant_note(notes,query):
    for i in notes:
        if query in i:
            return i 
        
    return "No matching note found "

query="api"
res = find_relevant_note(notes,query)
print(res)
# Step 3:
# Loop through the notes and return the first note
# that contains the query.


# Step 4:
# If nothing matches, return "No matching note found".


# Step 5:
# Call the function once with query "api" and print the result.
