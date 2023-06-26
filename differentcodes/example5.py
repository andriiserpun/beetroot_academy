class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def add_rear(self, item):
        self.items.append(item)

    def add_front(self, item):
        self.items.insert(0, item)
    def remove_rear(self):
        return self.items.pop()
    def remove_front(self):
        return self.items.pop(0)
def is_palindrome(word):
    word_deque = Deque()

    for char in word:
        word_deque.add_rear(char)

    while not word_deque.is_empty() and len(word_deque.items) > 1:
        if word_deque.remove_front() != word_deque.remove_rear():
            return False
    return True

word = input("Enter the word: ")

if is_palindrome(word):
    print("The word is a palindrom")
else:
    print("The word is not a palindrom")