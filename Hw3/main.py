# The Entry class contains the constructor, setters, and getters for priority and values of the entries
class Entry:
    # setting values for parameters priority and value
    def __init__(self, priority, value):
        self.prior = priority
        self.val = value

    # setting the priority for the entry
    def set_priority(self, priority):
        self.prior = priority

    # returning the priority for the entry
    def get_priority(self):
        return self.prior

    # returning the value for the entry
    def get_value(self):
        return self.val

    # returning the string indicating the priority and value for the entry
    def __str__(self):
        return "Priority: " + str(self.prior) + "; Value: " + self.val


# This class contains the constructor and functions to organize the entries by their priority
class PQ:
    # initializes an empty list of entries
    def __init__(self):
        self.entries = []

    # add the priority and value of an entry and adds it to the list
    def add(self, priority, value):
        self.entries.append(Entry(priority, value))

    # finds the entry with the lowest priority and removes it from the list, and returns a
    # reference to it
    def remove_min(self):
        index = -1
        for i in range(len(self.entries)):
            if index == -1 or self.entries[i].get_priority() < self.entries[index].get_priority():
                index = i
        return self.entries.pop(index)

    # takes parameters for the value and a new priority and, if there are
    # any entries with the specified value, sets the priority for all of them to the new
    # priority.
    def set_priority(self, value, priority):
        for entry in self.entries:
            if entry.get_value() == value:
                entry.set_priority(priority)

    # returns the length of the list
    def size(self):
        return len(self.entries)


def test():
    pq = PQ()
    pq.add(2, "Eat")
    pq.add(0, "Study for CS 3035")
    pq.add(3, "Sleep")
    pq.add(1, "Maintain Personal Relationships")
    pq.add(4, "Practice Good Personal Hygiene")
    pq.set_priority("Practice Good Personal Hygiene", 2)
    pq.set_priority("Eat", 4)

    while pq.size() > 0:
        print(pq.remove_min())


if __name__ == "__main__":
    test()
