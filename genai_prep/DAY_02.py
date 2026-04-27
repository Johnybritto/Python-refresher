# GenAI Prep Day 2 practice
# Write code that:
# - defines a generator function count_numbers()
# - uses yield to give 1, 2, and 3
# - loops through the generator
# - prints each number
def count_numbers():
    yield 1 
    yield 2 
    yield 3 

def count_numbers():
    for i in range(1,4):
        yield i

for i in count_numbers():
    print(i)