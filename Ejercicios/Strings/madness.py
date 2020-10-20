# madness.py

def madness(string):
    new_string = ''
    for i in string:
        if i == 'e' or i == 'E' or i == 'é' or i == 'É' or i == 'è' or i == 'È' or i == 'ë' or i == 'Ë' or i == 'ê' or i == 'Ê':
            new_string += '3'
        elif i == 'a' or i == 'A' or i == 'á' or i == 'Á' or i == 'à' or i == 'À' or i == 'ä' or i == 'Ä' or i == 'â' or i == 'Â':
            new_string += '4'
        elif i == 'o' or i == 'O' or i == 'ó' or i == 'Ó' or i == 'ò' or i == 'Ò' or i == 'ö' or i == 'Ö' or i == 'ô' or i == 'Ô':
            new_string += 'h'
        else:
            new_string += i
    return new_string

string = input()
print(madness(string))