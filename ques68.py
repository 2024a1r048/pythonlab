#WAP to input a list and create a new list containing only unique elements.

numbers = []
unique_numbers = []

n = int(input("Enter total numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original list:", numbers)
print("Unique list: ", unique_numbers)
