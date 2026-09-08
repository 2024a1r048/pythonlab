 #WAP to input marks of 5 students.
""" 
For each student,the program should check whether the entered marks are valid or invalid.Marks are considered valid only if they are between 0 and 100.If the marks are invalid,the program should display "Invalid marks skipped" and move to the next student without printing those marks.iF the marks are valid,the program should displa the marks as valid
 """
for i in range(1, 6):
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks skipped")
        continue

    print("Valid marks:", marks)
