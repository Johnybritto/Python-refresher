# Gemini Free Tier Day 4 basics problem
# Write code that:
# - stores the dictionary
# - checks whether both keys exist
# - checks whether age is at least 18
# - prints "valid" if all checks pass
# - otherwise prints "invalid"

data = {"name": "Ana", "age": 5}


if "name" in data and "age" in data:
    if data["age"] >=18:
        print("valid")
    else:
        print("invalid")
else:
    print("invalid")

