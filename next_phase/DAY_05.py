# Next Phase Day 5 practice
# Write code that:
# - creates a class Dog
# - stores name in self.name
# - adds a method bark(self) that returns self.name + " says Woof"
# - creates dog1 = Dog("Tommy") and dog2 = Dog("Rocky")
# - prints dog1.bark()
# - prints dog2.bark()


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return self.name + " says Woof"
    

dog1 = Dog("tommy")

dog2 = Dog("Rocky")

print(dog1.bark())

print(dog2.bark())