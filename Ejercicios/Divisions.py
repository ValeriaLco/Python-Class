def Division():
    points = 0
    questions = 0
    print('KANJAY MATH: Well a brief explanation, you will be given 5 problems, at the end, you will be told your score.')
    print('')
    print('¿Qué fracción del total es la mitad de una tercera cuarta parte?')
    questions += 1
    print('')
    print('1. (1/2)   2. (3/4)  3. (3/8) '.center(100))
    answer = input().strip()
    if answer == '3':
        points += 1
    else:
        points += 0
    print('')
    print('Calcular cuánto son dos tercios de tres quintas partes.')
    questions += 1
    print('')
    print('1. (1/15)   2. (3/25)  3. (2/5) '.center(100))
    answer = input().strip()
    if answer == '3':
        points += 1
    else:
        points += 0
    print('')
    print('Usamos tres quintas partes del agua de un depósito que sólo contiene tres octavas partes de su capacidad total.'
          ' Calcular la fracción de agua que hemos usado con respecto a la capacidad del depósito.')
    questions += 1
    print('')
    print('1. (9/40)   2. (3/25)  3. (3/5) '.center(100))
    answer = input().strip()
    if answer == '1':
        points += 1
    else:
        points += 0
    print('')
    print('Se reparte entre 4 personas el dos tercio de un batido. ¿Cuánto le corresponde a cada uno?')
    questions += 1
    print('')
    print('1. (1/6)   2. (1/3)  3. (3/5) '.center(100))
    answer = input().strip()
    if answer == '1':
        points += 1
    else:
        points += 0
    print('')
    print('Con dos números primos se forma una fracción que sumada con su inversa da 34/15. Cuál es la fracción que se'
          ' menciona?')
    questions += 1
    print('')
    print('1. (2/5)   2. (5/3)  3. (3/5) '.center(100))
    answer = input().strip()
    if answer == '2':
        points += 1
    else:
        points += 0
    print('')
    print('Your points are ', points, 'out of ', questions)
    sleep(5)
    
Division()