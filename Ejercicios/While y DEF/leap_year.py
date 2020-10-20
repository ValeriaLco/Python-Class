# leap_year.py
#
# This program takes a year and determines if it is a leap year. A leap year is any year that is divisible by 4,
# except when this year is also divisible by 100. However, if this year is divisible by 400, then it is a leap year.
#
# Written by Valeria Lucio Rangel (a01411381@itesm.mx)
# Date: August 30th, 2019
# Last revision: August 30th, 2019

def is_a_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

given_year = int(input())
print(is_a_leap_year(given_year))