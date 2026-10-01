#WAP Create a database using lists and tuples. Each student record must contain roll number, name, branch, and CGPA. Store each record as a tuple inside a list. Display all records and search for a student using roll number
#Conditions:
"""
Each record should be stored as a tuple.
The complete databases should be stored as a list.
Roll numbers must be unique.
"""
n = int(input("Enter number of students: "))
database = []
for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))
    student = (roll,name,branch,cgpa)
    database.append(student)
print("Student Records: ")
for student in database:
    print("student")
search = int(input("Enter roll number to search: "))
found = False
for student in database:
    if student[0] == search:
        print("Student Found")
        print("Roll:",student[0])
        print("Name:",student[1])
        print("Branch:",student[2])
        print("CGPA:",student[3])
        found = True
    if found == False:
        print("Student not found")