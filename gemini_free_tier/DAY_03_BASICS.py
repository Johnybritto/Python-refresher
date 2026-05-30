# Gemini Free Tier Day 3 basics problem
# Write code that:
# - stores the words list
# - counts how many times each word appears
# - prints the final dictionary

words = ["json", "prompt", "json", "reply"]

# Your code here

count = {}

for i in words:
    if i in count:
        count[i] += 1 
    else:
        count[i] = 1 

print(count)