# suma_N_cuadrados.py

# This programs asks the user for a number to set a range from 1 to "n", where it calculates the square of each
# number and at the end, shows the sum of all results.

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: September 11th 2019
# Last revision: September 11th 2019

# Fisrt I ask the user for a number to set a range
n = int(input())

# I set the sum value to 0 to then add all the results from the list.
sum = 0

# The program computes the squares and adds them to then show it.
for i in range(1, n+1):
    square = (i**2)
    sum = sum + square
    
print(sum)