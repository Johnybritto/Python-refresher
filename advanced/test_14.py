

class student:
    def __init__(self ,name ,score):
        self.name=name
        self.score=score

    def format_data(self):
        return "Name: " + self.name + "\n" +  "Score: " + str(self.score) 
    
students= [
    student("john", 25),
    student("mary", 30)
]

lines =[]

for i in students:
    lines.append(i.format_data())
    lines.append("")

text_write= "\n".join(lines)

try:
    with open("student_report.txt", "w") as file:
        file.write(text_write)
    
    with open("student_report.txt", "r") as file:
        print(file.read())
except:
    print("error")