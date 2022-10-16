import sys


def main():
    # Gather input from the user
    data = input('Enter a string: ')

    # variables to keep track of string length using count
    # and a new str variable to hold the reverse string
    count = 0
    count1 = len(data)
    newdata = ""

    # call the strlenrecursion function to print the string
    # and length each time the first character of the
    # string is removed until the string is empty
    # using a recursive method
    strlenrecursion(data, count)
    print()

    # call the revstrrecursion to print the string in
    # reverse order by using a recursive method
    print("Reverse the String")
    revstrrecursion(data, newdata, count1)

    # first remove punctuations from the string and
    # then pass the updated string to the ispalindrome
    # function to check to see if the string is a
    # palindrome
    data = (removePunctuation(data))
    print()
    print("Is the string", data, "a palindrome?")
    print(ispalindrome(data))


# this function takes a string and int count as a parameter
# and is recursively called to remove a letter and keep
# track of how many letters were removed
# the recursive call ends when it reaches the base case
# when the string length equals 0
def strlenrecursion(data, count):
    if(len(data)) == 0:
        print("letters removed: ", count)
        return
    else:
        print(data, " letters removed: ", count)
        count += 1
        strlenrecursion(data[1:], count)


# This function takes two string and an int count parameter
# and is recursively called to obtain the reverse of a string.
# The new string takes in the last character of the original
# string and then the original string has its last character
# removed. The count starts with the length of the string
# and decrements until the original string is empty.
# When the count reaches 0, it has entered the base case and
# it returns the new reversed string
def revstrrecursion(data, newdata, count1):
    if count1 == 0:
        print(newdata)
        return
    else:
        count1 -= 1
        newdata += data[-1]
        data = data[:-1]
        revstrrecursion(data, newdata, count1)


# This function removes any punctuation that a string may have
def removePunctuation(data):
    data = ''.join(c if c.isalpha() else '' for c in data.lower())
    return data


# This function recursively calls itself to check if the first
# and last index matches. Each time it enters into the recursive
# call, the starting and ending index of the original string
# decreases.
def ispalindrome(data):
    if len(data) < 2:
        return True
    if data[0] != data[-1]:
        return False
    return ispalindrome(data[1:-1])


if __name__ == "__main__":
    sys.exit(main())

