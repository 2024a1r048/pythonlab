 #WAP to input a number and check whether it is prime or not.
num = int(input("Enter a number: "))

if num <= 1:
    print("Number is not a prime.")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Number is not a prime.")
            break
    else:
        print("Number is prime.")

