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
        else:
            print('error')
    
    def pop(self):
        if self.is_empty():
            return None
        
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def print(self):
        print('s{:02d} t{:02d} h{:02d} q:{}'.format(self.size, self.tail, self.head, self.queue))

def main():

        num_commands = int(input())
        size = int(input())
        if num_commands > 5000 or size > 5000:
            return
        q = Queue(size)
        for _ in range(num_commands):
            command = input()
            # print('>', command.rstrip('\n'))
            if 'push' in command:
                q.push(int(command.split()[1]))

            elif 'peek' in command:
                print(q.peek())
            
            elif 'size' in command:
                print(q.size)
            
            elif 'pop' in command:
                print(q.pop())

    
if __name__ == '__main__':
    main()