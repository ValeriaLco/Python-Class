# LearningBlast.py

# This program has 6 game options, 4 for math, 2 for science and one challenge that has 4 questions related to both areas.

import random
from time import sleep

#This function when called, displays the main menu and shows the user the options available.
def Display_Menu():
    print('')
    print('KANJAY MATH: Remember to only introduce the number of your selection')
    print('')
    print('--------------------------------------------------------------------------'.center(100))
    print('1. Math'.center(100))
    print('2. Science'.center(100))
    print('3. Mortal Kombat'.center(100))
    print('')
    print('*If you would like to exit game, please enter 0 *'.center(100))
    print('--------------------------------------------------------------------------'.center(100))
    Users_Selection()

# In this function the program analizes the users selection and proceeds to send the user to the new section depending on the number
# the user selected, if the user selects an option that is not available, the program will ask for a valid option.
def Users_Selection():
    while True:
        selection = input().strip()
        if selection == '1':
            Math_Menu()
        elif selection == '2':
            Science_Menu()
        elif selection == '3':
            Mortal_KO_Menu()
        elif selection == '0':
            print('KANJAY MATH: Thank you for playing little Einstein, see you soon')
            break
        elif selection == '300311':
            Additional_Content()
        else:
            print("KANJAY MATH: Young Padawan, choose a number from 0 to 3, it's not that hard")
            continue

# This function displays the Math Menu in which the user will be able to select a game about any topic of their preference.
def Math_Menu():
    print('KANJAY MATH: Well, you know what to do, select an option')
    print('')
    print('-------------------------------------------------------------------'.center(100))
    print('1. Addition'.center(100))
    print('2. Subtraction'.center(100))
    print('3. Multiplication'.center(100))
    print('4. Division'.center(100))
    print('')
    print('0. Return to Main Menu'.center(100))
    print('-------------------------------------------------------------------'.center(100))
    Math_Selection()

# This function analyzes the users selection and starts the game of the users choice, if the user selects 0, it will send him/her to
# the main menu again. If the user selects any other choice, the program will ask for a valid choice.
def Math_Selection():
    while True:
        selection = input().strip()
        if selection == '1':
            Addition()
        elif selection == '2':
            Subtraction()
        elif selection == '3':
            Multiplication()
        elif selection == '4':
            Division()
        elif selection == '0':
            Display_Menu()
        else:
            print("KANJAY MATH: Yo bro, choose from 0 to 5, not THAT difficult.")
            continue

# This function starts the addition game, it prints an operation with 2 random numbers selected on a range of 0 to 5. For every right
# answer, the program will keep a score. If the user makes 5 mistakes is game over. After finishing the game, the program will print 
# the score and ask the user if he/she wants to play again. The function will also print words depending on the answer the user puts.
# If so, the game will begin again, on the contrary, it will send the user to the math menu.
def Addition():
    print('KANJAY MATH: Well a brief explanation, you have 5 lives only, you mess one operation, you loose one life. '
          'When you get to 0 lives, is Game Over for you pal. If you get 5 points correct, difficulty will go up '
          'every operation from that point forward. ')
    sleep(6)
    points = 0
    lives = 5
    y = 10
    questions = 0
    while True:
        questions += 1
        number = [random.randint(0,y), random.randint(0,y)]
        question = print(number[0], '+' ,number[1], '=')
        operation = number[0] + number[1]
        answer = float(input())
        words = ('Great!', 'Excellent!', 'Terrific!', 'W.O.W!', 'Nice!', 'Super!')
        if answer == operation:
            print(random.choice(words))
            points += 1
            if points >= 5:
                print('')
                print('LEVEL UP!'.center(100))
                print('')
                y += 10
            if questions == 20:
                print('You got ', points, 'out of', questions)
                print('KANJAY MATH: Wanna go again?')
                print('1. Yes       2. No'.center(100))
                while True:
                    response = input().strip()
                    if response == '1':
                        Addition()
                    elif response == '2':
                        Math_Menu()
                    else:
                        print('KANJAY MATH: Dude, select 1 or 2')
                        continue
        else:
            print('Check your numbers!')
            lives = lives - 1
            if lives == 0:
                print('You got ', points, 'out of', questions)
                print('')
                sleep(2)
                print('KANJAY MATH: Sorry pal, no more lives left. Wanna play again?')
                print(' ')
                print('1. Yes       2. No'.center(100))
                while True:
                    response = input().strip()
                    if response == '1':
                        Addition()
                    elif response == '2':
                        Math_Menu()
                    else:
                        print('KANJAY MATH: Dude, select 1 or 2, REALLY NOT that hard')
                        continue
            else:
                continue

