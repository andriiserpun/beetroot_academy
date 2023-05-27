# CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVcontroller:
    def __init__(self, BBC, Discovery, TV1000):
        self.BBC = BBC
        self.Discovery = Discovery
        self.TV1000 = TV1000
    def first_channel(self):
        print("BBC")
    def last_channel(self):
        print("TV1000")
    def turn_channel(self, title):
        self.title = title
        if title == 1:
            print("BBC")
        if title == 2:
            print("Discovery")
        if title == 3:
            print("TV1000")
    def next_channel(self, next):
        self.next = next
        if next == "BBC":
            print("Discovery")
        if next == "Discovery":
            print("TV1000")
        if next == "TV1000":
            print("BBC")
    def previous_channel(self, previous):
        self.previous = previous
        if previous == "BBC":
            print("TV1000")
        if previous == "Discovery":
            print("BBC")
        if previous == "TV1000":
            print("Discovery")
    def current_channel(self, current):
        self.current = current
        if current == "BBC":
            print("BBC")
        if current == "Discovery":
            print("Discovery")
        if current == "TV1000":
            print("TV1000")

    def is_exist(self, channel_namber):
        self.channel_namber = channel_namber
        # self.name_of_channel = name_of_channel
        if channel_namber == 1:
            print("Yes")
        if channel_namber == 2:
            print("Yes")
        if channel_namber == 3:
            print("Yes")
        else:
            print("No")


controller = TVcontroller("BBC", "Discovery", "TV1000")
controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel("BBC")
controller.previous_channel('Discovery')
controller.current_channel("BBC")
controller.is_exist("4")

# я не успел доделать задание, потому что не понял, как
# в controller.is_exist() выводить Yes or No, если вводить название канала.


#

# controller = TVController(CHANNELS)
# controller.first_channel() == "BBC"
# controller.last_channel() == "TV1000"
# controller.turn_channel(1) == "BBC"
# controller.next_channel() == "Discovery"
# controller.previous_channel() == "BBC"
# controller.current_channel() == "BBC"
# controller.is_exist(4) == "Нет"
# controller.is_exis"BBC") == "Да"