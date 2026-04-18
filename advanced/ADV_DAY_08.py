# Advanced Day 8 practice
# Write code that:
# - creates a file named day8_note.txt
# - writes Python file practice into it
# - reads the text back from the file
# - prints the text

with open("day8_note.txt", "w") as file:
    file.write("Python file practice")

with open("day8_note.txt", "r") as f:
    content = f.read()
    print(content)


with open("hello.txt" , "w") as file:
    file.write("Hello")

with open("hello.txt", "r") as file:
    print(file.read())
