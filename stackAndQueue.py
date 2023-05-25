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

    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if not self.top:
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        if not self.top:
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        return not self.top

    def __len__(self):
        return self.size

# Queue class
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return value

    def peek(self):
        if not self.front:
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        return not self.front
