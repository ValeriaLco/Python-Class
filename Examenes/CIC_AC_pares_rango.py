def pair_numbers (n1, n2):
    
    for i in range(n1, n2):
        if i % 2 == 0:
            print(i)
        
       
n1 = abs(int(input()))
n2 = abs(int(input()))

if n1 == n2:
    print ("No hay pares")

if n1 > n2:
    pair_numbers(n2, n1)
    
else:
    pair_numbers(n1, n2)