#write a python program to take total minutes as input and convert it into hours and remaining minutes

import os
a = int(input("enter time in minutes: "))
hours = a // 60
minutes = a % 60
print("time in hours: ",hours)
print("time in minutes: ",minutes)