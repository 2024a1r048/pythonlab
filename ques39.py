 # Take roll number Like 2024a1r057 and extract admission year , program code
# and  roll no. digits using slicing
r = input("Enter Roll Number:")
print(r)
year = r[:4]
prog_code = r[4:7]
roll_no = r[7:]
print(f"Year: {year} & Program Code : {prog_code} & Roll No. {roll_no}")