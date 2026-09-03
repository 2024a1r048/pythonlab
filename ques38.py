 # Take student full name and roll number.Generate email using first 3 letters of first name, first 3 letters of last name, and last 3 characters of roll numbers.
name = input("Enter Full Name: ")
roll = input("Enter Roll Number: ")

name = name.split()

email = name[0][:3] + name[1][:3] + roll[-3:] + "@gmail.com"
print("Email:", email)