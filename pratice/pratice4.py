'''
    Create a program that asks the user for a number and then prints
    out a list all the divisors of that number. (if you don't know
    what a divisor is, it is a number that divides evenly into another
    number. For example, 13 is a divisor of 26 because 26/13 has no remainder)
'''

numb = int(input('Enter number: '))
visualNumb = numb
divList = []

while numb > 0:
    if visualNumb % numb == 0:
        divList.append(numb)

    numb -= 1

print(divList)
