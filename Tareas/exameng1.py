def process_string(phrase):
    mayúsculas=0
    minúsculas=0
    números=0
    espacios=0
    especiales=0
    for x in range(len(phrase)):
        if phrase[x] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            mayúsculas+=1
        elif phrase[x] in "abcdefghijklmnopqrstuvwxyz":
            minúsculas+=1
        elif phrase[x] in "1234567890":
            números+=1
        elif phrase[x] in " ":
            espacios+=1
        else:
            especiales+=1
    print(mayúsculas)
    print(minúsculas)
    print(números)
    print(espacios)
    print(especiales)

def average():
    cont=0
    suma=0
    sumapositivos=0
    contpositivos=0
    sumanegativos=0
    contnegativos=0
    while True:
        num= int(input())
        if num==0:
            break
        if num!=0:
            cont+=1
            suma+=num
        if num>0:
            contpositivos+=1
            sumapositivos+=num
        if num<0:
            contnegativos+=1
            sumanegativos+=num
            
    print(suma/cont)
    print(sumapositivos/contpositivos)
    print(sumanegativos/contnegativos)
         
number= int(input())
if number==1:
    phrase= input()
    (process_string(phrase))
elif number==2:
    (average())
else:
    print("ERROR")