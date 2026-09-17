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
