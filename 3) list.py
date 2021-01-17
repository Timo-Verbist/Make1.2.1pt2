#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"


def main():
    array = []
    ls = []
    print("We are going to make a list of numbers.")
    amount = int(input("How many numbers do you want to give?\n"))
    print("Give your numbers:")
    for i in range(amount):
        number = int(input(""))
        array.append(number)

    print("uw lijst")
    print(array)

    ls.append(array[0])
    ls.append(array[amount-1])
    print("\nHet eerste en laatste nummer in uw lijst: " + str(ls))


if __name__ == '__main__':  # code to execute if called from command-line
    main()
