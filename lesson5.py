"""
Object Oriented programming(OOP) - programming paradigm:
    - "Blue-print" => Class
    - "Actual/ Physical  House => Object
    - keyword is class

Concepts:
    - Inheritance    
    - Polymorphism
    - Encapsulation

Adavnatage:
    - Enable code reusability 
    - Enable clean code (structural perspective)
"""

# creating a blueorint of a puppy
class Puppy:
    # attributes
    name = "Scooby"
    weight = "35kgs"
    color = "brown"

    # methods(function that resides inside a class)
    def speak(self):
        print("whooof whoof!")

    def intro(self):
        print(f"My owner calls me {Scooby}!")


#   bringing a pppy to "life" i.e creating an object
# puppy_one = Puppy()
# puppy_two = Puppy()
# puppy_three = Puppy()

# puppy_one.speak()
# print(puppy_one.name)
# print(puppy_two.name)
# print(puppy_three.name)


class Dog:    
    #  initializaing with the inique attributes per dog
    def __init__(self, name:str, age:int, color:str):
        self.name = name
        self.age = age
        self.color = color 

    def speak(self):
        print(f"whoof whooof, I, {self.name} am speaking")

    def intro(self):
        print(f"My name is {self.name}. I am {self.age}yrs old and my fur is color {self.color}")



dog_one = Dog("Scooby",12,"Brown")
dog_two = Dog("Scott",11,"Golden Brown")

dog_one.speak()
dog_two.speak()
dog_one.intro()
dog_two.intro()


class SecurityDog(Dog): # inheritance
    def speak(self): # poly morphism (many forms of speak)
        print(f"Sniffing for anomalies in the vehicle!")

    def intro(self):# poly morphism (many forms of intro)
        print(f"My name is {self.name}. I am a soldier at war!")



security_dog_one = SecurityDog("Major",15,"Black & Brown")
security_dog_one.speak()
security_dog_one.intro()
