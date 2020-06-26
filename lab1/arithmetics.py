import sys

firstValue = sys.argv[1]
operator = sys.argv[2]
secoundValue = sys.argv[3]

if operator == "+":
    print(int(firstValue) + int(secoundValue))
elif operator == "-":
    print(int(firstValue) - int(secoundValue))
elif operator == "*":
    print(int(firstValue) * int(secoundValue))
else:
    print("Unsupported operator")