# This function starts the subtraction game, it prints an operation with 2 random numbers selected on a range of 0 to 5. For every right
# answer, the program will keep a score. If the user makes 5 mistakes is game over. After finishing the game, the program will  print 
# the score and ask the user if he/she wants to play again. The function will also print words depending on the answer the user puts.
# If so, the game will begin again, on the contrary, it will send the user
# to the math menu.
def Subtraction():
    print('KANJAY MATH: Well a brief explanation, you have 5 lives only, you mess one operation, you loose one life. '
          'When you get to 0 lives, is Game Over for you pal. If you get 5 points correct, difficulty will go up '
          'every operation from that point forward. ')
    sleep(6)
    points = 0
    lives = 5
    y = 10
    questions = 0
    while True:
        questions += 1
        number = [random.randint(0,y), random.randint(0,y)]
        question = print(number[0], '-' ,number[1], '=')
        operation = number[0] - number[1]
        answer = float(input())
        words = ('Great!', 'Excellent!', 'Terrific!', 'W.O.W!', 'Nice!', 'Super!')
        if answer == operation:
            print(random.choice(words))
            points += 1
            if points >= 7:
                print('')
                print('LEVEL UP!'.center(100))
                print('')
                y += 5
            if questions == 20:
                print('You got ', points, 'out of', questions)
                print('KANJAY MATH: Wanna go again?')
                print('1. Yes       2. No'.center(100))
                while True:
                    response = input().strip()
                    if response == '1':
                        Addition()
                    elif response == '2':
                        Math_Menu()
                    else:
                        print('KANJAY MATH: Dude, select 1 or 2')
                        continue
        else:
            print('Try harder!')
            lives = lives - 1
            if lives == 0:
                print('You got ', points, 'out of', questions)
                print('')
                sleep(2)
                print("KANJAY MATH: Maybe you'll get better with practice. Try again?")
                print(' ')
                print('1. Yes       2. No'.center(100))
                while True:
                    response = input().strip()
                    if response == '1':
                        Subtraction()
                    elif response == '2':
                        Math_Menu()
                    else:
                        print("KANJAY MATH: C'mon, select 1 or 2, O-N-E OR T-W-O")
                        continue
            else:
                continue

# This function starts the muliplication game, it prints an operation with 2 random numbers selected on a range of 0 to 5. For every 
# right answer, the program will keep a score. If the user makes 5 mistakes is game over. After finishing the game, the program will 
# print the score and ask the  user if he/she wants to play again. The function will also print words depending on the answer the
# user puts. If so, the game will begin again, on the contrary, it will send the user
# to the math menu.
def Multiplication():
    print('KANJAY MATH: Well a brief explanation, you have 5 lives only, you mess one operation, you loose one life. '
          'When you get to 0 lives, is Game Over for you pal. If you get 5 points correct, difficulty will go up '
          'every operation from that point forward. ')
    sleep(6)
    points = 0
    lives = 5
    y = 10
    questions = 0
    while True:
        questions += 1
        number = [random.randint(0,y), random.randint(0,y)]
        question = print(number[0], 'x' ,number[1], '=')
        operation = number[0] * number[1]
        answer = float(input())
        words = ('Great!', 'Excellent!', 'Terrific!', 'W.O.W!', 'Nice!', 'Super!')
        if answer == operation:
            print(random.choice(words))
            points += 1
            if points >= 7:
                print('')
                print('LEVEL UP!'.center(100))
                print('')
                y += 2
            if questions == 20:
                print('You got ', points, 'out of', questions)
                print('KANJAY MATH: Wanna go again?')
                print('1. Yes       2. No'.center(100))
                while True:
                    response = input().strip()
                    if response == '1':
                        Addition()
                    elif response == '2':
                        Math_Menu()
                    else:
                        print('KANJAY MATH: Dude, select 1 or 2')
                        continue
        else:
            print('Oops, try harder!')
            lives = lives - 1
            if lives == 0:
                print('You got ', points, 'out of', questions)
                print('')
                sleep(2)
                print("KANJAY MATH: Not everyone is great at first, wanna give it a second chance?")
                print(' ')
                print('1. Yes       2. No'.center(100))
                while True:
                    response = input().strip()
                    if response == '1':
                        Multiplication()
                    elif response == '2':
                        Math_Menu()
                    else:
                        print('KANJAY MATH: Again, 1 equals "Yes, do it again" and 2 means "I DONT WANNA PLAY"')
                        continue
            else:
                continue

