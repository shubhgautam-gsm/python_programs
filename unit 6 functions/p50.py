class Student:
    id = 101
    name = "Pranshu"
    email = "pranshu@abc.com"
    course = "Computer Science"  # Added missing class variable

    # Declaring function
    def getinfo(self):
        print(self.id, self.name, self.email,self.course)
        
Student().getinfo()
# Removing attribute which is not available
delattr(Student, 'course')
# Attempting to call getinfo() after removing 'course'
Student().getinfo()
