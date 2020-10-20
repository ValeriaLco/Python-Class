import math
def cruzando_palabras(palabra1, palabra2):
    mitad1 = math.ceil(len(palabra1) / 2)
    mitad2 = math.ceil(len(palabra2) / 2)
    
    string1 = palabra1[:mitad1] + palabra2[mitad2:]
    string2 = palabra1[mitad1:] + palabra2[:mitad2]
    
    print(string1)
    print(string2)
    
string1 = input()
string2 = input()
cruzando_palabras(string1, string2)