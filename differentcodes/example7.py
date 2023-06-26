# Implement LinkedList class.
# The class should contain the methods:
#   is_empty
#   insert_to_head
#   delete_from_head
#   show
#   find
#   delete_by_item
#   insert_by_position
#   reverse
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def is_empty(self):
        return not self.head
    def insert_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    def delete_from_head(self):
        if self.is_empty():
            raise ValueError("LinkedList is empty")
        else:
            self.head = self.head.next
            self.length -= 1
    def show(self):
        if self.is_empty():
            print("LinkedList is empty")
        else:
            temp_ref = self.head
            while temp_ref:
                print(temp_ref.data, end=" -> ")
                temp_ref = temp_ref.next
            print("None")
    def find(self, value):
        if self.is_empty():
            return False
        temp_ref = self.head
        while temp_ref:
            if temp_ref.data == value:
                return True
            temp_ref = temp_ref.next
        return False
    def get_size(self):
        return self.length
    def delete_by_item(self, value):
        if self.is_empty():
            raise ValueError("LinkedList is empty")
        temp_ref = self.head
        if temp_ref.data == value:
            self.delete_from_head()
            return
        while temp_ref.next:
            if temp_ref.next.data == value:
                temp_ref.next = temp_ref.next.next
                self.length -= 1
                return
            temp_ref = temp_ref.next
        raise ValueError(f"Item {value} was not found in the LinkedList")
    def insert_by_position(self, value, position):
        if position == 0:
            self.insert_to_head(value)
            return
        if position > self.length - 1 or position < 0:
            raise ValueError(f"Wrong value for position. Position = {position}")
        new_node = Node(value)
        temp_ref = self.head
        counter = 0
        while temp_ref and counter < position - 1:
            temp_ref = temp_ref.next
            counter += 1
        new_node.next = temp_ref.next
        temp_ref.next = new_node
        self.length += 1
    def reverse(self):
        if self.is_empty() or self.length == 1:
            return
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_to_head(10)
    linked_list.insert_to_head(20)
    linked_list.insert_to_head(30)
    linked_list.insert_to_head(40)
    linked_list.insert_to_head(50)
    linked_list.insert_to_head(60)
    #linked_list.delete_from_head()
    linked_list.show()
    linked_list.reverse()
    linked_list.show()