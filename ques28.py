 #WAP to take a wordnand count the number of vowels a,e,i,o,u#
word = input("Enter a word: ")

count = 0
for i in word:
    if i in "aeiou":
        count += 1
print("Number of vowels =", count)