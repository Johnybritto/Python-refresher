# Day 7 practice
# Create one dictionary named student.
student={}
# Add: name, age, and grade.
student={"name": "Johny",
         "age": 12,
         "grade": "A"}
# Then print each value one by one.
print(student["name"])
print(student["age"])
print(student["grade"])

for i,j in student.items():
    print(f"{i}: {j}")

student["grade"]="A+"
print(student["grade"])

print(student.values())

student["city"] = "mumbai"
print(student)