# Next Phase Day 6 practice
# Write code that:
# - creates a class Dog
# - adds a class attribute animal_type = "dog"
# - stores name in self.name
# - creates dog1 = Dog("Tommy") and dog2 = Dog("Rocky")
# - prints dog1.name
# - prints dog2.name
# - prints Dog.animal_type


class Dog:
    animal_type = "dog"

    def __init__(self, name):
        self.name = name
    

dog1 = Dog("tommy")
dog2 = Dog("Rocky")
print(dog1.name)
print(dog2.name)
print(Dog.animal_type)