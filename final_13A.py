# Спринт 13. Задача A
# Суменко В.А.
# попытки: 51820280


class QueueIsEmpty(Exception):
    pass


class QueueIsFull(Exception):
    pass


class Deque():
    def __init__(self, n):
        self._queue_length = n
        self._queue = [None] * n
        self.__idx_front = self._queue_length - 1
        self.__idx_back = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.size != self._queue_length:
            self._queue[self.__idx_back] = x
            self.__idx_back = (self.__idx_back + 1) % self._queue_length
            self.size += 1
        else:
            raise QueueIsFull

    def pop_back(self):
        if self.size:
            self.size -= 1
            self.__idx_back = (self.__idx_back - 1) % self._queue_length
            value = self._queue[self.__idx_back]
            self._queue[self.__idx_back] = None
            return value
        raise QueueIsEmpty

    def push_front(self, x):
        if self.size != self._queue_length:
            self._queue[self.__idx_front] = x
            self.size += 1
            self.__idx_front = (self.__idx_front - 1) % self._queue_length
        else:
            raise QueueIsFull

    def pop_front(self):
        if self.size:
            self.size -= 1
            self.__idx_front = (self.__idx_front + 1) % self._queue_length
            value = self._queue[self.__idx_front]
            self._queue[self.__idx_front] = None
            return value
        raise QueueIsEmpty

    def print(self):
        data = {'size': self.size,
                '__idx_front': self.__idx_front,
                '__idx_back': self.__idx_back}

        print('\n'.join([f'{k}: {str(data[k])}' for k in data]))

        lst = ()

        for a in self._queue:
            b = f'{a:>3}' if a else '___'
            lst += (b, )
        print(*lst, sep=' | ')


def main():
    n = int(input())
    m = int(input())

    if not (0 < n <= 5000 and 0 < m <= 1000):
        return

    d = Deque(m)
    for _ in range(n):
        try:
            action, *val = input().split()
            value = getattr(d, action)(*val)
            if value:
                print(value)

        except QueueIsEmpty:
            print('error')
        except QueueIsFull:
            print('error')


if __name__ == '__main__':
    main()
