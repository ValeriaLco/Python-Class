# promedio_decision.py

# This program gets the average of given numbers and breaks when the user gives a negative number

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: September 12th 2019
# Last revision: September 12th 2019

add = 0
number = 0

while True:
    values = float(input())
    if values >= 0:
        add += values
        number += 1
    else:
        break
    
print(add/number)
