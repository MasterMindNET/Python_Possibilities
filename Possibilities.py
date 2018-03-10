import random
import sys
import os

# if else elif == != > >= <=

age = 18

if age >= 16:
    print('you`re old enough to drive')
else:
    print('you`re not old enough to drive')

if age >= 21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print('You are not ol enough to drive')

if(age >= 1) and (age <= 18):
    print('You get a birthday')
elif (age == 21) or (age >= 65):
    print("You get a birthday")
elif age == 30:
    print("you don't get a birthday")
else:
    print("You get a birthday yeah")

'''
you`re old enough to drive
You are old enough to drive a car
You get a birthday

Process finished with exit code 0
'''