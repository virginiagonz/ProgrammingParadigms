import sys


class Node:
    # Constructor to initialize the data and the one that follows
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    # Initializes the head to a new node
    def __init__(self):
        self.head = Node()

    # Function to add a new node to the linked list
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    # Function to print the data in nodes from the linked list
    def printlist(self):
        elements = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)


def main():
    llist = LinkedList()
    llist.printlist()
    llist.append(2)
    llist.append(5)
    llist.append(7)
    llist.append(9)
    llist.printlist()


if __name__ == "__main__":
    sys.exit(main())


