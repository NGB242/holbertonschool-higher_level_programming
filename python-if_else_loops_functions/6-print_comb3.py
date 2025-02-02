#!/usr/bin/python3

for num1 in range(0, 10):
    for num2 in range(num1 + 1, 10):
        if (num1 * 10 + num2) == 89:
            print("{:02}".format(num1 * 10 + num2), end="")
        else:
            print("{:02}, ".format(num1 * 10 + num2), end="")
print()
