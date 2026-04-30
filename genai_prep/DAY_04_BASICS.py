# GenAI Prep Day 4 basics problem
# Write code that:
# - stores text = "banana"
# - counts the frequency of each character
# - prints the final dictionary


text = "banana"
count={}

for i in text:
    if i in count:
        count[i] += 1 
    else:
        count[i] = 1 

print(count)