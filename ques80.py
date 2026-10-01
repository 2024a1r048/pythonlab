#WAP to reverse every kth row in a matrix.
rows = int(input("Enter number of rows: "))
col = int(input("Enter number of  columns: "))
matrix = []

for i in range(rows):
    row = []

    for j in range(col):
        value = int(input(f"Enter element at row {i+1}, column {j+1}: "))
        row.append(value)

        matrix.append(row)

k = int(input("Enter value of k: "))

if k <= 0:
    print("Invalid value of k:")
else:
    for i in range(k - 1, rows, k): matrix[i].reverse()

    print("\nUpdated Matrix:")

    for row in matrix:
        print(row)