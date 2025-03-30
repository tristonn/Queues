class Node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
    
    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev
    
    def get_value(self):
        return self.value
    
    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

class Queue:
    def __init__(self, max_size = None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.current_size = 0

    def get_size(self):
        return self.current_size
    
    def has_space(self):
        if self.max_size is None or self.get_size() < self.max_size:
            return True
        else:
            return False
    
    def is_empty(self):
        return self.get_size() == 0
    
    def peek(self):
        if self.get_size() > 0:
            return self.head.get_value()
        else:
            print("There is nothing in the queue!")
    
    def enqueue(self, value):
        if self.has_space():
            new_node = Node(value)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.set_next(new_node)
                self.tail = new_node
            self.current_size += 1
        else:
            print("Not enough room!")

    def dequeue(self, value):
        if not self.is_empty():
            to_remove = self.head
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = to_remove.get_next()
            self.current_size -= 1
        else:
            print("The queue is empty!")