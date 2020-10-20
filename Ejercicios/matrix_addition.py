matriz1 = []
while True:
    data = input().strip()
    if data == '':
        break
    matriz1.append(list(map(int,data.split())))
    
matriz2 = []
while True:
    data = input().strip()
    if data == '':
        break
    matriz2.append(list(map(int,data.split())))
    
if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
    matriz3 =[]
    for r in range(len(matriz1)):
        row = []
        for c in range(len(matriz1[0])):
            row.append(matriz1[r][c] + matriz2[r][c])
        matriz3.append(row)
    print(matriz3)
else:
    print("Matrices have not the same size")
