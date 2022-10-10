# This program converts values from Celsius to Fahrenheit
# Created by Virginia Gonzalez
# October 9, 2022


# sys provides access to some system-level variables maintained by the interpeter
import sys


# this function converts C to F and places the new values to a Fahrenheit list
def convert(list_c):
    list_f=[]
    for x in list_c:
        y = x * (9.0 / 5.0) + 32
        list_f.append(y)
    return list_f


# the 'main' point at which code execution will start:
def main():
    c_min = int(input('Enter the minimum value: '))
    c_max = int(input('Enter the maximum value: '))

    c_range = range(c_min, c_max+1, 1)
    list_c = list(c_range)
    list_f = convert(list_c)

    print("First number: " + str(c_min))
    print("Second number: " + str(c_max))
    print(" C       F")

    # key-value pair of C and F and prints as two columns
    for (x,y) in zip(list_c,list_f):
        print(x,'   ',y)

# The following statements indicate that the starting point of our execution is main.
# We will discuss them in more detail over the next week.


if __name__ == "__main__":
    sys.exit(main())