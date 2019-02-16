'''
    Take a list, say for example this one:
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements of the list
    that are less than 5.

    https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

'''

numberList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

print('Numbers less than 5: ')
for numb in numberList:
    if numb < 5:
        newList.append(numb)
        print(numb)

#extra 1 and 2
'''
    1. Instead of printing the elements one by one,
    make a new list that has all the elements less
    than 5 from this list in it and print out this new list.

    2. Write this in one line of Python.

'''

print('numbers less than 5 in the new list: ')
print(type(newList), newList)

#extra 3
'''
    Ask the user for a number and return a list that contains
    only elements from the original list a that are smaller
    than that number given by the user.
'''

userList = []
takeNumb = int(input('Enter number: '))

for numb in numberList:
    if numb < takeNumb:
        userList.append(numb)

print('user numbers: ')
for numb in userList:
    print(numb)
