# Gemini Free Tier Day 1 basics problem
# Write code that:
# - stores "hello world" in text
# - counts how many vowels are in the string
# - prints the final count

text = "hello world"
vowels = "aeiou"

# Your code here
count=0
for i in text:
    if i in vowels:
        count +=1

print(count)
