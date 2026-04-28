# GenAI Prep Day 3 basics problem
# Write code that:
# - stores text = "level"
# - checks whether it is a palindrome
# - prints "palindrome" or "not palindrome"

text = "level"

rev =""

for i in text:
    rev = i + rev 
print(rev)

if rev == text:
    print("Palindrome")
else:
    print("Not Palindrome")