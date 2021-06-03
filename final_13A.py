from typing import DefaultDict


class Deque():
    def __init__(self, n):
        self.queue_length = n
        self.queue = [None] * n
        self.idx_front = self.queue_length - 1
        self.idx_back = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.size != self.queue_length:
            self.queue[self.idx_back] = x
            self.idx_back = (self.idx_back + 1) % self.queue_length
            self.size += 1
        else:
            print('error')


    def pop_back(self):
        if self.size:
            self.size -= 1
            if self.idx_back:
                self.idx_back -= 1
            else:
                self.idx_back = self.queue_length - 1

            value = self.queue[self.idx_back]
            self.queue[self.idx_back] = None
            print(value)
            return
        print('error') # TODO сделать raise

    def push_front(self, x):
        if self.size != self.queue_length:
            self.queue[self.idx_front] = x
            self.size += 1

            if self.idx_front:
                self.idx_front-=1
            else:
                self.idx_front = self.queue_length - 1
            return
        print('error') # TODO сделать raise
        

    def pop_front(self):
        if self.size:
            self.size -= 1
            self.idx_front = (self.idx_front + 1) % self.queue_length
            value = self.queue[self.idx_front]
            print(value)
            return
        print('error')


    def print(self):
        data={'size': self.size,
              'idx_front': self.idx_front,
              'idx_back': self.idx_back}
        
        print('\n'.join([f'{k}: {str(data[k])}' for k in data]))
        
        lst = ()

        for a in self.queue:
            b = f'{a:>3}' if a else '___'
            lst += (b, )
        print(*lst, sep=' | ')

class QueueIsEmpty(Exception):
    def __init__(self, msg):
        print(msg)


def main():
    n = int(input())
    m = int(input())

    if not (0 < n <= 5000 and 0 < m <= 1000):
        return
    
    d = Deque(m)
    for _ in range(n):
        try:
            action, *val = input().split()
            getattr(d, action)(*val)

        except AttributeError:
            print('error')
            break

def manual():
    n = 10
    m = 15
    test = ('print', 'push_back 1', 'print', 'push_back 2', 'print', 'push_back 599', 'pop_back', 'print', 'pop_back', 'print')
    d = Deque(m)
    for t in test:
        action, *val = t.split()
        getattr(d, action)(*val)
        # method = getattr(d, action)(*argc, **kwargs)
        # if val:
        #     method(*val)
        # else:
        #     method()

    # d.print()
    
    # for name, inp, res in tests:
    #     print(name, '\n', inp, '\n', res)

if __name__ == '__main__':
    main()