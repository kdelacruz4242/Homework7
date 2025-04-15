class Node:
    """
    Node class to be used in the linked list implementation of the stack.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularStack:
    """
    Circular stack class using a linked list with a maximum size of 5 elements.
    """
    MAX_SIZE = 5

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, distance):
        new_node = Node(distance)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node

        elif self.size < self.MAX_SIZE:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node

        else:
            self.tail.data = distance
            self.head = self.tail.next
            self.tail = self.tail.next

        if self.size < self.MAX_SIZE:
            self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None

        temp = self.tail.data #check for oldest node

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.next
            self.head.next = self.tail

        self.size -= 1

        return temp


    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.head.data

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
            return

        value = self.tail
        count = 0

        while count < self.size:
            print(value.data)   #print from oldest to newest
            value = value.next
            count += 1

    def is_empty(self):
        return self.size == 0
