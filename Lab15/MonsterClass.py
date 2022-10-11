# This program overloads the methods __init__, __str__,
# __eq__, and __add__ which affects the constructor, printf,
#  == and +. The console displays the new outputs from the
#  overloaded methods.
#
# Created by Virginia Gonzalez
# October 11, 2022


# Created a Monster class which contains overloaded methods
class Monster:
    def __init__(self, monsterName, monsterSize, monsterLocation):
        self.name = monsterName  # initialize an attribute name
        self.size = monsterSize  # initialize an attribute size
        self.location = monsterLocation  # initialize an attribute location

    # Overriding method __str__ to print "monsterName" attacks "location"
    def __str__(self):
        return self.name + " attacks " + str(self.location)

    # Overriding method __eq__ to compare monster name and size
    def __eq__(self, other):
        return self.name == other.name and self.size == other.size

    # Overriding method __add__ to concatenate two monster names
    def __add__(self, other):
        return self.name + str(other.name)


# Creating instances Dougie and Pluto
LochNess = Monster("LochNess", 4, "London")
BigFoot = Monster("BigFoot", 5, "Tokyo")

# Testing the print method
print()
print(LochNess)
print(BigFoot)
print(LochNess == BigFoot)
print(LochNess + BigFoot)
