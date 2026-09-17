#WAP to rotate a list one position to the right#

n = int(input("Enter the number of elements in a list: "))

list = []

for i in range(0,n):
    num = int(input("Enter the number: "))
    list.append(num)

list = [list[-1]] + list[:-1]
print("Rotated list:", list)
              
