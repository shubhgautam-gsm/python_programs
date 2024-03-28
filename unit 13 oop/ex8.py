class Student:
    # Class variable to keep track of the number of instances
    count = 1

    def __init__(self):
        # Increment the count each time a new instance is created
        Student.count =Student.count + 1

# Create instances of the Student class
s1 = Student()
s2 = Student()
s3 = Student()

# Output the total number of students
print("The number of students:", Student.count)
