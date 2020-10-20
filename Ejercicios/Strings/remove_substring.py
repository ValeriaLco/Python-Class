#Exercise 4
# This program receives two strings: a base string and a substring, and then calls a function that returns
# the same base string but without any occurrence of the substring.

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: September 27th 2019
# Last revision: September 27th 2019

def delete_substring(string, substring):
    return string.replace(substring, '')

string = input()
substring = input()
print(delete_substring(string, substring))