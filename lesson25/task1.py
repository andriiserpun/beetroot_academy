class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} not found in the list")

    def pop(self, pos=None):
        if self.head is None:
            raise IndexError("pop from empty list")

        if pos is None:
            pos = self.size() - 1

        if pos == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            current = self.head
            prev = None
            index = 0
            while current is not None and index != pos:
                prev = current
                current = current.next
                index += 1

            if current is None:
                raise IndexError("pop index out of range")

            data = current.data
            prev.next = current.next
            return data

    def insert(self, pos, item):
        if pos == 0:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            index = 0
            while current is not None and index != pos:
                prev = current
                current = current.next
                index += 1

            if current is None and index != pos:
                raise IndexError("insert index out of range")

            new_node = Node(item)
            prev.next = new_node
            new_node.next = current

    def slice(self, start, stop):
        if start < 0 or start >= self.size() or stop <= start:
            raise ValueError("Invalid start or stop values")

        new_list = UnorderedList()
        current = self.head
        index = 0
        while current is not None and index < stop:
            if index >= start:
                new_list.append(current.data)
            current = current.next
            index += 1

        return new_list

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
