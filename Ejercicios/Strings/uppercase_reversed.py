# uppercase_reversed.py

# Write a Python program (name it uppercase_reversed.py) that has a function. This function must receive a string
# and it must return the same string but reversed (beginning with the last character and ending with the first one),
# and all characters in uppercase

def new_string(string):
    return string[::-1]

string = input()
string = string.upper()
print(new_string(string))