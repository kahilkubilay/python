'''
    Generate a random number between 1 and 9(including 1 and 9). Ask
    the user to guess the number, then tell them whether they guessed
    too low, too high, or exactly right.(Hint: remember to use the uesr
    input lessons from the very first exercise)

    Extras:
        Keep the game going until the user types “exit”
        Keep track of how many guesses the user has taken, and when the
        game ends, print this out.

    https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
'''

import random

print('Guess a number. Enter between 1 - 9 number')

def genNumb():
    randNumb = random.randrange(1, 10)
    i = 0
    
    while True: 
        userNumb = input('Enter numb: ')
        i += 1
        if userNumb == 'exit':
            break

        userNumb = int(userNumb)
        
        if userNumb == randNumb:
            print('Yeah! You know on trial', i)
            genNumb()
        elif userNumb > randNumb:
            print('too high')
        elif userNumb < randNumb:
            print('too low')

genNumb()
