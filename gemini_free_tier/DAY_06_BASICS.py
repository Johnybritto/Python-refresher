# Gemini Free Tier Day 6 basics problem
# Write code that:
# - stores messages = ["hi", "hello", "bye"]
# - prints each message with its position starting from 1

messages = ["hi", "hello", "bye"]

# Your code here

for i , message in enumerate(messages, start=1):
    print(i, message)


counter = 1 

for i in messages:
    print( counter , i )
    counter +=1


