# GenAI Prep Day 4 practice
# Write code that:
# - creates a class Dog
# - stores name in self.name
# - adds a method bark(self) that returns self.name + " says Woof"
# - adds a method rename(self, new_name) that changes self.name
# - creates dog1 = Dog("Tommy")
# - prints dog1.bark()
# - changes the name to "Bruno" using rename
# - prints dog1.bark() again

class Dog:
    def __init__(self, name):
        self.name=name
    
    def bark(self):
        return self.name + " says Woof"
    
    def rename(self, new_name):
        self.name=new_name

dog1=Dog("Tommy")

print(dog1.bark())

dog1.rename("Bruno")

print(dog1.bark())