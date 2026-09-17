#WAP to input numbers in a list and create two separate lists for even nd odd numbers#

n = int(input("Enter the number of elements: "))

list = []

for i in range(0,n):
    num = int(input("Enter the number: "))
    list.append(num)

even_list = []
odd_list = []

for i in list:
    if i%2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("even_list:", even_list )
print("odd_list:", odd_list)
