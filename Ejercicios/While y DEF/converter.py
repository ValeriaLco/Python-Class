# converter.py

# This programs asks for three numbers (A, B, C) and shows the
# results of certain operations made with given numbers.

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: August 29th 2019
# Last revision: August 29th 2019

# Fisrt I define the functions that will compute the values given in feet, inches and yards
# and return them into the measure in centimeters
def feets(value1):
    ft = 30.48
    return value1 * ft

def inches(value2):
    inch = 2.54
    return value2 * inch

def yards(value3):
    yd = 91.44
    return value3 * yd

# Then the program asks the user for the type of unit requested and then the measure to convert.
unit = (int(input()))
lenght = float(input())

# Then I add some conditions to run the program and compute correctly the values.
# If the user enters a value smaller or equal to 0 then the program will print ERROR.
if lenght<=0:
    print("ERROR")
elif unit==1:
    print(feets(lenght))
elif unit==2:
    print(inches(lenght))
elif unit==3:
    print(yards(lenght))
else:
    print("ERROR")