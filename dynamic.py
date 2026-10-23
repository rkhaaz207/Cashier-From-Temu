from node import Node

class DynamicQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        
    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def get_all(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class DynamicStack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    def get_all(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements