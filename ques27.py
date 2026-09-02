name = input("Enter name: ")
roll_no = int(input("Enter roll number: "))
cgpa = float(input("Enter CGPA: "))
is_hosteller = input("Are you a hosteller? (True/False): ") == "True"

print("Name:", name, type(name))
print("Roll Number:", roll_no, type(roll_no))
print("CGPA:", cgpa, type(cgpa))
print("Hosteller:", is_hosteller, type(is_hosteller)) 