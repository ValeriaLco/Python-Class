# type_triangle.py

# This programs tells you the type of triangle you have based on given lenghts. It validates the lenghts and if they
# are not, the program tells the user so.

# Written by Valeria Lucio
# a01411381@itesm.mx

# Date: August 23th 2019
# Last revision: August 23th 2019

# I first ask the user for sides X, Y and Z.
X = abs(int(input('Give me the distance of side "X": ')))
Y = abs(int(input('Give me the distance of side "Y": ')))
Z = abs(int(input('Give me the distance of side "Z": ')))

# The program checks the values received.
if X == 0 or Y == 0 or Z == 0:
    print('Values are invalid')
# It also checks if the sum of 2 sides is greater than the third.
else:
    if not((X + Y) > Z and (X + Z) > Y and (Z + Y) > X):
        print('Values are invalid')
# After checking that the values are valid, the program tells the type of triangle the user has.
    else:
        if (X==Y==Z):
            print('Your triangle is equilateral')
        if ((X==Y) and Z!=X) or ((X==Z) and Y!=X) or ((Y==Z) and X!=Y):
            print('Your triangle is isosceles')
        if (X!=Y and Y!=Z and X!=Z):
            print('Your triangle is scalene')
