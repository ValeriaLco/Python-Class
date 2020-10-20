#Exercise 2
# This program receives a string and a character c, then it returns the string but replacing all characters
# different from c with an asterisk.

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: September 27th 2019
# Last revision: September 27th 2019
def hide_characters(string, letter):
    for c in string:
        if c != letter:
            print('*', end='')
        else:
            print(c, end= '')

string = input()
letter = input()
hide_characters(string, letter)