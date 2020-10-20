# squared_bigger_than.py

# Your program must receive an integer number N,and then it must find the smallest integer n less than N that,
# when squared it is bigger than N (n2 > N).

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: September 9th 2019
# Last revision: September 9th 2019

n1 = int(input())
n2 = 0
if n1 < 0:
    print("E-R-R-O-R")
else:
    while n2**2 <= n1:
        n2 = n2 + 1
    print(n2)