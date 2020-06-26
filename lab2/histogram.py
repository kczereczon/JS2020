import sys


def histogram(string):
    print(string)
    charList = {'a': 1}
    for char in string:
        if charList.get(char) == None:
            charList[char] = 1
        else:
            charList[char] += 1
    return charList


print(histogram("ala ma kota"))
