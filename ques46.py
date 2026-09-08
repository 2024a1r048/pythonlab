 #WAP to  create a simple password validation system.
"""
The program should repeatedly ask the user to enter a password until a valid password is entered.A password will be considered valid only if it has at least 8 characterd and contain the @symbol
Once the user enters a valid password, the program should display"Passord accepted" and stop.Otherwise,it should display"Weak password,Try again." ask for the password again.
"""

password = input("Enter password: ")
while len(password)< 8 or "@" not in password:
    print("Weak password.Try Again")
    password = input("Enter password: ")
print("Password Accepted.")
