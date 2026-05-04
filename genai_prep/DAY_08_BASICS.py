# GenAI Prep Day 8 basics problem
# Write code that:
# - stores first = {"a": 1, "b": 2}
# - stores second = {"c": 3, "d": 4}
# - merges them into one dictionary
# - prints the result


first = {"a" : 1 , "b" : 2 }
second = { "c": 3 , "d": 4}

result={}

result.update(first)
result.update(second)
print(result)