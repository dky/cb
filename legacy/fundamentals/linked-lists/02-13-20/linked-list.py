class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next

class LinkedList:
    # Init the class
    def __init__(self):
        # This dummy item is so we don't have to worry about an "empty" list.
        self.head = Node("dummy")
        self._size = 0

    # Debugging
    def __str__(self):
        out = ""
        cur = self.head.next
        while(cur):
            out += str(cur.item) + "|"
            cur = cur.next
        return out

    # Adds object to front
    def insertFront(self, item):
        # H => 1 => 2 insert 3
        # H => 3 => 1 => 2

        # Save value pointed to by the current head, in this case 1.
        next = self.head.next
        self.head.next = Node(item)
        self.head.next.next = next
        # Increment self._size += 1
        self._size += 1

    # Adds object to last
    def insertLast(self, item):
        cur = self.head
        while(cur.next is not None):
            cur = cur.next
        cur.next = Node(item)
        self._size += 1

    # Removes the first node object from list.
    def removeBeginning(self):
        # Make sure the list is not 0
        assert(self.size() > 0)
        # Otherwise assume there is at least 1 item to remove
        # H => 2
        self.head.next = self.head.next.next
        self._size -= 1

    def size(self):
        return self._size


if __name__ == "__main__":
    # Test cases
    linkedList = LinkedList()

    for i in range(1,6):
        linkedList.insertLast(i)
    # 1|2|3|4|5
    print(linkedList)

    linkedList.removeBeginning()
    # 2|3|4|5
    print(linkedList)
    linkedList.removeBeginning()
    # 3|4|5
    print(linkedList)

    for i in range(6, 11):
        linkedList.insertLast(i)
    print(linkedList)
