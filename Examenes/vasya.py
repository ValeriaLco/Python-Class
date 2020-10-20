# vasya.py
# Valeria Lucio Rangel
# A01411381

def is_in_equilibrium():
    positive_n = int(input())
    Xi = Yi = Zi = 0
    for i in range(positive_n):
        x,y,z=map(int,input().split())
        Xi += x
        Yi += y
        Zi += z
    if(Xi == Yi == Zi == 0):
        print("YES")
    else:
        print("NO")

is_in_equilibrium()