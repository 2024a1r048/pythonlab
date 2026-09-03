 # 5. Take a password and check length, presence of @, and whether first and last characters are different.
password = input("Enter Password: ")

print("Length >= 8:", len(password) >= 8)
print("Contains @:", "@" in password)
print("First and last different:", password[0] != password[-1])
