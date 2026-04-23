# Next Phase Day 3 practice
# Write code that:
# - imports json
# - creates student = {"name": "Ravi", "score": 95}
# - writes it to student.json using json.dump(...)
# - reads it back using json.load(...)
# - prints the loaded data
import json

student = {
    "name" : "Ravi",
    "score" : 90
}


with open("student.json", "w") as file:
    json.dump(student ,file)

with open("student.json", "r") as file:
    data = json.load(file)

    print(data)
    