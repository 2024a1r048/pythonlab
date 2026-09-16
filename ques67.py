 #WAP to input numbers in a list and find the second largest number.#
numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
numbers.sort()
print("Second Largest Number: ",numbers[-2])