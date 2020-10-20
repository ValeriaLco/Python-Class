#Exercise 3
# This program receives a string receives and then calls a function that returns the same
# string but with all the white spaces removed.

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: September 27th 2019
# Last revision: September 27th 2019

def remove_whites(string):
    return string.replace(' ', '')

string = input()
print(remove_whites(string))