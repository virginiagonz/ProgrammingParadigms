import sys
import math


def main():
    # Problem 1: taking a list of numbers and squaring each value
    # the new values are then added to a new list
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = []
    for x in list1:
        list2.append(math.pow(x, 2))

    print(list2)

    # Problem 2:
    currelem = 0.0
    list3 = [(1, 2, 3), (3, 4, 5)]

    for tuples in list1:

        currelem = fv(x, y, z)
        print(currelem + " ")


def fv(principal, rate, time):
    curr = principal * ((1 + rate) ** time)
    return curr


if __name__ == "__main__":
    sys.exit(main())

