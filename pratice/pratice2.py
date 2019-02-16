'''
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate message to the user. Hint: how does an even/odd
    number react differently when divided by 2?

    https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
'''

numb = int(input('Number enter: '))

if numb % 2 == 0:
    print(numb, 'is even')
else:
    print(numb, 'is odd')


#extras 1
#if the number is a multiple of 4, print out a different message

if numb % 4 == 0:
    print(numb, 'is the floor of 4')

#extra 2
'''
    Ask the user for two numbers: one number to check (call it num)
    and one number to divide by (check). If check divides evenly into
    num, tell that to the user. If not, print a different appropriate message.
'''

numb2 = int(input('Enter the different number: '))
numb3 = int(input('Enter the and different number: '))

if numb2 % numb3 == 0:
    print(numb2, 'divisible', numb3)
else:
    print(numb, 'indivisible', numb3)
