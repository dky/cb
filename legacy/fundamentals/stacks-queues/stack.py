class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    # creates an empty stack
    def __init__(self):
        self.first_name = None
        self._size = 0

    # prints out stack in order
    def __str__(self):
        pass

    # adds an item to teh stack
    def push(self, item):
        # add 5
        # 5 -> 4 -> 3 -> 2
        old_first_item = self.first_item
        self.first_item = Node(item)
        self.first_item.next = old_first_item
        self._size += 1
        pass

    def pop(self):
        if self.isEmpty():
            return

    # returns a boolean indicating if the stack is empty
    def isEmpty(self):
        if self.isEmpty():
            return

    # returns the number of items in the stack
    def size(self):
        pass

    if __name__ == "__main__":
        pass
