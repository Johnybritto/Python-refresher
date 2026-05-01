# GenAI Prep Day 7 basics problem
# Write code that:
# - stores text = "python is fun to learn"
# - counts how many words are in the sentence
# - prints the count

text = "python is fun to learn"

print(len(text.split()))

count = 1

for i in text:
    if i == " ":
        count += 1 

print(count)