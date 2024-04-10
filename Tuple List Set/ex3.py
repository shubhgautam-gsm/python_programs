data = ["Surat", "Baroda", "Bhuj", "Rajkot", "Jamnagar","Rajkot", "Ahamdabad", "Morbi", "Rajkot"]
first_index = data.index("Rajkot")
second_index = data.index("Rajkot", first_index + 1)
third_index = data.index("Rajkot", second_index + 1)

class SwitchCaseExample:
    def ooption1(self):
     print("Index of first 'Rajkot':", first_index)

    def ooption2(self):
        print("Index of second 'Rajkot':", second_index)

    def ooption3(self):
        print("Index of third 'Rajkot':", third_index)


    def default(self):
        print("Invalid option")

    def switch_case(self, argument):
        method_name = argument.lower()
        method = getattr(self, method_name, self.default)
        return method()

# Usage:
example = SwitchCaseExample()
ooption = str(input('ooption1 | ooption2 | ooption3 write  choose which rajkot need : '))
example.switch_case(ooption)
