 # write a program to take password and check whether it contains @  and has atleast  8 character
p = input("Enter PASSWORD: ")
s = p.find("@")!=-1 and len(p)>=8 and len(p)!=-1
print(s)