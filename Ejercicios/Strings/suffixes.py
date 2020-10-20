#madness.py

def new_string(string):
    suffix= "ing"
    a="ly"
    string_2= string+suffix
    if suffix in string :
        string_2=string+a
    return string_2
    
string= input()
print(new_string(string))
