class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.top:
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if not self.top:
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        return not self.top


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
