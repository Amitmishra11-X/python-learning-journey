"""Creating and using a Class"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is now sitting")
        
    def roll_over(self):
        print(f"{self.name} is rolled over!")
        
my_dog = Dog('tommy', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()      