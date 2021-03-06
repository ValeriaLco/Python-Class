#Exercise 5
# This program receives two strings: a base string and a substring, and then calls a function that returns
# the number of times substring appears within base string.

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: September 27th 2019
# Last revision: September 27th 2019

def count_substring(string, substring):
    string = string.lower()
    substring = substring.lower()
    cont = 0
    for i in range(len(string)):
        if substring == string[i:i+len(substring)]:
            cont += 1
    return cont

string = input()
substring = input()
print('the substring', substring, 'is repeated', count_substring(string, substring), 'times')