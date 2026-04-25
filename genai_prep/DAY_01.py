# GenAI Prep Day 1 practice
# Write code that:
# - opens notes.txt in read mode using with
# - stores the file content in content
# - prints content


with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
