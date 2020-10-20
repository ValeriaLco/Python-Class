# diagonal.py

# This programs calculates the value of the diagonal of any rectangle.

# Written by Valeria Lucio
# a01411381@itesm.mx

# Date: August 21th 2019
# Last revision: August 21th 2019

import math

# First I ask the user for the lenght and the width of the rectangle.
l = float(input())
w = float(input())

# I then ask the program to give only absolute values.
a = (abs(l))
b = (abs(w))

# Then I evaluate both sides to mark as error if any of the values is 0.
if w == 0 or l == 0:
    print('ERROR')

# If there is no error found, the program gets the value of C.
else:
    c = (math.sqrt((a)**2 + (b)**2))
    print(c)
