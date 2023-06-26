# Deque should have max number of items and contain the following methods:
#   is_empty
#   add_front
#   remove_front
#   add_rear
#   remove_rear
#   size
#   front
#   rear
#   is_full
class Deque:
    def __init__(self, max_size):
        self.data = []
        self.max_size = max_size
    def is_empty(self):
        return not bool(self.data)
    def size(self):
        return len(self.data)
    def is_full(self):
        return len(self.data) == self.max_size
    def add_front(self, item):
        if not self.is_full():
            self.data.append(item)
            print(f"Item {item} was added into Deque")
        else:
            print("Deque is overloaded")
    def add_rear(self, item):
        if not self.is_full():
            self.data.insert(0, item)
            print(f"Item {item} was added into Deque")
        else:
            print("Deque is overloaded")
    def remove_rear(self):
        if not self.is_empty():
            item = self.data.pop(0)
            print(f"Item {item} was removed into Deque")
        else:
            print("Deque is already empty")
    def remove_front(self):
        if not self.is_empty():
            item = self.data.pop()
            print(f"Item {item} was removed into Deque")
        else:
            print("Deque is already empty")
    def front(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return "Deque doesn't have items"
    def rear(self):
        if not self.is_empty():
            return self.data[0]
        else:
            return "Deque doesn't have items"
    def __str__(self):
        result = ""
        if not self.is_empty():
            for i in self.data:
                result += str(i) + " | "
        else:
            result = "Deque is empty"
        return result
q = Deque(5)
q.add_front(10)
print(q)
q.add_front(20)
print(q)
q.add_front(30)
print(q)
q.add_rear(40)
print(q)
q.add_rear(50)
print(q)
q.add_rear(60)
print(q)
print(q.front())
print(q.rear())