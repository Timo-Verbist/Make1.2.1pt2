#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"


def main():
    while True:
        numbers = []
        print("Give three numbers please.")
        for i in range(3):
            number = int(input(""))
            numbers.append(number)

        if numbers[0] > numbers[1] and numbers[0] > numbers[2]:
            print("number 1 is the biggest number of the three.\n")
        elif numbers[1] > numbers[0] and numbers[1] > numbers[2]:
            print("number 2 is the biggest number of the three.\n")
        else:
            print("number 3 is the biggest number of the three.\n")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
