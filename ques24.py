 # write a program to take the marks of 3 subjects out of 100 . Print true if the student store atleast 
# 40 in all subjects and average marks are atleast 50
a = int(input("Enter Marks ofSUB1: "))
b = int(input("Enter Marks ofSUB2: "))
c = int(input("Enter Marks ofSUB3: "))
avg = (a+b+c)/3
if a  and b  and c>=40 and avg >=50:
    print("True")

else:
    print("False")