#write a python program to take an amount in rupees and calculate how many rs 500 and rs 100 notes are needed

a = int(input("Amount in rupees: "))
notes_500 = a // 500
remaining = a % 500
notes_100 = remaining // 100
print("Notes of 500: ",notes_500)
print("Notes of 100: ",notes_100)