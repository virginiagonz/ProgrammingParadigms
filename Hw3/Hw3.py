

class Entry:
    def __init__(self, priority, value):
        self.prior = priority
        self.val = value

    def set_priority(self, priority):
        self.prior = priority

    def get_priority(self):
        return self.prior

    def get_value(self):
        return self.val

    def __str__(self):
        return "Priority: " + str(self.prior) + "; Value: " + self.val


class PQ:
    def __init__(self):
        self.entries = []

    def add(self, priority, value):
        self.entries.append(Entry(priority, value))

    def set_priority(self, value, priority):
        for entry in self.entries:
            if entry.get_value() == value:
                entry.set_priority(priority)

    def size(self):
        return len(self.entries)

    def remove_min(self):
        index = -1
        for i in range(len(self.entries)):
            if index == -1 or self.entries[i].get_priority() < self.entries[index].get_priority():
                index = i
        return self.entries.pop(index)


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
