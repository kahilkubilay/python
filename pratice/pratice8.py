'''
    make a two-player Rock-Paper-Scissors game.(Hint: Ask for player
    plays(using input), compare them, print out a message of
    congratulations to the winner, and ask if the players want to
    start a new game)

    https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
'''

import random

print('Rock-Paper-Scissors Game')

actRange = ['rock', 'paper', 'scissors']

while True:
    act = input('Enter act: ')
    randomNumb = random.randrange(0,3)
    print('First player:', act)
    print('Second player:', actRange[randomNumb])

    if act == 'rock':
        if actRange[randomNumb] == 'paper':
            print('lose')
        elif actRange[randomNumb] == 'scissors':
            print('win')
        else:
            print('draw')
        
    elif act == 'paper':
        if actRange[randomNumb] == 'scissors':
            print('lose')
        elif actRange[randomNumb] == 'rock':
            print('win')
        else:
            print('draw')

    elif act == 'scissors':
        if actRange[randomNumb] == 'rock':
            print('lose')
        elif actRange[randomNumb] == 'paper':
            print('win')
        else:
            print('draw')
            
    else:
        print('wrong parameter, try again.')

    status = input('Are you want to start a new game? Y/N: ')

    if status == 'N' or status == 'n':
        break
