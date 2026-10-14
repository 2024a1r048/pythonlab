#WAP to manage a small library using a dictionary.The program must repeatedly allow user to add books, issue books, return books and display the current book record.
"""
Conditions:
Store a book title as the key and available copies as the value 
"""

# WAP to manage a small library using a dictionary

library = {}

while True:

    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        copies = int(input("Enter number of copies: "))

        library[title] = copies
        print("Book added successfully.")

    elif choice == 2:
        title = input("Enter book title to issue: ")

        if title in library:
            if library[title] > 0:
                library[title] -= 1
                print("Book issued successfully.")
            else:
                print("Book is not available.")
        else:
            print("Book not found.")

    elif choice == 3:
        title = input("Enter book title to return: ")

        if title in library:
            library[title] += 1
            print("Book returned successfully.")
        else:
            print("Book not found.")

    elif choice == 4:
        print("\nCurrent Book Records:")

        for title, copies in library.items():
            print(title, ":", copies)

    elif choice == 5:
        print("Exiting library...")
        break

    else:
        print("Invalid choice.")