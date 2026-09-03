 # 7. Write a Python program to simulate a digital lock system.
'''
The lock should ask the user to enter a 4-digit PIN.if the entered PIN does not contain exactly 
4 digits, the program should display an error message and ask again.if the entered PIN is correct,the lock should open.
Otherwise,the program should ask the user to try again.
'''
correct_pin = "1234"

while True:
    pin = input("Enter 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("Error: Enter exactly 4 digits.")
    elif pin == correct_pin:
        print("Lock Opened!")
        break
    else:
        print("Wrong PIN. Try again.")