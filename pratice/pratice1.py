'''
    Create a program that asks the user to enter their name and their age.
    Print out message addressed to them that tells them the year that
    they will turn 100 years old.

    https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
'''

from datetime import datetime

while True:
    name = str(input('Enter name: '))
    age = int(input('Enter age: '))

    if (age > 0) and (age < 100) : 
        birthYear = (datetime.now().year - age)

        century = (birthYear + 100)
        print(name, 'will be 100 years old in', century)
        
    else: 
        print('Wrong age parameter. Please try again.')
