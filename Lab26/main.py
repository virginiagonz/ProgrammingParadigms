# This program calculates the input values from the user to
# determine whether it forms a right triangle.
# Try-except are used to catch errors in the process.
# Created by Virginia Gonzalez
# November 30th, 2022


import sys
import math


class RightTriangle:
    # This function initializes all the sides of a right triangle
    def __init__(self, side_a, side_b, side_c='0'):
        try:
            self.side_a = float(side_a)
            self.side_b = float(side_b)
            if side_c == '0':
                self.side_c = math.sqrt(self.side_a ** 2 + self.side_b ** 2)
            else:
                self.side_c = float(side_c)
        # ValueError exceptions are thrown when an argument that has the right type but an inappropriate value,
        except:
            # first exception is raised when the values cannot be casted to a float
            raise ValueError('Error: Invalid numbers.')
        if self.side_a <= 0 or self.side_b <= 0 or self.side_c <= 0:
            # second exception is raised if the values are negative
            raise ValueError('Error: Both sides and the hypotenuse must be non negative.')
        if math.fabs(self.side_a ** 2 + self.side_b ** 2 - self.side_c ** 2) > 0.01:
            # third exception is raised if the values entered do not form a right triangle
            raise ValueError('Error: Sides a, b, and c do not form a valid Pythagorean triplet.')

    def __eq__(self, other):
        result = math.fabs(self.side_c - other.side_c)
        # returns true if the two sides of the other triangle are very close to the two sides of this triangle,
        # including if the other triangle's side a is very close to this triangle's side b and vice-versa
        if result <= 0.01:
            return True
        # Returns false if the hypotenuse of the other RightTriangle is not very close to equal to
        # the hypotenuse of this RightTriangle
        else:
            return False

    def __str__(self):
        return f'Right Triangle with side a = {self.side_a:.1f}, side b = {self.side_b:.1f}, ' \
               f'and hypotenuse = {self.side_c:.1f}'


def main():
    print()
    print('This program calculates the input values from the user to ')
    print('determine whether it forms a right triangle.')
    print()
    righttriangle = 0
    righttriangle2 = 0
    while True:
        try:
            a = input('Enter side a: ')
            b = input('Enter side b: ')
            righttriangle = RightTriangle(a, b)
            print(righttriangle)
            break
        except ValueError as value:
            print(value)
    while True:
        try:
            a = input('Enter side a: ')
            b = input('Enter side b: ')
            c = input('Enter side c: ')
            righttriangle2 = RightTriangle(a, b, c)
            print(righttriangle2)
            break
        except ValueError as value:
            print(value)
    print()
    print('First triangle: ')
    print(righttriangle)
    print()
    print('Second triangle: ')
    print(righttriangle2)
    print()
    print('Does the first triangle equal to itself?')
    print(righttriangle == righttriangle)
    print('Does the first triangle equal to the second?')
    print(righttriangle == righttriangle2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.exit(main())
