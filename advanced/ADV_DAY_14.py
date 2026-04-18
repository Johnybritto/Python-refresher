# Advanced Day 14 practice
# Write code that:
# - creates a student dictionary with "name" and "score"
# - defines a function format_student(student)
# - writes the formatted text to student_report.txt
# - reads the file back
# - prints the file content
# - uses try/except around the file operations

student =[
    {
        "name":"Jack",
        "score" : 50,
    },
    {
        "name":"Rose",
        "score": 75
    }
]


def format_student(student):
    for i in student:
        for k in i:
            a= k + " : " + str(i[k]) + "\n"
            with open("student_report.txt", "a") as file:
                try:
                    file.writelines(a)
                except:
                    print("unableto write")
    
    with open("student_report.txt", "r") as file:
        print(file.read())


format_student(student)

###
students = [
    {"name": "Jack", "score": 50},
    {"name": "Rose", "score": 75}
]

def format_students(students):
    lines = []

    for student in students:
        lines.append("Name: " + student["name"])
        lines.append("Score: " + str(student["score"]))
        lines.append("")

    return "\n".join(lines)

try:
    text = format_students(students)

    with open("student_report.txt", "w") as file:
        file.write(text)

    with open("student_report.txt", "r") as file:
        print(file.read())

except:
    print("unable to work with file")


#class
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def format_data(self):
        return "Name: " + self.name + "\nScore: " + str(self.score)

students = [
    Student("Jack", 50),
    Student("Rose", 75)
]

lines = []

for student in students:
    lines.append(student.format_data())
    lines.append("")

text = "\n".join(lines)

try:
    with open("student_report.txt", "w") as file:
        file.write(text)

    with open("student_report.txt", "r") as file:
        print(file.read())
except:
    print("unable to work with file")
