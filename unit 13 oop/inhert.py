# Parent class
class Animal:
    def speak(self):
        print("Animal Speaking")

# Child class inheriting from Animal
class Dog(Animal):
    
    def bark(self):
        print("Dog Barking")

dog = Dog()
dog.bark()  # Output: Dog Barking
dog.speak() # Output: Animal Speaking
