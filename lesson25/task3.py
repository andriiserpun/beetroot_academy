class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        dequeued_item = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return dequeued_item
    def front_item(self):
        if self.is_empty():
            raise IndexError("front_item from empty queue")
        return self.front.data

    def size(self):
        current = self.front
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front item:", queue.front_item())

print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())

print("Size:", queue.size())
print("Is empty:", queue.is_empty())
