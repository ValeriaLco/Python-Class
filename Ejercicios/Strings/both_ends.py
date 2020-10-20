def both_ends(string):
    if len(string)<2:
        return ''
    x = string[:2]+string[-2:]
    return x

string = input()
print(both_ends(string))