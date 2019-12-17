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
        # wth is size?
        # see size size(self) below.
        # [dummy]
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
    # Need to go over this...
    def insertFront(self, item):
        # dummy => 1 => 2 insert 3
        # dummy => 3 => 1 => 2
        # save current head
        next = self.head.next
        self.head.next = Node(item)
        self.head.next.next = next
        # self._size += 1

    # Adds object to back of ll
    # To insert item at end of linked list we need to iterate through linked
    # list since we only have a pointer to head
    def insertLast(self, item):
        # keep track of node we are on.
        cur = self.head
        # while loop to check if not none.
        while (cur.next is not None):
            cur = cur.next
        cur.next = Node(item)
        self._size += 1

    # Removes first node object from ll
    def removeBeginning(self):
        # verify that there is a node to remove.
        assert (self.size() > 0)  # If this isn't true throw error
        # H => 1 => 2 remove ()
        # H => 2
        # update head pointer to point to 2.
        self.head.next = self.head.next.next
        # decrement
        self._size -= 1

    # Returns # of items in our linked list
    def size(self):
        return self._size


if __name__ == "__main__":
    linkedList = LinkedList()
    # add 5 items (1 => 5)
    for i in range(1, 6):
        linkedList.insertFront(i)
    # should print 1|2|3|4|5
    print(LinkedList)
    # linkedList.removeBeginning()
    # linkedList.removeBeginning()
    for i in range(6, 11):
        # linkedList.insertLast()
