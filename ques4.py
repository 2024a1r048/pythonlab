#write a python program to take a 2 digit number as input and print the sum of its digits

a = int(input("A 2-digit number: "))
tens = a // 10
ones = a % 10
print("Sum of digits: ", tens + ones)