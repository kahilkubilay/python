'''
    Take two lists, say for example these two:
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the
    elements that are common between the lists (without duplicates).
    Make sure your program works on two lists of different sizes.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89]
commonNumb = []

for numb in a:
    for numb2 in b:
        if  numb == numb2:
            #print(numb, '==', numb2)
            commonNumb.append(numb)

for numb in commonNumb:
    i = 0
    for numb2 in commonNumb:
        if numb == numb2:
            i += 1
            if i >= 2:
                commonNumb.remove(numb)

print(type(commonNumb), commonNumb)

