 #Write a python program to calculate simple Interest total amount using Principal,Rate, Time entered by the user 
P = float(input("Enter Principal : "))
R = float(input("Enter Rate : "))
T = float(input("Enter Time : "))

SI = (P * R * T) / 100
Amount = P + SI

print("Simple Interest =", SI)
print("Total Amount =", Amount)