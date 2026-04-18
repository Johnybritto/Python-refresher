# Advanced Day 11 practice
# Write code that:
# - creates a class named Dog
# - adds __init__(self, name)
# - stores name in self.name
# - creates my_dog = Dog("Tommy")
# - prints my_dog.name

class Dog:
    def __init__(self,name):
        self.name =name


my_dog = Dog("Tommy")
print(my_dog.name)


class cat:
    def __init__(self,name):
        self.name=name

my_cat=cat("Here")
print(my_cat.name)




class bird:
    def __init__(self,name):
        self.name=name

parrot=bird("parrot")
print(parrot.name)