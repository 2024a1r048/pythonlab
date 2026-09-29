 #WAP to input numbers in a list and find the second largest number.#
numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
numbers.sort()
print("Second Largest Number: ",numbers[-2])
""""""

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




#WAP to rotate a list one position to the right#

n = int(input("Enter the number of elements in a list: "))

list = []

for i in range(0,n):
    num = int(input("Enter the number: "))
    list.append(num)

list = [list[-1]] + list[:-1]
print("Rotated list:", list)


 #Write a menu-driven program where the user can add items,remove items,view cart and exit#

n = int(input("Enter the number of elements in a list: "))

cart = []

for i in range(0,n):
    num = int(input("Enter the value: "))
    cart.append(num)

while True:

    print("\n1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Exit\n")

    choice = int(input("Enter the operation you want to  perform: "))

    if choice ==1:
        num = int(input("Enter the number : "))
        cart.append(num)
        continue
    elif choice == 2:
        item = int(input("Enter the item: "))
        cart.remove(item) if item in cart else print("Not in cart")
        continue
    elif choice ==3:
        print("cart",cart)
        continue
    elif choice ==4:
        print("Exiting...")
        break



    #WAP to count how many times a particular elements appear in a list#

numbers = [10,20,30,40,50]

search = int(input("Enter number to count: "))

count = 0

for num in numbers:
    if num == search:
        count = count + 1

print("Frequency:", count)





#WAP to count how many times a particular elements appear in a list#

numbers = [10,20,30,40,50]

search = int(input("Enter number to count: "))

count = 0

for num in numbers:
    if num == search:
        count = count + 1

print("Frequency:", count)
""""""