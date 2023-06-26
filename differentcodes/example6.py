class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete_from_head(self):
        self.head = self.head.next
    def insert_to_tail(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    def delete_from_tail(self):
        if self.head and self.head.next:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        else:
            raise ValueError("You tried to remove item from empty LinkedList")
    def show(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.insert_to_head(10)
    linked_list.insert_to_head(20)
    linked_list.insert_to_head(30)
    linked_list.insert_to_head(40)
    linked_list.delete_from_head()
    linked_list.delete_from_head()
    linked_list.show() # 20 -> 10 -> None
    linked_list.insert_to_tail(50)
    linked_list.insert_to_tail(60)
    linked_list.insert_to_tail(70)
    linked_list.insert_to_tail(80)
    linked_list.show()
    linked_list.delete_from_tail()
    linked_list.delete_from_tail()
    linked_list.show() # 20 -> 10 -> 50 -> 60 -> None