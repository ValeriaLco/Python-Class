# promedio_sencillo.py

# This programs asks the user for a number of values to average and then asks for the values. Finally it prints
# the average.

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: September 11th 2019
# Last revision: September 11th 2019

n_values = int(input())

def n_v_to_average (n_values):
    add = 0
    for i in range(1, n_values + 1):
        numbers = abs(float(input()))
        add+=numbers
    return add

def average(add, n_values):
    return(add / n_values)

add = (n_v_to_average(n_values))
result = (average(add, n_values))

print(result)