 # write a program  to take input from user  without  typecasting and multiply it by 3. Then  type cate the same input
# to int and multiply it by 3 . And print the result to show difference  bw both
a = (input("enter a number:"))
result = a*3
print("Without typecasting:",result)
a = int(a)
a = a*3
print("With Typecasting:",a)