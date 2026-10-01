
#WAP to perform searching using Linear and Binary search.

a = list(map(int, input("Enter sorted elements: ").split()))
x = int(input("Enter element to search: "))

if x in a:
    print("Linear Search: Found")
else:
    print("Linear Search: Not Found")

low = 0
high = len(a) - 1

while low <= high:
    mid = (low + high) // 2

    if a[mid] == x:
        print("Binary Search: Found")
        break
    elif a[mid] < x:
        low = mid + 1
    else:
        high = mid - 1 
else:
    print("Binary Search: Not Found") 