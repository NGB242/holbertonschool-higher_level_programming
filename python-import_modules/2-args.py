#!/usr/bin/python3
import sys


def args():

    number_of_arguments = len(sys.argv) - 1

    if number_of_arguments == 0:
        print("{} arguments.".format(number_of_arguments))
    elif number_of_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number_of_arguments))
    for count in range(1, len(sys.argv)):
        print("{}: {}".format(count, sys.argv[count]))


if __name__ == "__main__":
    args()
