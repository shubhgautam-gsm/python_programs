class Dog:
    def speak(self):
        print("Dog says: Woof!")

class Cat:
    def speak(self):
        print("Cat says: Meow!")

def make_animal_speak(animal):
    animal.speak()

# Usage
dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Dog says: Woof!
make_animal_speak(cat)  # Output: Cat says: Meow!
