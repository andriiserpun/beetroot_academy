class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")

        popped_item = self.head.data
        self.head = self.head.next
        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")

        return self.head.data

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top item:", stack.peek())

print("Pop:", stack.pop())
print("Pop:", stack.pop())

print("Size:", stack.size())
print("Is empty:", stack.is_empty())