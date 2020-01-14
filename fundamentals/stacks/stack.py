class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    # creates an empty stack
    def __init__(self):
        self.first_item = None
        self.size = 0

    # prints out stack in order
    def __str__(self):
        pass

    # adds an item to the stack
    def push(self, item):
        # add 5
        # 4 => 3 => 2
        # 5 => 4 =>
        old_first_item = self.first_item
        self.first_item = Node(item)
        self.first_item.next = old_first_item
        self._size += 1

    # removes and returns the most recently added item
    def pop(self):
        if self.isEmpty():
            return
        old_first_item = self.first_item
        self.first_item = self.first_item.next
        self._size -= 1

    # returns a boolean indicating if the stack is empty
    def isEmpty(self):
        return self.size() == 0

    # returns the numbber of items in the stack
    def size(self):
        return self._size


if __name__ == "__main__":
    # test cases
    pass
