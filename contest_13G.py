# import time

class StackMax():
    def __init__(self):
        self.items = []
        self.max_items = []

    def command(self, cmd):
        parsed = cmd.split()
        length = len(parsed)
        if length == 2 and parsed[0] == 'push':
            self.push(int(parsed[1]))
            return

        if length and parsed[0] == 'get_max':
            print(self.get_max())
            return
        
        if length and parsed[0] == 'pop':
            self.pop()
    
    def get_max(self):
        if self.items != []:
            return self.max_items[-1]

        return None

    def pop(self):
        try:
            item = self.items.pop()
            if item == self.max_items[-1]:
                self.max_items.pop()
        except IndexError:
            print('error')
            return

    def push(self, i):
        self.items.append(i)
        length_max = len(self.max_items)
        if length_max == 0 or (length_max > 0 and i > self.max_items[-1]):
            self.max_items.append(i)


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
    # start = time.time()
    for n in range(100):
        stack.command(input())
    
    with open('input.txt', 'r') as inp:
        n = int(inp.readline())
        lines = inp.readlines()
        for i in range(n):
            stack.command(lines[i])

    # end = time.time()
    # print('Finished at {:.2} s'.format(end-start))