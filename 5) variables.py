#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"


def main():
    numbers = []
    print("Give three numbers please.")
    number1 = int(input("number1 = "))
    number2 = int(input("number2 = "))
    number3 = int(input("number3 = "))
    numbers.append(number1)
    numbers.append(number2)
    numbers.append(number3)
    print("The biggest number of the three is: " + str(max(numbers)))


if __name__ == '__main__':  # code to execute if called from command-line
    main()
