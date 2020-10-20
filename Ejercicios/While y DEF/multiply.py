while True:
    n = int(input('Give me a number: '))
    r = int(input('Tell me the rows: '))
    
    if n == 0:
        break
    
    for i in range (1, r+1):
        print(n, 'x', i, '=', n*i)