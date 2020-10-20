#Exercise 1
def reverse_string(string):
    new_string = ' '
    for c in reversed(string):
        new_string += c
    return new_string

def reverse_string2(string):
    return ''.join(reversed(string))

def reverse_string3(string):
    return string[::-1]

string = input()
print(reverse_string(string))
print(reverse_string2(string))
print(reverse_string3(string))