# Next Phase Day 2 practice
# Write code that:
# - imports json
# - creates a dictionary student = {"name": "Ravi", "score": 95}
# - converts it into JSON text using json.dumps(...)
# - stores the result in json_text
# - prints json_text

import json

student = {
    "name": "Ravi",
    "score": 80
}

text = json.dumps(student)

print(text)


stud = {
    "id" : 102155,
    "name": "asdasd",
    "tag": "best"
}

t = json.dumps(stud)

print(t)