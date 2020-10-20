a = int(input("give me a number: "))
b = int(input("give me a number: "))

i = a
while i <= b:
   if i % 2 == 0:
       print(i)
       i += 2
       continue 
   i += 1