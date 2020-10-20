# exercise1.py

# This programs calculates the area of a triangle given the lenght of each side.

# Written by Valeria Lucio and Manuel Hernández
# a01411381@itesm.mx and a01411514@itesm.mx

# Date: August 20th 2019
# Last revision: August 20th 2019

# Import math
import math
from math import sqrt

# I first ask the user for the value of the three sides.
a = int(input('Please give the value of side "a"'))
b = int(input('Please give the value of side "b"'))
c = int(input('Please give the value of side "c"'))

# Then I calculate the value of "s" to then get the area.
s = ((a + b + c) / 2)

# Then I calculate the area
try:
    Area = sqrt(s*(s - a)*(s - b)*(s - c))
except:
    print('There is no triangle with those lenghts')

    
Area = sqrt(s*(s - a)*(s - b)*(s - c))
print('The area of your triangle is', Area)
