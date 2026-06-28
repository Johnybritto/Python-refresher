# Gemini Free Tier Day 12 basics problem
# Write code that:
# - uses a list of dictionaries with question and answer
# - checks for one matching question
# - prints the matching answer


# Your code here
notes = [{"question":"what is the city name ", "answer": "the city name is pune "}, { "question":"population size", "answer": " its very big"}]
query ="name"
for i in notes:
    if query in i["question"]:
        print(i["answer"])
