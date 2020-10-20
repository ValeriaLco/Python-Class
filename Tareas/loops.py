# loops.py

# This program checks for valid password has: 1 uppercase, 1 lowercase, 1 number, no spaces, one special character,
# 8 characters long, no
# more than 20.


def valid_password (password):
    if (len(password)<8 or len(password)>20):
        print(False)
    
    else:
        uppercase=0
        lowercase=0
        number=0
        zero_spaces=0
        valid_sc=0
        other_sc=0
        for i in range(len(password)):
            if password[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                uppercase+=1
            elif password[i] in 'abcdefghijklmnopqrstuvwxyz':
                lowercase+=1
            elif password[i] in '1234567890':
                number+=1
            elif password[i] in ' ':
                zero_spaces+=1
            elif password[i] in '#$%&()-_.,;:~[]{}^@':
                valid_sc+=1
            else:
                other_sc+=1
        if (uppercase > 0) and (lowercase > 0) and (number > 0) and (zero_spaces == 0) and (valid_sc > 0) and (other_sc == 0):
            print(True)
    

def no_parameters(values):
    add = 0
    av_num = 0
    while True:
        values = float(input())
        if values == 0:
            add += values
            av_num += 1
        else:
            break
    
print(add / av_num)
    
    
    
number = int(input())
if number == 1:
    password = str(input())
    print(valid_password(password))
    
elif number == 2:
    values = float(input())
    print(no_parameters(values))
    
else:
    print('ERROR')