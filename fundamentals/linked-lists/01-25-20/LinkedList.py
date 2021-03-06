# Linked list is composed of Node objects.
# Node objects have two attributes
# item + next (pointer)

# HEAD => 1 => 2 => 3 => NULL


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        # O(1) - Pointer to the front of the list.
        self.head = Node("dummy")
        self._size = 0

    # Prints output
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
        temporary = self.head.next  # gets 1
        self.head.next = Node(item)  # overwrite 1 with 3
        # H => 3 ~~~~   1 => 2
        self.head.next.next = temporary
        #  self.head.next = 3  -> 3.next = temporary
        #  H => 3 => 1 => 2
        self._size += 1

    def insertLast(self, item):
        # Iterate through the entire list
        cur = self.head
        while (cur.next is not None):
            cur = cur.next
        # After the loop cur.next has to be None which means this is the tail
        # of the list
        cur.next = Node(item)
        # push a new node to the tail of the list
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
        linkedList.insertLast(i)
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
