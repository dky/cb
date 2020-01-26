# Linked list is composed of Node objects.
# Node objects have two attributes
# item + next (pointer)


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        # O(1) - Pointer to the front of the list.
        self.head = Node("dummy")
        self._size = 0

    def __str__(self):
        # O(N) - Iterating through N items
        out = ""
        cur = self.head.next
        while (cur):
            out += str(cur.item) + "|"
            cur = cur.next
        return out

    def insertFront(self, item):
        # H => 1 => 2   insert 3
        # H => 3 => 1 => 2
        next = self.head.next  # assuming this gets 1
        self.head.next = Node(item)
        self.head.next.next = next
        self._size += 1

    def insertLast(self, item):
        # Iterate through the entire list
        cur = self.head
        while (cur.next is not None):
            cur = cur.next
        cur.next = Node(item)
        self._size += 1

    def removeBeginning(self):
        # H => 1 => 2    remove()
        # H => 2
        assert (self.size() > 0)
        self.head.next = self.head.next.next
        self._size -= 1

    def size(self):
        return self._size


if __name__ == "__main__":
    linkedList = LinkedList()
    for i in range(1, 6):
        linkedList.insertFront(i)
    # should print 1|2|3|4|5
    print(linkedList)
    # should print 3|4|5
    linkedList.removeBeginning()
    linkedList.removeBeginning()
    print(linkedList)
    for i in range(6, 11):
        linkedList.insertLast(i)
    # should print 3|4|5|6|7|8|9|10
    print(linkedList)
