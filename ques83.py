#WAP to create a class  and object:Student details
"""
Problem: Create a Student class to store a student name and roll number.
Create an object and display the details using an instance method.
"""
### Python Program: Create a Class and Object — Student Details

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)


s1 = Student("Manav", 101)

s1.display()