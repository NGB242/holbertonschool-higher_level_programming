#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sumofall = 0

    for arg in sys.argv[1:]:
        sumofall += int(arg)

    print(sumofall)
