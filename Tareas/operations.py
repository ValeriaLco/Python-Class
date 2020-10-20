# operations.py

# This programs asks for three numbers (A, B, C) and shows the
# results of certain operations made with given numbers.

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: August 17th 2019
# Last revision: August 17th 2019

# I ask for the value of A, B and C
A = input()
B = input()
C = input()

# I then make the sum of all values and display the result
Sum = int(A) + int(B) + int(C)
print(Sum)

# Then the program computes the residue of the division A by C
Residue = int(A) % int(C)
print(Residue)

# Now the quotient of dividing A times B, by C
Quotient = (int(A) * int(B)) / int(C)
print(Quotient)

# Next the substraction of A from C, storing that result in a
# in a temp variable, and then showing the quotient of dividing
# C by that temp variable.
temp_variable = int(A) - int(C)
second_quotient = int(C) / int(temp_variable)
print(second_quotient)

# Finally the average of all three numbers
Average = float(Sum / 3)
print(Average)