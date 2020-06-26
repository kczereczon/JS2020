import sys

array = []
for num, arg in enumerate(sys.argv, start=0):
    if len(arg) >= 3 and num != 0:
        array.insert(0, arg)

strings = ""
for string in array:
    strings += string+" "

print(strings)
