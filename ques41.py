 # 4. Take name,branch,and year.Generate a code name using string concatenation,slicing,and repetition.
name = input("Enter Name: ")
branch = input("Enter Branch: ")
year = input("Enter Year: ")

code = name[:3] + branch[:3] + year[-2:] + "X" * 2

print("Code Name:", code)