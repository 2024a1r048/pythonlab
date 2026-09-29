
# Write a python prorgam to store multiple student records as a list of tuples. Each tuple should contain name,roll numberand marks .Display students who scored above 75


students = [
    ("Alice", 101, 82),
    ("Bob", 102, 67),
    ("Charlie", 103, 91),
    ("David", 104, 58),
    ("Emma", 105, 76),
    ("Frank", 106, 45)
]

print("Students who scored above 75:\n")

for name, roll_number, marks in students:
    if marks > 75:
        print(f"Name: {name}, Roll Number: {roll_number}, Marks: {marks}")

