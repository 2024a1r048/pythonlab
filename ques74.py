
#WAP to store one student data as a tuple:name, roll number, and marks.Display grade based on marks.
student=("Vishavjeet Singh","2024a1r011",98)
name=student[0]
roll_no=student[1]
marks=student[2]

print("Name:",name)
print("Roll Number:",roll_no)
print("Marks:",marks)

if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=40:
    print("Grade D")
else:
    print("Grade F")


