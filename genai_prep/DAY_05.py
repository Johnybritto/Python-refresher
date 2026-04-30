# GenAI Prep Day 5 practice
# Write code that:
# - creates a class Dog
# - adds a class attribute animal_type = "dog"
# - adds a class method get_animal_type(cls) that returns cls.animal_type
# - adds a static method sound() that returns "Woof"
# - prints Dog.get_animal_type()
# - prints Dog.sound()

class Dog:
    animal_type = "dog"
    
    @classmethod
    def get_animal_type(cls):
        return cls.animal_type
    
    @staticmethod
    def sound():
        return "woof"
    


print(Dog.get_animal_type())
print(Dog.sound())