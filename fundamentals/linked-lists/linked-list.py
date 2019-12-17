class Node:
    def __init__(self, item, next=None):
        # two attributes
        # linked list is essentially a list of all these node objects connected
        # by the next pointer
        self.item = item
        # Points to the next node in the linked list implementation
        self.next = next


# linked list is made up of node objects above.
class LinkedList:
    # Initialize linked list class
    def __init__(self):
        self.head = Node("dummy")
        self.size = 0

    # Used for debugging
    def __str__(self):
        out = ""
        cur = self.head.next
        while (cur):
            out += cur.item + "|"
        return out

    # Adds object to front of ll
    # no edge cases to be aware of?
    def insertFront(self, item):
        # H => 1 => 2 insert 3
        # H => 3 => 1 => 2
        next = self.head.next
        self.head.next = Node(item)
        self.head.next.next = next
        self.size += 1

    # Adds object to back of ll
    def insertLast(self, item):
        cur = self.head
        while (cur.next is not None):
            cur = cur.next
        cur.next = Node(item)

    # Removes first node object from ll
    def removeBeginning(self):
        assert (self.size() > 0)  # If this isn't true through error
        # H => 1 => 2 remove ()
        # H => 2

    # Returns # of items in our linked list
    def size(self):
        return self.size


if __name__ == "__main__":
    linkedList = LinkedList()
    for i in range(1, 6):
        linkedList.insertFront(i)
    print(LinkedList)
