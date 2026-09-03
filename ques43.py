 # write a program to determine the student is eligible for scholarship . The scholarship is granted
# a) The cgpa 8.5 or above annd attendance 85% or above
# b) The student Has a national level competition
# the progarm should take cgpa attendance percentage and national level compition status as input 
# then display whether the student is eligible for scholarship
c = float(input("Enter CGPA"))
P = float(input("Enter Attendance Percent:"))
n = input("Enter National Level Competition Status(yes/no): ")
if (c>=8.5 and P>=85) or n =="yes":
    print("CONGRATS YOU ARE ELIGIBLE FOR SCHOLARSHIP!!!!!!")
else:
    print("SORRY YOR ARE NOT ELIGIBLE FOR SCHOLARSHIP")    
    