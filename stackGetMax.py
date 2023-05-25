#Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Stack class 
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.max_stack = []

    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.top:
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        self.size -= 1

        if value == self.max_stack[-1]:
            self.max_stack.pop()

        return value

    def peek(self):
        if not self.top:
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        return not self.top

    def __len__(self):
        return self.size

    def get_max(self):
        if not self.max_stack:
            raise Exception("Stack is empty")
        return self.max_stack[-1]