# This function starts the division game in which 5 questions are displayed one by one. Any number that is not between 1,2 or 3 is
# taken as a wrong answer. For every right answer, the program keeps a score. After the user answers the 5 questions, the program will
# display the score and ask if the user wants to play again. If so, the game will begin again, on the contrary, it will send the user
# to the math menu.
def Division():
    points = 0
    questions = 0
    print('KANJAY MATH: Well a brief explanation, you will be given 5 problems, at the end, you will be told your score. WARNING: '
          ' any other number different than 1, 2 or 3 will automatically be taken as a mistake.')
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
    print('KANJAY MATH: Wanna play again?')
    print(' ')
    print('1. Yes       2. No'.center(100))
    while True:
        response = input().strip()
        if response == '1':
            Division()
        elif response == '2':
            Math_Menu()
        else:
            print('KANJAY MATH: Again, 1 equals "Yes, do it again" and 2 means "I DONT WANNA PLAY"')
            continue

    
# This function displays the Science Menu in which the user can see all the options to play.
def Science_Menu():
    print('-------------------------------------------------------------------')
    print('KANJAY MATH: Tell me what you want to learn today')
    print('1. Biology')
    print('2. Chemistry')
    print('')
    print('0. Return to Main Menu')
    print('-------------------------------------------------------------------')
    Science_Selection()
   
# This function analyzes the user's choice and depending on the selection it starts either the Biology game, the Chemistry game or
# take the user to the main menu. If the user selects any other number, the program asks for a valid choice.
def Science_Selection():
    while True:
        selection = input().strip()
        if selection == '1':
            Biology()
        elif selection == '2':
            Chemistry()
        elif selection == '0':
            Display_Menu()
        else:
            print("KANJAY MATH: Okay, don't be nervous, you can do it, just choose a number, 0, 1, 2 or 3.")
            continue

# This game displays 6 questions one by one, for every right answer, the program keeps a score. The Bonus question is worth 2 points,
# at the end the program displays the score and then takes the user to the science menu.
def Biology():
    print('')
    points = 0
    questions = 0
    print('KANJAY MATH: Well, this game has no lives, it has 5 biology questions worth 1 point and one Bonus question '
          'that will give you 2 points. Oh and for the record, ANY number that is not 1, 2 or 3 will be taken wrong'
          ' so please take that into account. For your understanding, questions are on spanish.')
    sleep(3)
    print('')
    print('¿Quién propuso la teoría evolutiva biológica?')
    questions += 1
    print('')
    print('1. Thomas Edison   2. Robespierre  3. Charles Darwin'.center(100))
    answer = input().strip()
    if answer == '3':
        points += 1
    else:
        points += 0
    print('')
    print('¿Qué significa ADN?')
    questions += 1
    print('')
    print('1. Ácido Denso Normal   2. Ácido Desoxirribonucleico   3. Ácido Ribonucleico'.center(100))
    answer = input().strip()
    if answer == '2':
        points += 1
    else:
        points += 0
    print('')
    print('¿División celular en la que se forman dos células idénticas?')
    questions += 1
    print('')
    print('1. Mitosis   2. Meiosis  3. Celulosis'.center(100))
    answer = input().strip()
    if answer == '1':
        points += 1
    else:
        points += 0
    print('')
    print('¿Qué tipos de reproducción existen?')
    questions += 1
    print('')
    print('1. Sexual y Asexual   2. Vegetal y Animal  3. Celular y Respiratoria'.center(100))
    answer = input().strip()
    if answer == '1':
        points += 1
    else:
        points += 0
    print('')
    print('¿Cuál es la unidad fundamental de la vida?')
    questions += 1
    print('')
    print('1. El agua   2. El oxígeno  3. La célula'.center(100))
    answer = input().strip()
    if answer == '3':
        points += 1
    else:
        points += 0
    print('')
    print('BONUS QUESTION')
    print('¿Quién es el mejor neurocirujano en la historia de las novelas?')
    questions += 1
    print('')
    print('1. Dr. Drake Ramoray  2. Dr. Regina Phallange  3. Dr. Christina Yang')
    answer = input().strip()
    if answer == '1':
        points += 2
    else:
        points += 0
    print('')
    print('Your points are ', points, 'out of ', questions)
    sleep(5)
    Science_Menu()

