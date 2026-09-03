#WAP to take a word and print it in reverse order using slicing.also check whether it is the same forward and backward
w = input("Enter a word:")
print(w)
a = w[::-1]
print(a)
if a==w:
    print("The backward word is same as forward")
else:
    print("The forward word is different from backword")    
    