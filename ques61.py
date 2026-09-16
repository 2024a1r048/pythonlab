 #WAP tp print an inverted right-angled triangle using stars.
"""
****
***
**
*
"""
n = int(input("Enter n: "))

for i in range(n, 0, -1):
    print("*" * i)