# This game displays 6 questions one by one, for every right answer, the program keeps a score. The Bonus question is worth 2 points,
# at the end the program displays the score and then takes the user to the science menu.
def Chemistry():
    points = 0
    questions = 0
    print('')
    print('KANJAY MATH: Well, this game has no lives, it has 5 chemistry questions worth 1 point and one Bonus question '
          'that will give you 2 points. Oh and for the record, ANY number that is not 1, 2 or 3 will be taken wrong'
          'so please take that into account. For your understanding, questions are on spanish.')
    sleep(3)
    print('')
    print('¿Cómo se llama el cambio de estado de gaseoso a líquido?')
    questions += 1
    print('')
    print('1. Evaporación   2. Enfriación  3. Condesación'.center(100))
    answer = input().strip()
    if answer == '3':
        points += 1
    else:
        points += 0
    print('')
    print('¿Cuál es la formula química del agua?')
    questions += 1
    print('')
    print('1. OH   2. H20  3. CH3'.center(100))
    answer = input().strip()
    if answer == '2':
        points += 1
    else:
        points += 0
    print('')
    print('¿Quién descubrió la radiación?')
    questions += 1
    print('')
    print('1. Henri Becquerel   2. Marie Curie  3. Lavoisier'.center(100))
    answer = input().strip()
    if answer == '1':
        points += 1
    else:
        points += 0
    print('')
    print('¿Cuál es el elemento mas electronegativo?')
    questions += 1
    print('')
    print('1. Fluor   2. Oro  3. Plomo'.center(100))
    answer = input().strip()
    if answer == '1':
        points += 1
    else:
        points += 0
    print('')
    print('¿Cuál es el símbolo químico de la plata?')
    questions += 1
    print('')
    print('1. Pt   2. Li  3. Ag'.center(100))
    answer = input().strip()
    if answer == '3':
        points += 1
    else:
        points += 0
    print('')
    print('BONUS QUESTION')
    print('¿Cuál genio de la química inventó la metanfetamina azul?')
    questions += 1
    print('')
    print('1. PINKMAN  2. HEISENBERG  3. FRING')
    answer = input().strip()
    if answer == '2':
        points += 2
    else:
        points += 0
    print('')
    print('Your points are ', points, 'out of ', questions)
    sleep(4)
    Science_Menu()

# This function is for additional content, it shows a "conversation" with the narrator. After conversation ends, the function takes
# the user to the main menu.
def Additional_Content():
    print(' ')
    print("LOADING", end='')
    sleep(1)
    print(".", end='')
    sleep(1)
    print(".", end='')
    sleep(1)
    print(".", end='')
    sleep(1)
    print('')
    print('')
    print('KANJAY MATH: Oh, hi there, looks like someone unlocked something. What is your name?')
    print('')
    name = str(input())
    print('')
    print('KANJAY MATH: Hi there ', name, ', how old are you?')
    print('')
    age = float(input())
    print('')
    print('KANJAY MATH: Well look at that, little ', name, ' is not so little. Wow, ', age, 'years old.')
    sleep(5)
    print('')
    print('KANJAY MATH: You know, the programmers started developing the game 2 days before due date. They finished it one class '
          'before Computational Thinking.')
    print('')
    sleep(5)
    print('KANJAY MATH: Have you ever listened to my music? Spotify misspelled my name, they call me "Kanye West,",'
          ' I mean, who writes that name? I recommend you my tune "Gold Digger"')
    sleep(5)
    print('')
    print('KANJAY MATH: Well, see you later ', name, '!')
    sleep(5)
    Display_Menu()

