  #WAP to check whteher a number is perfect number.A number is perfect if the sum of its proper divisors is equal to the number itself
a = int(input("Enter a number: "))
sum = 0
for i in range(1,a):
    if a%i == 0:
     sum = sum+i
if sum == a:
    print("Number is perfect.")
else:
    print("Number is not perfect.")