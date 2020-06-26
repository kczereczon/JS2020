import sys

counter = 0
for arg in sys.argv:
    if len(arg) >= 3:
        counter += 1

print(counter-1)
