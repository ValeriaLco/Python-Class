#Exercise 1
# This program receives a a string and then calls a function that returns the same string but in reverse order.
# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: September 27th 2019
# Last revision: September 27th 2019

def reverse_string(string):
    new_string = ' '
    for c in reversed(string):
        new_string += c
    return new_string

string = input()
print(reverse_string(string))