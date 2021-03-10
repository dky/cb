class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    # Initialize deque
    def __init__(self):
        self.size = 0  # start off with zero elements

        self.head = ListNode("head")
        self.tail = ListNode("tail")

        # head <=> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # Return Type: Boolean
    # Description: Return True if the deque is empty, else False
    def isEmpty(self):
        self.getSize() == 0

    # Return Type: int
    # Description: Return the number of items in the deque
    def getSize(self):
        pass

    # Return Type: None
    # Description: Insert item to the front of the deque
    def addFirst(self, item):
        # head <=> tail
        # head <=> 1 <=> tail
        # head <=> 2 <=> 1 <=> tail

        # new_node: head <=> 1 <=> tail
        # prev_first: tail
        # tail.prev: 1
        # head.next: 1

        new_node = ListNode(item)
        # store a pointer to tail
        prev_first = self.head.next
        # update head.next.prev, set new_node(1) <= tail
        self.head.next.prev = new_node
        # update head.next head => new_node
        self.head.next = new_node
        # update new nodes next and prev
        new_node.prev = self.head
        new_node.next = prev_first
        # increment size of lru
        self.size += 1

    # Return Type: None
    # Description: Inserts item to the end of the deque
    def addLast(self, item):
        # head <=> tail
        # head <=> 1 <=> tail

        new_node = ListNode(item)
        # store a pointer to head
        prev_head = self.tail.prev
        # update head => new_node
        self.tail.prev.next = new_node
        # update new node <= tail
        self.tail.prev = new_node
        # update new nodes next and prev
        new_node.prev = prev_head
        new_node.next = self.tail
        self.size += 1

    # Return Type: Object
    # Description: Delete and return the item at the front of the deque
    # 16:32
    def removeFirst(self):
        # head <=> 1 <=> 2 <=> tail
        # head <=> 2 <=> last
        if self.isEmpty():
            print("trying to remove from empty list")
            return

    # Return Type: List
    # Description: construct a list holding all of the items in the deque from
    # front to end and return it.
    def asList(self):
        pass
