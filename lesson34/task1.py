import threading

class Counter(threading.Thread):
    def __init__(self, rounds):
        super(Counter, self).__init__()
        self.counter = 0
        self.rounds = rounds

    def run(self):
        for _ in range(self.rounds):
            self.counter += 1

if __name__ == "__main__":
    rounds = 100000

    thread1 = Counter(rounds)
    thread2 = Counter(rounds)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    total_counter = thread1.counter + thread2.counter
    print("Final counter value:", total_counter)
