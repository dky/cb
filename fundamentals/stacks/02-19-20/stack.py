class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    # creates an empty stack
    def __init__(self):
        self.first_item = None
        self._size = 0

    # prints out the stack in order
    def __str__(self):
        cur = self.first_item
        out = ""
        while cur:
            out += str(cur.val) + "|"
            cur = cur.next
        return out

    # adds an item to the stack
    def push(self, item):
        old_first_item = self.first_item
        self.first_item = Node(item)
        self.first_item.next = old_first_item
        self._size += 1

    # removes an returns the most recently added item
    # depends on isEmpty()
    def pop(self):
        if self.isEmpty():
            return

        old_first_item = self.first_item
        self.first_item = self.first_item
        self._size -= 1
        return old_first_item.val

    # returns a boolean indicating if the stack is empty
    # depends on size
    def isEmpty(self):
        return self.size() == 0

    # returns the number of items in the stack
    def size(self):
        return self._size


if __name__ == "__main__":
    # test cases
    stack = Stack()
    for i in range(5):
        stack.push(i)
    print(stack)

    for _ in range(3):
        print(stack.pop())

    for i in range(5, 10):
        stack.push(i)

    print(stack)
