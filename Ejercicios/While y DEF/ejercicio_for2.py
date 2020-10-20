n = int(input('Give me a number: '))
salida = ' '

for i in range(1, n):
    salida = salida + str(i) + ','
    
for i in range(n, 1, -1):
    salida = salida + str(i) + ','

salida += '1'

print(salida)