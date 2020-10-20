#Exercise 6
# This program receives ta string and then calls a function that returns True if such string is a palindrome,
# or False otherwise. 

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: September 27th 2019
# Last revision: September 27th 2019

def is_palindrome(string):
    clean_string = string.lower().replace(' ','')
    return clean_string == ''.join(reversed(clean_string))

string = input()
print(is_palindrome(string))