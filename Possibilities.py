import random
import sys
import os


'''
URL(https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w)

r for reading
r+ opens for reading and writing (cannot truncate a file)
w for writing
w+ for writing and reading (can truncate a file)
rb for reading a binary file. The file pointer is placed at the beginning of the file.
rb+ reading or writing a binary file
wb+ writing a binary file
a+ opens for appending
ab+ Opens a file for both appending and reading in binary. The file pointer is at the end of the file if the file exists. The file opens in the append mode.
x open for exclusive creation, failing if the file already exists (Python 3)
'''


test_file = open('test.txt', 'ab+')  # wb

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("Write me to the file\n", 'UTF-8'))

test_file.close()

test_file = open('test.txt', 'r+')

text_in_file = test_file.read()
print(text_in_file)

#os.remove('test.txt')


