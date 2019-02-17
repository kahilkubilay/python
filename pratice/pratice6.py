'''
    Ask the user for a string and print out whether this string
    is a palindrome or not.(A palindrome is a string that reads
    the same forwards and backwards.)

    https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
'''

print('Palindrome Test')
print('for exit write in "exit" ')

while True:
    text = input('Enter word: ')

    if text == 'exit':
        break
    
    else:
        rText = text[::-1]
        if text == rText:
            print('Palindrome')
        else:
            print('not')
