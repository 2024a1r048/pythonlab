#WAP to count how many times a particular elements appear in a list#

numbers = [10,20,30,40,50]

search = int(input("Enter number to count: "))

count = 0

for num in numbers:
    if num == search:
        count = count + 1

print("Frequency:", count)
