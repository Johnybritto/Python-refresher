# Next Phase Day 7 practice
# Write code that:
# - uses try
# - tries to open notes.txt in read mode
# - prints the file content if it exists
# - prints "File not found" in except if it does not exist

try:
    with open("notes.txt", "r") as file:
        file.read()
except:
    print("file error or file not found ")
    