# Advanced Day 3 practice
# Write code that:
# - stores a word in a variable
word = "madam"
# - reverses it using a for loop
res = ""
for i in word:
    res = i + res


# - prints the reversed word
print(res)
# - prints "palindrome" if the reversed word matches the original word
if res == word:
    print("palindrome")
else:
    print("not palindrome")
# - otherwise prints "not palindrome"
