from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    # Non-abstract method
    def greet(self):
        print(f"Hello, I'm {self.name}!")

# Subclass
class Dog(Animal):
    def sound(self):
        print("Woof!")

# Create object of the subclass
my_dog = Dog("Buddy")

# Access non-abstract method from the abstract class
my_dog.greet() 

# Access abstract method implemented in the subclass
my_dog.sound()