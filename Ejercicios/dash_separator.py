# Separator
# This program receives a string and an integer positive number n. The program then returns the string but
# separated using dashes (-) every n characters.

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: September 28th 2019
# Last revision: September 29th 2019

def dash_separator(string, integer):
    x = '-'.join(string[i:i+integer] for i in range(0, len(string), integer))
    return(x)

string = input()
integer = int(input())

if integer <= 0:
    print('Error')

else:
    print(dash_separator(string, integer))