class SwitchCaseExample:
    def ooption1(self):
        print("You chose option 1")

    def ooption2(self):
        print("You chose option 2")

    def ooption3(self):
        print("You chose option 3")

    def default(self):
        print("Invalid option")

    def switch_case(self,argument):
        method_name = argument.lower()
        method = getattr(self, method_name, self.ooption2)
        return method()

# Usage:
example = SwitchCaseExample()
ooption = "Default"
example.switch_case(ooption)
