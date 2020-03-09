class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        # We always have a dummy node so the list is never empty.
        self.head = Node("dummy")
        self.size = 0

    def __str__(self):
        out = ""
        cur = self.head.next
        while (cur):
            out += str(cur.item) + "/"
            cur = cur.next
        return out

    # Description: Insert a node at the front of the LinkedList
    def insertFront(self, item):
        # H => 1 => 2   # insert 3
        # H => 3 => 1 => 2

        # Store H => 1, now head = 1
        prevNext = self.head.next
        # Insert a new node item ex: 3, this would replace 1 with 3.
        self.head.next = Node(item)
        # Set the next pointer of the new node to point to 1, which was the
        # previous head.
        self.head.next.next = prevNext
        # increment the size
        self._size += 1

    def insertLast(self, item):
        # Since we cannot just insert at the end of a singly linked list we
        # have to iterate to the end to insert an item.
        # keep track of node we are on
        cur = self.head
        # This can also be while (cur.next)
        while (cur.next is not None):
            cur = cur.next

        cur.next = Node(item)
        self._size += 1

    # Description: Remove a node from the beginning.
    def removeBeginning(self):
        # No idea what assert is?
        assert (self.size() > 0)
        # H => 1 => 2   # removeBeginning
        # H => 2

        # H => 1, Now, set it to point to 2.
        self.head.next = self.head.next.next
        self._size -= 1

    def size(self):
        return self._size


if __name__ == "__main__":
    # test cases
    linkedList = LinkedList
    for i in range(1, 6):
        # print(i)
        linkedList.insertFront(i)
