# Gemini Free Tier Day 2 basics problem
# Write code that:
# - stores "prompt" in text
# - reverses the string without slicing
# - prints the reversed string

text = "prompt"
#text = "madam"
# Your code here

rev = ""

for i in text:
    rev = i+rev
print(rev)

#palindrome
#left , right = 0, len(text)-1
#
#while left < right:
#    while left < right and not text[left].isalnum():
#        left+=1
#    while left <right and not text[right].isalnum():
#        right-=1
#    while left< right:
#         if text[left] != text[right]:
#             print("False")
#         left+=1
#         right-=1
#    print("true")
