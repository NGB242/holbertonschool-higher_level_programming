#!/usr/bin/python3
for ascii in range(0, 100):
    if ascii != 99:
        print("{:02d}".format(ascii), end=", ")
    else:
        print("{:02d}".format(ascii))
