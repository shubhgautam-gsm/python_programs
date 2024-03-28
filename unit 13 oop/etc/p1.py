class Employee:
    id = 10
    name = "Demo Text"
    country="india"
    state="gujarat"
    print(id)
    def displayFeild(self):
        print("ID:", self.id,"Name:", self.name)

    def displayLocation(self):
        print("country:", self.country,"state:", self.state)


emp=Employee()
emp.displayFeild()
emp.displayLocation()
