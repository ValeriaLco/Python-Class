# loops.py
# Partial Exam 2 (second try)
import sys
import math
from statistics import mean

def delete_char_at_pos(string, num):
    for i in string:
        if len(i) > num[0]:
            new_string= i[:num[0]]+ i[num[0+1]:]
            return new_string
        else:
            return string
    
def string_stats(string):
    number_vowels = 0
    number_consonants = 0
    number_spaces = 0
    special = 0
    for i in range(len(string)):
        if string[i] in 'aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛ':
            number_vowels = number_vowels+1
        elif string[i] == ' ':
            number_spaces = number_spaces+1
        elif string[i] == '!"·$%&/()=?¿*^¨çÇ_:;><,.-ç´+}{][¡ºª':
            special = special+1
        else:
            number_consonants = number_consonants+1
    upper = sum(letter.isupper() for letter in string)
    lower = sum(letter.islower() for letter in string)

    return((len(string)), number_vowels, number_consonants, number_spaces, upper, lower, special)

list_strings = []
list_nums = []
a = ''
while True:
    string = (input()).strip()
    if string.lower() == 'exit':
        break
    list_strings.append(string)
    try:
        number = input()
        number_2 = abs(int(math.floor(float(number))))
        a += number
        list_nums.append(number_2)
    except:
        list_strings.append(a)
        continue
    
lenght, vowels, consonants, spaces, uppercase, lowercase, others = string_stats(len(string), number_vowels, number_consonants, number_spaces, upper, lower, special)
total_lenght += lenght
total_vowels += vowels
total_consonants += consonants
total_spaces += spaces
total_uppercase += uppercase
total_lowercase += lowercase
total_others += others
print(total_lenght)
print(total_vowels)
print(total_consonants)
print(total_spaces)
print(total_uppercase)
print(total_lowercase)
print(total_others)