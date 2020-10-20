# golden_ratio.py

# This programs calculates the value oh phi, multiplies it by a given value "f" and
# rounds up to a given value "k" precision decimal places.

# Written by Valeria Lucio
# a01411381@itesm.mx

# Date: August 21th 2019
# Last revision: August 21th 2019

from decimal import Decimal
from math import sqrt

# I frist compute the value of phi by the formula given in the instructions.
φ = (1 + (sqrt(5)))/2

# First I ask the user for the value "f" that will be multiplied by phi.
f = float(input())

# Then I ask for the number of decimal places the user would like to round up to.
k = int(input())
if k < 0:
    print ('ERROR')

else:
    x = Decimal(f * φ)
    output = round(x,k)
    print(output)