 #WAP to input a number and reverse it using arithmetic operaions only.
a = int(input("Enter a number: "))
reverse = 0
while a>0:
    digits = a%10
    reverse = (reverse*10)+digits
    a = a//10
print(reverse)