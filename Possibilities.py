import random
import sys
import os

# you can't change tuple(кортеж) after it's been created!!!

pi_tuple = (3, 1, 4, 1, 5, 6)

new_list = list(pi_tuple)
new_list.append(1)
print(new_list)
new_tuple = tuple(new_list)
print(new_tuple)

print(len(new_tuple), min(new_tuple), max(new_tuple))