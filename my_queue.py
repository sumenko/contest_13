class Queue():
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.tail != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
    
    def pop(self):
        pass

    def print(self):
        print('s{:02d} t{:02d} h{:02d} q:{}'.format(self.size, self.tail, self.head, self.queue))

if __name__ == '__main__':
    q = Queue(10)
    print(q.is_empty())
    q.print()
    q.push(10)
    q.push(1)
    q.print()
    print(q.is_empty())
