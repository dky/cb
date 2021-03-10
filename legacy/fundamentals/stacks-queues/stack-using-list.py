class Stack:
    def __init__(self):
        self.stack = []

    # if the stack is empty it will return a bool True else, bool False.
    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peak(self):
        return self.stack[-1]

    def sizeOfStack(self):
        return len(self.stack)


mystack = Stack()
mystack.push(1)
mystack.push(2)
print(mystack.sizeOfStack())
print(mystack.peak()) # 2
mystack.pop()
mystack.pop()
print(mystack.sizeOfStack())
