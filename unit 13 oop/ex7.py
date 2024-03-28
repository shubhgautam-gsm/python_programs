class Employee:
    # Parameterized Constructor

    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s"%(self.id, self.name))

# Creating instances and calling methods
emp1 = Employee("John", 101)
emp2 = Employee("David", 102)
emp1.display()
emp2.display()
