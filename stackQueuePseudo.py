class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        # Move all elements from stack1 to stack2
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

        # Push the new value to stack1
        self.stack1.push(value)

        # Move all elements back from stack2 to stack1
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        if self.stack1.is_empty():
            raise Exception("PseudoQueue is empty")

        return self.stack1.pop()
