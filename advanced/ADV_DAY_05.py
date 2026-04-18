
student = {
    "name": "Ravi",
    "marks": [80,90,85]
}
# - prints the student's name
print(student["name"])

# - prints the second mark
print(student["marks"][1])

students = [
    {"name": "Ravi", "city": "Delhi"},
    {"name": "Asha", "city": "Mumbai"}
]

print(students[1]["name"])

student = {
    "name": "Ravi",
    "address": {
        "city": "Delhi",
        "pin": 110001
    }
}

print(student["address"]["pin"])

print(student["address"])

students = [
    {"name": "Ravi", "city": "Delhi"},
    {"name": "Asha", "city": "Mumbai"}
]


for i in students:
    print(i["name"])


students = {
    "student1": {
        "name": "Johny",
        "city": "Delhi"
    },
    "student2": {
        "name": "Asha",
        "city": "Mumbai"
    }
}

for i in students:
    print(students[i]["city"])


students = {
    "student1": {"name": "sweety", "city": "Delhi"},
    "student2": {"name": "jo", "city": "Mumbai"}
}

for outer_key in students:
    inner_dict = students[outer_key]
    for inner_key in inner_dict:
        print(inner_key, inner_dict[inner_key])