# This function asks the user if he/she wants to take the challende, if the user selects 1, Mortal Kombat starts, if user selects 2
# the function takes the user back to main menu. Any other option the game asks for another valid choice. The function keeps a score.
def Mortal_KO_Menu():
    print('LORD VALDOMERO: So we meet again "Mr. KnowItAll", seems like you believe you can pass my test. Very well, '
          'do you accept my challenge?')
    print('')
    print('Choose "1" for "YES I CAN BEAT YOU", and "2" for "Maybe I need more study :("')
    print('')
    while True:
        C_Answer = input('KANJAY MATH: So, what will it be? ').strip()
        if C_Answer == '1':
            print('LORD VALDOMERO: If you say so, let us begin...')
            sleep(2)
            Mortal_Kombat()
        elif C_Answer == '2':
            print("LORD VALDOMERO: HA! Poor little thing, go study more you bastard, don't bother me until you are "
                  "worthy of my challenge")
            print('')
            Display_Menu()
        else:
            print("LORD VALDOMERO: You wanna challenge me and you can't even choose the right number?!")
            continue

# This function displays 4 questions 1 by 1, if the user has 1 mistake, the function takes the user to main menu after a phrase. If the
# user has all 4 correct, it will display a secret code and take the user back to main menu.
def Mortal_Kombat():
    points = 0
    print('')
    print("KANJAY MATH: Okay, let me explain to you, you have to choose between 1, 2 or 3. Any other number will be "
          "taken as a mistake. Also, if you have ONE mistake, you loose the challenge. Lord Valdomero won't tell you "
          "which ones you have wrong so be careful.")
    print(' ')
    sleep(10)
    print('LORD VALDOMERO: How many molecules are in a mol?')
    print('1. (3.025 x 10^34)  2. (6.023 x 10^23)   3. (123 000)'.center(100))
    answer = input().strip()
    if answer == '2':
        points += 1
    else:
        points = 0
    print(' ')
    print('LORD VALDOMERO: It has endocrine function?')
    print('1. Limbic system  2. Hypothalamus   3. Brain tonsil'.center(100))
    answer = input().strip()
    if answer == '2':
        points += 1
    else:
        points = 0
    print(' ')
    print('LORD VALDOMERO: Solve the equation system 3(x^2-9)=0 & 3x^2-27=0')
    print('1. (X1= 3 X2= -3)   2. (X1= 2 X2= 4)   3. No solution '.center(100))
    answer = input().strip()
    if answer == '1':
        points += 1
    else:
        points = 0
    print(' ')
    print(' ')
    print('LORD VALDOMERO: Okay, let us see if this fits you.')
    sleep(2)
    print('LORD VALDOMERO: From where do I come from?')
    sleep(2)
    print('1. Courage the Cowardly Dog  2. The Grim adventures of Billy and Mandy  3. Samurai Jack')
    answer = input().strip()
    if answer == '2':
        points += 1
    else:
        points = 0
    if points == 4:
        sleep(2)
        print('LORD VALDOMERO: Well, looks like someone knows their facts. Fine, you win this battle. Now, I shall '
              'give you a reward. If you enter the code 300311 on the Main Menu screen, you unlock the secret '
              'content. ')
        sleep(10)
        Display_Menu()
    else:
        print('LORD VALDOMERO: Well, well, well, looks like someone needs more study. Bye-bye loser!')
        sleep(3)
        Display_Menu()

# This starts the game with a message and with the Loading message. After that it takes the user to the main menu.
print('KANJAY MATH: Welcome to Learning Blast, my name is Kanjay Math and I will accompany you through the game.')
sleep(5)
print('')
print("LOADING", end='')
sleep(1)
print(".", end='')
sleep(1)
print(".", end='')
sleep(1)
print(".", end='')
sleep(1)
print('')
Display_Menu()