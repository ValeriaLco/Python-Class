def rango_pares(li, ls):
    pares = False
    
    for i in range(li,ls):
        if i % 2 == 0:
            print(i)
            pares = True
    if not pares:
        print('No hay pares')
        
a = int(input())
b = int(input())

if a < b:
    rango_pares(a,b)
else:
    rango_pares(b,a)