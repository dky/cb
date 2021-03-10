# I'm just going to implement a linked list daily until this gets ingrained in
# my head...


class Node:
    # A linked list is really a list of all these Node objects. That are
    # connected by the self.next pointer
    # I really don't get what self means.
    # Package generic item
    # Pointer
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    # Initialize the class
    def __init__(self):
        # item here is just dummy.
        # 0(1)
        self.head = Node("dummy")
        # what's up with the _size... I think this means private or
        # something...
        self._size = 0

    def __str__(self):
        # This is used for debugging purposes
        # O(n)
        # O(n)
        out = ""
        cur = self.head.next
        while (cur):
            out += str(cur.item) + "|"
            cur = cur.next
        return out

    def insertFront(self, item):
        # adds an object to the front of the linked list
        # H => 1 => 2  let's say we want to insert 3
        # H => 3 => 1 => 2
        # O(1)
        # O(1)
        next = self.head.next
        self.head.next = Node(item)
        self.head.next.next = next
        self._size += 1

    def insertLast(self, item):
        # Inserts object to the end of the list.
        # O(n)
        # O(1)
        cur = self.head  # Keep track of the node we are currently on.
        while (cur.next is not None):  # while there's a next node to go to.
            cur = cur.next
        cur.next = Node(item)
        self._size += 1

    def removeBeginning(self):
        # removes the first object from the list
        assert (self.size() > 0)
        # H => 1 => 2   remove()
        # H => 2
        # If we want to remove 1 we need to update the head pointer to point to
        # 2.
        self.head.next = self.head.next.next
        self._size -= 1

    def size(self):
        return self._size


if __name__ == "__main__":
    # test cases
    linkedList = LinkedList()
    for i in range(1, 6):
        linkedList.insertFront(i)
    # should print 1|2|3|4|5|
    # should print 5|4|3|2|1| because we are adding items to the front of the
    # list.
    print(linkedList)
    linkedList.removeBeginning()
    linkedList.removeBeginning()
    # should print 3,4,5
    for i in range(6, 11):
        linkedList.insertLast(i)
    # should print 3,4,5,6,7,8,9,10
    print(linkedList)
