import random
import sys
import os


def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum


string = addNumber(1, 4)
print(addNumber(1, 4))


# name = sys.stdin.readline() # user input

#print('Hello', name)


long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])

print(long_string[-5:])

print(long_string[:-5]) # I'll catch you if you fall - The

print(long_string[:4] + ' be there')

print("%c is my %s letter and my number %d is %.5f" %
      ('X', 'favorite' , 1, .14))

print(long_string.capitalize())

print(long_string.find("Floor")) # case sensitive

print(long_string.isalpha())

print(long_string.isalnum())

print(len(long_string))

print(long_string.replace("Floor", "Ground"))

print(long_string.strip())

quote_list = long_string.split(" ")

print(quote_list)