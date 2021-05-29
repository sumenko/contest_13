"""
    Списочная очередь
    get() — вывести элемент, находящийся в голове очереди, и удалить его. Если очередь пуста, то вывести «error».
    put(x) — добавить число x в очередь
    size() — вывести текущий размер очереди
"""

class ListQueue():
    class Node():
        def __init__(self, x, next=None, prev=None):
            self.value = x
            self.next_item = next
            self.prev_item = prev

    def __init__(self):
        self.queue_size = 0
        self.tail = None
        self.head = None
    
    def is_empty(self):
        return self.queue_size == 0
    
    def put(self, x):
        self.tail = self.Node(x, self.tail, self.head)
        # self.tail.prev_item = # TODO
        if self.queue_size == 0:
            self.head = self.tail
        self.queue_size += 1
    
    def get(self):
        if self.is_empty():
            return 'error'
        value = self.head.value
        self.head = self.head.next_item
        self.queue_size -= 1
        return value
    
    def size(self):
        return self.queue_size
    
    def print(self):
        node = self.tail
        lst = []

        while node:
            lst.append(str(node.value))
            node = node.next_item
        print('>', ' '.join(lst))


def main():
    num = int(input())
    if num > 1000:
        return
    q = ListQueue()
    for _ in range(num):
        q.print()
        command = input()

        if 'put' in command:
          q.put(int(command.split()[1]))

        elif 'get' in command:
            print(q.get())

        elif 'size' in command:
            print(q.size())

if __name__ == '__main__':
    main()