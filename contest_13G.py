import time

class StackMax():
    def __init__(self):
        self.items = []
        self.max_item = None
        self.max_items = []

    def command(self, cmd):
        parsed = cmd.split()
        length = len(parsed)
        if length == 2 and parsed[0] == 'push':
            self.push(int(parsed[1]))
            return

        if length and parsed[0] == 'get_max':
            print(self.max_item)
            return
        
        if length and parsed[0] == 'pop':
            self.pop()
    
    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            print('error')

        try:
            self.max_item = max(self.items)
        except ValueError:
            self.max_item = None

    def push(self, i):
        self.items.append(i)
        
        if self.max_items:
            self.max_items.append(i)
            return

        if i > self.max_items[-1]:
            self.max_items.append(i)
            return



if __name__=='__main__':
    stack = StackMax()
    # with open('input.txt', 'w') as outp:
    #     n = 99999
    #     outp.write(f'{n}\n')
    #     for i in range(n):
    #         outp.write(f'push {i}\n')
    #     for i in range(n//2):
    #         outp.write(f'pop\n')
    #     for i in range(n):
    #         outp.write(f'get_max\n')
    start = time.time()
    with open('input.txt', 'r') as inp:
        n = int(inp.readline())
        lines = inp.readlines()
        for i in range(n):
            stack.command(lines[i])

    end = time.time()
    print('Finished at {:.2} s'.format(end-start))