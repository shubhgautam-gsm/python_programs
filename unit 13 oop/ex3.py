# Abstraction Example



class Vehicle():

    def start(self):
        pass

    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

class Plane(Vehicle):
    def start(self):
        print("Plane is starting")



# Encapsulation Example

class Vehicle:
    def __init__(self, make, model):
        self._make = make  # Encapsulated attribute
        self._model = model  # Encapsulated attribute

    def start(self):
        pass  # Implementation omitted for brevity

    def stop(self):
        pass  # Implementation omitted for brevity

    def get_make(self):  # Getter method
        return self._make

    def get_model(self):  # Getter method
        return self._model

# Usage of Abstraction

car = Car()
car.start()  # Output: Car is starting

plane = Plane()
plane.start()  # Output: Plane is starting

# Usage of Encapsulation

vehicle = Vehicle("Toyota", "Camry")
print("Make:", vehicle.get_make())  # Output: Make: Toyota
print("Model:", vehicle.get_model())  # Output: Model: Camry
