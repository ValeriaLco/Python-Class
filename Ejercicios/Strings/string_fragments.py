#string_fragments.py

# This is a program that reads a string and shows fragments of such string.


def string_fragments(string):
    print(len(string))
    print(string[0])
    print(string[-1])
    
    for index in range(len(string)):
        if index % 2 != 0:
            print(string[index], end='')

    
string = input()
string_fragments(string)