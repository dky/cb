# helper linked list class
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:
    # Creates an empty Queue
    def __init__(self):
        # notice how _size is used, this is so we don't conflict with the size
        # function.
        self._size = 0
        self.head = Node('dummy')
        self.tail = self.head

    # adds an item to the queue
    def enqueue(self, item):
        self.tail.next = Node(item)
        self.tail = self.tail.next
        self._size += 1

    # removes and return the least recently added item
    def dequeue(self):
        # [1]
        # self.head.next = 1
        # self.tail = 1
        if self.isEmpty():
            print("Trying to remove from empty queue")
            return

        out = self.head.next
        self.head.next = self.head.next.next
        self._size -= 1
        if self.isEmpty():
            self.tail = self.head
        return out.item

    # Returns a boolean indiciating if the queue is empty
    def isEmpty(self):
        return self.size() == 0

    # returns the number of items in the queue
    def size(self):
        return self.size

    # returns a list of items in the queue
    def items(self):
        output = []
        cur = self.head.next
        while (cur):
            output.append(cur.item)
            cur = cur.next
        return output


if __name__ == '__main__':
    queue = Queue()
    print(queue.isEmpty())
    for i in range(3):
        queue.enqueue(i)
    print(queue.items())
    print("Now removing items...")
    for _ in range(4):
        print(queue.dequeue())
    # 0 1 2 then error
    for i in range(2, 4):
        queue.enqueue(i)
    print(queue.items())
