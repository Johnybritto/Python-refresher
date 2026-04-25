# GenAI Prep Day 1 basics problem
# Write code that:
# - stores "hello world" in text
# - counts how many vowels are in the string
# - prints the final count

text = "hello world"
vowels = [ "a", "e", "i", "o", "u"]
v = "aeiou"
count = {}

for i in text:
    if i in v:
        if i in count:
            count[i] += 1 
        else:
            count[i] = 1 
print(count)
print(sum(count.values()))
