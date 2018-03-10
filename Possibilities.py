import random
import sys
import os

grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                                     'Bananas'] # бакалейная лавка

print('First Item', grocery_list[0])
grocery_list[0] = 'Green Juice'
print(grocery_list[1:3]) # prints from 1 to 2 included

other_events = ['Wash Car', 'Pick Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]
print(to_do_list)

print((to_do_list[1][1])) # tomatoes

print(to_do_list)
grocery_list.append('Onions')
''' we added ONIONS
 to grocery_list but it also will
  appear int to_do_list'''
print(to_do_list)

grocery_list.insert(1, "Pickle")

grocery_list.remove("Pickle")

grocery_list.sort()

grocery_list.reverse()

del grocery_list[4]
print(to_do_list) # it refers to he grocery_list that's why it' also changing

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

'''
RESULTS

First Item Juice
['Tomatoes', 'Potatoes']
[['Wash Car', 'Pick Kids', 'Cash Check'], ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas']]
Tomatoes
[['Wash Car', 'Pick Kids', 'Cash Check'], ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas']]
[['Wash Car', 'Pick Kids', 'Cash Check'], ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas', 'Onions']]
[['Wash Car', 'Pick Kids', 'Cash Check'], ['Tomatoes', 'Potatoes', 'Onions', 'Green Juice']]
7
Wash Car
Cash Check

Process finished with exit code 0
'''