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
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def print(self):
        print('s{:02d} t{:02d} h{:02d} q:{}'.format(self.size, self.tail, self.head, self.queue))

if __name__ == '__main__':
    q = Queue(10)
    print(q.is_empty())
    for n in range(12):
        q.print()
        q.push(n)

    for n in range(3):
        print(q.pop())
        q.print()

    for n in range(1,9):
        q.print()
        q.push(n*3)
