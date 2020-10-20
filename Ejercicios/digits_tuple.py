n= input()
lista=[]
for i in n:
    if i in "1234567890":
        lista.append(int(i))

tupla = tuple(lista)

print(tupla)