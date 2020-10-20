# uppercase_vowels.py

def uppercase_vowels(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] in 'aeiouáéíóú':
            new_string += string[i].upper()
        else:
            new_string += string[i]
    print(new_string)
    
string = input()
uppercase_vowels(string)